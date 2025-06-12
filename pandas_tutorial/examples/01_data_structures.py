#!/usr/bin/env python3
"""
Pandasチュートリアル - 例1: データ構造の基礎
"""

import pandas as pd
import numpy as np

print("=== Pandasデータ構造の基礎 ===\n")

# Pandasバージョン確認
print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}\n")

# 1. Series（シリーズ）
print("--- 1. Series（1次元データ構造） ---")

# 基本的なSeries
s1 = pd.Series([1, 3, 5, np.nan, 6, 8])
print("基本的なSeries:")
print(s1)
print(f"データ型: {s1.dtype}")
print(f"形状: {s1.shape}")

# インデックス付きSeries
s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("\nインデックス付きSeries:")
print(s2)
print(f"インデックス: {s2.index.tolist()}")

# 辞書からSeries作成
dict_data = {'Tokyo': 13929286, 'Osaka': 2665314, 'Yokohama': 3724844}
s3 = pd.Series(dict_data)
print("\n辞書から作成したSeries:")
print(s3)

# Seriesの操作
print("\nSeriesの操作:")
print(f"s3['Tokyo']: {s3['Tokyo']}")
print(f"s3 > 3000000:\n{s3 > 3000000}")
print(f"s3 * 2:\n{s3 * 2}")

# 2. DataFrame（データフレーム）
print("\n--- 2. DataFrame（2次元データ構造） ---")

# 辞書からDataFrame作成
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['Tokyo', 'Osaka', 'Kyoto', 'Tokyo'],
    'Salary': [50000, 60000, 55000, 52000]
})
print("辞書から作成したDataFrame:")
print(df1)

# NumPy配列からDataFrame作成
np_array = np.random.randn(5, 3)
df2 = pd.DataFrame(np_array, columns=['A', 'B', 'C'])
print("\nNumPy配列から作成したDataFrame:")
print(df2)

# 日付インデックス付きDataFrame
dates = pd.date_range('2023-01-01', periods=6)
df3 = pd.DataFrame(np.random.randn(6, 4), 
                   index=dates, 
                   columns=['A', 'B', 'C', 'D'])
print("\n日付インデックス付きDataFrame:")
print(df3)

# 3. DataFrameの基本属性
print("\n--- 3. DataFrameの基本属性 ---")
print(f"形状 (shape): {df1.shape}")
print(f"サイズ (size): {df1.size}")
print(f"次元数 (ndim): {df1.ndim}")
print(f"インデックス: {df1.index.tolist()}")
print(f"カラム: {df1.columns.tolist()}")
print(f"\nデータ型:\n{df1.dtypes}")

# 4. 基本的な統計情報
print("\n--- 4. 基本的な統計情報 ---")
print("数値列の統計:")
print(df1.describe())

print("\n情報サマリー:")
df1.info()

# 5. データの表示
print("\n--- 5. データの表示 ---")
print("最初の2行:")
print(df1.head(2))

print("\n最後の2行:")
print(df1.tail(2))

print("\nランダムサンプル（2行）:")
print(df1.sample(2))

# 6. インデックスとカラムの操作
print("\n--- 6. インデックスとカラムの操作 ---")

# カラム名の変更
df_renamed = df1.rename(columns={'Name': '名前', 'Age': '年齢'})
print("カラム名を変更:")
print(df_renamed)

# インデックスの設定
df_indexed = df1.set_index('Name')
print("\nNameをインデックスに設定:")
print(df_indexed)

# インデックスのリセット
df_reset = df_indexed.reset_index()
print("\nインデックスをリセット:")
print(df_reset)

# 7. データ型の混在
print("\n--- 7. 様々なデータ型の混在 ---")
df_mixed = pd.DataFrame({
    'Integer': [1, 2, 3],
    'Float': [1.1, 2.2, 3.3],
    'String': ['A', 'B', 'C'],
    'Boolean': [True, False, True],
    'DateTime': pd.date_range('2023-01-01', periods=3),
    'Category': pd.Categorical(['High', 'Low', 'Medium'])
})
print("様々なデータ型を含むDataFrame:")
print(df_mixed)
print("\nデータ型:")
print(df_mixed.dtypes)

# 8. メモリ使用量
print("\n--- 8. メモリ使用量 ---")
print("各列のメモリ使用量:")
print(df_mixed.memory_usage(deep=True))

# 9. 転置
print("\n--- 9. 転置 ---")
print("元のDataFrame:")
print(df1)
print("\n転置後:")
print(df1.T)

print("\nデータ構造の基礎の例を完了しました！")