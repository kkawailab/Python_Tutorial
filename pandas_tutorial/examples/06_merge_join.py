#!/usr/bin/env python3
"""
Pandasチュートリアル - 例6: データの結合とマージ
"""

import pandas as pd
import numpy as np

print("=== データの結合とマージ ===\n")

# 1. concat（連結）
print("--- 1. concat（連結） ---")

# サンプルデータの作成
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}, index=[0, 1, 2])

df2 = pd.DataFrame({
    'A': ['A3', 'A4', 'A5'],
    'B': ['B3', 'B4', 'B5']
}, index=[3, 4, 5])

df3 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']
}, index=[0, 1, 2])

print("df1:")
print(df1)
print("\ndf2:")
print(df2)
print("\ndf3:")
print(df3)

# 縦方向の連結（デフォルト）
print("\n縦方向の連結（df1 + df2）:")
result_v = pd.concat([df1, df2])
print(result_v)

# 横方向の連結
print("\n横方向の連結（df1 + df3）:")
result_h = pd.concat([df1, df3], axis=1)
print(result_h)

# インデックスを無視して連結
print("\nインデックスを無視して連結:")
result_ignore = pd.concat([df1, df2], ignore_index=True)
print(result_ignore)

# キーを使った階層的連結
print("\nキーを使った連結:")
result_keys = pd.concat([df1, df2], keys=['first', 'second'])
print(result_keys)

# 2. merge（マージ）
print("\n--- 2. merge（マージ） ---")

# マージ用のデータ作成
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'city': ['Tokyo', 'Osaka', 'Kyoto', 'Tokyo']
})

orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105],
    'customer_id': [1, 2, 1, 3, 5],
    'product': ['A', 'B', 'C', 'A', 'B'],
    'amount': [1000, 2000, 1500, 1200, 1800]
})

print("customers:")
print(customers)
print("\norders:")
print(orders)

# 内部結合（inner join）- デフォルト
print("\n内部結合（両方に存在するcustomer_idのみ）:")
inner_merge = pd.merge(customers, orders, on='customer_id')
print(inner_merge)

# 左外部結合（left join）
print("\n左外部結合（すべての顧客を保持）:")
left_merge = pd.merge(customers, orders, on='customer_id', how='left')
print(left_merge)

# 右外部結合（right join）
print("\n右外部結合（すべての注文を保持）:")
right_merge = pd.merge(customers, orders, on='customer_id', how='right')
print(right_merge)

# 完全外部結合（outer join）
print("\n完全外部結合（両方のデータを保持）:")
outer_merge = pd.merge(customers, orders, on='customer_id', how='outer')
print(outer_merge)

# 3. 異なる列名でのマージ
print("\n--- 3. 異なる列名でのマージ ---")

# 列名が異なる場合のデータ
products = pd.DataFrame({
    'prod_id': ['A', 'B', 'C', 'D'],
    'prod_name': ['Product A', 'Product B', 'Product C', 'Product D'],
    'price': [1000, 2000, 1500, 2500]
})

orders_renamed = orders.rename(columns={'product': 'prod_id'})

print("異なる列名でマージ:")
result = pd.merge(orders_renamed, products, on='prod_id', how='left')
print(result)

# left_on と right_on を使用
print("\nleft_on と right_on を使用:")
result2 = pd.merge(orders, products, left_on='product', right_on='prod_id', how='left')
print(result2)

# 4. 複数のキーでマージ
print("\n--- 4. 複数のキーでマージ ---")

# 複数キー用のデータ
sales_2022 = pd.DataFrame({
    'product': ['A', 'B', 'C', 'A', 'B'],
    'region': ['East', 'East', 'West', 'West', 'West'],
    'sales_2022': [100, 150, 200, 120, 180]
})

sales_2023 = pd.DataFrame({
    'product': ['A', 'B', 'C', 'A', 'B', 'D'],
    'region': ['East', 'East', 'West', 'West', 'West', 'East'],
    'sales_2023': [110, 160, 210, 130, 190, 50]
})

print("sales_2022:")
print(sales_2022)
print("\nsales_2023:")
print(sales_2023)

print("\n複数のキーでマージ:")
multi_merge = pd.merge(sales_2022, sales_2023, on=['product', 'region'], how='outer')
print(multi_merge)

# 5. join（結合）
print("\n--- 5. join（インデックスベースの結合） ---")

# インデックスを持つデータ
df_a = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3']
}, index=['K0', 'K1', 'K2', 'K3'])

df_b = pd.DataFrame({
    'B': ['B0', 'B1', 'B2', 'B3']
}, index=['K0', 'K1', 'K2', 'K3'])

df_c = pd.DataFrame({
    'C': ['C0', 'C1', 'C2', 'C3']
}, index=['K0', 'K1', 'K2', 'K3'])

print("インデックスでjoin:")
result_join = df_a.join([df_b, df_c])
print(result_join)

# 異なるインデックスでのjoin
df_d = pd.DataFrame({
    'D': ['D1', 'D2', 'D3']
}, index=['K1', 'K2', 'K4'])

print("\n異なるインデックスでjoin（left）:")
result_join_left = df_a.join(df_d, how='left')
print(result_join_left)

print("\n異なるインデックスでjoin（outer）:")
result_join_outer = df_a.join(df_d, how='outer')
print(result_join_outer)

# 6. 実践的な例：売上データの統合
print("\n--- 6. 実践的な例：売上データの統合 ---")

# 商品マスタ
products_master = pd.DataFrame({
    'product_id': [1, 2, 3, 4],
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics'],
    'unit_price': [80000, 3000, 5000, 30000]
})

# 売上トランザクション
transactions = pd.DataFrame({
    'trans_id': range(1, 8),
    'date': pd.date_range('2023-01-01', periods=7),
    'product_id': [1, 2, 1, 3, 4, 2, 3],
    'quantity': [2, 5, 1, 3, 1, 10, 2],
    'customer_id': [101, 102, 103, 101, 104, 105, 102]
})

# 顧客マスタ
customers_master = pd.DataFrame({
    'customer_id': [101, 102, 103, 104, 105],
    'customer_name': ['Company A', 'Company B', 'Company C', 'Company D', 'Company E'],
    'region': ['Tokyo', 'Osaka', 'Tokyo', 'Kyoto', 'Osaka']
})

print("商品マスタ:")
print(products_master)
print("\n売上トランザクション:")
print(transactions)
print("\n顧客マスタ:")
print(customers_master)

# データの統合
# 1. トランザクションに商品情報を追加
result = pd.merge(transactions, products_master, on='product_id', how='left')

# 2. 顧客情報を追加
result = pd.merge(result, customers_master, on='customer_id', how='left')

# 3. 売上金額を計算
result['total_amount'] = result['quantity'] * result['unit_price']

print("\n統合された売上データ:")
print(result)

# 集計
print("\n地域別・カテゴリ別売上:")
summary = result.groupby(['region', 'category'])['total_amount'].sum().unstack(fill_value=0)
print(summary)

# 7. サフィックスの処理
print("\n--- 7. 同じ列名の処理（サフィックス） ---")

df_2022 = pd.DataFrame({
    'product': ['A', 'B', 'C'],
    'sales': [100, 200, 300],
    'profit': [20, 40, 60]
})

df_2023 = pd.DataFrame({
    'product': ['A', 'B', 'C'],
    'sales': [110, 220, 280],
    'profit': [25, 45, 55]
})

# デフォルトのサフィックス
print("デフォルトのサフィックス:")
result_suffix = pd.merge(df_2022, df_2023, on='product')
print(result_suffix)

# カスタムサフィックス
print("\nカスタムサフィックス:")
result_custom = pd.merge(df_2022, df_2023, on='product', 
                        suffixes=('_2022', '_2023'))
print(result_custom)

print("\nデータの結合とマージの例を完了しました！")