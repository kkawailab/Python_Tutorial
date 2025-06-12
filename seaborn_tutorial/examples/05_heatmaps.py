#!/usr/bin/env python3
"""
Seabornチュートリアル - 例5: ヒートマップと相関行列
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# スタイル設定
sns.set_theme(style="white")

# データの準備
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
flights = sns.load_dataset("flights")

print("=== ヒートマップと相関行列 ===\n")

# 1. 基本的なヒートマップ
print("--- 1. 基本的なヒートマップ ---")
# フライトデータをピボット
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

plt.figure(figsize=(12, 8))
sns.heatmap(flights_pivot)
plt.title("Basic Heatmap: Flight Passengers")
plt.show()

# アノテーション付きヒートマップ
plt.figure(figsize=(14, 10))
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlOrRd")
plt.title("Annotated Heatmap")
plt.show()

# 2. 相関行列のヒートマップ
print("\n--- 2. 相関行列 ---")
# 数値データの相関行列
numeric_tips = tips.select_dtypes(include=[np.number])
correlation = numeric_tips.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap="coolwarm", 
            center=0, square=True, linewidths=1,
            cbar_kws={"shrink": 0.8})
plt.title("Correlation Heatmap")
plt.show()

# マスク付きヒートマップ（上三角のみ表示）
mask = np.triu(np.ones_like(correlation), k=1)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, mask=mask, annot=True, 
            cmap="RdBu_r", center=0, square=True,
            vmin=-1, vmax=1)
plt.title("Triangular Correlation Heatmap")
plt.show()

# 3. カスタムカラーマップ
print("\n--- 3. カスタムカラーマップ ---")
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# 異なるカラーマップ
cmaps = ['viridis', 'plasma', 'coolwarm', 'RdYlBu_r']
for ax, cmap in zip(axes.flat, cmaps):
    sns.heatmap(flights_pivot.iloc[:6, :6], cmap=cmap, 
                annot=True, fmt="d", ax=ax,
                cbar_kws={'label': 'Passengers'})
    ax.set_title(f'Colormap: {cmap}')

plt.tight_layout()
plt.show()

# 4. クラスターマップ
print("\n--- 4. クラスターマップ ---")
# アイリスデータセットの数値部分
iris_data = iris.iloc[:, :-1]

# 標準化
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
iris_scaled = pd.DataFrame(
    scaler.fit_transform(iris_data),
    columns=iris_data.columns
)

# クラスターマップ
g = sns.clustermap(iris_scaled.T, cmap="viridis", 
                   figsize=(10, 8), 
                   row_cluster=True, col_cluster=True)
g.fig.suptitle("Hierarchical Clustering Heatmap", y=1.02)
plt.show()

# 5. カスタムヒートマップ（欠損値の可視化）
print("\n--- 5. 欠損値の可視化 ---")
# 欠損値を含むデータの作成
missing_data = tips.copy()
# ランダムに欠損値を追加
np.random.seed(42)
for col in ['total_bill', 'tip', 'size']:
    missing_indices = np.random.choice(missing_data.index, size=20, replace=False)
    missing_data.loc[missing_indices, col] = np.nan

# 欠損値パターンの可視化
plt.figure(figsize=(10, 8))
missing_pattern = missing_data.isnull().astype(int)
sns.heatmap(missing_pattern.T, cmap="RdYlGn_r", 
            cbar_kws={'label': 'Missing (1) / Present (0)'},
            yticklabels=missing_pattern.columns)
plt.title("Missing Value Pattern")
plt.xlabel("Sample Index")
plt.show()

# 6. 時系列ヒートマップ
print("\n--- 6. 時系列ヒートマップ ---")
# 時系列データの作成
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=365, freq='D')
hours = np.arange(24)
data = np.random.randn(365, 24) + np.sin(np.arange(365) * 2 * np.pi / 365)[:, np.newaxis]
time_data = pd.DataFrame(data, index=dates, columns=hours)

# 月別・時間別の平均
monthly_hourly = time_data.resample('M').mean().T

plt.figure(figsize=(14, 8))
sns.heatmap(monthly_hourly, cmap="coolwarm", center=0,
            xticklabels=[d.strftime('%b') for d in monthly_hourly.columns],
            cbar_kws={'label': 'Average Value'})
plt.title("Monthly-Hourly Heatmap")
plt.xlabel("Month")
plt.ylabel("Hour of Day")
plt.show()

# 7. 分割ヒートマップ
print("\n--- 7. 分割ヒートマップ ---")
# カテゴリ別の平均値を計算
pivot_data = tips.pivot_table(
    values='tip',
    index='day',
    columns=['time', 'sex'],
    aggfunc='mean'
)

plt.figure(figsize=(12, 6))
sns.heatmap(pivot_data, annot=True, fmt=".2f", 
            cmap="YlGnBu", linewidths=2)
plt.title("Average Tip by Day, Time, and Sex")
plt.show()

# 8. カスタムアノテーション
print("\n--- 8. カスタムアノテーション ---")
# パーセンテージとして表示
percentage_data = (flights_pivot / flights_pivot.sum().sum() * 100)

plt.figure(figsize=(14, 10))
ax = sns.heatmap(percentage_data, annot=True, fmt=".1f", 
                 cmap="Blues", cbar_kws={'label': 'Percentage (%)'})

# カスタムアノテーション（%記号を追加）
for text in ax.texts:
    text.set_text(text.get_text() + "%")

plt.title("Flight Passengers as Percentage of Total")
plt.show()

# 9. 複数のヒートマップ
print("\n--- 9. 複数のヒートマップ ---")
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# 平均
pivot_mean = tips.pivot_table(values='total_bill', index='day', 
                             columns='time', aggfunc='mean')
sns.heatmap(pivot_mean, annot=True, fmt=".1f", 
            cmap="Greens", ax=axes[0])
axes[0].set_title("Mean Total Bill")

# 中央値
pivot_median = tips.pivot_table(values='total_bill', index='day', 
                               columns='time', aggfunc='median')
sns.heatmap(pivot_median, annot=True, fmt=".1f", 
            cmap="Blues", ax=axes[1])
axes[1].set_title("Median Total Bill")

# カウント
pivot_count = tips.pivot_table(values='total_bill', index='day', 
                              columns='time', aggfunc='count')
sns.heatmap(pivot_count, annot=True, fmt="d", 
            cmap="Oranges", ax=axes[2])
axes[2].set_title("Count")

plt.tight_layout()
plt.show()

# 10. 相関の強さによる色分け
print("\n--- 10. 相関の強さによる色分け ---")
# より大きなデータセットの相関行列
# ランダムデータの生成
np.random.seed(42)
n_features = 15
feature_names = [f'Feature_{i}' for i in range(n_features)]
random_data = pd.DataFrame(
    np.random.randn(100, n_features),
    columns=feature_names
)

# いくつかの相関を追加
random_data['Feature_1'] = random_data['Feature_0'] * 0.8 + np.random.randn(100) * 0.2
random_data['Feature_3'] = -random_data['Feature_2'] * 0.7 + np.random.randn(100) * 0.3

corr_matrix = random_data.corr()

# 相関の強さでマスク
strong_corr_mask = np.abs(corr_matrix) < 0.3

plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, mask=strong_corr_mask, 
            annot=True, fmt=".2f", cmap="RdBu_r",
            center=0, vmin=-1, vmax=1)
plt.title("Strong Correlations Only (|r| > 0.3)")
plt.show()

print("\nヒートマップの例を完了しました！")