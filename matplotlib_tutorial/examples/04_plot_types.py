#!/usr/bin/env python3
"""
Matplotlibチュートリアル - 例4: 様々なプロットタイプ
"""

import matplotlib.pyplot as plt
import numpy as np

print("=== 様々なプロットタイプ ===\n")

# 1. ヒストグラム
print("--- 1. ヒストグラム ---")
np.random.seed(42)
data1 = np.random.normal(100, 15, 1000)
data2 = np.random.normal(130, 20, 1000)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 基本的なヒストグラム
ax1.hist(data1, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
ax1.set_title('Basic Histogram')
ax1.set_xlabel('Value')
ax1.set_ylabel('Frequency')
ax1.grid(True, alpha=0.3)

# 重ね合わせヒストグラム
ax2.hist(data1, bins=30, alpha=0.5, label='Dataset 1', color='blue')
ax2.hist(data2, bins=30, alpha=0.5, label='Dataset 2', color='red')
ax2.set_title('Overlapping Histograms')
ax2.set_xlabel('Value')
ax2.set_ylabel('Frequency')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 2. 箱ひげ図
print("\n--- 2. 箱ひげ図 ---")
# データの生成
data = [np.random.normal(100, 10, 200),
        np.random.normal(90, 20, 200),
        np.random.normal(110, 15, 200),
        np.random.normal(95, 25, 200)]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 垂直箱ひげ図
bp1 = ax1.boxplot(data, labels=['A', 'B', 'C', 'D'], patch_artist=True)
ax1.set_title('Vertical Box Plot')
ax1.set_ylabel('Values')
ax1.grid(True, axis='y', alpha=0.3)

# 色付け
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']
for patch, color in zip(bp1['boxes'], colors):
    patch.set_facecolor(color)

# 水平箱ひげ図
bp2 = ax2.boxplot(data, labels=['A', 'B', 'C', 'D'], 
                  vert=False, patch_artist=True, notch=True)
ax2.set_title('Horizontal Box Plot with Notch')
ax2.set_xlabel('Values')
ax2.grid(True, axis='x', alpha=0.3)

plt.tight_layout()
plt.show()

# 3. バイオリンプロット
print("\n--- 3. バイオリンプロット ---")
fig, ax = plt.subplots(figsize=(10, 6))

# データ
np.random.seed(42)
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

parts = ax.violinplot(data, positions=range(1, 5), showmeans=True, showmedians=True)

# カスタマイズ
for pc in parts['bodies']:
    pc.set_facecolor('#D43F3A')
    pc.set_alpha(0.7)

ax.set_title('Violin Plot')
ax.set_xlabel('Dataset')
ax.set_ylabel('Values')
ax.set_xticks(range(1, 5))
ax.set_xticklabels(['σ=1', 'σ=2', 'σ=3', 'σ=4'])
ax.grid(True, alpha=0.3)

plt.show()

# 4. ヒートマップ
print("\n--- 4. ヒートマップ ---")
# データの生成
data = np.random.randn(10, 12)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 基本的なヒートマップ
im1 = ax1.imshow(data, cmap='hot', interpolation='nearest')
ax1.set_title('Basic Heatmap')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
plt.colorbar(im1, ax=ax1)

# 注釈付きヒートマップ
im2 = ax2.imshow(data, cmap='coolwarm', interpolation='nearest')
ax2.set_title('Annotated Heatmap')

# 各セルに値を表示
for i in range(10):
    for j in range(12):
        text = ax2.text(j, i, f'{data[i, j]:.1f}',
                       ha="center", va="center", color="black", fontsize=8)

ax2.set_xticks(np.arange(12))
ax2.set_yticks(np.arange(10))
plt.colorbar(im2, ax=ax2)

plt.tight_layout()
plt.show()

# 5. 等高線図
print("\n--- 5. 等高線図 ---")
# 2D関数のデータ
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2)) * np.exp(-0.1 * (X**2 + Y**2))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 塗りつぶし等高線
cs1 = ax1.contourf(X, Y, Z, levels=20, cmap='viridis')
ax1.set_title('Filled Contour')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
plt.colorbar(cs1, ax=ax1)

# 等高線
cs2 = ax2.contour(X, Y, Z, levels=15, colors='black', linewidths=0.5)
ax2.clabel(cs2, inline=True, fontsize=8)
im2 = ax2.imshow(Z, extent=[-3, 3, -3, 3], origin='lower', 
                 cmap='RdBu', alpha=0.5)
ax2.set_title('Contour Lines with Background')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
plt.colorbar(im2, ax=ax2)

plt.tight_layout()
plt.show()

# 6. 極座標プロット
print("\n--- 6. 極座標プロット ---")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), 
                               subplot_kw=dict(projection='polar'))

# 花の形
theta = np.linspace(0, 2*np.pi, 100)
r1 = 1 + np.sin(5*theta)
ax1.plot(theta, r1, 'b-', linewidth=2)
ax1.fill(theta, r1, alpha=0.2)
ax1.set_title('Flower Pattern')

# レーダーチャート
categories = ['Speed', 'Power', 'Skill', 'Defense', 'Magic']
values = [4, 3, 5, 2, 4]
values += values[:1]  # 閉じるため

angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
angles = np.concatenate([angles, [angles[0]]])

ax2.plot(angles, values, 'o-', linewidth=2)
ax2.fill(angles, values, alpha=0.25)
ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(categories)
ax2.set_ylim(0, 5)
ax2.set_title('Radar Chart')
ax2.grid(True)

plt.tight_layout()
plt.show()

# 7. ステップ関数と階段プロット
print("\n--- 7. ステップ関数と階段プロット ---")
x = np.arange(10)
y = np.random.randint(0, 10, 10)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# ステップ関数（デフォルト）
ax1.step(x, y, where='mid', label='mid')
ax1.plot(x, y, 'o', alpha=0.5)
ax1.set_title('Step Function (where="mid")')
ax1.grid(True, alpha=0.3)
ax1.legend()

# ステップ関数（pre）
ax2.step(x, y, where='pre', label='pre', color='red')
ax2.plot(x, y, 'o', alpha=0.5)
ax2.set_title('Step Function (where="pre")')
ax2.grid(True, alpha=0.3)
ax2.legend()

# ステップ関数（post）
ax3.step(x, y, where='post', label='post', color='green')
ax3.plot(x, y, 'o', alpha=0.5)
ax3.set_title('Step Function (where="post")')
ax3.grid(True, alpha=0.3)
ax3.legend()

plt.tight_layout()
plt.show()

# 8. エラーバー
print("\n--- 8. エラーバー ---")
x = np.linspace(0, 10, 10)
y = np.sin(x)
y_err = 0.1 + 0.1 * np.random.rand(10)
x_err = 0.1 + 0.1 * np.random.rand(10)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Y方向のエラーバー
ax1.errorbar(x, y, yerr=y_err, fmt='o-', capsize=5, capthick=2,
             label='Data with y-error')
ax1.set_title('Y Error Bars')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.legend()
ax1.grid(True, alpha=0.3)

# X方向とY方向のエラーバー
ax2.errorbar(x, y, xerr=x_err, yerr=y_err, fmt='s', capsize=5,
             capthick=2, label='Data with x,y-error', color='red')
ax2.set_title('X and Y Error Bars')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n様々なプロットタイプの例を完了しました！")