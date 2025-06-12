#!/usr/bin/env python3
"""
Matplotlibチュートリアル - 例2: プロットのカスタマイズ
"""

import matplotlib.pyplot as plt
import numpy as np

print("=== プロットのカスタマイズ ===\n")

# 1. 色のカスタマイズ
print("--- 1. 色のカスタマイズ ---")
x = np.linspace(0, 10, 100)

plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x), color='red', label='Color name')
plt.plot(x, np.sin(x + 0.5), color='#1f77b4', label='Hex color')
plt.plot(x, np.sin(x + 1.0), color=(0.2, 0.8, 0.2), label='RGB tuple')
plt.plot(x, np.sin(x + 1.5), color='C3', label='Default color cycle')

plt.title('Color Customization')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 2. 線の幅とスタイル
print("\n--- 2. 線の幅とスタイル ---")
plt.figure(figsize=(10, 6))

plt.plot(x, np.sin(x), linewidth=1, label='linewidth=1')
plt.plot(x, np.sin(x + 0.5), linewidth=2, label='linewidth=2')
plt.plot(x, np.sin(x + 1.0), linewidth=3, label='linewidth=3')
plt.plot(x, np.sin(x + 1.5), linewidth=4, linestyle='--', label='linewidth=4, dashed')

plt.title('Line Width and Style')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 3. マーカーのカスタマイズ
print("\n--- 3. マーカーのカスタマイズ ---")
x = np.linspace(0, 10, 10)

plt.figure(figsize=(12, 8))

# 様々なマーカースタイル
markers = ['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h']
for i, marker in enumerate(markers):
    y_offset = i * 0.2
    plt.plot(x, np.sin(x) + y_offset, marker=marker, markersize=10, 
             linestyle='-', label=f'marker={marker}')

plt.title('Marker Styles')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 4. 軸のカスタマイズ
print("\n--- 4. 軸のカスタマイズ ---")
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'b-', linewidth=2)

# 軸の範囲
ax.set_xlim(-8, 8)
ax.set_ylim(-1.5, 1.5)

# 軸の目盛り
ax.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
ax.set_xticklabels(['-2π', '-π', '0', 'π', '2π'])
ax.set_yticks([-1, -0.5, 0, 0.5, 1])

# 軸ラベル
ax.set_xlabel('Angle (radians)', fontsize=14, fontweight='bold')
ax.set_ylabel('sin(x)', fontsize=14, fontweight='bold')
ax.set_title('Customized Axes', fontsize=16, fontweight='bold')

# グリッドのカスタマイズ
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.grid(True, which='minor', linestyle=':', linewidth=0.5, alpha=0.3)
ax.minorticks_on()

plt.show()

# 5. 注釈とテキスト
print("\n--- 5. 注釈とテキスト ---")
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'b-', linewidth=2)

# 最大値と最小値に注釈を追加
max_idx = np.argmax(y)
min_idx = np.argmin(y)

ax.annotate('Maximum', xy=(x[max_idx], y[max_idx]), 
            xytext=(x[max_idx]+0.5, y[max_idx]+0.3),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=12, fontweight='bold', color='red')

ax.annotate('Minimum', xy=(x[min_idx], y[min_idx]), 
            xytext=(x[min_idx]+0.5, y[min_idx]-0.3),
            arrowprops=dict(arrowstyle='->', color='blue', lw=2),
            fontsize=12, fontweight='bold', color='blue')

# テキストボックス
ax.text(0.5, 0.95, 'Sine Wave Analysis', transform=ax.transAxes,
        fontsize=14, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

ax.set_title('Annotations and Text')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.grid(True, alpha=0.3)
plt.show()

# 6. カラーマップの使用
print("\n--- 6. カラーマップの使用 ---")
x = np.linspace(0, 10, 20)
y = np.linspace(0, 10, 20)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
cmaps = ['viridis', 'plasma', 'coolwarm', 'RdYlBu']

for ax, cmap in zip(axes.flat, cmaps):
    im = ax.imshow(Z, cmap=cmap, extent=[0, 10, 0, 10], 
                   origin='lower', aspect='auto')
    ax.set_title(f'Colormap: {cmap}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.colorbar(im, ax=ax)

plt.tight_layout()
plt.show()

# 7. カスタムスタイル
print("\n--- 7. カスタムスタイル ---")
# スタイルの設定
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

with plt.rc_context(custom_style):
    x = np.linspace(0, 10, 100)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, np.sin(x), 'o-', label='sin(x)', markevery=10)
    plt.plot(x, np.cos(x), 's-', label='cos(x)', markevery=10)
    
    plt.title('Custom Style Example')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.grid(True)
    plt.show()

print("\nカスタマイズの例を完了しました！")