#!/usr/bin/env python3
"""
Pandasチュートリアル - 例9: データの可視化
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 日本語フォント設定（必要に応じて変更）
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['figure.figsize'] = (10, 6)

print("=== データの可視化 ===\n")

# サンプルデータの作成
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=100)
df = pd.DataFrame({
    'date': dates,
    'sales': np.random.randn(100).cumsum() + 100,
    'profit': np.random.randn(100).cumsum() + 50,
    'customers': np.random.randint(50, 150, 100),
    'category': np.random.choice(['A', 'B', 'C'], 100),
    'region': np.random.choice(['East', 'West', 'North', 'South'], 100)
})

# 1. 線グラフ
print("--- 1. 線グラフ ---")
plt.figure(figsize=(12, 6))
df.set_index('date')[['sales', 'profit']].plot(figsize=(12, 6))
plt.title('Sales and Profit Trend')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend(['Sales', 'Profit'])
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# サブプロットで表示
df.set_index('date')[['sales', 'profit']].plot(subplots=True, figsize=(12, 8))
plt.tight_layout()
plt.show()

# 2. 棒グラフ
print("\n--- 2. 棒グラフ ---")
# カテゴリ別集計
category_sales = df.groupby('category')['sales'].sum()

plt.figure(figsize=(8, 6))
category_sales.plot(kind='bar', color=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

# 横棒グラフ
region_profit = df.groupby('region')['profit'].sum().sort_values()
plt.figure(figsize=(8, 6))
region_profit.plot(kind='barh', color='steelblue')
plt.title('Total Profit by Region')
plt.xlabel('Total Profit')
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.show()

# 3. ヒストグラム
print("\n--- 3. ヒストグラム ---")
plt.figure(figsize=(10, 6))
df['customers'].plot(kind='hist', bins=20, alpha=0.7, color='purple', edgecolor='black')
plt.title('Customer Distribution')
plt.xlabel('Number of Customers')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

# 複数列のヒストグラム
df[['sales', 'profit']].plot(kind='hist', bins=15, alpha=0.7, figsize=(10, 6))
plt.title('Sales and Profit Distribution')
plt.xlabel('Value')
plt.legend()
plt.tight_layout()
plt.show()

# 4. 箱ひげ図
print("\n--- 4. 箱ひげ図 ---")
# カテゴリ別の箱ひげ図
df_box = df.pivot(columns='category', values='sales')
plt.figure(figsize=(8, 6))
df_box.plot(kind='box')
plt.title('Sales Distribution by Category')
plt.ylabel('Sales')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

# 5. 散布図
print("\n--- 5. 散布図 ---")
plt.figure(figsize=(10, 8))
df.plot(kind='scatter', x='sales', y='profit', c='customers', 
        colormap='viridis', s=50, alpha=0.6)
plt.title('Sales vs Profit (colored by Customers)')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.colorbar(label='Number of Customers')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 6. 面グラフ
print("\n--- 6. 面グラフ ---")
# 地域別の日次売上
daily_regional = df.pivot_table(values='sales', index='date', columns='region', aggfunc='sum')
plt.figure(figsize=(12, 6))
daily_regional.plot(kind='area', alpha=0.7, stacked=True)
plt.title('Daily Sales by Region (Stacked)')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 7. 円グラフ
print("\n--- 7. 円グラフ ---")
plt.figure(figsize=(8, 8))
category_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90, 
                    colors=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Sales Distribution by Category')
plt.ylabel('')  # Y軸ラベルを消す
plt.tight_layout()
plt.show()

# 8. 高度な可視化（Seabornとの連携）
print("\n--- 8. 高度な可視化 ---")

# ペアプロット
numerical_cols = ['sales', 'profit', 'customers']
plt.figure(figsize=(10, 10))
sns.pairplot(df[numerical_cols + ['category']], hue='category', diag_kind='kde')
plt.suptitle('Pairplot of Numerical Variables', y=1.02)
plt.tight_layout()
plt.show()

# ヒートマップ（相関行列）
plt.figure(figsize=(8, 6))
correlation = df[numerical_cols].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# 9. カスタムスタイリング
print("\n--- 9. カスタムスタイリング ---")

# スタイル設定
plt.style.use('seaborn-v0_8-darkgrid')
colors = plt.cm.Set3(np.linspace(0, 1, 3))

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 左上：線グラフ（カスタムカラー）
ax = axes[0, 0]
df.set_index('date')['sales'].rolling(7).mean().plot(ax=ax, color='darkblue', linewidth=2)
ax.set_title('7-Day Moving Average of Sales', fontsize=14, fontweight='bold')
ax.set_ylabel('Sales', fontsize=12)
ax.grid(True, alpha=0.3)

# 右上：棒グラフ（グラデーション）
ax = axes[0, 1]
monthly_sales = df.set_index('date')['sales'].resample('M').sum()
bars = ax.bar(range(len(monthly_sales)), monthly_sales.values)
for i, bar in enumerate(bars):
    bar.set_color(plt.cm.viridis(i / len(bars)))
ax.set_title('Monthly Sales', fontsize=14, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Total Sales', fontsize=12)

# 左下：カテゴリ別箱ひげ図（カスタムカラー）
ax = axes[1, 0]
df.boxplot(column='profit', by='category', ax=ax, patch_artist=True)
ax.set_title('Profit Distribution by Category', fontsize=14, fontweight='bold')
ax.set_xlabel('Category', fontsize=12)
ax.set_ylabel('Profit', fontsize=12)

# 右下：散布図（サイズと色のカスタマイズ）
ax = axes[1, 1]
scatter = ax.scatter(df['sales'], df['profit'], 
                    c=df['customers'], s=df['customers']/2,
                    alpha=0.6, cmap='plasma')
ax.set_title('Sales vs Profit', fontsize=14, fontweight='bold')
ax.set_xlabel('Sales', fontsize=12)
ax.set_ylabel('Profit', fontsize=12)
plt.colorbar(scatter, ax=ax, label='Customers')

plt.suptitle('Custom Styled Dashboard', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# 10. DataFrameスタイリング（HTMLレポート用）
print("\n--- 10. DataFrameスタイリング ---")

# 集計データの作成
summary = df.groupby('category').agg({
    'sales': ['mean', 'sum', 'std'],
    'profit': ['mean', 'sum'],
    'customers': ['mean', 'sum']
}).round(2)

# スタイリング関数
def highlight_max(s):
    is_max = s == s.max()
    return ['background-color: lightgreen' if v else '' for v in is_max]

def color_negative(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

# スタイルの適用
styled = summary.style.\
    apply(highlight_max, subset=[('sales', 'sum'), ('profit', 'sum')]).\
    applymap(color_negative, subset=[('profit', 'mean')]).\
    set_caption("Category Performance Summary").\
    set_properties(**{'text-align': 'center'})

# 表示（Jupyter Notebookで効果的）
print("スタイル付きDataFrame（HTML出力用）:")
print(summary)

# グラフの保存例
print("\n--- グラフの保存 ---")
fig, ax = plt.subplots(figsize=(10, 6))
df.groupby('category')['sales'].mean().plot(kind='bar', ax=ax)
ax.set_title('Average Sales by Category')
ax.set_ylabel('Average Sales')
ax.set_xlabel('Category')
plt.xticks(rotation=0)
plt.tight_layout()

# 保存（高解像度）
# plt.savefig('sales_by_category.png', dpi=300, bbox_inches='tight')
# plt.savefig('sales_by_category.pdf', bbox_inches='tight')

plt.show()

print("\nデータの可視化の例を完了しました！")