#!/usr/bin/env python3
"""
Matplotlibチュートリアル - 例1: 基本的なプロット
"""

import matplotlib.pyplot as plt
import numpy as np

# 日本語フォントの設定
plt.rcParams['font.family'] = 'DejaVu Sans'  # 環境に応じて変更
plt.rcParams['axes.unicode_minus'] = False

print("=== 基本的なプロット ===\n")

# 1. 単純な折れ線グラフ
print("--- 1. 単純な折れ線グラフ ---")
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title('Simple Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()

# 2. 複数の線を持つグラフ
print("\n--- 2. 複数の線を持つグラフ ---")
y2 = np.cos(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.title('Trigonometric Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# 3. 線のスタイルとマーカー
print("\n--- 3. 線のスタイルとマーカー ---")
x = np.linspace(0, 10, 20)

plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x), 'b-', label='Solid line', linewidth=2)
plt.plot(x, np.sin(x + 0.5), 'r--', label='Dashed line', linewidth=2)
plt.plot(x, np.sin(x + 1.0), 'g-.', label='Dash-dot line', linewidth=2)
plt.plot(x, np.sin(x + 1.5), 'm:', label='Dotted line', linewidth=2)
plt.plot(x, np.sin(x + 2.0), 'co-', label='With markers', markersize=8)

plt.title('Line Styles and Markers')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.ylim(-1.5, 1.5)
plt.show()

# 4. 散布図
print("\n--- 4. 散布図 ---")
np.random.seed(42)
n = 100
x = np.random.randn(n)
y = 2 * x + np.random.randn(n)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.6)
plt.title('Scatter Plot Example')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True, alpha=0.3)

# 回帰直線の追加
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(np.sort(x), p(np.sort(x)), "r--", linewidth=2, label=f'y={z[0]:.2f}x+{z[1]:.2f}')
plt.legend()
plt.show()

# 5. 棒グラフ
print("\n--- 5. 棒グラフ ---")
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']

plt.figure(figsize=(8, 6))
bars = plt.bar(categories, values, color=colors, edgecolor='black', linewidth=1.5)

# 値をバーの上に表示
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             str(value), ha='center', va='bottom')

plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.ylim(0, 90)
plt.grid(True, axis='y', alpha=0.3)
plt.show()

# 6. 円グラフ
print("\n--- 6. 円グラフ ---")
labels = ['Python', 'JavaScript', 'Java', 'C++', 'Others']
sizes = [35, 25, 20, 15, 5]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
explode = (0.1, 0, 0, 0, 0)  # Pythonを強調

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Programming Language Usage')
plt.axis('equal')
plt.show()

# 7. ヒストグラム
print("\n--- 7. ヒストグラム ---")
data = np.random.normal(100, 15, 1000)

plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(data, bins=30, color='skyblue', 
                           edgecolor='black', alpha=0.7)

# 正規分布曲線を重ねる
mu, sigma = data.mean(), data.std()
x = np.linspace(data.min(), data.max(), 100)
plt.plot(x, ((1 / (np.sqrt(2 * np.pi) * sigma)) *
              np.exp(-0.5 * (1 / sigma * (x - mu))**2)) * len(data) * (bins[1] - bins[0]),
         'r-', linewidth=2, label=f'Normal Distribution\nμ={mu:.1f}, σ={sigma:.1f}')

plt.title('Histogram with Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True, axis='y', alpha=0.3)
plt.show()

print("\n基本的なプロットの例を完了しました！")