# Seaborn完全チュートリアル：統計的データ可視化の決定版

## 目次
1. [Seabornとは](#1-seabornとは)
2. [環境設定とインポート](#2-環境設定とインポート)
3. [基本的なプロット](#3-基本的なプロット)
4. [カテゴリカルプロット](#4-カテゴリカルプロット)
5. [分布の可視化](#5-分布の可視化)
6. [回帰プロット](#6-回帰プロット)
7. [ヒートマップと相関行列](#7-ヒートマップと相関行列)
8. [ペアプロットとファセットグリッド](#8-ペアプロットとファセットグリッド)
9. [スタイルとカラーパレット](#9-スタイルとカラーパレット)
10. [時系列データの可視化](#10-時系列データの可視化)
11. [高度な統計プロット](#11-高度な統計プロット)
12. [実践的な応用例とベストプラクティス](#12-実践的な応用例とベストプラクティス)

## 1. Seabornとは

Seabornは、Matplotlibをベースにした統計データ可視化ライブラリです。美しく洗練されたグラフを簡単に作成でき、特に統計的な洞察を得るための可視化に優れています。

### Seabornの特徴

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Seabornのバージョン確認
print(f"Seaborn version: {sns.__version__}")

# サンプルデータセットの確認
print("\n利用可能なデータセット:")
print(sns.get_dataset_names())
```

### なぜSeabornを使うのか

1. **美しいデフォルトスタイル**：最小限のコードで洗練されたグラフを作成
2. **統計的可視化に特化**：分布、回帰、カテゴリ比較などの専門的なプロット
3. **Pandas統合**：DataFrameとの相性が抜群
4. **複雑なプロットの簡素化**：ファセット、ペアプロットなどを簡単に作成

## 2. 環境設定とインポート

### インストールと基本設定

```python
# インストール（コマンドライン）
# pip install seaborn pandas matplotlib scipy

# 基本的なインポート
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

# 日本語フォント設定
plt.rcParams['font.family'] = 'DejaVu Sans'
# Windowsの場合：plt.rcParams['font.family'] = 'MS Gothic'
# Macの場合：plt.rcParams['font.family'] = 'Hiragino Sans'

# Seabornのスタイル設定
sns.set_theme(style="whitegrid", palette="husl")

# 図のDPI設定（高解像度出力用）
plt.rcParams['figure.dpi'] = 100
plt.rcParams['savefig.dpi'] = 300
```

### サンプルデータの準備

```python
# 組み込みデータセットの読み込み
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")

print("Tips dataset:")
print(tips.head())
print(f"\nShape: {tips.shape}")
print(f"Columns: {list(tips.columns)}")
```

## 3. 基本的なプロット

### 散布図（Scatter Plot）

```python
# 基本的な散布図
plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title("Total Bill vs Tip")
plt.show()

# hueパラメータで色分け
plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
plt.title("Total Bill vs Tip by Time")
plt.show()

# size、style、hueを組み合わせた高度な散布図
plt.figure(figsize=(12, 8))
sns.scatterplot(data=tips, x="total_bill", y="tip", 
                hue="day", size="size", style="sex",
                palette="deep", sizes=(50, 200))
plt.title("Advanced Scatter Plot")
plt.show()
```

### 線グラフ（Line Plot）

```python
# 時系列データの作成
dates = pd.date_range('2023-01-01', periods=100)
data = pd.DataFrame({
    'date': dates,
    'value': np.cumsum(np.random.randn(100)) + 50,
    'category': np.random.choice(['A', 'B'], 100)
})

plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='date', y='value', hue='category')
plt.title("Time Series Line Plot")
plt.xticks(rotation=45)
plt.show()

# 信頼区間付き線グラフ
fmri = sns.load_dataset("fmri")
plt.figure(figsize=(10, 6))
sns.lineplot(data=fmri, x="timepoint", y="signal", 
             hue="region", style="event", markers=True)
plt.title("Line Plot with Confidence Intervals")
plt.show()
```

## 4. カテゴリカルプロット

### 棒グラフ（Bar Plot）

```python
# 基本的な棒グラフ
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x="day", y="total_bill")
plt.title("Average Total Bill by Day")
plt.show()

# hueで分割した棒グラフ
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x="day", y="total_bill", hue="sex")
plt.title("Average Total Bill by Day and Gender")
plt.show()

# エラーバーのカスタマイズ
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x="day", y="total_bill", 
            errorbar="sd", capsize=0.2)
plt.title("Total Bill by Day with Standard Deviation")
plt.show()
```

### 箱ひげ図（Box Plot）

```python
# 基本的な箱ひげ図
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("Total Bill Distribution by Day")
plt.show()

# 複数カテゴリの箱ひげ図
plt.figure(figsize=(12, 6))
sns.boxplot(data=tips, x="day", y="total_bill", hue="time")
plt.title("Total Bill Distribution by Day and Time")
plt.show()

# 横向きの箱ひげ図
plt.figure(figsize=(10, 8))
sns.boxplot(data=tips, y="day", x="total_bill", orient="h")
plt.title("Horizontal Box Plot")
plt.show()
```

### バイオリンプロット（Violin Plot）

```python
# 基本的なバイオリンプロット
plt.figure(figsize=(10, 6))
sns.violinplot(data=tips, x="day", y="total_bill")
plt.title("Total Bill Distribution by Day (Violin Plot)")
plt.show()

# 分割バイオリンプロット
plt.figure(figsize=(12, 6))
sns.violinplot(data=tips, x="day", y="total_bill", 
               hue="sex", split=True)
plt.title("Split Violin Plot by Gender")
plt.show()

# 内部の分布表示オプション
plt.figure(figsize=(14, 6))
fig, axes = plt.subplots(1, 3, figsize=(14, 6))

# クォータイル
sns.violinplot(data=tips, x="day", y="total_bill", 
               inner="quartiles", ax=axes[0])
axes[0].set_title("Quartiles")

# ボックス
sns.violinplot(data=tips, x="day", y="total_bill", 
               inner="box", ax=axes[1])
axes[1].set_title("Box")

# ポイント
sns.violinplot(data=tips, x="day", y="total_bill", 
               inner="points", ax=axes[2])
axes[2].set_title("Points")

plt.tight_layout()
plt.show()
```

### スウォームプロット（Swarm Plot）

```python
# 基本的なスウォームプロット
plt.figure(figsize=(10, 6))
sns.swarmplot(data=tips, x="day", y="total_bill")
plt.title("Swarm Plot of Total Bill by Day")
plt.show()

# カテゴリプロットの組み合わせ
plt.figure(figsize=(12, 8))
sns.violinplot(data=tips, x="day", y="total_bill", 
               inner=None, alpha=0.3)
sns.swarmplot(data=tips, x="day", y="total_bill", 
              color="black", alpha=0.5, size=3)
plt.title("Violin + Swarm Plot Combination")
plt.show()
```

## 5. 分布の可視化

### ヒストグラム（Histogram）

```python
# 基本的なヒストグラム
plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x="total_bill")
plt.title("Distribution of Total Bill")
plt.show()

# KDE（カーネル密度推定）付きヒストグラム
plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x="total_bill", kde=True)
plt.title("Histogram with KDE")
plt.show()

# 複数変数のヒストグラム
plt.figure(figsize=(12, 6))
sns.histplot(data=tips, x="total_bill", hue="time", 
             multiple="dodge", shrink=0.8)
plt.title("Histogram by Time")
plt.show()

# 2次元ヒストグラム
plt.figure(figsize=(10, 8))
sns.histplot(data=tips, x="total_bill", y="tip", 
             cbar=True, cmap="YlOrRd")
plt.title("2D Histogram")
plt.show()
```

### カーネル密度推定（KDE Plot）

```python
# 基本的なKDEプロット
plt.figure(figsize=(10, 6))
sns.kdeplot(data=tips, x="total_bill")
plt.title("KDE of Total Bill")
plt.show()

# 複数グループのKDE
plt.figure(figsize=(10, 6))
sns.kdeplot(data=tips, x="total_bill", hue="time", 
            shade=True, alpha=0.5)
plt.title("KDE by Time")
plt.show()

# 2次元KDE
plt.figure(figsize=(10, 8))
sns.kdeplot(data=tips, x="total_bill", y="tip", 
            cmap="Reds", shade=True, levels=10)
plt.title("2D KDE Plot")
plt.show()

# 累積分布
plt.figure(figsize=(10, 6))
sns.kdeplot(data=tips, x="total_bill", cumulative=True, 
            hue="time", common_norm=False)
plt.title("Cumulative Distribution")
plt.show()
```

### 経験的累積分布関数（ECDF）

```python
# ECDFプロット
plt.figure(figsize=(10, 6))
sns.ecdfplot(data=tips, x="total_bill")
plt.title("ECDF of Total Bill")
plt.show()

# 複数グループのECDF
plt.figure(figsize=(10, 6))
sns.ecdfplot(data=tips, x="total_bill", hue="day")
plt.title("ECDF by Day")
plt.show()
```

## 6. 回帰プロット

### 線形回帰（Linear Regression）

```python
# 基本的な回帰プロット
plt.figure(figsize=(10, 6))
sns.regplot(data=tips, x="total_bill", y="tip")
plt.title("Linear Regression: Total Bill vs Tip")
plt.show()

# 信頼区間のカスタマイズ
plt.figure(figsize=(10, 6))
sns.regplot(data=tips, x="total_bill", y="tip", 
            ci=99, color="red", scatter_kws={'alpha': 0.5})
plt.title("Regression with 99% Confidence Interval")
plt.show()

# 多項式回帰
plt.figure(figsize=(12, 6))
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1次
sns.regplot(data=tips, x="total_bill", y="tip", 
            order=1, ax=axes[0])
axes[0].set_title("Linear (order=1)")

# 2次
sns.regplot(data=tips, x="total_bill", y="tip", 
            order=2, ax=axes[1])
axes[1].set_title("Quadratic (order=2)")

# 3次
sns.regplot(data=tips, x="total_bill", y="tip", 
            order=3, ax=axes[2])
axes[2].set_title("Cubic (order=3)")

plt.tight_layout()
plt.show()
```

### 残差プロット（Residual Plot）

```python
# 残差プロット
plt.figure(figsize=(10, 6))
sns.residplot(data=tips, x="total_bill", y="tip", 
              lowess=True, color="g")
plt.title("Residual Plot")
plt.axhline(0, color='red', linestyle='--')
plt.show()
```

### カテゴリ別回帰（lmplot）

```python
# カテゴリ別の回帰線
g = sns.lmplot(data=tips, x="total_bill", y="tip", 
               hue="smoker", col="time", row="sex",
               height=4, aspect=1.2)
g.fig.suptitle("Regression by Multiple Categories", y=1.02)
plt.show()

# 信頼区間なしの回帰
g = sns.lmplot(data=tips, x="total_bill", y="tip", 
               hue="day", ci=None, palette="Set1",
               height=6, aspect=1.5)
plt.title("Regression by Day without CI")
plt.show()
```

## 7. ヒートマップと相関行列

### 相関行列のヒートマップ

```python
# 数値データの相関行列
numeric_tips = tips.select_dtypes(include=[np.number])
correlation = numeric_tips.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap="coolwarm", 
            center=0, square=True, linewidths=1)
plt.title("Correlation Heatmap")
plt.show()

# マスク付きヒートマップ（上三角のみ表示）
mask = np.triu(np.ones_like(correlation), k=1)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, mask=mask, annot=True, 
            cmap="RdBu_r", center=0, square=True)
plt.title("Triangular Correlation Heatmap")
plt.show()
```

### クラスターマップ

```python
# 階層的クラスタリング付きヒートマップ
plt.figure(figsize=(12, 10))
g = sns.clustermap(iris.iloc[:, :-1], cmap="viridis", 
                   standard_scale=1, figsize=(10, 10))
g.fig.suptitle("Hierarchical Clustering Heatmap")
plt.show()
```

### カスタムヒートマップ

```python
# カスタムデータでヒートマップ
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

plt.figure(figsize=(14, 8))
sns.heatmap(flights_pivot, annot=True, fmt="d", 
            cmap="YlOrRd", cbar_kws={'label': 'Passengers'})
plt.title("Flight Passengers Heatmap")
plt.show()
```

## 8. ペアプロットとファセットグリッド

### ペアプロット（Pair Plot）

```python
# 基本的なペアプロット
g = sns.pairplot(iris, hue="species")
g.fig.suptitle("Iris Dataset Pairplot", y=1.02)
plt.show()

# カスタマイズされたペアプロット
g = sns.pairplot(iris, hue="species", 
                 diag_kind="kde", 
                 plot_kws={'alpha': 0.6},
                 height=3, aspect=1)
plt.show()

# 特定の変数のみでペアプロット
g = sns.pairplot(tips[['total_bill', 'tip', 'size', 'time']], 
                 hue="time", diag_kind="hist",
                 corner=True)  # 下三角のみ表示
plt.show()
```

### ファセットグリッド（FacetGrid）

```python
# 基本的なファセットグリッド
g = sns.FacetGrid(tips, col="time", row="smoker", 
                  height=4, aspect=1.2)
g.map(sns.scatterplot, "total_bill", "tip")
g.add_legend()
plt.show()

# ヒストグラムのファセットグリッド
g = sns.FacetGrid(tips, col="day", col_wrap=2, height=4)
g.map(sns.histplot, "total_bill", kde=True)
g.set_titles("{col_name}")
plt.show()

# カスタム関数でのマッピング
def custom_plot(x, y, **kwargs):
    plt.scatter(x, y, **kwargs)
    plt.axline((0, 0), slope=0.2, color='red', linestyle='--')

g = sns.FacetGrid(tips, col="time", hue="smoker", height=5)
g.map(custom_plot, "total_bill", "tip")
g.add_legend()
plt.show()
```

### カテゴリプロット（catplot）

```python
# カテゴリプロットの統合インターフェース
g = sns.catplot(data=tips, x="day", y="total_bill", 
                hue="sex", col="time", kind="box",
                height=4, aspect=1.2)
g.fig.suptitle("Box Plots by Multiple Categories", y=1.02)
plt.show()

# 様々なプロットタイプ
plot_types = ['strip', 'swarm', 'box', 'violin', 'bar']
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for idx, kind in enumerate(plot_types):
    if idx < len(axes):
        if kind in ['strip', 'swarm']:
            sns.catplot(data=tips, x="day", y="total_bill", 
                       kind=kind, ax=axes[idx], height=4)
        else:
            ax = axes[idx]
            if kind == 'box':
                sns.boxplot(data=tips, x="day", y="total_bill", ax=ax)
            elif kind == 'violin':
                sns.violinplot(data=tips, x="day", y="total_bill", ax=ax)
            elif kind == 'bar':
                sns.barplot(data=tips, x="day", y="total_bill", ax=ax)
        axes[idx].set_title(f'{kind.capitalize()} Plot')

# 余った軸を削除
if len(plot_types) < len(axes):
    fig.delaxes(axes[-1])

plt.tight_layout()
plt.show()
```

## 9. スタイルとカラーパレット

### Seabornのスタイル

```python
# 利用可能なスタイル
styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for idx, style in enumerate(styles):
    if idx < len(axes):
        with sns.axes_style(style):
            ax = axes[idx]
            tips_sample = tips.sample(50)
            sns.scatterplot(data=tips_sample, x="total_bill", 
                          y="tip", ax=ax)
            ax.set_title(f"Style: {style}")

# 余った軸を削除
if len(styles) < len(axes):
    fig.delaxes(axes[-1])

plt.tight_layout()
plt.show()
```

### カラーパレット

```python
# 組み込みカラーパレット
palettes = ['deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind']
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for idx, palette in enumerate(palettes):
    if idx < len(axes):
        ax = axes[idx]
        sns.barplot(data=tips, x="day", y="total_bill", 
                   hue="time", palette=palette, ax=ax)
        ax.set_title(f"Palette: {palette}")
        ax.legend(loc='upper right')

plt.tight_layout()
plt.show()

# カスタムカラーパレット
custom_palette = sns.color_palette("husl", 8)
plt.figure(figsize=(10, 2))
sns.palplot(custom_palette)
plt.title("Custom Color Palette")
plt.show()

# グラデーションパレット
plt.figure(figsize=(12, 6))
n_colors = 8
palettes_gradient = {
    'Blues': sns.color_palette("Blues", n_colors),
    'Reds': sns.color_palette("Reds", n_colors),
    'Greens': sns.color_palette("Greens", n_colors),
    'RdBu': sns.color_palette("RdBu", n_colors),
    'coolwarm': sns.color_palette("coolwarm", n_colors)
}

fig, axes = plt.subplots(len(palettes_gradient), 1, 
                        figsize=(10, len(palettes_gradient)))
for idx, (name, palette) in enumerate(palettes_gradient.items()):
    sns.palplot(palette, ax=axes[idx])
    axes[idx].set_title(name)
    axes[idx].set_xticks([])

plt.tight_layout()
plt.show()
```

### コンテキスト設定

```python
# 異なるコンテキストでの表示
contexts = ['paper', 'notebook', 'talk', 'poster']
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for idx, context in enumerate(contexts):
    with sns.plotting_context(context):
        ax = axes[idx]
        sns.lineplot(data=tips.groupby('size')['total_bill'].mean().reset_index(),
                    x='size', y='total_bill', ax=ax, marker='o')
        ax.set_title(f"Context: {context}")

plt.tight_layout()
plt.show()
```

## 10. 時系列データの可視化

### 時系列プロット

```python
# 時系列データの準備
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=365, freq='D')
ts_data = pd.DataFrame({
    'date': dates,
    'value': np.cumsum(np.random.randn(365)) + 100,
    'category': np.random.choice(['A', 'B', 'C'], 365),
    'temperature': 20 + 10 * np.sin(np.arange(365) * 2 * np.pi / 365) + np.random.randn(365) * 2
})

# 基本的な時系列プロット
plt.figure(figsize=(14, 6))
sns.lineplot(data=ts_data, x='date', y='value')
plt.title("Time Series Plot")
plt.xticks(rotation=45)
plt.show()

# カテゴリ別時系列
plt.figure(figsize=(14, 6))
sns.lineplot(data=ts_data, x='date', y='value', 
             hue='category', style='category')
plt.title("Time Series by Category")
plt.xticks(rotation=45)
plt.show()

# 移動平均の追加
ts_data['ma7'] = ts_data['value'].rolling(7).mean()
ts_data['ma30'] = ts_data['value'].rolling(30).mean()

plt.figure(figsize=(14, 8))
plt.plot(ts_data['date'], ts_data['value'], 
         alpha=0.3, label='Original')
plt.plot(ts_data['date'], ts_data['ma7'], 
         label='7-day MA', linewidth=2)
plt.plot(ts_data['date'], ts_data['ma30'], 
         label='30-day MA', linewidth=2)
plt.title("Time Series with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### 季節性の可視化

```python
# 月別集計
ts_data['month'] = ts_data['date'].dt.month
ts_data['day_of_year'] = ts_data['date'].dt.dayofyear

# 季節性パターン
plt.figure(figsize=(14, 8))
pivot_seasonal = ts_data.pivot_table(values='temperature', 
                                    index='day_of_year', 
                                    columns=pd.cut(ts_data['date'].dt.month, 
                                                  bins=[0, 3, 6, 9, 12],
                                                  labels=['Winter', 'Spring', 'Summer', 'Fall']))

for season in pivot_seasonal.columns:
    if season in pivot_seasonal:
        plt.plot(pivot_seasonal.index, pivot_seasonal[season], 
                label=season, alpha=0.7)

plt.title("Seasonal Temperature Patterns")
plt.xlabel("Day of Year")
plt.ylabel("Temperature")
plt.legend()
plt.show()

# ヒートマップカレンダー
# 月別・日別のヒートマップ
ts_data['day'] = ts_data['date'].dt.day
monthly_data = ts_data.pivot_table(values='value', 
                                  index='day', 
                                  columns='month')

plt.figure(figsize=(14, 8))
sns.heatmap(monthly_data, cmap='RdYlBu_r', 
            cbar_kws={'label': 'Value'},
            linewidths=0.5)
plt.title("Calendar Heatmap")
plt.xlabel("Month")
plt.ylabel("Day")
plt.show()
```

## 11. 高度な統計プロット

### 統計的推定の可視化

```python
# ブートストラップ信頼区間
plt.figure(figsize=(12, 6))
sns.barplot(data=tips, x="day", y="total_bill", 
            errorbar=('ci', 95), n_boot=1000,
            capsize=0.1)
plt.title("Bar Plot with Bootstrap Confidence Intervals")
plt.show()

# ポイントプロット（平均値と信頼区間）
plt.figure(figsize=(12, 6))
sns.pointplot(data=tips, x="day", y="total_bill", 
              hue="sex", dodge=True, 
              markers=["o", "s"], linestyles=["-", "--"])
plt.title("Point Plot with Confidence Intervals")
plt.show()
```

### 分布の比較

```python
# 複数分布の比較
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Q-Qプロット風の比較
ax = axes[0, 0]
for day in tips['day'].unique():
    data = tips[tips['day'] == day]['total_bill']
    stats.probplot(data, dist="norm", plot=ax)
ax.set_title("Q-Q Plots by Day")
ax.get_lines()[0].set_markerfacecolor('C0')
ax.get_lines()[2].set_markerfacecolor('C1')

# 累積分布の比較
ax = axes[0, 1]
for day in ['Thur', 'Fri', 'Sat', 'Sun']:
    data = tips[tips['day'] == day]['total_bill']
    sns.ecdfplot(data=data, label=day, ax=ax)
ax.set_title("Cumulative Distribution Comparison")
ax.legend()

# KDE比較（filled）
ax = axes[1, 0]
for time in tips['time'].unique():
    data = tips[tips['time'] == time]['total_bill']
    sns.kdeplot(data=data, label=time, fill=True, 
                alpha=0.5, ax=ax)
ax.set_title("KDE Comparison by Time")

# リッジプロット風
ax = axes[1, 1]
days = ['Thur', 'Fri', 'Sat', 'Sun']
for i, day in enumerate(days):
    data = tips[tips['day'] == day]['total_bill']
    density = stats.gaussian_kde(data)
    x = np.linspace(data.min(), data.max(), 100)
    y = density(x)
    ax.fill_between(x, i + y * 3, i, alpha=0.6)
    ax.plot(x, i + y * 3, color='black', linewidth=1)
ax.set_yticks(range(len(days)))
ax.set_yticklabels(days)
ax.set_title("Ridge Plot Style")
ax.set_xlabel("Total Bill")

plt.tight_layout()
plt.show()
```

### 相関と関係性の高度な可視化

```python
# 共分散楕円
from matplotlib.patches import Ellipse

def plot_covariance_ellipse(ax, data, n_std=2):
    """共分散楕円をプロット"""
    mean = data.mean(axis=0)
    cov = np.cov(data.T)
    
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    angle = np.degrees(np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0]))
    
    width, height = 2 * n_std * np.sqrt(eigenvalues)
    ellipse = Ellipse(mean, width, height, angle=angle, 
                     facecolor='none', edgecolor='red', 
                     linewidth=2, linestyle='--')
    ax.add_patch(ellipse)

plt.figure(figsize=(10, 8))
data = tips[['total_bill', 'tip']].values
plt.scatter(data[:, 0], data[:, 1], alpha=0.5)
plot_covariance_ellipse(plt.gca(), data)
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Scatter Plot with Covariance Ellipse")
plt.show()

# 条件付き分布
g = sns.FacetGrid(tips, col="time", row="smoker", 
                  margin_titles=True, height=4)
g.map(sns.regplot, "total_bill", "tip", 
      scatter_kws={'alpha': 0.5})
g.fig.suptitle("Conditional Distributions", y=1.02)
plt.show()
```

## 12. 実践的な応用例とベストプラクティス

### データ探索ダッシュボード

```python
def create_eda_dashboard(df, target_col, feature_cols):
    """探索的データ分析ダッシュボードを作成"""
    fig = plt.figure(figsize=(20, 15))
    gs = fig.add_gridspec(4, 4, hspace=0.3, wspace=0.3)
    
    # 1. ターゲット変数の分布
    ax1 = fig.add_subplot(gs[0, :2])
    sns.histplot(data=df, x=target_col, kde=True, ax=ax1)
    ax1.set_title(f"Distribution of {target_col}")
    
    # 2. 相関行列
    ax2 = fig.add_subplot(gs[0, 2:])
    numeric_cols = [target_col] + [col for col in feature_cols 
                                   if df[col].dtype in ['int64', 'float64']]
    if len(numeric_cols) > 1:
        corr = df[numeric_cols].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', 
                   center=0, ax=ax2)
        ax2.set_title("Correlation Matrix")
    
    # 3. カテゴリ変数との関係
    cat_cols = [col for col in feature_cols 
                if df[col].dtype == 'object' or df[col].nunique() < 10]
    
    if cat_cols:
        for i, col in enumerate(cat_cols[:4]):
            ax = fig.add_subplot(gs[1, i])
            sns.boxplot(data=df, x=col, y=target_col, ax=ax)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
            ax.set_title(f"{target_col} by {col}")
    
    # 4. 数値変数との散布図
    num_cols = [col for col in feature_cols 
                if df[col].dtype in ['int64', 'float64'] and col != target_col]
    
    if num_cols:
        for i, col in enumerate(num_cols[:4]):
            ax = fig.add_subplot(gs[2, i])
            sns.regplot(data=df, x=col, y=target_col, 
                       scatter_kws={'alpha': 0.5}, ax=ax)
            ax.set_title(f"{target_col} vs {col}")
    
    # 5. ペアプロット（主要変数）
    if len(numeric_cols) > 2:
        ax_pair = fig.add_subplot(gs[3, :])
        main_cols = numeric_cols[:4]  # 最大4変数
        pair_data = df[main_cols].sample(min(len(df), 100))  # サンプリング
        
        # 小さなペアプロットを作成
        from itertools import combinations
        pairs = list(combinations(main_cols, 2))
        n_pairs = len(pairs)
        n_cols = int(np.ceil(np.sqrt(n_pairs)))
        n_rows = int(np.ceil(n_pairs / n_cols))
        
        for idx, (x, y) in enumerate(pairs[:6]):  # 最大6ペア
            ax = plt.subplot(gs[3, :], n_rows, n_cols, idx + 1)
            ax.scatter(pair_data[x], pair_data[y], alpha=0.5, s=10)
            ax.set_xlabel(x, fontsize=8)
            ax.set_ylabel(y, fontsize=8)
            ax.tick_params(labelsize=6)
    
    plt.suptitle(f"EDA Dashboard for {target_col}", fontsize=16)
    return fig

# 使用例
fig = create_eda_dashboard(tips, 'tip', 
                          ['total_bill', 'size', 'day', 'time', 'sex'])
plt.show()
```

### カスタム統計プロット関数

```python
def plot_statistical_summary(data, x, y, hue=None, figsize=(15, 10)):
    """包括的な統計サマリープロット"""
    fig, axes = plt.subplots(2, 3, figsize=figsize)
    
    # 1. ボックスプロット
    sns.boxplot(data=data, x=x, y=y, hue=hue, ax=axes[0, 0])
    axes[0, 0].set_title("Box Plot")
    
    # 2. バイオリンプロット
    sns.violinplot(data=data, x=x, y=y, hue=hue, ax=axes[0, 1])
    axes[0, 1].set_title("Violin Plot")
    
    # 3. スウォームプロット
    if len(data) < 500:  # データが多すぎない場合のみ
        sns.swarmplot(data=data, x=x, y=y, hue=hue, 
                     ax=axes[0, 2], size=3)
    else:
        sns.stripplot(data=data, x=x, y=y, hue=hue, 
                     ax=axes[0, 2], size=3, alpha=0.5)
    axes[0, 2].set_title("Swarm/Strip Plot")
    
    # 4. 平均値と信頼区間
    sns.barplot(data=data, x=x, y=y, hue=hue, 
               errorbar='ci', ax=axes[1, 0])
    axes[1, 0].set_title("Mean with 95% CI")
    
    # 5. ポイントプロット
    sns.pointplot(data=data, x=x, y=y, hue=hue, 
                 ax=axes[1, 1], dodge=True)
    axes[1, 1].set_title("Point Plot")
    
    # 6. カウントプロット
    if hue:
        sns.countplot(data=data, x=x, hue=hue, ax=axes[1, 2])
    else:
        value_counts = data.groupby(x)[y].count()
        axes[1, 2].bar(value_counts.index, value_counts.values)
        axes[1, 2].set_xlabel(x)
        axes[1, 2].set_ylabel('Count')
    axes[1, 2].set_title("Count by Category")
    
    # レイアウト調整
    for ax in axes.flat:
        ax.tick_params(axis='x', rotation=45)
    
    plt.suptitle(f"Statistical Summary: {y} by {x}" + 
                 (f" (grouped by {hue})" if hue else ""), 
                 fontsize=14)
    plt.tight_layout()
    return fig

# 使用例
fig = plot_statistical_summary(tips, x='day', y='total_bill', hue='time')
plt.show()
```

### パフォーマンス最適化のベストプラクティス

```python
# 大規模データセットの可視化
def plot_large_dataset(data, x_col, y_col, sample_size=5000):
    """大規模データセット用の最適化されたプロット"""
    
    # データサンプリング
    if len(data) > sample_size:
        data_sample = data.sample(sample_size)
        print(f"Sampled {sample_size} points from {len(data)} total")
    else:
        data_sample = data
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. ヘックスビン（大量の点に適している）
    ax = axes[0, 0]
    hb = ax.hexbin(data[x_col], data[y_col], gridsize=30, cmap='YlOrRd')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title("Hexbin Plot")
    plt.colorbar(hb, ax=ax)
    
    # 2. 2D KDE（密度推定）
    ax = axes[0, 1]
    sns.kdeplot(data=data_sample, x=x_col, y=y_col, 
               cmap='viridis', fill=True, ax=ax)
    ax.set_title("2D KDE Plot")
    
    # 3. ラスタライズ散布図
    ax = axes[1, 0]
    ax.scatter(data_sample[x_col], data_sample[y_col], 
              alpha=0.5, s=1, rasterized=True)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title("Rasterized Scatter")
    
    # 4. ビン統計
    ax = axes[1, 1]
    x_bins = pd.cut(data[x_col], bins=20)
    bin_stats = data.groupby(x_bins)[y_col].agg(['mean', 'std'])
    bin_centers = [interval.mid for interval in bin_stats.index]
    
    ax.errorbar(bin_centers, bin_stats['mean'], 
               yerr=bin_stats['std'], fmt='o-', capsize=5)
    ax.set_xlabel(f"{x_col} (binned)")
    ax.set_ylabel(f"{y_col} (mean ± std)")
    ax.set_title("Binned Statistics")
    
    plt.suptitle(f"Large Dataset Visualization: {y_col} vs {x_col}", 
                fontsize=14)
    plt.tight_layout()
    return fig

# 大規模データのシミュレーション
large_data = pd.DataFrame({
    'x': np.random.normal(0, 1, 10000),
    'y': np.random.normal(0, 1, 10000)
})
large_data['y'] = large_data['x'] * 0.5 + np.random.normal(0, 0.5, 10000)

fig = plot_large_dataset(large_data, 'x', 'y')
plt.show()
```

### 出版品質のプロット

```python
def publication_ready_plot(data, x, y, hue=None, 
                          title="", xlabel="", ylabel="",
                          figsize=(8, 6), dpi=300):
    """出版品質のプロットを作成"""
    
    # スタイル設定
    plt.style.use('seaborn-v0_8-whitegrid')
    sns.set_palette("colorblind")
    
    # フォント設定
    plt.rcParams.update({
        'font.size': 12,
        'axes.labelsize': 14,
        'axes.titlesize': 16,
        'xtick.labelsize': 12,
        'ytick.labelsize': 12,
        'legend.fontsize': 12,
        'figure.dpi': dpi
    })
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # メインプロット
    if hue:
        sns.scatterplot(data=data, x=x, y=y, hue=hue, 
                       s=50, alpha=0.7, ax=ax)
        # 回帰線を追加
        for category in data[hue].unique():
            subset = data[data[hue] == category]
            sns.regplot(data=subset, x=x, y=y, 
                       scatter=False, ax=ax, label=None)
    else:
        sns.regplot(data=data, x=x, y=y, 
                   scatter_kws={'alpha': 0.7, 's': 50}, ax=ax)
    
    # ラベルとタイトル
    ax.set_xlabel(xlabel or x, fontweight='bold')
    ax.set_ylabel(ylabel or y, fontweight='bold')
    ax.set_title(title, fontweight='bold', pad=20)
    
    # グリッドとスパイン
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    
    # 凡例の調整
    if hue:
        ax.legend(title=hue, frameon=True, fancybox=True, 
                 shadow=True, loc='best')
    
    # タイトレイアウト
    plt.tight_layout()
    
    return fig, ax

# 使用例
fig, ax = publication_ready_plot(
    tips, 'total_bill', 'tip', hue='day',
    title="Relationship between Total Bill and Tip",
    xlabel="Total Bill ($)",
    ylabel="Tip ($)"
)
plt.show()

# 保存（高解像度）
# fig.savefig('publication_plot.png', dpi=300, bbox_inches='tight')
# fig.savefig('publication_plot.pdf', bbox_inches='tight')
```

## まとめ

Seabornは統計的データ可視化のための強力なツールです：

1. **簡潔なAPI**：少ないコードで洗練されたプロットを作成
2. **統計機能の統合**：自動的な統計計算と可視化
3. **美しいデフォルト**：出版品質のグラフをすぐに作成
4. **柔軟性**：Matplotlibとの完全な互換性

主要な使用場面：
- 探索的データ分析（EDA）
- 統計的な関係性の可視化
- レポートやプレゼンテーション用のグラフ作成
- 機械学習の結果可視化

次のステップ：
- 実際のデータセットでの練習
- カスタムスタイルの開発
- インタラクティブな可視化（Plotlyなど）との組み合わせ
- 自動レポート生成システムの構築

継続的な学習のために、公式ドキュメントやギャラリーを参照し、実践的なプロジェクトで活用してください。