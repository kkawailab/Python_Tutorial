#!/usr/bin/env python3
"""
Matplotlibチュートリアル - 例7: スタイルとテーマ
"""

import matplotlib.pyplot as plt
import numpy as np

print("=== スタイルとテーマ ===\n")

# 1. 利用可能なスタイルの確認
print("--- 1. 利用可能なスタイル ---")
print("Available styles:")
for i, style in enumerate(plt.style.available):
    print(f"  {i+1:2d}. {style}")
print()

# 2. 主要なスタイルの比較
print("--- 2. 主要なスタイルの比較 ---")
styles = ['default', 'seaborn', 'ggplot', 'bmh', 'fivethirtyeight', 'dark_background']

# データの準備
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig = plt.figure(figsize=(15, 10))

for i, style_name in enumerate(styles, 1):
    with plt.style.context(style_name):
        ax = fig.add_subplot(2, 3, i)
        ax.plot(x, y1, label='sin(x)')
        ax.plot(x, y2, label='cos(x)')
        ax.set_title(f'Style: {style_name}')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()
        ax.grid(True)

plt.tight_layout()
plt.show()

# 3. カスタムスタイルの作成
print("\n--- 3. カスタムスタイルの作成 ---")
# カスタムスタイルパラメータ
custom_style = {
    # 図のサイズとDPI
    'figure.figsize': (10, 6),
    'figure.dpi': 100,
    'savefig.dpi': 300,
    
    # フォント
    'font.size': 12,
    'font.family': 'sans-serif',
    'axes.titlesize': 16,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    
    # 色
    'axes.prop_cycle': plt.cycler('color', 
        ['#E24A33', '#348ABD', '#988ED5', '#777777', 
         '#FBC15E', '#8EBA42', '#FFB5B8']),
    
    # 軸
    'axes.facecolor': '#f5f5f5',
    'axes.edgecolor': '#333333',
    'axes.linewidth': 1.5,
    'axes.grid': True,
    'axes.spines.top': False,
    'axes.spines.right': False,
    
    # グリッド
    'grid.color': '#cccccc',
    'grid.linestyle': '--',
    'grid.linewidth': 0.5,
    'grid.alpha': 0.7,
    
    # 線
    'lines.linewidth': 2.5,
    'lines.markersize': 8,
    
    # 凡例
    'legend.frameon': True,
    'legend.framealpha': 0.9,
    'legend.fancybox': True,
    'legend.shadow': True,
}

# カスタムスタイルの適用
with plt.rc_context(custom_style):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左のプロット
    x = np.linspace(0, 10, 100)
    for i in range(5):
        ax1.plot(x, np.sin(x + i*0.5), label=f'Wave {i+1}')
    ax1.set_title('Custom Style - Line Plot')
    ax1.set_xlabel('X Axis')
    ax1.set_ylabel('Y Axis')
    ax1.legend()
    
    # 右のプロット
    data = [np.random.normal(0, std, 100) for std in range(1, 6)]
    bp = ax2.boxplot(data, patch_artist=True, labels=[f'σ={i}' for i in range(1, 6)])
    
    # ボックスプロットの色付け
    colors = ['#E24A33', '#348ABD', '#988ED5', '#FBC15E', '#8EBA42']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax2.set_title('Custom Style - Box Plot')
    ax2.set_ylabel('Values')

plt.tight_layout()
plt.show()

# 4. テーマの組み合わせ
print("\n--- 4. テーマの組み合わせ ---")
# ベーススタイルとカスタマイズの組み合わせ
with plt.style.context('seaborn-darkgrid'):
    # さらにカスタマイズ
    plt.rcParams['figure.facecolor'] = '#f0f0f0'
    plt.rcParams['axes.facecolor'] = 'white'
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.ravel()
    
    # データ
    x = np.linspace(0, 10, 100)
    
    # プロット1: 線グラフ
    axes[0].plot(x, np.sin(x), 'o-', markersize=4, markevery=10)
    axes[0].set_title('Line with Markers')
    
    # プロット2: 塗りつぶし
    axes[1].fill_between(x, 0, np.sin(x), alpha=0.3, label='sin(x)')
    axes[1].fill_between(x, 0, np.cos(x), alpha=0.3, label='cos(x)')
    axes[1].set_title('Filled Areas')
    axes[1].legend()
    
    # プロット3: 散布図
    n = 100
    axes[2].scatter(np.random.randn(n), np.random.randn(n), 
                   c=np.random.rand(n), s=100*np.random.rand(n), 
                   alpha=0.6, cmap='viridis')
    axes[2].set_title('Scatter Plot')
    
    # プロット4: ヒストグラム
    data = np.random.normal(100, 15, 1000)
    axes[3].hist(data, bins=30, alpha=0.7, color='skyblue', 
                edgecolor='black', linewidth=1.2)
    axes[3].set_title('Histogram')
    
    for ax in axes:
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# 5. 出版品質のスタイル
print("\n--- 5. 出版品質のスタイル ---")
# 科学論文向けのスタイル
publication_style = {
    'figure.figsize': (8, 6),
    'figure.dpi': 300,
    
    'font.size': 10,
    'font.family': 'serif',
    'text.usetex': False,  # LaTeX使用（要LaTeX環境）
    
    'axes.linewidth': 0.8,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    
    'xtick.major.size': 4,
    'xtick.minor.size': 2,
    'ytick.major.size': 4,
    'ytick.minor.size': 2,
    
    'lines.linewidth': 1.5,
    'lines.markersize': 5,
    
    'legend.fontsize': 9,
    'legend.frameon': True,
    'legend.framealpha': 1.0,
    
    'grid.alpha': 0.3,
    'grid.linestyle': ':',
}

with plt.rc_context(publication_style):
    fig, ax = plt.subplots()
    
    # データ
    x = np.linspace(0, 4*np.pi, 100)
    y1 = np.sin(x)
    y2 = np.sin(x) * np.exp(-x/10)
    
    # プロット
    ax.plot(x, y1, 'k-', label='$\\sin(x)$')
    ax.plot(x, y2, 'k--', label='$\\sin(x)e^{-x/10}$')
    
    ax.set_xlabel('$x$ (radians)')
    ax.set_ylabel('$f(x)$')
    ax.set_title('Publication Quality Figure')
    ax.legend(loc='upper right')
    ax.grid(True)
    
    # 軸の調整
    ax.set_xlim(0, 4*np.pi)
    ax.set_ylim(-1.2, 1.2)
    
    plt.tight_layout()
    plt.show()

# 6. カラーマップのカスタマイズ
print("\n--- 6. カラーマップのカスタマイズ ---")
from matplotlib.colors import LinearSegmentedColormap

# カスタムカラーマップの作成
colors = ['#FF0000', '#FFFF00', '#00FF00', '#00FFFF', '#0000FF']
n_bins = 100
cmap_name = 'custom_rainbow'
custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

# データ
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 標準カラーマップ
im1 = ax1.imshow(Z, extent=[-3, 3, -3, 3], cmap='viridis')
ax1.set_title('Standard Colormap (viridis)')
plt.colorbar(im1, ax=ax1)

# カスタムカラーマップ
im2 = ax2.imshow(Z, extent=[-3, 3, -3, 3], cmap=custom_cmap)
ax2.set_title('Custom Colormap')
plt.colorbar(im2, ax=ax2)

plt.tight_layout()
plt.show()

# 7. アクセシビリティを考慮したスタイル
print("\n--- 7. アクセシビリティを考慮したスタイル ---")
# 色覚多様性に配慮したカラーパレット
colorblind_colors = ['#0173B2', '#DE8F05', '#029E73', '#CC78BC', 
                    '#CA9161', '#FBAFE4', '#949494', '#ECE133', '#56B4E9']

with plt.style.context('default'):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.linspace(0, 10, 100)
    for i, color in enumerate(colorblind_colors[:5]):
        y = np.sin(x + i*0.5)
        ax.plot(x, y, color=color, linewidth=2.5, label=f'Series {i+1}')
    
    ax.set_title('Colorblind-friendly Plot', fontsize=16)
    ax.set_xlabel('X Axis', fontsize=14)
    ax.set_ylabel('Y Axis', fontsize=14)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    
    # 線のスタイルも変える
    ax2 = ax.twinx()
    linestyles = ['-', '--', '-.', ':', '-']
    for i in range(5):
        y = np.cos(x + i*0.5) * 0.5
        ax2.plot(x, y, color='black', linestyle=linestyles[i], 
                linewidth=1.5, alpha=0.7, label=f'Cos {i+1}')
    
    ax2.set_ylabel('Secondary Y Axis', fontsize=14)
    ax2.legend(loc='lower right', fontsize=12)

plt.tight_layout()
plt.show()

print("\nスタイルとテーマの例を完了しました！")