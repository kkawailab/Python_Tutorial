#!/usr/bin/env python3
"""
Seabornチュートリアル - 例6: ペアプロットとファセットグリッド
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# スタイル設定
sns.set_theme(style="ticks")

# データの準備
iris = sns.load_dataset("iris")
tips = sns.load_dataset("tips")
titanic = sns.load_dataset("titanic")

print("=== ペアプロットとファセットグリッド ===\n")

# 1. 基本的なペアプロット
print("--- 1. 基本的なペアプロット ---")
g = sns.pairplot(iris)
g.fig.suptitle("Basic Pairplot of Iris Dataset", y=1.02)
plt.show()

# hueで色分け
g = sns.pairplot(iris, hue="species")
g.fig.suptitle("Pairplot with Species Coloring", y=1.02)
plt.show()

# 2. カスタマイズされたペアプロット
print("\n--- 2. カスタマイズされたペアプロット ---")
# 対角線のプロットタイプを変更
g = sns.pairplot(iris, hue="species", 
                 diag_kind="kde",  # 'hist' or 'kde'
                 plot_kws={'alpha': 0.6, 's': 80, 'edgecolor': 'k'},
                 diag_kws={'alpha': 0.5})
g.fig.suptitle("Customized Pairplot", y=1.02)
plt.show()

# マーカーの変更
g = sns.pairplot(iris, hue="species", 
                 markers=["o", "s", "D"],
                 palette="Set2")
g.fig.suptitle("Pairplot with Different Markers", y=1.02)
plt.show()

# 3. 特定の変数のみでペアプロット
print("\n--- 3. 選択的ペアプロット ---")
# 特定の変数のみ
selected_vars = ['sepal_length', 'sepal_width', 'petal_length']
g = sns.pairplot(iris[selected_vars + ['species']], 
                 hue="species", height=3)
g.fig.suptitle("Pairplot with Selected Variables", y=1.02)
plt.show()

# 下三角のみ（corner=True）
g = sns.pairplot(tips[['total_bill', 'tip', 'size']], 
                 corner=True, kind="reg")
g.fig.suptitle("Corner Pairplot with Regression", y=1.02)
plt.show()

# 4. 基本的なFacetGrid
print("\n--- 4. 基本的なFacetGrid ---")
# 単一の行/列
g = sns.FacetGrid(tips, col="time", height=5)
g.map(plt.hist, "total_bill", bins=20)
g.fig.suptitle("FacetGrid: Histogram by Time", y=1.02)
plt.show()

# 行と列の両方
g = sns.FacetGrid(tips, row="sex", col="time", height=4)
g.map(plt.scatter, "total_bill", "tip")
g.add_legend()
g.fig.suptitle("FacetGrid: Row and Column Split", y=1.02)
plt.show()

# 5. FacetGridの高度な使用
print("\n--- 5. 高度なFacetGrid ---")
# hueパラメータの追加
g = sns.FacetGrid(tips, col="day", hue="sex", 
                  height=4, aspect=0.8, col_wrap=2)
g.map(plt.scatter, "total_bill", "tip", alpha=0.7)
g.add_legend()
g.fig.suptitle("FacetGrid with Hue and Column Wrap", y=1.02)
plt.show()

# カスタム関数のマッピング
def custom_hist(x, **kwargs):
    plt.hist(x, **kwargs)
    plt.axvline(x.mean(), color='red', linestyle='--', linewidth=2)
    plt.axvline(x.median(), color='green', linestyle='--', linewidth=2)

g = sns.FacetGrid(tips, col="time", row="smoker", height=4)
g.map(custom_hist, "total_bill", bins=15, alpha=0.7)
g.fig.suptitle("Custom Function Mapping", y=1.02)
plt.show()

# 6. カテゴリプロット（catplot）
print("\n--- 6. カテゴリプロット（catplot） ---")
# 複数のプロットタイプ
plot_types = ['strip', 'box', 'violin', 'bar']
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

for idx, kind in enumerate(plot_types):
    plt.subplot(2, 2, idx + 1)
    if kind == 'strip':
        g = sns.catplot(data=tips, x="day", y="total_bill", 
                       kind=kind, height=4, aspect=1)
    else:
        ax = axes[idx // 2, idx % 2]
        if kind == 'box':
            sns.boxplot(data=tips, x="day", y="total_bill", ax=ax)
        elif kind == 'violin':
            sns.violinplot(data=tips, x="day", y="total_bill", ax=ax)
        elif kind == 'bar':
            sns.barplot(data=tips, x="day", y="total_bill", ax=ax)
    
    if idx == 0:
        plt.close(g.fig)
    else:
        axes[idx // 2, idx % 2].set_title(f'{kind.capitalize()} Plot')

plt.suptitle("Different Category Plot Types", fontsize=16)
plt.tight_layout()
plt.show()

# 7. 複雑なFacetGrid
print("\n--- 7. 複雑なFacetGrid ---")
# 複数の変数でファセット
g = sns.FacetGrid(tips, col="time", row="smoker", 
                  hue="sex", height=4, aspect=1.2,
                  margin_titles=True)
g.map(sns.scatterplot, "total_bill", "tip", alpha=0.7)
g.add_legend()
g.fig.suptitle("Complex FacetGrid with Multiple Variables", y=1.02)

# 各サブプロットにタイトルを追加
for ax in g.axes.flat:
    ax.set_xlabel("Total Bill ($)")
    ax.set_ylabel("Tip ($)")

plt.show()

# 8. PairGridの使用
print("\n--- 8. PairGrid（より柔軟なペアプロット） ---")
g = sns.PairGrid(iris, hue="species")

# 異なるプロットタイプを各部分に適用
g.map_upper(sns.scatterplot, alpha=0.5)
g.map_lower(sns.kdeplot)
g.map_diag(sns.histplot, kde=True)

g.add_legend()
g.fig.suptitle("PairGrid with Different Plot Types", y=1.02)
plt.show()

# 9. 時系列データのFacetGrid
print("\n--- 9. 時系列FacetGrid ---")
# 時系列データの作成
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=365, freq='D')
categories = ['A', 'B', 'C']
time_data = []

for cat in categories:
    for date in dates:
        value = np.sin(date.dayofyear * 2 * np.pi / 365) + np.random.randn() * 0.2
        if cat == 'B':
            value += 1
        elif cat == 'C':
            value += 2
        time_data.append({
            'date': date,
            'category': cat,
            'value': value,
            'month': date.month
        })

time_df = pd.DataFrame(time_data)

# 月別のファセット
g = sns.FacetGrid(time_df[time_df['month'] <= 6], 
                  col="month", hue="category",
                  col_wrap=3, height=4)
g.map(sns.lineplot, "date", "value")
g.add_legend()
g.fig.suptitle("Time Series by Month", y=1.02)

# X軸の日付フォーマット
for ax in g.axes.flat:
    ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

# 10. インタラクティブな探索
print("\n--- 10. データ探索ダッシュボード ---")
# 複数の視点からデータを探索
fig = plt.figure(figsize=(16, 12))

# 1. ペアプロット（主要変数）
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2, rowspan=2)
numeric_cols = tips.select_dtypes(include=[np.number]).columns[:3]
for i, col1 in enumerate(numeric_cols):
    for j, col2 in enumerate(numeric_cols):
        if i < j:
            ax1.scatter(tips[col1], tips[col2], alpha=0.5, s=20)

ax1.set_title("Pairwise Relationships")
ax1.set_xlabel("Various Features")
ax1.set_ylabel("Various Features")

# 2. カテゴリ別分布
ax2 = plt.subplot2grid((3, 3), (0, 2))
sns.violinplot(data=tips, x="day", y="total_bill", ax=ax2)
ax2.set_title("Distribution by Day")
ax2.tick_params(axis='x', rotation=45)

# 3. 時間別比較
ax3 = plt.subplot2grid((3, 3), (1, 2))
sns.boxplot(data=tips, x="time", y="tip", ax=ax3)
ax3.set_title("Tips by Time")

# 4. 相関ヒートマップ
ax4 = plt.subplot2grid((3, 3), (2, 0), colspan=2)
corr = tips[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, ax=ax4)
ax4.set_title("Correlation Matrix")

# 5. カウントプロット
ax5 = plt.subplot2grid((3, 3), (2, 2))
sns.countplot(data=tips, x="day", hue="time", ax=ax5)
ax5.set_title("Counts by Day and Time")
ax5.tick_params(axis='x', rotation=45)

plt.suptitle("Multi-View Data Exploration Dashboard", fontsize=16)
plt.tight_layout()
plt.show()

print("\nペアプロットとファセットグリッドの例を完了しました！")