#!/usr/bin/env python3
"""
Pandasチュートリアル - 例4: データの操作と変換
"""

import pandas as pd
import numpy as np

print("=== データの操作と変換 ===\n")

# 1. データの変更
print("--- 1. データの変更 ---")

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': ['a', 'b', 'c', 'd', 'e']
})

print("元のDataFrame:")
print(df)

# 特定のセルの値を変更
df.at[2, 'A'] = 100
print("\n特定のセルを変更（at）:")
print(df)

# 条件に基づく値の変更
df.loc[df['B'] > 25, 'B'] = 999
print("\n条件に基づく変更（loc）:")
print(df)

# 列全体の変更
df['D'] = df['A'] * 10
print("\n新しい列を追加:")
print(df)

# 2. apply()関数
print("\n--- 2. apply()関数 ---")

# Series.apply()
df['A_squared'] = df['A'].apply(lambda x: x ** 2)
print("Seriesにapply:")
print(df)

# DataFrame.apply()
def row_sum(row):
    return row['A'] + row['B']

df['Row_Sum'] = df.apply(row_sum, axis=1)
print("\nDataFrameにapply（行方向）:")
print(df)

# 複数の値を返す関数
def stats(col):
    return pd.Series({
        'mean': col.mean(),
        'std': col.std(),
        'min': col.min(),
        'max': col.max()
    })

numeric_cols = df.select_dtypes(include=[np.number])
stats_df = numeric_cols.apply(stats)
print("\n統計情報（列方向）:")
print(stats_df)

# 3. データ型の変換
print("\n--- 3. データ型の変換 ---")

df_mixed = pd.DataFrame({
    'strings': ['1', '2', '3', '4', '5'],
    'floats': ['1.1', '2.2', '3.3', '4.4', '5.5'],
    'dates': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'booleans': ['True', 'False', 'True', 'False', 'True']
})

print("元のデータ型:")
print(df_mixed.dtypes)

# 数値型への変換
df_mixed['integers'] = pd.to_numeric(df_mixed['strings'])
df_mixed['floats'] = df_mixed['floats'].astype(float)

# 日付型への変換
df_mixed['dates'] = pd.to_datetime(df_mixed['dates'])

# ブール型への変換
df_mixed['booleans'] = df_mixed['booleans'].map({'True': True, 'False': False})

print("\n変換後のデータ型:")
print(df_mixed.dtypes)
print("\nDataFrame:")
print(df_mixed)

# 4. 文字列操作
print("\n--- 4. 文字列操作 ---")

df_str = pd.DataFrame({
    'Name': ['Alice Smith', 'Bob Jones', 'Charlie Brown', 'David Lee'],
    'Email': ['alice@email.com', 'BOB@GMAIL.COM', 'charlie@yahoo.com', 'david@hotmail.com'],
    'Phone': ['123-456-7890', '987-654-3210', '555-123-4567', '111-222-3333']
})

print("元のデータ:")
print(df_str)

# 文字列の分割
df_str[['First', 'Last']] = df_str['Name'].str.split(' ', expand=True)

# 大文字・小文字変換
df_str['Email_Lower'] = df_str['Email'].str.lower()
df_str['Name_Upper'] = df_str['Name'].str.upper()

# 文字列の抽出
df_str['Domain'] = df_str['Email'].str.extract(r'@(.+)\.com')
df_str['Area_Code'] = df_str['Phone'].str[:3]

print("\n文字列操作後:")
print(df_str)

# 文字列の置換
df_str['Phone_Clean'] = df_str['Phone'].str.replace('-', '')
print("\n電話番号のハイフン除去:")
print(df_str[['Phone', 'Phone_Clean']])

# 5. カテゴリカルデータ
print("\n--- 5. カテゴリカルデータ ---")

df_cat = pd.DataFrame({
    'Product': ['Apple', 'Banana', 'Apple', 'Orange', 'Banana', 'Apple'],
    'Quality': ['Good', 'Excellent', 'Good', 'Poor', 'Good', 'Excellent'],
    'Price': [100, 80, 95, 60, 85, 105]
})

print("元のデータ:")
print(df_cat)
print(f"\nメモリ使用量: {df_cat.memory_usage(deep=True).sum()} bytes")

# カテゴリ型に変換
df_cat['Product'] = df_cat['Product'].astype('category')
df_cat['Quality'] = pd.Categorical(df_cat['Quality'], 
                                   categories=['Poor', 'Good', 'Excellent'], 
                                   ordered=True)

print("\nカテゴリ型に変換後:")
print(df_cat.dtypes)
print(f"メモリ使用量: {df_cat.memory_usage(deep=True).sum()} bytes")

# カテゴリの操作
print("\n品質カテゴリ:")
print(df_cat['Quality'].cat.categories)
print("\n品質コード:")
print(df_cat['Quality'].cat.codes)

# カテゴリでソート
print("\n品質でソート:")
print(df_cat.sort_values('Quality'))

# 6. ビニング（区間分割）
print("\n--- 6. ビニング（区間分割） ---")

df_age = pd.DataFrame({
    'Name': ['Person' + str(i) for i in range(1, 11)],
    'Age': [23, 45, 18, 67, 34, 52, 29, 41, 55, 38]
})

# 等間隔ビニング
df_age['Age_Group'] = pd.cut(df_age['Age'], 
                             bins=[0, 30, 50, 100], 
                             labels=['Young', 'Middle', 'Senior'])

print("年齢グループ分け:")
print(df_age)

# 分位数ベースのビニング
df_age['Age_Quartile'] = pd.qcut(df_age['Age'], 
                                 q=4, 
                                 labels=['Q1', 'Q2', 'Q3', 'Q4'])

print("\n四分位でのグループ分け:")
print(df_age)

# 7. 列の追加・削除・並び替え
print("\n--- 7. 列の追加・削除・並び替え ---")

df_cols = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

print("元のDataFrame:")
print(df_cols)

# 列の追加（複数の方法）
df_cols['D'] = [10, 11, 12]  # 直接代入
df_cols.insert(1, 'A2', df_cols['A'] * 2)  # 特定位置に挿入
df_cols = df_cols.assign(E=lambda x: x['B'] + x['C'])  # assignメソッド

print("\n列を追加:")
print(df_cols)

# 列の削除
df_cols = df_cols.drop(['A2'], axis=1)
print("\n列を削除:")
print(df_cols)

# 列の並び替え
df_cols = df_cols[['A', 'C', 'B', 'D', 'E']]
print("\n列を並び替え:")
print(df_cols)

# 8. インデックスの操作
print("\n--- 8. インデックスの操作 ---")

df_idx = pd.DataFrame({
    'Data': [10, 20, 30, 40],
    'Label': ['A', 'B', 'C', 'D']
})

print("元のDataFrame:")
print(df_idx)

# インデックスの設定
df_idx = df_idx.set_index('Label')
print("\nLabelをインデックスに:")
print(df_idx)

# マルチインデックス
df_multi = pd.DataFrame({
    'Year': [2022, 2022, 2023, 2023],
    'Month': [1, 2, 1, 2],
    'Sales': [100, 150, 120, 180]
})

df_multi = df_multi.set_index(['Year', 'Month'])
print("\nマルチインデックス:")
print(df_multi)

# インデックスのリセット
df_reset = df_multi.reset_index()
print("\nインデックスをリセット:")
print(df_reset)

print("\nデータの操作と変換の例を完了しました！")