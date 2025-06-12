#!/usr/bin/env python3
"""
Pandasチュートリアル - 例5: 欠損値の処理
"""

import pandas as pd
import numpy as np

print("=== 欠損値の処理 ===\n")

# 1. 欠損値を含むデータの作成
print("--- 1. 欠損値を含むデータ ---")

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5, np.nan, 7],
    'B': [np.nan, 2, 3, np.nan, 5, 6, 7],
    'C': [1, 2, 3, 4, 5, 6, 7],
    'D': [np.nan, np.nan, np.nan, 4, 5, 6, 7],
    'E': ['a', 'b', np.nan, 'd', np.nan, 'f', 'g']
})

print("欠損値を含むDataFrame:")
print(df)

# 2. 欠損値の検出
print("\n--- 2. 欠損値の検出 ---")

# 欠損値の確認
print("欠損値の有無（True=欠損）:")
print(df.isnull())

# 欠損値でない値の確認
print("\n欠損値でない値（True=非欠損）:")
print(df.notnull())

# 各列の欠損値数
print("\n各列の欠損値数:")
print(df.isnull().sum())

# 各行の欠損値数
print("\n各行の欠損値数:")
print(df.isnull().sum(axis=1))

# 欠損値の割合
print("\n欠損値の割合（%）:")
print((df.isnull().sum() / len(df)) * 100)

# 欠損値を含む行の表示
print("\n欠損値を含む行:")
print(df[df.isnull().any(axis=1)])

# 3. 欠損値の削除
print("\n--- 3. 欠損値の削除 ---")

# 欠損値を含む行を削除（any）
print("欠損値を含む行をすべて削除:")
print(df.dropna())

# すべてが欠損値の行のみ削除（all）
print("\nすべてが欠損値の行のみ削除:")
print(df.dropna(how='all'))

# 特定の列の欠損値を基準に削除
print("\n列Aに欠損値がある行を削除:")
print(df.dropna(subset=['A']))

# 欠損値を含む列を削除
print("\n欠損値を含む列を削除:")
print(df.dropna(axis=1))

# 閾値を設定（非欠損値が4個以上の行のみ残す）
print("\n非欠損値が4個以上の行のみ:")
print(df.dropna(thresh=4))

# 4. 欠損値の補完
print("\n--- 4. 欠損値の補完 ---")

# 特定の値で補完
print("0で補完:")
print(df.fillna(0))

# 列ごとに異なる値で補完
print("\n列ごとに異なる値で補完:")
fill_values = {'A': 999, 'B': -1, 'E': 'missing'}
print(df.fillna(value=fill_values))

# 前方補完（forward fill）
print("\n前方補完:")
print(df.fillna(method='ffill'))

# 後方補完（backward fill）
print("\n後方補完:")
print(df.fillna(method='bfill'))

# 補完回数の制限
print("\n前方補完（最大1回）:")
print(df.fillna(method='ffill', limit=1))

# 5. 統計値での補完
print("\n--- 5. 統計値での補完 ---")

# 平均値で補完
df_mean = df.copy()
df_mean['A'] = df_mean['A'].fillna(df_mean['A'].mean())
df_mean['B'] = df_mean['B'].fillna(df_mean['B'].mean())
print("平均値で補完:")
print(df_mean)

# 中央値で補完
df_median = df.copy()
df_median = df_median.fillna(df.median())
print("\n中央値で補完:")
print(df_median)

# 最頻値で補完（カテゴリカルデータ）
df_mode = df.copy()
df_mode['E'] = df_mode['E'].fillna(df_mode['E'].mode()[0])
print("\n最頻値で補完（E列）:")
print(df_mode)

# 6. 補間
print("\n--- 6. 補間 ---")

# 時系列データの作成
dates = pd.date_range('2023-01-01', periods=10)
ts_df = pd.DataFrame({
    'date': dates,
    'value': [1, np.nan, np.nan, 4, 5, np.nan, 7, 8, np.nan, 10],
    'value2': [10, 20, np.nan, 40, np.nan, np.nan, 70, 80, 90, 100]
})

print("時系列データ:")
print(ts_df)

# 線形補間
ts_df['linear'] = ts_df['value'].interpolate(method='linear')
print("\n線形補間:")
print(ts_df[['date', 'value', 'linear']])

# 多項式補間
ts_df['polynomial'] = ts_df['value'].interpolate(method='polynomial', order=2)
print("\n多項式補間（2次）:")
print(ts_df[['date', 'value', 'polynomial']])

# 時間ベースの補間
ts_df_time = ts_df.set_index('date')
ts_df_time['time_based'] = ts_df_time['value'].interpolate(method='time')
print("\n時間ベースの補間:")
print(ts_df_time[['value', 'time_based']])

# 7. グループごとの欠損値処理
print("\n--- 7. グループごとの欠損値処理 ---")

df_group = pd.DataFrame({
    'Category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, np.nan, 30, np.nan, 50, 60, 70, np.nan, 90],
    'Date': pd.date_range('2023-01-01', periods=9)
})

print("グループデータ:")
print(df_group)

# グループごとの平均で補完
df_group['Value_filled'] = df_group.groupby('Category')['Value'].transform(
    lambda x: x.fillna(x.mean())
)

print("\nグループごとの平均で補完:")
print(df_group)

# グループごとの前方補完
df_group['Value_ffill'] = df_group.groupby('Category')['Value'].transform(
    lambda x: x.fillna(method='ffill')
)

print("\nグループごとの前方補完:")
print(df_group)

# 8. 欠損値のパターン分析
print("\n--- 8. 欠損値のパターン分析 ---")

# 大きなデータセットでの欠損値パターン
np.random.seed(42)
large_df = pd.DataFrame(
    np.random.randn(100, 5),
    columns=['A', 'B', 'C', 'D', 'E']
)

# ランダムに欠損値を挿入
for col in large_df.columns:
    missing_idx = np.random.choice(large_df.index, size=20, replace=False)
    large_df.loc[missing_idx, col] = np.nan

# 欠損値のヒートマップ用データ
missing_pattern = large_df.isnull().astype(int)

print("欠損値パターンのサマリー:")
print(f"総データ数: {large_df.size}")
print(f"欠損値数: {large_df.isnull().sum().sum()}")
print(f"欠損値率: {(large_df.isnull().sum().sum() / large_df.size) * 100:.2f}%")

# 欠損値の相関
print("\n欠損値の相関（列間）:")
missing_corr = missing_pattern.corr()
print(missing_corr)

print("\n欠損値の処理の例を完了しました！")