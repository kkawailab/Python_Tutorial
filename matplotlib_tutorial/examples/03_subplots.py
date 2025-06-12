#!/usr/bin/env python3
"""
Matplotlibチュートリアル - 例3: 複数のグラフとサブプロット
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

print("=== 複数のグラフとサブプロット ===\n")

# 1. subplot()を使った基本的な方法
print("--- 1. subplot()を使った基本的な方法 ---")
plt.figure(figsize=(12, 8))

# 2x2のグリッド
plt.subplot(2, 2, 1)
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.title('Sine Wave')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x), 'r-')
plt.title('Cosine Wave')
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(x, np.exp(-x/10) * np.sin(x), 'g-')
plt.title('Damped Sine')
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(x, np.log(x + 1), 'm-')
plt.title('Logarithm')
plt.grid(True)

plt.tight_layout()
plt.show()

# 2. subplots()を使った方法
print("\n--- 2. subplots()を使った方法 ---")
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# データの生成
x = np.linspace(0, 2*np.pi, 100)

# 各サブプロットに描画
for i in range(2):
    for j in range(3):
        ax = axes[i, j]
        phase = i*np.pi/2 + j*np.pi/3
        ax.plot(x, np.sin(x + phase), 'b-')
        ax.plot(x, np.cos(x + phase), 'r--')
        ax.set_title(f'Phase shift: {phase:.2f}')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(True, alpha=0.3)
        ax.legend(['sin', 'cos'])

plt.tight_layout()
plt.show()

# 3. 異なるサイズのサブプロット
print("\n--- 3. 異なるサイズのサブプロット ---")
fig = plt.figure(figsize=(12, 8))

# 左側に大きなプロット
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2, rowspan=3)
x = np.linspace(0, 10, 100)
ax1.plot(x, np.sin(x), 'b-', linewidth=2)
ax1.set_title('Main Plot', fontsize=14)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.grid(True)

# 右側に小さなプロット
ax2 = plt.subplot2grid((3, 3), (0, 2))
ax2.plot(np.random.randn(50), 'g-')
ax2.set_title('Random Walk')

ax3 = plt.subplot2grid((3, 3), (1, 2))
ax3.hist(np.random.randn(100), bins=20, color='orange')
ax3.set_title('Histogram')

ax4 = plt.subplot2grid((3, 3), (2, 2))
ax4.scatter(np.random.rand(30), np.random.rand(30))
ax4.set_title('Scatter')

plt.tight_layout()
plt.show()

# 4. GridSpecを使った高度なレイアウト
print("\n--- 4. GridSpecを使った高度なレイアウト ---")
fig = plt.figure(figsize=(12, 10))
gs = gridspec.GridSpec(4, 4, figure=fig)

# 大きな中央プロット
ax_main = fig.add_subplot(gs[1:3, 1:3])
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
im = ax_main.imshow(Z, extent=[-5, 5, -5, 5], cmap='viridis')
ax_main.set_title('2D Function')

# 上部のプロット
ax_top = fig.add_subplot(gs[0, 1:3])
ax_top.plot(x, np.sin(x), 'b-')
ax_top.set_title('Top View')
ax_top.set_xlim(-5, 5)

# 右側のプロット
ax_right = fig.add_subplot(gs[1:3, 3])
ax_right.plot(np.sin(y), y, 'r-')
ax_right.set_title('Side View')
ax_right.set_ylim(-5, 5)

# カラーバー
ax_cbar = fig.add_subplot(gs[1:3, 0])
plt.colorbar(im, cax=ax_cbar)

plt.tight_layout()
plt.show()

# 5. 共有軸を持つサブプロット
print("\n--- 5. 共有軸を持つサブプロット ---")
fig, axes = plt.subplots(3, 1, figsize=(10, 10), sharex=True)

x = np.linspace(0, 10, 1000)
signals = [
    np.sin(2 * np.pi * x),
    np.sin(4 * np.pi * x),
    np.sin(6 * np.pi * x)
]
titles = ['2 Hz', '4 Hz', '6 Hz']

for ax, signal, title in zip(axes, signals, titles):
    ax.plot(x, signal)
    ax.set_title(f'Signal: {title}')
    ax.set_ylabel('Amplitude')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-1.5, 1.5)

axes[-1].set_xlabel('Time (s)')
plt.tight_layout()
plt.show()

# 6. 双軸グラフ
print("\n--- 6. 双軸グラフ ---")
fig, ax1 = plt.subplots(figsize=(10, 6))

# 第一軸
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
color = 'tab:blue'
ax1.set_xlabel('X')
ax1.set_ylabel('sin(x)', color=color)
ax1.plot(x, y1, color=color, linewidth=2)
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, alpha=0.3)

# 第二軸
ax2 = ax1.twinx()
y2 = np.exp(-x/10)
color = 'tab:red'
ax2.set_ylabel('exp(-x/10)', color=color)
ax2.plot(x, y2, color=color, linewidth=2, linestyle='--')
ax2.tick_params(axis='y', labelcolor=color)

ax1.set_title('Dual Y-axis Plot')
fig.tight_layout()
plt.show()

# 7. インセット（挿入図）
print("\n--- 7. インセット（挿入図） ---")
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

fig, ax = plt.subplots(figsize=(10, 8))

# メインプロット
x = np.linspace(0, 10, 1000)
y = np.sin(x) * np.exp(-x/10)
ax.plot(x, y, 'b-', linewidth=2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Main Plot with Inset')
ax.grid(True, alpha=0.3)

# インセット
axins = inset_axes(ax, width="40%", height="30%", loc='upper right')
axins.plot(x[200:400], y[200:400], 'r-', linewidth=2)
axins.set_xlim(2, 4)
axins.set_ylim(0.2, 0.6)
axins.grid(True, alpha=0.3)
axins.set_title('Zoomed Region', fontsize=10)

# ズーム領域を示す
from matplotlib.patches import Rectangle
rect = Rectangle((2, 0.2), 2, 0.4, fill=False, 
                edgecolor='red', linewidth=2)
ax.add_patch(rect)

plt.show()

print("\nサブプロットの例を完了しました！")