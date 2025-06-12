#!/usr/bin/env python3
"""
Pandasチュートリアル - 例3: データの選択とフィルタリング
"""

import pandas as pd
import numpy as np

print("=== データの選択とフィルタリング ===\n")

# サンプルデータの作成
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank'],
    'Age': [25, 30, 35, 28, 32, 27],
    'Department': ['Sales', 'IT', 'Sales', 'HR', 'IT', 'Sales'],
    'Salary': [50000, 60000, 55000, 52000, 58000, 51000],
    'Years': [2, 5, 8, 3, 6, 2]
})

print("サンプルデータ:")
print(df)
print()

# 1. 列の選択
print("--- 1. 列の選択 ---")

# 単一列の選択（Series）
print("Name列（Series）:")
print(df['Name'])
print(f"型: {type(df['Name'])}")

# 複数列の選択（DataFrame）
print("\nName列とSalary列（DataFrame）:")
print(df[['Name', 'Salary']])
print(f"型: {type(df[['Name', 'Salary']])}")

# ドット記法での選択
print("\nドット記法でAge列を選択:")
print(df.Age)

# 2. 行の選択
print("\n--- 2. 行の選択 ---")

# インデックスによる選択
print("インデックス0から2:")
print(df[0:3])

# 条件による選択
print("\n年齢が30以上:")
print(df[df['Age'] >= 30])

# 複数条件（AND）
print("\n年齢が30以上かつ給与が55000以上:")
print(df[(df['Age'] >= 30) & (df['Salary'] >= 55000)])

# 複数条件（OR）
print("\n部署がSalesまたはIT:")
print(df[(df['Department'] == 'Sales') | (df['Department'] == 'IT')])

# 3. loc（ラベルベース選択）
print("\n--- 3. loc（ラベルベース選択） ---")

# 単一行
print("インデックス2の行:")
print(df.loc[2])

# 複数行
print("\nインデックス1から3:")
print(df.loc[1:3])

# 行と列を指定
print("\nインデックス0から2、Name列とSalary列:")
print(df.loc[0:2, ['Name', 'Salary']])

# 条件とloc
print("\n条件を使ったloc:")
print(df.loc[df['Age'] > 30, ['Name', 'Age', 'Department']])

# 4. iloc（位置ベース選択）
print("\n--- 4. iloc（位置ベース選択） ---")

# 単一行
print("3行目（位置2）:")
print(df.iloc[2])

# 複数行
print("\n2行目から4行目:")
print(df.iloc[1:4])

# 行と列を位置で指定
print("\n最初の3行、最初の2列:")
print(df.iloc[:3, :2])

# 特定の行と列
print("\n特定の位置:")
print(df.iloc[[0, 2, 4], [0, 3]])

# 5. at と iat（単一の値へのアクセス）
print("\n--- 5. at と iat ---")

# atでラベルベースアクセス
print(f"インデックス1のName: {df.at[1, 'Name']}")

# iatで位置ベースアクセス
print(f"2行目3列目の値: {df.iat[1, 2]}")

# 6. isin() メソッド
print("\n--- 6. isin() メソッド ---")

# 特定の値を含む行
print("部署がSalesまたはHRの従業員:")
print(df[df['Department'].isin(['Sales', 'HR'])])

# 複数の列でisin
ages_to_find = [25, 30, 35]
print(f"\n年齢が{ages_to_find}のいずれかの従業員:")
print(df[df['Age'].isin(ages_to_find)])

# 7. query() メソッド
print("\n--- 7. query() メソッド ---")

# 基本的なクエリ
print("query: Age > 30")
print(df.query('Age > 30'))

# 複雑なクエリ
print("\nquery: (Age > 30) and (Salary > 55000)")
print(df.query('(Age > 30) and (Salary > 55000)'))

# 変数を使ったクエリ
min_salary = 55000
print(f"\nquery: Salary >= {min_salary}")
print(df.query('Salary >= @min_salary'))

# 8. where() メソッド
print("\n--- 8. where() メソッド ---")

# 条件を満たさない値をNaNに
print("年齢が30未満の値をNaNに:")
print(df['Age'].where(df['Age'] >= 30))

# 条件を満たさない値を別の値に
print("\n給与が55000未満を0に:")
print(df['Salary'].where(df['Salary'] >= 55000, 0))

# 9. フィルタリングのテクニック
print("\n--- 9. 高度なフィルタリング ---")

# 文字列を含む検索
print("名前に'a'を含む（大文字小文字区別なし）:")
print(df[df['Name'].str.contains('a', case=False)])

# 開始文字での検索
print("\n名前が'C'で始まる:")
print(df[df['Name'].str.startswith('C')])

# 数値の範囲
print("\n年齢が27から32の範囲:")
print(df[df['Age'].between(27, 32)])

# 最大値・最小値の行
print("\n給与が最大の従業員:")
print(df[df['Salary'] == df['Salary'].max()])

# 10. サンプリング
print("\n--- 10. サンプリング ---")

# ランダムサンプル
print("ランダムに3行抽出:")
print(df.sample(n=3, random_state=42))

# 割合でサンプリング
print("\n50%をランダムに抽出:")
print(df.sample(frac=0.5, random_state=42))

# 11. 重複の処理
print("\n--- 11. 重複の処理 ---")

# 重複データを追加
df_with_dup = pd.concat([df, df.iloc[[0, 2]]], ignore_index=True)
print("重複を含むデータ:")
print(df_with_dup)

# 重複の確認
print("\n重複行の確認:")
print(df_with_dup[df_with_dup.duplicated()])

# 重複の削除
print("\n重複を削除:")
print(df_with_dup.drop_duplicates())

# 特定の列で重複確認
print("\n部署列で重複を削除（最初の値を保持）:")
print(df_with_dup.drop_duplicates(subset=['Department'], keep='first'))

print("\nデータの選択とフィルタリングの例を完了しました！")