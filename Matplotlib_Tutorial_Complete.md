# Matplotlib完全チュートリアル

## 目次
1. [Matplotlibとは](#1-matplotlibとは)
2. [インストールと基本設定](#2-インストールと基本設定)
3. [基本的なプロット](#3-基本的なプロット)
4. [プロットのカスタマイズ](#4-プロットのカスタマイズ)
5. [複数のグラフとサブプロット](#5-複数のグラフとサブプロット)
6. [様々なプロットタイプ](#6-様々なプロットタイプ)
7. [3Dプロット](#7-3dプロット)
8. [アニメーション](#8-アニメーション)
9. [スタイルとテーマ](#9-スタイルとテーマ)
10. [画像の保存とエクスポート](#10-画像の保存とエクスポート)
11. [実践的な応用例](#11-実践的な応用例)
12. [パフォーマンスとベストプラクティス](#12-パフォーマンスとベストプラクティス)

## 1. Matplotlibとは

MatplotlibはPythonの最も広く使われているグラフ描画ライブラリです。科学計算、データ分析、機械学習などの分野で、データの可視化に欠かせないツールとなっています。

### Matplotlibの特徴

- **豊富なグラフタイプ**: 折れ線グラフ、散布図、ヒストグラム、3Dプロットなど
- **高度なカスタマイズ性**: 色、スタイル、フォント、レイアウトを細かく制御
- **複数の出力形式**: PNG、PDF、SVG、インタラクティブな表示
- **NumPyとの統合**: NumPy配列を直接プロット
- **オブジェクト指向とpyplotインターフェース**: 用途に応じて選択可能

### なぜMatplotlibを使うのか？

```python
import numpy as np
import matplotlib.pyplot as plt

# データの生成
x = np.linspace(0, 10, 100)
y = np.sin(x)

# プロット
plt.plot(x, y)
plt.title('サイン波')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()
```

## 2. インストールと基本設定

### インストール

```bash
pip install matplotlib
```

### 基本的なインポート

```python
import matplotlib.pyplot as plt
import numpy as np

# 日本語フォントの設定（Windows）
plt.rcParams['font.family'] = 'MS Gothic'

# 日本語フォントの設定（Mac）
# plt.rcParams['font.family'] = 'Hiragino Sans'

# 日本語フォントの設定（Linux）
# plt.rcParams['font.family'] = 'IPAexGothic'

# マイナス記号の文字化けを防ぐ
plt.rcParams['axes.unicode_minus'] = False
```

### Jupyter Notebookでの設定

```python
# インライン表示
%matplotlib inline

# インタラクティブ表示
# %matplotlib widget

# 高解像度表示
%config InlineBackend.figure_format = 'retina'
```

## 3. 基本的なプロット

### 折れ線グラフ

```python
# データの準備
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 基本的な折れ線グラフ
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title('正弦波')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

# 複数の線
y2 = np.cos(x)
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.title('三角関数')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
```

### 散布図

```python
# ランダムデータの生成
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)

# 散布図
plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.6)
plt.title('散布図の例')
plt.xlabel('X値')
plt.ylabel('Y値')
plt.grid(True, alpha=0.3)
plt.show()

# 色とサイズを変える
colors = np.random.rand(100)
sizes = 100 * np.random.rand(100)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
plt.colorbar(label='色の値')
plt.title('カラフルな散布図')
plt.xlabel('X値')
plt.ylabel('Y値')
plt.show()
```

### 棒グラフ

```python
# カテゴリデータ
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

# 縦棒グラフ
plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='skyblue', edgecolor='navy')
plt.title('売上高比較')
plt.xlabel('カテゴリ')
plt.ylabel('売上高')
plt.show()

# 横棒グラフ
plt.figure(figsize=(8, 6))
plt.barh(categories, values, color='lightgreen', edgecolor='darkgreen')
plt.title('売上高比較（横棒）')
plt.xlabel('売上高')
plt.ylabel('カテゴリ')
plt.show()
```

## 4. プロットのカスタマイズ

### 線のスタイル

```python
x = np.linspace(0, 10, 100)

plt.figure(figsize=(10, 6))

# 異なる線のスタイル
plt.plot(x, np.sin(x), 'b-', label='実線', linewidth=2)
plt.plot(x, np.sin(x + 0.5), 'r--', label='破線', linewidth=2)
plt.plot(x, np.sin(x + 1.0), 'g-.', label='一点鎖線', linewidth=2)
plt.plot(x, np.sin(x + 1.5), 'm:', label='点線', linewidth=2)

plt.title('線のスタイル')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### マーカー

```python
x = np.linspace(0, 10, 20)

plt.figure(figsize=(10, 6))

# 異なるマーカー
plt.plot(x, np.sin(x), 'o-', label='円', markersize=8)
plt.plot(x, np.sin(x + 0.5), 's--', label='四角', markersize=8)
plt.plot(x, np.sin(x + 1.0), '^-.', label='三角', markersize=8)
plt.plot(x, np.sin(x + 1.5), 'D:', label='ダイヤモンド', markersize=8)

plt.title('マーカーのスタイル')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### 色の指定

```python
x = np.linspace(0, 10, 100)

plt.figure(figsize=(10, 6))

# 様々な色の指定方法
plt.plot(x, np.sin(x), color='red', label='名前で指定')
plt.plot(x, np.sin(x + 0.5), color='#FF5733', label='16進数で指定')
plt.plot(x, np.sin(x + 1.0), color=(0.1, 0.8, 0.5), label='RGBで指定')
plt.plot(x, np.sin(x + 1.5), color='C3', label='デフォルトカラー')

plt.title('色の指定方法')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### 軸の設定

```python
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)

# 軸の範囲
plt.xlim(-8, 8)
plt.ylim(-1.5, 1.5)

# 軸の目盛り
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], 
           ['-2π', '-π', '0', 'π', '2π'])
plt.yticks([-1, 0, 1])

# グリッドの追加
plt.grid(True, linestyle='--', alpha=0.7)

# 軸ラベル
plt.xlabel('角度', fontsize=12)
plt.ylabel('sin(x)', fontsize=12)
plt.title('正弦波のプロット', fontsize=16)

plt.show()
```

## 5. 複数のグラフとサブプロット

### subplot()を使った方法

```python
# 2x2のサブプロット
plt.figure(figsize=(12, 10))

# 左上
plt.subplot(2, 2, 1)
plt.plot(np.random.rand(100))
plt.title('ランダムウォーク')

# 右上
plt.subplot(2, 2, 2)
plt.hist(np.random.randn(1000), bins=30)
plt.title('正規分布')

# 左下
plt.subplot(2, 2, 3)
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y)
plt.title('散布図')

# 右下
plt.subplot(2, 2, 4)
categories = ['A', 'B', 'C', 'D']
values = np.random.randint(10, 100, 4)
plt.bar(categories, values)
plt.title('棒グラフ')

plt.tight_layout()
plt.show()
```

### subplots()を使った方法

```python
# より柔軟なサブプロット
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# データの生成
x = np.linspace(0, 2*np.pi, 100)

# 各サブプロットに描画
for i in range(2):
    for j in range(3):
        ax = axes[i, j]
        ax.plot(x, np.sin(x + i*np.pi/2 + j*np.pi/3))
        ax.set_title(f'位相シフト: {i},{j}')
        ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### GridSpecを使った高度なレイアウト

```python
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(3, 3)

# 大きなプロット（左側）
ax1 = fig.add_subplot(gs[:, :2])
ax1.plot(np.random.randn(100).cumsum())
ax1.set_title('メインプロット')

# 右上
ax2 = fig.add_subplot(gs[0, 2])
ax2.scatter(np.random.rand(20), np.random.rand(20))
ax2.set_title('散布図')

# 右中
ax3 = fig.add_subplot(gs[1, 2])
ax3.bar(['A', 'B', 'C'], [3, 7, 5])
ax3.set_title('棒グラフ')

# 右下
ax4 = fig.add_subplot(gs[2, 2])
ax4.pie([30, 40, 20, 10], labels=['A', 'B', 'C', 'D'])
ax4.set_title('円グラフ')

plt.tight_layout()
plt.show()
```

## 6. 様々なプロットタイプ

### ヒストグラム

```python
# データの生成
data = np.random.randn(1000)

plt.figure(figsize=(12, 5))

# 基本的なヒストグラム
plt.subplot(1, 2, 1)
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('基本的なヒストグラム')
plt.xlabel('値')
plt.ylabel('頻度')

# 正規化されたヒストグラム
plt.subplot(1, 2, 2)
plt.hist(data, bins=30, density=True, alpha=0.7, color='green')
# 理論的な正規分布を重ねる
x = np.linspace(-4, 4, 100)
plt.plot(x, 1/np.sqrt(2*np.pi) * np.exp(-x**2/2), 'r-', linewidth=2)
plt.title('正規化されたヒストグラム')
plt.xlabel('値')
plt.ylabel('確率密度')

plt.tight_layout()
plt.show()
```

### 箱ひげ図

```python
# 複数のデータセット
data1 = np.random.normal(100, 10, 200)
data2 = np.random.normal(90, 20, 200)
data3 = np.random.normal(110, 15, 200)
data4 = np.random.normal(95, 25, 200)

data = [data1, data2, data3, data4]

plt.figure(figsize=(8, 6))
plt.boxplot(data, labels=['グループA', 'グループB', 'グループC', 'グループD'])
plt.title('箱ひげ図の例')
plt.ylabel('値')
plt.grid(True, axis='y', alpha=0.3)
plt.show()
```

### ヒートマップ

```python
# 2次元データの生成
data = np.random.randn(10, 10)

plt.figure(figsize=(8, 6))
im = plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar(im, label='値')
plt.title('ヒートマップ')
plt.xlabel('X軸')
plt.ylabel('Y軸')

# 値を表示
for i in range(10):
    for j in range(10):
        plt.text(j, i, f'{data[i, j]:.1f}', 
                ha='center', va='center', fontsize=8)

plt.show()
```

### 等高線図

```python
# 2次元関数のデータ
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

plt.figure(figsize=(12, 5))

# 塗りつぶし等高線
plt.subplot(1, 2, 1)
cs = plt.contourf(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(cs, label='値')
plt.title('塗りつぶし等高線')
plt.xlabel('X')
plt.ylabel('Y')

# 等高線
plt.subplot(1, 2, 2)
cs = plt.contour(X, Y, Z, levels=20, colors='black', linewidths=0.5)
plt.clabel(cs, inline=True, fontsize=8)
plt.title('等高線')
plt.xlabel('X')
plt.ylabel('Y')

plt.tight_layout()
plt.show()
```

### 円グラフ

```python
# データ
labels = ['Python', 'JavaScript', 'Java', 'C++', 'その他']
sizes = [35, 25, 20, 15, 5]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
explode = (0.1, 0, 0, 0, 0)  # Pythonを強調

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('プログラミング言語の使用率')
plt.axis('equal')
plt.show()
```

### 極座標プロット

```python
# 極座標データ
theta = np.linspace(0, 2*np.pi, 100)
r = 1 + np.sin(5*theta)

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, 'b-', linewidth=2)
ax.fill(theta, r, alpha=0.2)
ax.set_title('極座標プロット：花の形')
plt.show()
```

## 7. 3Dプロット

### 3D線プロット

```python
from mpl_toolkits.mplot3d import Axes3D

# データの生成
t = np.linspace(0, 20, 100)
x = np.sin(t)
y = np.cos(t)
z = t

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, 'b-', linewidth=2)
ax.set_xlabel('X軸')
ax.set_ylabel('Y軸')
ax.set_zlabel('Z軸')
ax.set_title('3Dらせん')

plt.show()
```

### 3D曲面プロット

```python
# メッシュグリッドの作成
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure(figsize=(12, 5))

# ワイヤーフレーム
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_wireframe(X, Y, Z, color='blue', alpha=0.5)
ax1.set_title('ワイヤーフレーム')

# サーフェス
ax2 = fig.add_subplot(122, projection='3d')
surf = ax2.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
fig.colorbar(surf, ax=ax2, shrink=0.5)
ax2.set_title('サーフェスプロット')

plt.show()
```

### 3D散布図

```python
# ランダムデータ
n = 100
x = np.random.randn(n)
y = np.random.randn(n)
z = np.random.randn(n)
colors = np.random.rand(n)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x, y, z, c=colors, cmap='viridis', s=50)
fig.colorbar(scatter, ax=ax, shrink=0.5)

ax.set_xlabel('X軸')
ax.set_ylabel('Y軸')
ax.set_zlabel('Z軸')
ax.set_title('3D散布図')

plt.show()
```

## 8. アニメーション

### 基本的なアニメーション

```python
from matplotlib.animation import FuncAnimation

# アニメーション用の関数
def animate_sine():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1.5, 1.5)
    
    x = np.linspace(0, 2*np.pi, 100)
    line, = ax.plot([], [], 'b-')
    
    def init():
        line.set_data([], [])
        return line,
    
    def animate(frame):
        y = np.sin(x + frame/10)
        line.set_data(x, y)
        return line,
    
    anim = FuncAnimation(fig, animate, init_func=init,
                        frames=100, interval=50, blit=True)
    plt.title('アニメーション：移動する正弦波')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.grid(True)
    plt.show()
    
    return anim

# アニメーションの実行
# anim = animate_sine()
```

### リアルタイムプロット

```python
# リアルタイムデータのシミュレーション
def realtime_plot():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 100)
    ax.set_ylim(-2, 2)
    
    x_data = []
    y_data = []
    line, = ax.plot([], [], 'r-')
    
    def init():
        line.set_data([], [])
        return line,
    
    def update(frame):
        x_data.append(frame)
        y_data.append(np.sin(frame/10) + np.random.normal(0, 0.1))
        
        # 最新の100点のみ表示
        if len(x_data) > 100:
            x_data.pop(0)
            y_data.pop(0)
            ax.set_xlim(frame-100, frame)
        
        line.set_data(x_data, y_data)
        return line,
    
    anim = FuncAnimation(fig, update, init_func=init,
                        frames=range(1000), interval=50, blit=True)
    plt.title('リアルタイムデータプロット')
    plt.xlabel('時間')
    plt.ylabel('値')
    plt.grid(True)
    plt.show()
    
    return anim

# リアルタイムプロットの実行
# anim = realtime_plot()
```

## 9. スタイルとテーマ

### 組み込みスタイル

```python
# 利用可能なスタイルの確認
print("利用可能なスタイル:")
print(plt.style.available)

# スタイルの比較
styles = ['default', 'seaborn', 'ggplot', 'bmh']
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.ravel()

x = np.linspace(0, 10, 100)

for ax, style in zip(axes, styles):
    with plt.style.context(style):
        ax.plot(x, np.sin(x), label='sin(x)')
        ax.plot(x, np.cos(x), label='cos(x)')
        ax.set_title(f'スタイル: {style}')
        ax.legend()
        ax.grid(True)

plt.tight_layout()
plt.show()
```

### カスタムスタイル

```python
# カスタムスタイルの作成
custom_style = {
    'axes.facecolor': '#f0f0f0',
    'axes.edgecolor': '#333333',
    'axes.linewidth': 2,
    'grid.color': '#cccccc',
    'grid.linestyle': '--',
    'grid.linewidth': 0.5,
    'lines.linewidth': 2.5,
    'lines.markersize': 8,
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'legend.fontsize': 12,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11
}

plt.figure(figsize=(10, 6))
with plt.rc_context(custom_style):
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x), 'o-', label='sin(x)', markevery=5)
    plt.plot(x, np.cos(x), 's-', label='cos(x)', markevery=5)
    plt.title('カスタムスタイルの例')
    plt.xlabel('X軸')
    plt.ylabel('Y軸')
    plt.legend()
    plt.grid(True)

plt.show()
```

## 10. 画像の保存とエクスポート

### 基本的な保存

```python
# プロットの作成
fig, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), 'b-', linewidth=2)
ax.set_title('保存用のプロット')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.grid(True)

# 様々な形式で保存
fig.savefig('plot.png', dpi=300)  # PNG形式（高解像度）
fig.savefig('plot.pdf')  # PDF形式（ベクター）
fig.savefig('plot.svg')  # SVG形式（ベクター）
fig.savefig('plot.jpg', quality=95)  # JPEG形式

# オプション付き保存
fig.savefig('plot_tight.png', 
           dpi=300, 
           bbox_inches='tight',  # 余白を最小化
           pad_inches=0.1,       # パディング
           facecolor='white',    # 背景色
           edgecolor='none')     # 枠線なし

plt.close(fig)
print("画像を保存しました")
```

### 複数の図の保存

```python
# 複数の図を一度に作成・保存
for i in range(3):
    fig, ax = plt.subplots(figsize=(6, 4))
    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x + i*np.pi/3))
    ax.set_title(f'図 {i+1}')
    
    # ファイル名に番号を付けて保存
    fig.savefig(f'figure_{i+1}.png', dpi=150)
    plt.close(fig)

print("複数の図を保存しました")
```

## 11. 実践的な応用例

### 例1: 株価データの可視化

```python
# 株価データのシミュレーション
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=100, freq='D')
price = 100 + np.cumsum(np.random.randn(100) * 2)
volume = np.random.randint(1000000, 5000000, 100)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), 
                               gridspec_kw={'height_ratios': [3, 1]})

# 価格チャート
ax1.plot(dates, price, 'b-', linewidth=2)
ax1.fill_between(dates, price, alpha=0.3)
ax1.set_title('株価チャート', fontsize=16)
ax1.set_ylabel('価格（円）')
ax1.grid(True, alpha=0.3)

# 移動平均線の追加
ma20 = pd.Series(price).rolling(20).mean()
ma50 = pd.Series(price).rolling(50).mean()
ax1.plot(dates, ma20, 'r-', label='20日移動平均', alpha=0.8)
ax1.plot(dates, ma50, 'g-', label='50日移動平均', alpha=0.8)
ax1.legend()

# 出来高チャート
ax2.bar(dates, volume, color='gray', alpha=0.5)
ax2.set_ylabel('出来高')
ax2.set_xlabel('日付')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### 例2: 科学データの可視化

```python
# 実験データのシミュレーション
x = np.linspace(0, 10, 50)
y_true = 2 * x + 1
y_measured = y_true + np.random.normal(0, 2, 50)
y_error = np.random.uniform(0.5, 1.5, 50)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# エラーバー付きプロット
ax1.errorbar(x, y_measured, yerr=y_error, fmt='o', 
            capsize=5, capthick=2, label='測定値')
ax1.plot(x, y_true, 'r-', linewidth=2, label='理論値')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('実験データと理論値の比較')
ax1.legend()
ax1.grid(True, alpha=0.3)

# 残差プロット
residuals = y_measured - y_true
ax2.scatter(x, residuals, alpha=0.6)
ax2.axhline(y=0, color='r', linestyle='--')
ax2.fill_between(x, -2, 2, alpha=0.2, color='gray', 
                 label='±2σ範囲')
ax2.set_xlabel('X')
ax2.set_ylabel('残差')
ax2.set_title('残差プロット')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### 例3: 統計データのダッシュボード

```python
# データの生成
np.random.seed(42)
categories = ['A', 'B', 'C', 'D', 'E']
values1 = np.random.randint(50, 100, 5)
values2 = np.random.randint(30, 80, 5)
correlation_data = np.random.randn(100, 2)
correlation_data[:, 1] = correlation_data[:, 0] * 0.5 + np.random.randn(100) * 0.5

# ダッシュボードの作成
fig = plt.figure(figsize=(15, 10))
gs = gridspec.GridSpec(3, 3, figure=fig)

# 1. 棒グラフ比較
ax1 = fig.add_subplot(gs[0, :2])
x = np.arange(len(categories))
width = 0.35
ax1.bar(x - width/2, values1, width, label='2023年', alpha=0.8)
ax1.bar(x + width/2, values2, width, label='2024年', alpha=0.8)
ax1.set_xlabel('カテゴリ')
ax1.set_ylabel('値')
ax1.set_title('年度別比較')
ax1.set_xticks(x)
ax1.set_xticklabels(categories)
ax1.legend()
ax1.grid(True, axis='y', alpha=0.3)

# 2. 円グラフ
ax2 = fig.add_subplot(gs[0, 2])
ax2.pie(values1, labels=categories, autopct='%1.1f%%', startangle=90)
ax2.set_title('2023年の構成比')

# 3. 相関散布図
ax3 = fig.add_subplot(gs[1, :2])
ax3.scatter(correlation_data[:, 0], correlation_data[:, 1], alpha=0.6)
ax3.set_xlabel('変数1')
ax3.set_ylabel('変数2')
ax3.set_title('相関関係')
ax3.grid(True, alpha=0.3)

# 相関係数を表示
corr = np.corrcoef(correlation_data[:, 0], correlation_data[:, 1])[0, 1]
ax3.text(0.05, 0.95, f'相関係数: {corr:.3f}', 
         transform=ax3.transAxes, fontsize=12,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# 4. ヒートマップ
ax4 = fig.add_subplot(gs[1:, 2])
heatmap_data = np.random.rand(8, 5)
im = ax4.imshow(heatmap_data, cmap='YlOrRd', aspect='auto')
ax4.set_xticks(range(5))
ax4.set_xticklabels(categories)
ax4.set_yticks(range(8))
ax4.set_yticklabels([f'項目{i+1}' for i in range(8)])
ax4.set_title('パフォーマンスマトリックス')
plt.colorbar(im, ax=ax4)

# 5. 時系列データ
ax5 = fig.add_subplot(gs[2, :2])
time = np.arange(100)
signal = np.sin(time/10) + np.random.normal(0, 0.1, 100)
ax5.plot(time, signal, 'b-', alpha=0.7)
ax5.fill_between(time, signal-0.2, signal+0.2, alpha=0.2)
ax5.set_xlabel('時間')
ax5.set_ylabel('信号強度')
ax5.set_title('時系列データ')
ax5.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

## 12. パフォーマンスとベストプラクティス

### メモリ効率的なプロット

```python
# 大量データのプロット
n_points = 1000000

# 非効率的な方法（避けるべき）
# plt.plot(np.random.randn(n_points))

# 効率的な方法1: ダウンサンプリング
data = np.random.randn(n_points)
step = max(1, n_points // 10000)
plt.figure(figsize=(10, 6))
plt.plot(data[::step], 'b-', alpha=0.7)
plt.title(f'ダウンサンプリング（1/{step}）')
plt.show()

# 効率的な方法2: rasterized
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(np.random.randn(10000), 'b-', alpha=0.5, rasterized=True)
ax.set_title('ラスタライズされたプロット')
plt.show()
```

### インタラクティブ機能

```python
# マウスイベントの処理
def interactive_plot():
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.linspace(0, 10, 100)
    line, = ax.plot(x, np.sin(x))
    
    # クリック位置を表示
    def on_click(event):
        if event.inaxes == ax:
            ax.plot(event.xdata, event.ydata, 'ro', markersize=10)
            ax.text(event.xdata, event.ydata, 
                   f'({event.xdata:.2f}, {event.ydata:.2f})',
                   fontsize=9, ha='right')
            fig.canvas.draw()
    
    fig.canvas.mpl_connect('button_press_event', on_click)
    ax.set_title('クリックして点を追加')
    ax.grid(True)
    plt.show()

# インタラクティブプロットの実行
# interactive_plot()
```

### ベストプラクティス

1. **図のサイズを適切に設定**
```python
# 用途に応じたサイズ設定
plt.figure(figsize=(10, 6))  # 横長のプロット
plt.figure(figsize=(8, 8))   # 正方形のプロット
plt.figure(figsize=(6, 8))   # 縦長のプロット
```

2. **カラーマップの選択**
```python
# 用途別カラーマップ
# 連続データ: 'viridis', 'plasma', 'inferno', 'magma'
# 発散データ: 'RdBu', 'coolwarm', 'seismic'
# カテゴリデータ: 'tab10', 'tab20', 'Set1', 'Set2'
```

3. **アクセシビリティ**
```python
# 色覚多様性への配慮
colors = ['#0173B2', '#DE8F05', '#029E73', '#CC78BC', '#CA9161']
# または
plt.style.use('tableau-colorblind10')
```

4. **再利用可能な関数**
```python
def create_publication_plot(x, y, xlabel, ylabel, title, filename=None):
    """出版品質のプロットを作成"""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    ax.plot(x, y, 'b-', linewidth=2)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
    
    return fig, ax
```

## まとめ

Matplotlibは非常に柔軟で強力な可視化ライブラリです。主なポイント：

1. **基本から応用まで**: 単純な折れ線グラフから複雑な3Dプロットまで対応
2. **カスタマイズ性**: あらゆる要素を細かく制御可能
3. **統合性**: NumPy、pandas、SciPyなど他のライブラリとシームレスに連携
4. **出力形式**: 画面表示、画像ファイル、PDFなど多様な出力に対応
5. **拡張性**: アニメーション、インタラクティブ機能も実装可能

### 学習のヒント

- 基本的なプロットから始めて徐々に複雑な機能を学ぶ
- 公式ギャラリーで様々な例を参考にする
- 実際のデータで練習する
- SeabornやPlotlyなどの他の可視化ライブラリとも組み合わせる

### 次のステップ

- **Seaborn**: 統計プロットに特化した高レベルライブラリ
- **Plotly**: インタラクティブな可視化
- **Bokeh**: Webアプリケーション向けの可視化
- **Altair**: 宣言的な可視化文法

Matplotlibをマスターすることで、データの可視化における基礎が身につき、より高度な可視化ツールの理解も深まります。