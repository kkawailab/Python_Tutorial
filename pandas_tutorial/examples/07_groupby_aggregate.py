#!/usr/bin/env python3
"""
Pandasチュートリアル - 例7: グループ化と集計
"""

import pandas as pd
import numpy as np

print("=== グループ化と集計 ===\n")

# サンプルデータの作成
np.random.seed(42)
sales_data = pd.DataFrame({
    'date': pd.date_range('2023-01-01', periods=100),
    'store': np.random.choice(['Tokyo', 'Osaka', 'Kyoto'], 100),
    'product': np.random.choice(['A', 'B', 'C'], 100),
    'quantity': np.random.randint(1, 20, 100),
    'price': np.random.randint(100, 1000, 100),
    'customer_type': np.random.choice(['Regular', 'VIP'], 100)
})
sales_data['total'] = sales_data['quantity'] * sales_data['price']

print("売上データ（最初の10行）:")
print(sales_data.head(10))

# 1. 基本的なグループ化
print("\n--- 1. 基本的なグループ化 ---")

# 単一列でグループ化
grouped_store = sales_data.groupby('store')
print("店舗別の平均売上:")
print(grouped_store['total'].mean())

# 複数の集計関数
print("\n店舗別の統計:")
print(grouped_store['total'].agg(['mean', 'sum', 'count', 'std']))

# 複数列でグループ化
grouped_multi = sales_data.groupby(['store', 'product'])
print("\n店舗・商品別の合計売上:")
print(grouped_multi['total'].sum())

# 2. 複数の列に対する集計
print("\n--- 2. 複数の列に対する集計 ---")

# 基本的な集計
print("店舗別の複数列集計:")
print(grouped_store[['quantity', 'total']].sum())

# 異なる集計関数を各列に適用
agg_dict = {
    'quantity': ['sum', 'mean'],
    'price': ['mean', 'max', 'min'],
    'total': ['sum', 'mean', 'count']
}
print("\n詳細な集計:")
result = grouped_store.agg(agg_dict)
print(result)

# 3. カスタム集計関数
print("\n--- 3. カスタム集計関数 ---")

# カスタム関数の定義
def revenue_range(series):
    return series.max() - series.min()

def top_percentile(series, percentile=90):
    return series.quantile(percentile / 100)

# カスタム関数の適用
print("店舗別の売上レンジ:")
print(grouped_store['total'].agg(revenue_range))

print("\n店舗別の90パーセンタイル売上:")
print(grouped_store['total'].agg(lambda x: top_percentile(x, 90)))

# 複数のカスタム関数
print("\n複数のカスタム集計:")
custom_agg = grouped_store['total'].agg([
    ('range', revenue_range),
    ('p90', lambda x: top_percentile(x, 90)),
    ('cv', lambda x: x.std() / x.mean())  # 変動係数
])
print(custom_agg)

# 4. transform メソッド
print("\n--- 4. transform メソッド ---")

# グループ内での正規化
sales_data['normalized_total'] = grouped_store['total'].transform(
    lambda x: (x - x.mean()) / x.std()
)

# グループ内でのランキング
sales_data['rank_in_store'] = grouped_store['total'].transform('rank', ascending=False)

print("transform後のデータ（最初の10行）:")
print(sales_data[['store', 'total', 'normalized_total', 'rank_in_store']].head(10))

# グループごとの累積和
sales_data['cumsum_by_store'] = grouped_store['total'].transform('cumsum')
print("\n店舗別累積売上（一部）:")
print(sales_data[['date', 'store', 'total', 'cumsum_by_store']].head(10))

# 5. filter メソッド
print("\n--- 5. filter メソッド ---")

# 平均売上が5000以上の店舗のデータのみ
high_sales_stores = sales_data.groupby('store').filter(
    lambda x: x['total'].mean() > 5000
)
print("平均売上が5000以上の店舗:")
print(high_sales_stores['store'].unique())

# 取引数が30以上の店舗
active_stores = sales_data.groupby('store').filter(
    lambda x: len(x) >= 30
)
print("\n取引数が30以上の店舗:")
print(active_stores.groupby('store').size())

# 6. ピボットテーブル
print("\n--- 6. ピボットテーブル ---")

# 基本的なピボットテーブル
pivot_basic = sales_data.pivot_table(
    values='total',
    index='store',
    columns='product',
    aggfunc='sum'
)
print("店舗×商品の売上合計:")
print(pivot_basic)

# 複数の値と集計関数
pivot_multi = sales_data.pivot_table(
    values=['quantity', 'total'],
    index='store',
    columns='product',
    aggfunc={'quantity': 'sum', 'total': ['sum', 'mean']}
)
print("\n複数の集計を含むピボットテーブル:")
print(pivot_multi)

# マージン（合計）を追加
pivot_margins = sales_data.pivot_table(
    values='total',
    index='store',
    columns='customer_type',
    aggfunc='sum',
    margins=True,
    margins_name='Total'
)
print("\n合計付きピボットテーブル:")
print(pivot_margins)

# 7. クロス集計
print("\n--- 7. クロス集計 ---")

# 基本的なクロス集計（カウント）
cross_basic = pd.crosstab(sales_data['store'], sales_data['product'])
print("店舗×商品のクロス集計:")
print(cross_basic)

# パーセンテージ表示
cross_pct = pd.crosstab(
    sales_data['store'], 
    sales_data['product'],
    normalize='index'  # 行方向で正規化
) * 100
print("\n店舗別の商品構成比（%）:")
print(cross_pct.round(1))

# 値の集計を含むクロス集計
cross_values = pd.crosstab(
    sales_data['store'],
    sales_data['customer_type'],
    values=sales_data['total'],
    aggfunc='sum'
)
print("\n店舗×顧客タイプ別売上:")
print(cross_values)

# 8. 時系列のグループ化
print("\n--- 8. 時系列のグループ化 ---")

# 月別集計
sales_data['month'] = sales_data['date'].dt.to_period('M')
monthly_sales = sales_data.groupby(['month', 'store'])['total'].sum().unstack()
print("月別・店舗別売上:")
print(monthly_sales)

# 曜日別集計
sales_data['dayofweek'] = sales_data['date'].dt.day_name()
dow_sales = sales_data.groupby('dayofweek')['total'].agg(['mean', 'count'])
print("\n曜日別の平均売上と取引数:")
print(dow_sales)

# 9. グループごとの高度な操作
print("\n--- 9. グループごとの高度な操作 ---")

# 各グループの上位N件を取得
def get_top_n(group, n=3):
    return group.nlargest(n, 'total')

top_sales = sales_data.groupby('store').apply(get_top_n, n=3)
print("各店舗の売上トップ3:")
print(top_sales[['store', 'date', 'product', 'total']])

# グループごとの相関
def calc_correlation(group):
    return group[['quantity', 'price', 'total']].corr().loc['quantity', 'price']

correlation_by_store = sales_data.groupby('store').apply(calc_correlation)
print("\n店舗別の数量-価格相関:")
print(correlation_by_store)

# 10. 実践的な分析例
print("\n--- 10. 実践的な分析例 ---")

# 包括的な店舗パフォーマンス分析
store_performance = sales_data.groupby('store').agg({
    'total': ['sum', 'mean', 'count'],
    'quantity': 'sum',
    'customer_type': lambda x: (x == 'VIP').sum()
}).round(2)

# カラム名を整理
store_performance.columns = ['total_sales', 'avg_transaction', 'num_transactions', 
                            'total_quantity', 'vip_customers']

# KPIを追加
store_performance['avg_quantity_per_trans'] = (
    store_performance['total_quantity'] / store_performance['num_transactions']
).round(2)

store_performance['vip_ratio'] = (
    store_performance['vip_customers'] / store_performance['num_transactions'] * 100
).round(1)

print("店舗パフォーマンス分析:")
print(store_performance)

print("\nグループ化と集計の例を完了しました！")