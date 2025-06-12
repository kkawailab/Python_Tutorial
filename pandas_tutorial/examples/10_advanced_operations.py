#!/usr/bin/env python3
"""
Pandasチュートリアル - 例10: 高度なデータ操作とパフォーマンス最適化
"""

import pandas as pd
import numpy as np
import time
from functools import wraps

print("=== 高度なデータ操作とパフォーマンス最適化 ===\n")

# タイミングデコレータ
def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 実行時間: {end - start:.4f}秒")
        return result
    return wrapper

# 1. マルチインデックスの操作
print("--- 1. マルチインデックスの操作 ---")

# マルチインデックスデータの作成
arrays = [
    ['Tokyo', 'Tokyo', 'Tokyo', 'Osaka', 'Osaka', 'Osaka'],
    ['2022', '2023', '2024', '2022', '2023', '2024']
]
index = pd.MultiIndex.from_arrays(arrays, names=['City', 'Year'])

data = pd.DataFrame({
    'Sales': [100, 120, 130, 80, 90, 95],
    'Profit': [20, 25, 28, 15, 18, 19],
    'Customers': [1000, 1200, 1300, 800, 900, 950]
}, index=index)

print("マルチインデックスDataFrame:")
print(data)

# マルチインデックスの選択
print("\nTokyoのデータ:")
print(data.loc['Tokyo'])

print("\n2023年のデータ:")
print(data.xs('2023', level='Year'))

# マルチインデックスの操作
print("\nインデックスレベルの入れ替え:")
print(data.swaplevel())

print("\nインデックスのソート:")
print(data.sort_index(level=['Year', 'City']))

# アンスタック
print("\nアンスタック（Year を列に）:")
unstacked = data.unstack(level='Year')
print(unstacked)

# 2. ウィンドウ関数とランキング
print("\n--- 2. ウィンドウ関数とランキング ---")

# サンプルデータ
df_window = pd.DataFrame({
    'Store': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'Month': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'Sales': [100, 150, 120, 110, 160, 125, 120, 170, 130],
    'Profit': [20, 30, 25, 22, 32, 26, 24, 34, 27]
})

# ランキング
df_window['Sales_Rank'] = df_window.groupby('Month')['Sales'].rank(ascending=False)
df_window['Sales_Pct_Rank'] = df_window.groupby('Month')['Sales'].rank(pct=True)

print("ランキング付きデータ:")
print(df_window)

# 累積関数
df_window['Cumsum_Sales'] = df_window.groupby('Store')['Sales'].cumsum()
df_window['Cummax_Sales'] = df_window.groupby('Store')['Sales'].cummax()

print("\n累積関数を適用:")
print(df_window[['Store', 'Month', 'Sales', 'Cumsum_Sales', 'Cummax_Sales']])

# 3. データの整形（melt, pivot, stack）
print("\n--- 3. データの整形 ---")

# 横持ちデータ
df_wide = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [90, 85, 78],
    'English': [85, 90, 82],
    'Science': [92, 88, 85]
})

print("横持ちデータ:")
print(df_wide)

# melt（縦持ちに変換）
df_long = df_wide.melt(id_vars=['ID', 'Name'], 
                       var_name='Subject', 
                       value_name='Score')
print("\n縦持ちデータ（melt後）:")
print(df_long)

# pivot（横持ちに戻す）
df_pivot = df_long.pivot_table(index=['ID', 'Name'], 
                               columns='Subject', 
                               values='Score')
print("\npivot_tableで横持ちに:")
print(df_pivot)

# 4. カスタム関数の適用（pipe, apply, applymap）
print("\n--- 4. カスタム関数の適用 ---")

# パイプライン処理
def add_metrics(df):
    df['Total_Score'] = df[['Math', 'English', 'Science']].sum(axis=1)
    return df

def add_grade(df):
    def get_grade(score):
        if score >= 90: return 'A'
        elif score >= 80: return 'B'
        elif score >= 70: return 'C'
        else: return 'D'
    
    df['Grade'] = df['Total_Score'].apply(lambda x: get_grade(x/3))
    return df

def add_ranking(df):
    df['Rank'] = df['Total_Score'].rank(ascending=False)
    return df

# パイプラインの実行
result = (df_wide
          .pipe(add_metrics)
          .pipe(add_grade)
          .pipe(add_ranking))

print("パイプライン処理後:")
print(result)

# 5. メモリ最適化
print("\n--- 5. メモリ最適化 ---")

# 大きなデータフレームの作成
@timeit
def create_large_df():
    return pd.DataFrame({
        'int_col': np.random.randint(0, 100, 1000000),
        'float_col': np.random.randn(1000000),
        'str_col': np.random.choice(['A', 'B', 'C', 'D'], 1000000),
        'bool_col': np.random.choice([True, False], 1000000)
    })

df_large = create_large_df()

print("\n元のメモリ使用量:")
memory_usage = df_large.memory_usage(deep=True)
print(memory_usage)
print(f"合計: {memory_usage.sum() / 1024**2:.2f} MB")

# データ型の最適化
@timeit
def optimize_dtypes(df):
    df_optimized = df.copy()
    
    # 整数型の最適化
    df_optimized['int_col'] = pd.to_numeric(df_optimized['int_col'], downcast='integer')
    
    # 文字列をカテゴリ型に
    df_optimized['str_col'] = df_optimized['str_col'].astype('category')
    
    # float32への変換（精度が許容される場合）
    df_optimized['float_col'] = df_optimized['float_col'].astype('float32')
    
    return df_optimized

df_optimized = optimize_dtypes(df_large)

print("\n最適化後のメモリ使用量:")
memory_usage_opt = df_optimized.memory_usage(deep=True)
print(memory_usage_opt)
print(f"合計: {memory_usage_opt.sum() / 1024**2:.2f} MB")
print(f"削減率: {(1 - memory_usage_opt.sum() / memory_usage.sum()) * 100:.1f}%")

# 6. 高速な演算（eval と query）
print("\n--- 6. 高速な演算 ---")

# 通常の方法
@timeit
def normal_calculation(df):
    df['result'] = (df['int_col'] + df['float_col']) * 2

# evalを使った方法
@timeit
def eval_calculation(df):
    df.eval('result = (int_col + float_col) * 2', inplace=True)

# データのコピーを作成
df_normal = df_optimized.copy()
df_eval = df_optimized.copy()

print("通常の計算:")
normal_calculation(df_normal)

print("\neval()を使った計算:")
eval_calculation(df_eval)

# queryを使った高速フィルタリング
@timeit
def normal_filter(df):
    return df[(df['int_col'] > 50) & (df['float_col'] > 0)]

@timeit
def query_filter(df):
    return df.query('int_col > 50 and float_col > 0')

print("\n通常のフィルタリング:")
result1 = normal_filter(df_optimized)

print("\nquery()を使ったフィルタリング:")
result2 = query_filter(df_optimized)

# 7. 並列処理（グループごとの処理）
print("\n--- 7. 並列処理風の最適化 ---")

# グループごとの複雑な処理
def complex_calculation(group):
    return pd.Series({
        'mean': group['float_col'].mean(),
        'std': group['float_col'].std(),
        'median': group['float_col'].median(),
        'skew': group['float_col'].skew(),
        'kurtosis': group['float_col'].kurtosis()
    })

# 小さなサンプルで実行
df_sample = df_optimized.sample(10000)

@timeit
def group_apply(df):
    return df.groupby('str_col').apply(complex_calculation)

print("グループごとの複雑な計算:")
result_grouped = group_apply(df_sample)
print(result_grouped)

# 8. 実践的な例：データ品質レポート
print("\n--- 8. 実践的な例：データ品質レポート ---")

def generate_data_quality_report(df):
    """包括的なデータ品質レポートを生成"""
    report = {}
    
    # 基本情報
    report['shape'] = df.shape
    report['memory_usage_mb'] = df.memory_usage(deep=True).sum() / 1024**2
    
    # データ型情報
    report['dtypes'] = df.dtypes.value_counts().to_dict()
    
    # 欠損値分析
    missing = df.isnull().sum()
    report['missing_values'] = {
        'total': missing.sum(),
        'by_column': missing[missing > 0].to_dict()
    }
    
    # 重複分析
    report['duplicates'] = {
        'total_rows': len(df),
        'duplicate_rows': df.duplicated().sum(),
        'unique_rows': len(df) - df.duplicated().sum()
    }
    
    # 数値列の統計
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        numeric_stats = df[numeric_cols].describe()
        report['numeric_summary'] = numeric_stats.to_dict()
    
    # カテゴリ列の情報
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    if len(cat_cols) > 0:
        cat_info = {}
        for col in cat_cols:
            cat_info[col] = {
                'unique_values': df[col].nunique(),
                'most_common': df[col].value_counts().head(3).to_dict()
            }
        report['categorical_info'] = cat_info
    
    return report

# レポート生成
quality_report = generate_data_quality_report(df_optimized.sample(10000))

print("データ品質レポート:")
print(f"データ形状: {quality_report['shape']}")
print(f"メモリ使用量: {quality_report['memory_usage_mb']:.2f} MB")
print(f"データ型: {quality_report['dtypes']}")
print(f"欠損値: {quality_report['missing_values']['total']}")
print(f"重複行: {quality_report['duplicates']['duplicate_rows']}")

# 9. ベストプラクティスまとめ
print("\n--- 9. ベストプラクティスまとめ ---")

print("""
Pandasパフォーマンス最適化のベストプラクティス:

1. データ型の最適化
   - 整数: downcast='integer'
   - カテゴリ: .astype('category')
   - 浮動小数点: float32（精度が許容される場合）

2. ベクトル化操作
   - ループの代わりにベクトル化された操作を使用
   - apply()よりも組み込み関数を優先

3. インデックスの活用
   - 頻繁にアクセスする列をインデックスに設定
   - ソートされたインデックスで高速検索

4. eval()とquery()の使用
   - 複雑な計算にはeval()
   - フィルタリングにはquery()

5. チャンク処理
   - 大きなファイルはchunksizeパラメータで分割読み込み
   - メモリに収まらないデータの処理

6. 不要なコピーの回避
   - inplace=Trueの適切な使用
   - ビューとコピーの理解

7. 適切なデータ構造の選択
   - 疎なデータにはSparseArray
   - 時系列データにはDatetimeIndex
""")

print("\n高度なデータ操作とパフォーマンス最適化の例を完了しました！")