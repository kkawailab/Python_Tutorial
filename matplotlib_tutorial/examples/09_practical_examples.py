#!/usr/bin/env python3
"""
Matplotlibチュートリアル - 例9: 実践的な応用例
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from datetime import datetime, timedelta

print("=== 実践的な応用例 ===\n")

# 1. 金融データの可視化
print("--- 1. 金融データの可視化 ---")
# 株価データのシミュレーション
np.random.seed(42)
days = 252  # 1年の営業日
dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(days)]

# 価格データ
initial_price = 100
returns = np.random.normal(0.0005, 0.02, days)
prices = initial_price * np.exp(np.cumsum(returns))

# ボリューム
volume = np.random.randint(1000000, 5000000, days)

# 移動平均
ma20 = np.convolve(prices, np.ones(20)/20, mode='valid')
ma50 = np.convolve(prices, np.ones(50)/50, mode='valid')

# プロット
fig = plt.figure(figsize=(14, 10))
gs = gridspec.GridSpec(3, 1, height_ratios=[3, 1, 1], hspace=0.1)

# 価格チャート
ax1 = plt.subplot(gs[0])
ax1.plot(dates, prices, 'b-', linewidth=1, label='Price')
ax1.plot(dates[19:], ma20, 'r-', linewidth=1.5, label='MA20')
ax1.plot(dates[49:], ma50, 'g-', linewidth=1.5, label='MA50')
ax1.fill_between(dates, prices * 0.95, prices * 1.05, alpha=0.1)
ax1.set_ylabel('Price ($)', fontsize=12)
ax1.set_title('Stock Price Analysis', fontsize=16, fontweight='bold')
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.3)
ax1.set_xticklabels([])

# RSI（相対力指数）
rsi_period = 14
delta = np.diff(prices)
gain = np.where(delta > 0, delta, 0)
loss = np.where(delta < 0, -delta, 0)
avg_gain = np.convolve(gain, np.ones(rsi_period)/rsi_period, mode='valid')
avg_loss = np.convolve(loss, np.ones(rsi_period)/rsi_period, mode='valid')
rs = avg_gain / (avg_loss + 1e-10)
rsi = 100 - (100 / (1 + rs))

ax2 = plt.subplot(gs[1], sharex=ax1)
ax2.plot(dates[rsi_period:], rsi, 'purple', linewidth=1.5)
ax2.axhline(y=70, color='r', linestyle='--', alpha=0.5)
ax2.axhline(y=30, color='g', linestyle='--', alpha=0.5)
ax2.fill_between(dates[rsi_period:], 30, 70, alpha=0.1)
ax2.set_ylabel('RSI', fontsize=12)
ax2.set_ylim(0, 100)
ax2.grid(True, alpha=0.3)
ax2.set_xticklabels([])

# ボリューム
ax3 = plt.subplot(gs[2], sharex=ax1)
colors = ['g' if prices[i] > prices[i-1] else 'r' for i in range(1, len(prices))]
colors = ['g'] + colors  # 最初の日
ax3.bar(dates, volume, color=colors, alpha=0.5)
ax3.set_ylabel('Volume', fontsize=12)
ax3.set_xlabel('Date', fontsize=12)
ax3.grid(True, alpha=0.3, axis='y')

# X軸のフォーマット
import matplotlib.dates as mdates
ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
ax3.xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# 2. 科学実験データの分析
print("\n--- 2. 科学実験データの分析 ---")
# 実験データのシミュレーション
x_theory = np.linspace(0, 10, 100)
y_theory = 2 * x_theory + 1

# 測定データ（ノイズ付き）
n_measurements = 50
x_measured = np.linspace(0.5, 9.5, n_measurements)
noise = np.random.normal(0, 1, n_measurements)
y_measured = 2 * x_measured + 1 + noise
y_error = np.abs(np.random.normal(0.5, 0.2, n_measurements))

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 測定データと理論値
ax = axes[0, 0]
ax.errorbar(x_measured, y_measured, yerr=y_error, fmt='o', 
           capsize=5, capthick=2, label='Measured', alpha=0.7)
ax.plot(x_theory, y_theory, 'r-', linewidth=2, label='Theory')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Experimental Data vs Theory')
ax.legend()
ax.grid(True, alpha=0.3)

# 残差プロット
ax = axes[0, 1]
residuals = y_measured - (2 * x_measured + 1)
ax.scatter(x_measured, residuals, alpha=0.6)
ax.axhline(y=0, color='r', linestyle='--')
ax.fill_between(x_measured, -2, 2, alpha=0.2, color='gray')
ax.set_xlabel('X')
ax.set_ylabel('Residuals')
ax.set_title('Residual Plot')
ax.grid(True, alpha=0.3)

# 残差のヒストグラム
ax = axes[1, 0]
ax.hist(residuals, bins=15, alpha=0.7, color='blue', edgecolor='black')
ax.axvline(x=0, color='r', linestyle='--')
ax.set_xlabel('Residuals')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Residuals')
ax.grid(True, alpha=0.3, axis='y')

# Q-Qプロット
ax = axes[1, 1]
from scipy import stats
stats.probplot(residuals, dist="norm", plot=ax)
ax.set_title('Q-Q Plot')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 3. 地理データの可視化
print("\n--- 3. 地理データの可視化 ---")
# 都市データのシミュレーション
cities = {
    'Tokyo': (35.6762, 139.6503, 37.4),
    'Delhi': (28.7041, 77.1025, 30.3),
    'Shanghai': (31.2304, 121.4737, 27.1),
    'São Paulo': (-23.5505, -46.6333, 22.0),
    'Mexico City': (19.4326, -99.1332, 21.8),
    'Cairo': (30.0444, 31.2357, 20.5),
    'Mumbai': (19.0760, 72.8777, 20.4),
    'Beijing': (39.9042, 116.4074, 20.4),
    'Dhaka': (23.8103, 90.4125, 20.3),
    'Osaka': (34.6937, 135.5023, 19.3)
}

fig, ax = plt.subplots(figsize=(12, 8))

# 散布図として都市をプロット
lats = [city[1][0] for city in cities.items()]
lons = [city[1][1] for city in cities.items()]
populations = [city[1][2] for city in cities.items()]
names = list(cities.keys())

scatter = ax.scatter(lons, lats, s=np.array(populations)*20, 
                    c=populations, cmap='YlOrRd', 
                    alpha=0.6, edgecolors='black', linewidth=1)

# 都市名を追加
for i, name in enumerate(names):
    ax.annotate(name, (lons[i], lats[i]), 
               xytext=(5, 5), textcoords='offset points',
               fontsize=9, fontweight='bold')

ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)
ax.set_title('World\'s Largest Cities by Population', fontsize=16, fontweight='bold')
ax.grid(True, alpha=0.3)

# カラーバー
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Population (millions)', fontsize=12)

# 世界地図の簡単な境界
ax.set_xlim(-180, 180)
ax.set_ylim(-60, 70)
ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
ax.axvline(x=0, color='gray', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

# 4. 機械学習の結果可視化
print("\n--- 4. 機械学習の結果可視化 ---")
# 分類データのシミュレーション
np.random.seed(42)
n_samples = 300

# 3つのクラスを生成
class1 = np.random.multivariate_normal([0, 0], [[0.5, 0], [0, 0.5]], n_samples//3)
class2 = np.random.multivariate_normal([3, 3], [[0.5, 0], [0, 0.5]], n_samples//3)
class3 = np.random.multivariate_normal([0, 3], [[0.5, 0], [0, 0.5]], n_samples//3)

X = np.vstack([class1, class2, class3])
y = np.array([0]*(n_samples//3) + [1]*(n_samples//3) + [2]*(n_samples//3))

# 決定境界のメッシュグリッド
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                     np.linspace(y_min, y_max, 100))

# 決定境界のシミュレーション
Z = np.sin(xx) + np.cos(yy)  # 実際の分類器の代わり

fig = plt.figure(figsize=(15, 5))

# 散布図
ax1 = plt.subplot(131)
scatter = ax1.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', 
                     s=50, alpha=0.6, edgecolors='black')
ax1.set_xlabel('Feature 1')
ax1.set_ylabel('Feature 2')
ax1.set_title('Classification Data')
ax1.grid(True, alpha=0.3)

# 決定境界
ax2 = plt.subplot(132)
contour = ax2.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')
ax2.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', 
           s=50, alpha=0.6, edgecolors='black')
ax2.set_xlabel('Feature 1')
ax2.set_ylabel('Feature 2')
ax2.set_title('Decision Boundaries')
ax2.grid(True, alpha=0.3)

# 混同行列
ax3 = plt.subplot(133)
# シミュレートされた混同行列
cm = np.array([[85, 10, 5],
               [8, 87, 5],
               [7, 3, 90]])

im = ax3.imshow(cm, interpolation='nearest', cmap='Blues')
ax3.set_title('Confusion Matrix')
ax3.set_xlabel('Predicted Label')
ax3.set_ylabel('True Label')

# 各セルに数値を表示
for i in range(3):
    for j in range(3):
        text = ax3.text(j, i, cm[i, j],
                       ha="center", va="center", color="black")

ax3.set_xticks([0, 1, 2])
ax3.set_yticks([0, 1, 2])
ax3.set_xticklabels(['Class 0', 'Class 1', 'Class 2'])
ax3.set_yticklabels(['Class 0', 'Class 1', 'Class 2'])

plt.colorbar(im, ax=ax3)
plt.tight_layout()
plt.show()

# 5. ダッシュボード風の複合プロット
print("\n--- 5. ダッシュボード風の複合プロット ---")
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(3, 4, figure=fig, hspace=0.3, wspace=0.3)

# KPIカード
ax_kpi1 = fig.add_subplot(gs[0, 0])
ax_kpi1.text(0.5, 0.7, '125.4K', ha='center', va='center', 
            fontsize=24, fontweight='bold', transform=ax_kpi1.transAxes)
ax_kpi1.text(0.5, 0.3, 'Total Users', ha='center', va='center', 
            fontsize=12, transform=ax_kpi1.transAxes)
ax_kpi1.text(0.5, 0.1, '↑ 12.5%', ha='center', va='center', 
            fontsize=10, color='green', transform=ax_kpi1.transAxes)
ax_kpi1.set_xticks([])
ax_kpi1.set_yticks([])
ax_kpi1.spines['top'].set_visible(False)
ax_kpi1.spines['right'].set_visible(False)
ax_kpi1.spines['bottom'].set_visible(False)
ax_kpi1.spines['left'].set_visible(False)

# 時系列グラフ
ax_time = fig.add_subplot(gs[0, 1:3])
days = np.arange(30)
values = 100 + np.cumsum(np.random.randn(30))
ax_time.plot(days, values, 'b-', linewidth=2)
ax_time.fill_between(days, values, alpha=0.3)
ax_time.set_title('Daily Active Users')
ax_time.set_xlabel('Days')
ax_time.set_ylabel('Users')
ax_time.grid(True, alpha=0.3)

# 円グラフ
ax_pie = fig.add_subplot(gs[0, 3])
sizes = [35, 25, 20, 15, 5]
labels = ['Mobile', 'Desktop', 'Tablet', 'Smart TV', 'Other']
ax_pie.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax_pie.set_title('Device Distribution')

# ヒートマップ
ax_heat = fig.add_subplot(gs[1, :2])
hours = np.arange(24)
days_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
data = np.random.rand(7, 24) * 100
im = ax_heat.imshow(data, cmap='YlOrRd', aspect='auto')
ax_heat.set_xticks(np.arange(24))
ax_heat.set_yticks(np.arange(7))
ax_heat.set_yticklabels(days_week)
ax_heat.set_xlabel('Hour of Day')
ax_heat.set_title('User Activity Heatmap')
plt.colorbar(im, ax=ax_heat)

# 棒グラフ
ax_bar = fig.add_subplot(gs[1, 2:])
categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = np.random.randint(50, 150, 5)
bars = ax_bar.bar(categories, values, color='skyblue')
ax_bar.set_title('Sales by Product')
ax_bar.set_ylabel('Sales ($)')
for bar, value in zip(bars, values):
    ax_bar.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
               f'${value}', ha='center', va='bottom')
ax_bar.grid(True, axis='y', alpha=0.3)

# 散布図とトレンドライン
ax_scatter = fig.add_subplot(gs[2, :])
x = np.random.rand(100) * 100
y = 2 * x + 10 + np.random.randn(100) * 20
ax_scatter.scatter(x, y, alpha=0.5)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
ax_scatter.plot(np.sort(x), p(np.sort(x)), "r--", linewidth=2)
ax_scatter.set_xlabel('Marketing Spend ($)')
ax_scatter.set_ylabel('Revenue ($)')
ax_scatter.set_title('Marketing Spend vs Revenue')
ax_scatter.grid(True, alpha=0.3)

plt.suptitle('Business Analytics Dashboard', fontsize=20, fontweight='bold')
plt.tight_layout()
plt.show()

print("\n実践的な応用例を完了しました！")