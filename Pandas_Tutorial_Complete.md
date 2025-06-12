# Pandas完全チュートリアル：データ分析の最強ツール

## 目次
1. [Pandasとは](#1-pandasとは)
2. [環境設定とデータ構造の基礎](#2-環境設定とデータ構造の基礎)
3. [データの読み込みと書き出し](#3-データの読み込みと書き出し)
4. [データの選択とフィルタリング](#4-データの選択とフィルタリング)
5. [データの操作と変換](#5-データの操作と変換)
6. [欠損値の処理](#6-欠損値の処理)
7. [データの結合とマージ](#7-データの結合とマージ)
8. [グループ化と集計](#8-グループ化と集計)
9. [時系列データの処理](#9-時系列データの処理)
10. [データの可視化](#10-データの可視化)
11. [高度なデータ操作](#11-高度なデータ操作)
12. [パフォーマンス最適化と実践的なテクニック](#12-パフォーマンス最適化と実践的なテクニック)

## 1. Pandasとは

Pandasは、Pythonでデータ分析を行うための強力なライブラリです。構造化データの操作と分析のために設計されており、データサイエンスの分野で最も広く使用されているツールの一つです。

### Pandasの特徴

```python
import pandas as pd
import numpy as np

# Pandasのバージョン確認
print(f"Pandas version: {pd.__version__}")

# 簡単な例：データフレームの作成
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['Tokyo', 'Osaka', 'Kyoto', 'Tokyo'],
    'Salary': [50000, 60000, 55000, 52000]
}

df = pd.DataFrame(data)
print("\n基本的なDataFrame:")
print(df)
```

### なぜPandasを使うのか

1. **高速なデータ処理**：大規模データセットの効率的な処理
2. **豊富な機能**：データクリーニング、変換、分析のための包括的なツールセット
3. **柔軟性**：様々なデータ形式のサポート（CSV、Excel、SQL、JSONなど）
4. **統合性**：NumPy、Matplotlib、Scikit-learnなどとの完璧な統合

## 2. 環境設定とデータ構造の基礎

### インストールと設定

```python
# インストール（コマンドライン）
# pip install pandas numpy matplotlib openpyxl

# 基本的なインポート
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 表示設定
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 100)
pd.set_option('display.precision', 2)

# 日本語表示設定（Matplotlibの場合）
plt.rcParams['font.family'] = 'DejaVu Sans'
```

### Series（シリーズ）

```python
# Seriesの作成
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("基本的なSeries:")
print(s)

# インデックス付きSeries
cities = pd.Series(['Tokyo', 'Osaka', 'Kyoto', 'Nagoya'],
                   index=['a', 'b', 'c', 'd'])
print("\nインデックス付きSeries:")
print(cities)

# 辞書からSeriesを作成
population = pd.Series({'Tokyo': 13929286, 'Osaka': 2665314, 
                       'Yokohama': 3724844})
print("\n辞書から作成したSeries:")
print(population)
```

### DataFrame（データフレーム）

```python
# 様々な方法でDataFrameを作成

# 1. 辞書から作成
df1 = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': pd.Timestamp('20230101'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
})
print("様々なデータ型を含むDataFrame:")
print(df1)
print("\nデータ型:")
print(df1.dtypes)

# 2. NumPy配列から作成
df2 = pd.DataFrame(np.random.randn(6, 4),
                   index=pd.date_range('20230101', periods=6),
                   columns=list('ABCD'))
print("\nNumPy配列から作成:")
print(df2)

# 3. リストのリストから作成
data_list = [['Alice', 25, 'Engineer'],
             ['Bob', 30, 'Designer'],
             ['Charlie', 35, 'Manager']]
df3 = pd.DataFrame(data_list, columns=['Name', 'Age', 'Job'])
print("\nリストから作成:")
print(df3)
```

### 基本的な属性とメソッド

```python
# DataFrameの基本情報
print("形状:", df3.shape)
print("インデックス:", df3.index)
print("カラム:", df3.columns)
print("値（NumPy配列）:", df3.values)

# 統計情報
print("\n基本統計量:")
print(df2.describe())

# データ型の確認
print("\nデータ型情報:")
print(df3.info())

# 最初/最後の行を表示
print("\n最初の2行:")
print(df3.head(2))
print("\n最後の2行:")
print(df3.tail(2))
```

## 3. データの読み込みと書き出し

### CSVファイル

```python
# CSVの読み込み
# df = pd.read_csv('data.csv')

# サンプルデータの作成と保存
sample_data = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', periods=10),
    'Sales': np.random.randint(100, 1000, 10),
    'Region': np.random.choice(['East', 'West', 'North', 'South'], 10)
})

# CSVに保存
sample_data.to_csv('sample_sales.csv', index=False)

# CSVから読み込み
df_csv = pd.read_csv('sample_sales.csv', parse_dates=['Date'])
print("CSVから読み込んだデータ:")
print(df_csv.head())

# 高度な読み込みオプション
# df = pd.read_csv('data.csv',
#                  sep=',',              # 区切り文字
#                  header=0,             # ヘッダー行
#                  index_col='id',       # インデックス列
#                  usecols=['A', 'B'],   # 使用する列
#                  dtype={'A': str},     # データ型指定
#                  parse_dates=['date'], # 日付列
#                  encoding='utf-8',     # エンコーディング
#                  nrows=1000)          # 読み込む行数
```

### Excelファイル

```python
# Excelファイルの操作
# 複数シートへの書き込み
with pd.ExcelWriter('output.xlsx') as writer:
    df_csv.to_excel(writer, sheet_name='Sales', index=False)
    df3.to_excel(writer, sheet_name='Employees', index=False)

# Excelから読み込み
# df_excel = pd.read_excel('output.xlsx', sheet_name='Sales')
# all_sheets = pd.read_excel('output.xlsx', sheet_name=None)  # 全シート
```

### JSONファイル

```python
# JSONへの変換
json_str = df3.to_json(orient='records', indent=2)
print("JSON形式:")
print(json_str)

# JSONファイルへの保存と読み込み
df3.to_json('data.json', orient='records', indent=2)
# df_json = pd.read_json('data.json')
```

### SQLデータベース

```python
# SQLiteの例
import sqlite3

# データベース接続
# conn = sqlite3.connect('database.db')

# DataFrameをSQLテーブルに保存
# df3.to_sql('employees', conn, if_exists='replace', index=False)

# SQLクエリでデータを読み込み
# df_sql = pd.read_sql_query("SELECT * FROM employees WHERE Age > 25", conn)
# conn.close()
```

## 4. データの選択とフィルタリング

### 列の選択

```python
# サンプルデータの作成
df = pd.DataFrame({
    'A': range(1, 6),
    'B': range(10, 60, 10),
    'C': list('abcde'),
    'D': [True, False, True, False, True]
})

print("元のDataFrame:")
print(df)

# 単一列の選択
print("\n列'A':")
print(df['A'])  # Series として返される

# 複数列の選択
print("\n列'A'と'C':")
print(df[['A', 'C']])  # DataFrame として返される

# 列の追加
df['E'] = df['A'] * df['B']
print("\n新しい列'E'を追加:")
print(df)
```

### 行の選択

```python
# インデックスによる選択
print("インデックス1の行:")
print(df.iloc[1])  # 位置ベース

# スライスによる選択
print("\nインデックス1から3:")
print(df.iloc[1:4])

# 条件による選択
print("\n'A'が3より大きい行:")
print(df[df['A'] > 3])

# 複数条件
print("\n複数条件（AとB）:")
print(df[(df['A'] > 2) & (df['B'] < 40)])
```

### loc と iloc

```python
# locとilocの違い
dates = pd.date_range('2023-01-01', periods=5)
df_indexed = pd.DataFrame(np.random.randn(5, 4),
                         index=dates,
                         columns=['A', 'B', 'C', 'D'])

print("日付インデックスのDataFrame:")
print(df_indexed)

# loc: ラベルベースの選択
print("\nloc['2023-01-02']:")
print(df_indexed.loc['2023-01-02'])

print("\nloc['2023-01-02':'2023-01-04', ['A', 'C']]:")
print(df_indexed.loc['2023-01-02':'2023-01-04', ['A', 'C']])

# iloc: 整数位置ベースの選択
print("\niloc[1]:")
print(df_indexed.iloc[1])

print("\niloc[1:3, [0, 2]]:")
print(df_indexed.iloc[1:3, [0, 2]])
```

### 高度なフィルタリング

```python
# isin()を使った選択
df = pd.DataFrame({
    'City': ['Tokyo', 'Osaka', 'Kyoto', 'Tokyo', 'Osaka'],
    'Year': [2020, 2021, 2020, 2021, 2022],
    'Sales': [100, 150, 80, 120, 160]
})

print("特定の都市のデータ:")
print(df[df['City'].isin(['Tokyo', 'Kyoto'])])

# query()メソッド
print("\nquery()を使った選択:")
print(df.query('Sales > 100 and Year == 2021'))

# where()メソッド
print("\nwhere()を使った選択:")
print(df.where(df['Sales'] > 100))
```

## 5. データの操作と変換

### データの変更

```python
# 値の代入
df = pd.DataFrame(np.random.randn(5, 4), columns=['A', 'B', 'C', 'D'])
print("元のDataFrame:")
print(df)

# 特定のセルの値を変更
df.at[2, 'B'] = 0
print("\n特定のセルを変更:")
print(df)

# 条件に基づく値の変更
df.loc[df['A'] > 0, 'A'] = 1
print("\n条件に基づく変更:")
print(df)

# apply()関数
df['E'] = df['A'].apply(lambda x: x ** 2)
print("\napply()を使った変換:")
print(df)
```

### データ型の変換

```python
# データ型変換の例
df_mixed = pd.DataFrame({
    'A': ['1', '2', '3', '4'],
    'B': ['1.1', '2.2', '3.3', '4.4'],
    'C': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'D': ['True', 'False', 'True', 'False']
})

print("元のデータ型:")
print(df_mixed.dtypes)

# 数値型への変換
df_mixed['A'] = pd.to_numeric(df_mixed['A'])
df_mixed['B'] = df_mixed['B'].astype(float)

# 日付型への変換
df_mixed['C'] = pd.to_datetime(df_mixed['C'])

# ブール型への変換
df_mixed['D'] = df_mixed['D'].map({'True': True, 'False': False})

print("\n変換後のデータ型:")
print(df_mixed.dtypes)
print("\nDataFrame:")
print(df_mixed)
```

### 文字列操作

```python
# 文字列データの操作
df_str = pd.DataFrame({
    'Name': ['Alice Smith', 'Bob Jones', 'Charlie Brown'],
    'Email': ['alice@email.com', 'BOB@GMAIL.COM', 'charlie@yahoo.com']
})

# 文字列メソッドの使用
df_str['First_Name'] = df_str['Name'].str.split().str[0]
df_str['Last_Name'] = df_str['Name'].str.split().str[1]
df_str['Email_Lower'] = df_str['Email'].str.lower()
df_str['Domain'] = df_str['Email'].str.split('@').str[1]

print("文字列操作の結果:")
print(df_str)

# 正規表現
df_str['Name_Length'] = df_str['Name'].str.len()
df_str['Contains_a'] = df_str['Name'].str.contains('a', case=False)

print("\n正規表現を使った操作:")
print(df_str[['Name', 'Name_Length', 'Contains_a']])
```

### カテゴリカルデータ

```python
# カテゴリカル型の使用
df_cat = pd.DataFrame({
    'Grade': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B'],
    'Score': [90, 80, 95, 70, 85, 92, 75, 82]
})

# カテゴリカル型に変換
df_cat['Grade'] = pd.Categorical(df_cat['Grade'], 
                                 categories=['C', 'B', 'A'], 
                                 ordered=True)

print("カテゴリカル型:")
print(df_cat.dtypes)
print("\nソート:")
print(df_cat.sort_values('Grade'))

# カテゴリの操作
print("\nカテゴリ情報:")
print(df_cat['Grade'].cat.categories)
print("カテゴリコード:")
print(df_cat['Grade'].cat.codes)
```

## 6. 欠損値の処理

### 欠損値の検出

```python
# 欠損値を含むデータの作成
df_missing = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, 3, 4, 5],
    'D': [np.nan, np.nan, np.nan, 4, 5]
})

print("欠損値を含むDataFrame:")
print(df_missing)

# 欠損値の確認
print("\n欠損値の有無:")
print(df_missing.isnull())

# 欠損値の数
print("\n各列の欠損値数:")
print(df_missing.isnull().sum())

# 欠損値の割合
print("\n欠損値の割合:")
print(df_missing.isnull().sum() / len(df_missing) * 100)
```

### 欠損値の処理方法

```python
# 1. 欠損値を削除
print("行を削除（any）:")
print(df_missing.dropna())  # 欠損値を含む行をすべて削除

print("\n行を削除（all）:")
print(df_missing.dropna(how='all'))  # すべてが欠損値の行のみ削除

print("\n列を削除:")
print(df_missing.dropna(axis=1))  # 欠損値を含む列を削除

# 2. 欠損値を補完
print("\n前方補完:")
print(df_missing.fillna(method='ffill'))

print("\n後方補完:")
print(df_missing.fillna(method='bfill'))

# 3. 特定の値で補完
print("\n0で補完:")
print(df_missing.fillna(0))

# 4. 統計値で補完
print("\n平均値で補完:")
print(df_missing.fillna(df_missing.mean()))

# 5. 補間
print("\n線形補間:")
print(df_missing.interpolate())
```

### 高度な欠損値処理

```python
# カスタム補完戦略
df_advanced = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, np.nan, 15, 20, np.nan, 25],
    'Date': pd.date_range('2023-01-01', periods=6)
})

# グループごとの平均で補完
df_advanced['Value_filled'] = df_advanced.groupby('Category')['Value'].transform(
    lambda x: x.fillna(x.mean())
)

print("グループごとの補完:")
print(df_advanced)

# 時系列データの補完
df_time = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', periods=10),
    'Value': [1, np.nan, np.nan, 4, 5, np.nan, 7, 8, np.nan, 10]
})

df_time = df_time.set_index('Date')
df_time['Linear'] = df_time['Value'].interpolate(method='linear')
df_time['Time'] = df_time['Value'].interpolate(method='time')

print("\n時系列データの補間:")
print(df_time)
```

## 7. データの結合とマージ

### concat（連結）

```python
# データフレームの作成
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2']},
                   index=[0, 1, 2])

df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'],
                    'B': ['B3', 'B4', 'B5']},
                   index=[3, 4, 5])

df3 = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                    'D': ['D0', 'D1', 'D2']},
                   index=[0, 1, 2])

# 縦方向の連結
print("縦方向の連結:")
print(pd.concat([df1, df2]))

# 横方向の連結
print("\n横方向の連結:")
print(pd.concat([df1, df3], axis=1))

# インデックスを無視
print("\nインデックスを無視した連結:")
print(pd.concat([df1, df2], ignore_index=True))
```

### merge（マージ）

```python
# マージ用のデータ作成
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

# 基本的なマージ
print("基本的なマージ:")
print(pd.merge(left, right, on='key'))

# 異なる結合タイプ
left2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                      'A': ['A0', 'A1', 'A2']})

right2 = pd.DataFrame({'key': ['K1', 'K2', 'K3'],
                       'B': ['B1', 'B2', 'B3']})

print("\n内部結合（inner）:")
print(pd.merge(left2, right2, how='inner'))

print("\n左外部結合（left）:")
print(pd.merge(left2, right2, how='left'))

print("\n右外部結合（right）:")
print(pd.merge(left2, right2, how='right'))

print("\n完全外部結合（outer）:")
print(pd.merge(left2, right2, how='outer'))
```

### join（結合）

```python
# インデックスベースの結合
df_a = pd.DataFrame({'A': ['A0', 'A1', 'A2']},
                    index=['K0', 'K1', 'K2'])

df_b = pd.DataFrame({'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])

print("インデックスでの結合:")
print(df_a.join(df_b))

# 複数のDataFrameの結合
df_c = pd.DataFrame({'C': ['C0', 'C1', 'C2']},
                    index=['K0', 'K1', 'K2'])

print("\n複数のDataFrameの結合:")
print(df_a.join([df_b, df_c]))
```

### 実践的な例

```python
# 売上データと商品マスタの結合
sales = pd.DataFrame({
    'product_id': [1, 2, 1, 3, 2],
    'date': pd.date_range('2023-01-01', periods=5),
    'quantity': [10, 5, 8, 12, 7],
    'price': [1000, 2000, 1000, 1500, 2000]
})

products = pd.DataFrame({
    'product_id': [1, 2, 3],
    'product_name': ['Product A', 'Product B', 'Product C'],
    'category': ['Electronics', 'Clothing', 'Electronics']
})

# 売上データに商品情報を追加
result = pd.merge(sales, products, on='product_id', how='left')
result['total'] = result['quantity'] * result['price']

print("結合後の売上データ:")
print(result)

# カテゴリ別の集計
print("\nカテゴリ別売上集計:")
print(result.groupby('category')['total'].sum())
```

## 8. グループ化と集計

### 基本的なグループ化

```python
# サンプルデータの作成
df = pd.DataFrame({
    'City': ['Tokyo', 'Osaka', 'Tokyo', 'Osaka', 'Tokyo', 'Kyoto'],
    'Year': [2021, 2021, 2022, 2022, 2023, 2023],
    'Sales': [100, 80, 120, 90, 150, 70],
    'Profit': [20, 15, 25, 18, 30, 12]
})

print("元のデータ:")
print(df)

# 単一列でグループ化
grouped = df.groupby('City')
print("\n都市別の平均:")
print(grouped.mean())

# 複数列でグループ化
grouped_multi = df.groupby(['City', 'Year'])
print("\n都市・年別の合計:")
print(grouped_multi.sum())
```

### 集計関数

```python
# 様々な集計関数
print("都市別の統計:")
print(df.groupby('City').agg({
    'Sales': ['sum', 'mean', 'max', 'min'],
    'Profit': ['sum', 'mean']
}))

# カスタム集計関数
def profit_margin(group):
    return group['Profit'].sum() / group['Sales'].sum() * 100

print("\n都市別の利益率:")
print(df.groupby('City').apply(profit_margin))

# 複数の集計を一度に
print("\n包括的な集計:")
print(df.groupby('City').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Profit': lambda x: x.sum() / len(x),  # 平均利益
    'Year': 'nunique'  # ユニークな年数
}))
```

### transform と filter

```python
# transform: グループごとの変換
df['Sales_pct'] = df.groupby('City')['Sales'].transform(
    lambda x: x / x.sum() * 100
)
print("各都市内での売上割合:")
print(df)

# filter: グループのフィルタリング
high_sales_cities = df.groupby('City').filter(
    lambda x: x['Sales'].sum() > 200
)
print("\n合計売上が200を超える都市のデータ:")
print(high_sales_cities)

# グループごとのランキング
df['Sales_rank'] = df.groupby('Year')['Sales'].rank(ascending=False)
print("\n年別売上ランキング:")
print(df.sort_values(['Year', 'Sales_rank']))
```

### ピボットテーブル

```python
# ピボットテーブルの作成
pivot = df.pivot_table(
    values='Sales',
    index='City',
    columns='Year',
    aggfunc='sum',
    fill_value=0
)
print("ピボットテーブル（売上）:")
print(pivot)

# 複数の値でピボット
pivot_multi = df.pivot_table(
    values=['Sales', 'Profit'],
    index='City',
    columns='Year',
    aggfunc='sum',
    fill_value=0
)
print("\n複数値のピボットテーブル:")
print(pivot_multi)

# マージンの追加
pivot_margins = df.pivot_table(
    values='Sales',
    index='City',
    columns='Year',
    aggfunc='sum',
    margins=True,
    margins_name='Total'
)
print("\n合計付きピボットテーブル:")
print(pivot_margins)
```

### クロス集計

```python
# カテゴリカルデータのクロス集計
df_cat = pd.DataFrame({
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'Age_Group': ['Young', 'Young', 'Adult', 'Adult', 
                  'Young', 'Adult', 'Senior', 'Senior'],
    'Purchase': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']
})

# クロス集計表
cross_tab = pd.crosstab(df_cat['Gender'], df_cat['Age_Group'])
print("クロス集計（カウント）:")
print(cross_tab)

# 購入率のクロス集計
purchase_rate = pd.crosstab(
    [df_cat['Gender'], df_cat['Age_Group']], 
    df_cat['Purchase'],
    normalize='index'
) * 100
print("\n購入率のクロス集計:")
print(purchase_rate.round(1))
```

## 9. 時系列データの処理

### 日付時刻の操作

```python
# 日付時刻インデックスの作成
dates = pd.date_range('2023-01-01', periods=365, freq='D')
ts = pd.Series(np.random.randn(365), index=dates)

print("時系列データの最初の5日:")
print(ts.head())

# 日付時刻の属性
df_dates = pd.DataFrame({
    'date': pd.date_range('2023-01-01', periods=10),
    'value': np.random.randn(10)
})

df_dates['year'] = df_dates['date'].dt.year
df_dates['month'] = df_dates['date'].dt.month
df_dates['day'] = df_dates['date'].dt.day
df_dates['dayofweek'] = df_dates['date'].dt.dayofweek
df_dates['dayname'] = df_dates['date'].dt.day_name()

print("\n日付時刻の属性:")
print(df_dates)
```

### リサンプリング

```python
# 月次リサンプリング
monthly = ts.resample('M').mean()
print("月次平均:")
print(monthly.head())

# 四半期リサンプリング
quarterly = ts.resample('Q').agg(['mean', 'std', 'min', 'max'])
print("\n四半期統計:")
print(quarterly.head())

# カスタム期間
weekly = ts.resample('W-MON').sum()  # 月曜始まりの週次
print("\n週次合計（月曜始まり）:")
print(weekly.head())
```

### 移動窓関数

```python
# 移動平均
df_ts = pd.DataFrame({
    'date': pd.date_range('2023-01-01', periods=100),
    'value': np.random.randn(100).cumsum() + 100
})
df_ts = df_ts.set_index('date')

df_ts['MA7'] = df_ts['value'].rolling(window=7).mean()
df_ts['MA30'] = df_ts['value'].rolling(window=30).mean()

print("移動平均:")
print(df_ts.tail(10))

# 移動統計
df_ts['rolling_std'] = df_ts['value'].rolling(window=7).std()
df_ts['rolling_max'] = df_ts['value'].rolling(window=7).max()
df_ts['rolling_min'] = df_ts['value'].rolling(window=7).min()

print("\n移動統計:")
print(df_ts[['value', 'rolling_std', 'rolling_max', 'rolling_min']].tail())
```

### 時系列の分析

```python
# トレンドと季節性
# 簡単な例：日次データから月次トレンドを抽出
df_trend = pd.DataFrame({
    'date': pd.date_range('2022-01-01', periods=365),
    'sales': 100 + np.arange(365) * 0.5 + 
             10 * np.sin(np.arange(365) * 2 * np.pi / 30) +  # 月次季節性
             np.random.randn(365) * 5  # ノイズ
})
df_trend = df_trend.set_index('date')

# トレンド成分（30日移動平均）
df_trend['trend'] = df_trend['sales'].rolling(window=30, center=True).mean()

# 季節性成分
df_trend['detrended'] = df_trend['sales'] - df_trend['trend']
df_trend['seasonal'] = df_trend.groupby(df_trend.index.day)['detrended'].transform('mean')

print("時系列分解:")
print(df_trend.head(10))

# 前期比・前年同期比
df_comparison = pd.DataFrame({
    'date': pd.date_range('2021-01-01', periods=24, freq='M'),
    'sales': np.random.randint(100, 200, 24)
})
df_comparison = df_comparison.set_index('date')

df_comparison['prev_month'] = df_comparison['sales'].shift(1)
df_comparison['mom_change'] = df_comparison['sales'].pct_change() * 100

df_comparison['prev_year'] = df_comparison['sales'].shift(12)
df_comparison['yoy_change'] = df_comparison['sales'].pct_change(12) * 100

print("\n前期比・前年同期比:")
print(df_comparison.tail(6))
```

## 10. データの可視化

### Pandasの組み込みプロット機能

```python
import matplotlib.pyplot as plt

# サンプルデータ
df_viz = pd.DataFrame({
    'A': np.random.randn(100).cumsum(),
    'B': np.random.randn(100).cumsum(),
    'C': np.random.randn(100).cumsum()
})

# 線グラフ
df_viz.plot(figsize=(10, 6), title='Line Plot')
plt.show()

# 棒グラフ
df_viz.iloc[-10:].plot(kind='bar', figsize=(10, 6), title='Bar Plot')
plt.show()

# ヒストグラム
df_viz.plot(kind='hist', bins=20, alpha=0.7, figsize=(10, 6), title='Histogram')
plt.show()

# 散布図
df_viz.plot(kind='scatter', x='A', y='B', figsize=(8, 6), title='Scatter Plot')
plt.show()
```

### 高度な可視化

```python
# 箱ひげ図
df_box = pd.DataFrame(np.random.randn(100, 4), 
                      columns=['A', 'B', 'C', 'D'])
df_box.plot(kind='box', figsize=(8, 6), title='Box Plot')
plt.show()

# 面グラフ
df_area = pd.DataFrame(np.random.rand(10, 4), 
                       columns=['A', 'B', 'C', 'D'])
df_area.plot(kind='area', figsize=(10, 6), alpha=0.7, title='Area Plot')
plt.show()

# ヒートマップ（相関行列）
import seaborn as sns

correlation = df_viz.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()
```

### スタイリング

```python
# DataFrameのスタイリング
df_style = pd.DataFrame(np.random.randn(5, 3), 
                        columns=['A', 'B', 'C'])

# 条件付き書式
def highlight_negative(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

styled = df_style.style.applymap(highlight_negative)
# styled  # Jupyter Notebookで表示

# 背景色のグラデーション
styled = df_style.style.background_gradient(cmap='RdYlGn', axis=None)
# styled  # Jupyter Notebookで表示

# バー表示
styled = df_style.style.bar(subset=['A', 'B'], color='lightblue')
# styled  # Jupyter Notebookで表示
```

## 11. 高度なデータ操作

### マルチインデックス

```python
# マルチインデックスの作成
arrays = [
    ['Tokyo', 'Tokyo', 'Osaka', 'Osaka'],
    ['2022', '2023', '2022', '2023']
]
index = pd.MultiIndex.from_arrays(arrays, names=['City', 'Year'])

df_multi = pd.DataFrame(np.random.randn(4, 3), 
                       index=index,
                       columns=['Sales', 'Profit', 'Cost'])

print("マルチインデックスDataFrame:")
print(df_multi)

# マルチインデックスの選択
print("\nTokyoのデータ:")
print(df_multi.loc['Tokyo'])

print("\n2023年のデータ:")
print(df_multi.xs('2023', level='Year'))

# インデックスの操作
print("\nインデックスのリセット:")
print(df_multi.reset_index())

print("\nインデックスの入れ替え:")
print(df_multi.swaplevel())
```

### ウィンドウ関数

```python
# ランキングとパーセンタイル
df_rank = pd.DataFrame({
    'Student': ['A', 'B', 'C', 'D', 'E'],
    'Math': [90, 85, 78, 92, 88],
    'English': [85, 90, 82, 88, 91]
})

df_rank['Math_rank'] = df_rank['Math'].rank(ascending=False)
df_rank['English_rank'] = df_rank['English'].rank(ascending=False)
df_rank['Math_percentile'] = df_rank['Math'].rank(pct=True) * 100

print("ランキングとパーセンタイル:")
print(df_rank)

# 累積関数
df_cumulative = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', periods=10),
    'Sales': np.random.randint(100, 200, 10)
})

df_cumulative['Cumsum'] = df_cumulative['Sales'].cumsum()
df_cumulative['Cumprod'] = (1 + df_cumulative['Sales'] / 1000).cumprod()
df_cumulative['Cummax'] = df_cumulative['Sales'].cummax()

print("\n累積関数:")
print(df_cumulative)
```

### データの整形

```python
# melt（縦持ち変換）
df_wide = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [90, 85, 78],
    'English': [85, 90, 82],
    'Science': [92, 88, 85]
})

df_long = df_wide.melt(id_vars=['Name'], 
                       var_name='Subject', 
                       value_name='Score')

print("縦持ちデータ:")
print(df_long)

# pivot（横持ち変換）
df_wide_again = df_long.pivot(index='Name', 
                              columns='Subject', 
                              values='Score')

print("\n横持ちデータ（再変換）:")
print(df_wide_again)

# stack と unstack
stacked = df_wide.set_index('Name').stack()
print("\nスタック:")
print(stacked)

unstacked = stacked.unstack()
print("\nアンスタック:")
print(unstacked)
```

### カスタム関数の適用

```python
# pipe：メソッドチェーン
def add_total(df):
    df['Total'] = df.select_dtypes(include=[np.number]).sum(axis=1)
    return df

def add_average(df):
    df['Average'] = df.select_dtypes(include=[np.number]).mean(axis=1)
    return df

result = (df_wide
          .pipe(add_total)
          .pipe(add_average))

print("パイプラインの結果:")
print(result)

# applymap：要素ごとの適用（非推奨、代わりにmap使用）
df_apply = pd.DataFrame(np.random.randn(3, 3))
df_rounded = df_apply.map(lambda x: round(x, 2))

print("\n要素ごとの丸め:")
print(df_rounded)

# groupby + apply：グループごとのカスタム処理
def normalize_group(group):
    return (group - group.mean()) / group.std()

df_grouped = pd.DataFrame({
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 15, 20, 25, 30, 35]
})

df_grouped['Normalized'] = df_grouped.groupby('Group')['Value'].apply(normalize_group)
print("\nグループごとの正規化:")
print(df_grouped)
```

## 12. パフォーマンス最適化と実践的なテクニック

### メモリ使用量の最適化

```python
# データ型の最適化
df_memory = pd.DataFrame({
    'int_col': np.random.randint(0, 100, 10000),
    'float_col': np.random.randn(10000),
    'str_col': ['category_' + str(i % 10) for i in range(10000)]
})

print("元のメモリ使用量:")
print(df_memory.memory_usage(deep=True))

# 整数型の最適化
df_memory['int_col'] = pd.to_numeric(df_memory['int_col'], downcast='integer')

# カテゴリ型への変換
df_memory['str_col'] = df_memory['str_col'].astype('category')

print("\n最適化後のメモリ使用量:")
print(df_memory.memory_usage(deep=True))

# メモリ使用量の詳細
print("\nデータ型情報:")
print(df_memory.dtypes)
```

### 大規模データの処理

```python
# チャンク単位での読み込み
# chunk_size = 1000
# chunks = []
# for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
#     # 各チャンクを処理
#     processed_chunk = chunk[chunk['value'] > 0]  # フィルタリング
#     chunks.append(processed_chunk)
# 
# result = pd.concat(chunks, ignore_index=True)

# eval()を使った高速演算
df_large = pd.DataFrame({
    'A': np.random.randn(100000),
    'B': np.random.randn(100000),
    'C': np.random.randn(100000)
})

# 通常の方法
%timeit df_large['D'] = df_large['A'] + df_large['B'] * df_large['C']

# eval()を使った方法
%timeit df_large.eval('D = A + B * C', inplace=True)

# query()を使った高速フィルタリング
%timeit df_large[df_large['A'] > 0]
%timeit df_large.query('A > 0')
```

### ベストプラクティス

```python
# 1. ベクトル化操作を使用
# 悪い例（ループ）
def bad_example(df):
    result = []
    for i in range(len(df)):
        result.append(df.iloc[i]['A'] * 2)
    return result

# 良い例（ベクトル化）
def good_example(df):
    return df['A'] * 2

# 2. インデックスの活用
df_indexed = df_large.set_index('A')
# インデックスを使った高速アクセス

# 3. コピーの最小化
# 悪い例
df_copy = df_large.copy()
df_copy['E'] = df_copy['A'] + 1

# 良い例（ビューを使用）
df_large['E'] = df_large['A'] + 1

# 4. 適切なデータ構造の選択
# 時系列データにはDatetimeIndex
# カテゴリカルデータにはCategorical型
# 疎なデータにはSparseArray
```

### 実践的な例：売上分析ダッシュボード

```python
# 総合的な売上分析
def create_sales_report(df):
    """売上データの包括的なレポートを作成"""
    
    report = {}
    
    # 基本統計
    report['summary'] = df.describe()
    
    # 時系列分析
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')
    
    # 月次集計
    monthly = df.resample('M').agg({
        'sales': ['sum', 'mean', 'count'],
        'profit': 'sum'
    })
    report['monthly'] = monthly
    
    # 商品別分析
    product_analysis = df.groupby('product').agg({
        'sales': ['sum', 'mean'],
        'profit': ['sum', lambda x: x.sum() / df['sales'].sum() * 100]
    })
    product_analysis.columns = ['total_sales', 'avg_sales', 
                               'total_profit', 'profit_contribution']
    report['by_product'] = product_analysis
    
    # トレンド分析
    df['sales_ma30'] = df['sales'].rolling(window=30).mean()
    df['sales_growth'] = df['sales'].pct_change(periods=30) * 100
    
    # 異常値検出
    Q1 = df['sales'].quantile(0.25)
    Q3 = df['sales'].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df['sales'] < Q1 - 1.5 * IQR) | 
                  (df['sales'] > Q3 + 1.5 * IQR)]
    report['outliers'] = outliers
    
    return report

# 使用例
# sales_data = pd.read_csv('sales.csv')
# report = create_sales_report(sales_data)
```

### データ品質チェック

```python
def data_quality_check(df):
    """データ品質の包括的なチェック"""
    
    print("=== データ品質レポート ===\n")
    
    # 基本情報
    print(f"行数: {len(df)}")
    print(f"列数: {len(df.columns)}")
    print(f"メモリ使用量: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB\n")
    
    # 欠損値
    missing = df.isnull().sum()
    missing_pct = missing / len(df) * 100
    missing_report = pd.DataFrame({
        'Missing': missing,
        'Percentage': missing_pct
    })
    print("欠損値:")
    print(missing_report[missing_report['Missing'] > 0])
    
    # 重複
    duplicates = df.duplicated().sum()
    print(f"\n重複行数: {duplicates}")
    
    # データ型
    print("\nデータ型:")
    print(df.dtypes.value_counts())
    
    # 数値列の統計
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        print("\n数値列の統計:")
        print(df[numeric_cols].describe())
    
    # カテゴリ列のユニーク値
    object_cols = df.select_dtypes(include=['object']).columns
    if len(object_cols) > 0:
        print("\nカテゴリ列のユニーク値数:")
        for col in object_cols:
            print(f"{col}: {df[col].nunique()}")
    
    return missing_report

# 使用例
# quality_report = data_quality_check(df)
```

## まとめ

Pandasは、Pythonでのデータ分析に欠かせない強力なツールです：

1. **データ構造**：SeriesとDataFrameによる効率的なデータ管理
2. **データ入出力**：様々な形式のファイルの読み書き
3. **データ操作**：選択、フィルタリング、変換の豊富な機能
4. **欠損値処理**：柔軟な欠損値の検出と処理方法
5. **データ結合**：merge、join、concatによる多様な結合操作
6. **集計分析**：groupby、pivot_table、crosstabによる強力な集計機能
7. **時系列処理**：日付時刻データの専門的な処理機能
8. **可視化**：組み込みのプロット機能とSeabornとの連携

主要な使用場面：
- データクリーニングと前処理
- 探索的データ分析（EDA）
- 時系列データの分析
- ビジネスインテリジェンスとレポート作成
- 機械学習の前処理

次のステップ：
- 実際のデータセットでの練習
- SQLとの連携
- 大規模データ処理（Dask、Vaexなど）
- 機械学習ライブラリとの統合（scikit-learn）

継続的な学習のために、公式ドキュメントを参照し、実際のプロジェクトで活用してください。