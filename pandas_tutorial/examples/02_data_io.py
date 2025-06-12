#!/usr/bin/env python3
"""
Pandasチュートリアル - 例2: データの読み込みと書き出し
"""

import pandas as pd
import numpy as np
import json
import os

print("=== データの読み込みと書き出し ===\n")

# 作業ディレクトリの作成
os.makedirs('data', exist_ok=True)

# 1. CSVファイルの操作
print("--- 1. CSVファイルの操作 ---")

# サンプルデータの作成
sample_data = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', periods=10),
    'Product': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A'],
    'Sales': np.random.randint(100, 1000, 10),
    'Cost': np.random.randint(50, 500, 10),
    'Region': np.random.choice(['East', 'West', 'North', 'South'], 10)
})
sample_data['Profit'] = sample_data['Sales'] - sample_data['Cost']

print("サンプルデータ:")
print(sample_data)

# CSVに保存
sample_data.to_csv('data/sales_data.csv', index=False)
print("\nCSVファイルに保存しました: data/sales_data.csv")

# CSVから読み込み
df_csv = pd.read_csv('data/sales_data.csv')
print("\nCSVから読み込んだデータ:")
print(df_csv.head())

# 日付列の処理を含む読み込み
df_csv_dates = pd.read_csv('data/sales_data.csv', parse_dates=['Date'])
print("\n日付型として読み込み:")
print(df_csv_dates.dtypes)

# 部分的な読み込み
df_partial = pd.read_csv('data/sales_data.csv', 
                        usecols=['Date', 'Product', 'Sales'],
                        nrows=5)
print("\n特定の列と行のみ読み込み:")
print(df_partial)

# 2. Excelファイルの操作
print("\n--- 2. Excelファイルの操作 ---")

# 複数のシートを作成
with pd.ExcelWriter('data/multi_sheet.xlsx', engine='openpyxl') as writer:
    # 売上データ
    sample_data.to_excel(writer, sheet_name='Sales', index=False)
    
    # 集計データ
    summary = sample_data.groupby('Product').agg({
        'Sales': ['sum', 'mean'],
        'Profit': ['sum', 'mean']
    })
    summary.to_excel(writer, sheet_name='Summary')
    
    # 地域別データ
    region_summary = sample_data.groupby('Region')['Sales'].sum()
    region_summary.to_excel(writer, sheet_name='By Region')

print("Excelファイルを作成しました: data/multi_sheet.xlsx")

# Excelから読み込み（特定のシート）
df_excel = pd.read_excel('data/multi_sheet.xlsx', sheet_name='Sales')
print("\nExcelから読み込み（Salesシート）:")
print(df_excel.head())

# すべてのシートを読み込み
all_sheets = pd.read_excel('data/multi_sheet.xlsx', sheet_name=None)
print("\n利用可能なシート:")
print(list(all_sheets.keys()))

# 3. JSONファイルの操作
print("\n--- 3. JSONファイルの操作 ---")

# JSONに変換（様々な形式）
# records形式
json_records = sample_data.to_json(orient='records', indent=2)
print("JSON (records形式):")
print(json_records[:200] + "...")

# JSONファイルに保存
sample_data.to_json('data/sales_data.json', orient='records', indent=2)

# 別の形式でも保存
sample_data.to_json('data/sales_data_index.json', orient='index', indent=2)
sample_data.to_json('data/sales_data_columns.json', orient='columns', indent=2)

# JSONから読み込み
df_json = pd.read_json('data/sales_data.json')
print("\nJSONから読み込み:")
print(df_json.head())

# 4. その他の形式
print("\n--- 4. その他の形式 ---")

# TSV（タブ区切り）
sample_data.to_csv('data/sales_data.tsv', sep='\t', index=False)
df_tsv = pd.read_csv('data/sales_data.tsv', sep='\t')
print("TSVファイルから読み込み:")
print(df_tsv.head(3))

# HTML
html_string = sample_data.to_html(index=False, classes='table table-striped')
with open('data/sales_data.html', 'w') as f:
    f.write(html_string)
print("\nHTMLファイルを作成しました")

# Pickle（バイナリ形式）
sample_data.to_pickle('data/sales_data.pkl')
df_pickle = pd.read_pickle('data/sales_data.pkl')
print("\nPickleから読み込み:")
print(df_pickle.head(3))

# 5. 大きなファイルの処理
print("\n--- 5. 大きなファイルの処理 ---")

# 大きなCSVファイルを作成（デモ用）
large_data = pd.DataFrame({
    'ID': range(10000),
    'Value': np.random.randn(10000),
    'Category': np.random.choice(['A', 'B', 'C', 'D'], 10000)
})
large_data.to_csv('data/large_data.csv', index=False)

# チャンク単位で読み込み
print("チャンク単位での読み込み:")
chunk_size = 2000
chunks = []

for i, chunk in enumerate(pd.read_csv('data/large_data.csv', chunksize=chunk_size)):
    # 各チャンクを処理
    filtered_chunk = chunk[chunk['Value'] > 0]
    chunks.append(filtered_chunk)
    print(f"チャンク {i+1}: {len(chunk)} 行読み込み, {len(filtered_chunk)} 行フィルタ後")

# チャンクを結合
result = pd.concat(chunks, ignore_index=True)
print(f"\n結合後の総行数: {len(result)}")

# 6. データ型の指定と最適化
print("\n--- 6. データ型の指定と最適化 ---")

# データ型を指定して読み込み
dtypes = {
    'Product': 'category',
    'Region': 'category',
    'Sales': 'int32',
    'Cost': 'int32'
}

df_optimized = pd.read_csv('data/sales_data.csv', dtype=dtypes)
print("最適化されたデータ型:")
print(df_optimized.dtypes)

# メモリ使用量の比較
print("\nメモリ使用量の比較:")
print(f"通常の読み込み: {df_csv.memory_usage(deep=True).sum() / 1024:.2f} KB")
print(f"最適化後: {df_optimized.memory_usage(deep=True).sum() / 1024:.2f} KB")

# 7. エンコーディングの処理
print("\n--- 7. エンコーディングの処理 ---")

# 日本語を含むデータ
japanese_data = pd.DataFrame({
    '名前': ['田中', '佐藤', '鈴木'],
    '年齢': [25, 30, 35],
    '都市': ['東京', '大阪', '京都']
})

# UTF-8で保存
japanese_data.to_csv('data/japanese_data.csv', index=False, encoding='utf-8')

# Shift-JISで保存
japanese_data.to_csv('data/japanese_data_sjis.csv', index=False, encoding='shift-jis')

# 読み込み
df_utf8 = pd.read_csv('data/japanese_data.csv', encoding='utf-8')
print("UTF-8エンコーディング:")
print(df_utf8)

# クリーンアップ
print("\n作成したファイル:")
for file in os.listdir('data'):
    print(f"  - data/{file}")

print("\nデータの読み込みと書き出しの例を完了しました！")