#!/usr/bin/env python3
"""
Matplotlibチュートリアル - 例5: 3Dプロット
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

print("=== 3Dプロット ===\n")

# 1. 3D線プロット
print("--- 1. 3D線プロット ---")
fig = plt.figure(figsize=(12, 10))

# らせん
ax1 = fig.add_subplot(221, projection='3d')
t = np.linspace(0, 20, 100)
x = np.sin(t)
y = np.cos(t)
z = t

ax1.plot(x, y, z, 'b-', linewidth=2)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('3D Helix')

# パラメトリック曲線
ax2 = fig.add_subplot(222, projection='3d')
u = np.linspace(0, 2 * np.pi, 100)
x = np.sin(u) * (1 + np.cos(8 * u) / 10)
y = np.cos(u) * (1 + np.cos(8 * u) / 10)
z = np.sin(8 * u) / 10

ax2.plot(x, y, z, 'r-', linewidth=2)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('3D Parametric Curve')

# 複数の線
ax3 = fig.add_subplot(223, projection='3d')
for i in range(5):
    theta = np.linspace(0, 4 * np.pi, 100)
    z = np.linspace(0, 5, 100)
    r = z / 5 + i / 5
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    ax3.plot(x, y, z, linewidth=2)

ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.set_title('Multiple 3D Lines')

plt.tight_layout()
plt.show()

# 2. 3D散布図
print("\n--- 2. 3D散布図 ---")
fig = plt.figure(figsize=(12, 5))

# 基本的な散布図
ax1 = fig.add_subplot(121, projection='3d')
n = 100
x = np.random.randn(n)
y = np.random.randn(n)
z = np.random.randn(n)
colors = np.random.rand(n)

scatter = ax1.scatter(x, y, z, c=colors, cmap='viridis', s=50, alpha=0.6)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('3D Scatter Plot')
plt.colorbar(scatter, ax=ax1)

# サイズを変えた散布図
ax2 = fig.add_subplot(122, projection='3d')
sizes = 1000 * np.random.rand(n)
scatter2 = ax2.scatter(x, y, z, c=z, s=sizes, alpha=0.3, cmap='plasma')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('3D Scatter with Variable Size')
plt.colorbar(scatter2, ax=ax2)

plt.tight_layout()
plt.show()

# 3. 3D曲面プロット
print("\n--- 3. 3D曲面プロット ---")
fig = plt.figure(figsize=(15, 10))

# メッシュグリッドの作成
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# 関数1: sin(sqrt(x^2 + y^2))
ax1 = fig.add_subplot(221, projection='3d')
Z1 = np.sin(np.sqrt(X**2 + Y**2))
surf1 = ax1.plot_surface(X, Y, Z1, cmap='viridis', alpha=0.8)
ax1.set_title('Surface: sin(sqrt(x² + y²))')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
plt.colorbar(surf1, ax=ax1, shrink=0.5)

# 関数2: ガウシアン
ax2 = fig.add_subplot(222, projection='3d')
Z2 = np.exp(-(X**2 + Y**2) / 10)
surf2 = ax2.plot_surface(X, Y, Z2, cmap='plasma', alpha=0.8)
ax2.set_title('Gaussian Surface')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
plt.colorbar(surf2, ax=ax2, shrink=0.5)

# ワイヤーフレーム
ax3 = fig.add_subplot(223, projection='3d')
Z3 = np.cos(X) * np.sin(Y)
wire = ax3.plot_wireframe(X, Y, Z3, color='blue', alpha=0.5)
ax3.set_title('Wireframe: cos(x)sin(y)')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')

# 等高線と曲面の組み合わせ
ax4 = fig.add_subplot(224, projection='3d')
Z4 = X**2 - Y**2
surf4 = ax4.plot_surface(X, Y, Z4, cmap='coolwarm', alpha=0.7)
contours = ax4.contour(X, Y, Z4, zdir='z', offset=-2, cmap='coolwarm')
ax4.set_title('Surface with Contours')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')
ax4.set_zlim(-2, 20)

plt.tight_layout()
plt.show()

# 4. 3D棒グラフ
print("\n--- 4. 3D棒グラフ ---")
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# データの準備
x_size = 5
y_size = 4
x_pos = np.arange(x_size)
y_pos = np.arange(y_size)
x_pos, y_pos = np.meshgrid(x_pos, y_pos)
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()
z_pos = np.zeros_like(x_pos)

# 高さとカラー
heights = np.random.rand(len(x_pos)) * 10
colors = plt.cm.viridis(heights / heights.max())

# 棒の幅
dx = dy = 0.8
dz = heights

ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=colors, alpha=0.8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Bar Plot')

plt.show()

# 5. 3Dベクトルフィールド
print("\n--- 5. 3Dベクトルフィールド ---")
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# グリッドポイント
x, y, z = np.meshgrid(np.arange(-2, 3, 1),
                      np.arange(-2, 3, 1),
                      np.arange(-2, 3, 1))

# ベクトル成分
u = -y
v = x
w = z * 0.1

ax.quiver(x, y, z, u, v, w, length=0.3, normalize=True, color='blue', alpha=0.6)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Vector Field')
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

plt.show()

# 6. 回転アニメーション用の関数（静止画として表示）
print("\n--- 6. 3Dプロットの視点変更 ---")
fig = plt.figure(figsize=(15, 5))

# データ
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi, 50)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

# 異なる視点
views = [(30, 45), (60, 45), (30, 135)]
titles = ['View 1: elev=30°, azim=45°', 
          'View 2: elev=60°, azim=45°', 
          'View 3: elev=30°, azim=135°']

for i, (elev, azim) in enumerate(views):
    ax = fig.add_subplot(1, 3, i+1, projection='3d')
    ax.plot_surface(x, y, z, cmap='ocean', alpha=0.8)
    ax.view_init(elev=elev, azim=azim)
    ax.set_title(titles[i])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

plt.tight_layout()
plt.show()

# 7. 複合3Dプロット
print("\n--- 7. 複合3Dプロット ---")
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# 曲面
x = np.linspace(-3, 3, 30)
y = np.linspace(-3, 3, 30)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)
surf = ax.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.6)

# 等高線を底面に投影
contours = ax.contour(X, Y, Z, zdir='z', offset=-1.5, cmap='coolwarm', alpha=0.8)

# 散布図を追加
n = 50
xs = np.random.uniform(-3, 3, n)
ys = np.random.uniform(-3, 3, n)
zs = np.sin(xs) * np.cos(ys) + np.random.normal(0, 0.1, n)
ax.scatter(xs, ys, zs, c='red', s=50, alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Combined 3D Plot: Surface + Scatter + Contours')
ax.set_zlim(-1.5, 1.5)

plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
plt.show()

print("\n3Dプロットの例を完了しました！")