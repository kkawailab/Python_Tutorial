#!/usr/bin/env python3
"""
Seabornチュートリアル - 例3: 分布の可視化
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

# スタイル設定
sns.set_theme(style="whitegrid")

# データの準備
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

print("=== 分布の可視化 ===\n")

# 1. ヒストグラム（Histogram）
print("--- 1. ヒストグラム ---")
plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x="total_bill")
plt.title("Distribution of Total Bill")
plt.show()

# KDE（カーネル密度推定）付きヒストグラム
plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x="total_bill", kde=True, color="skyblue")
plt.title("Histogram with KDE")
plt.show()

# ビン数とスタイルのカスタマイズ
plt.figure(figsize=(12, 6))
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# 異なるビン数
sns.histplot(data=tips, x="total_bill", bins=10, ax=axes[0])
axes[0].set_title("10 bins")

sns.histplot(data=tips, x="total_bill", bins=30, ax=axes[1])
axes[1].set_title("30 bins")

plt.tight_layout()
plt.show()

# 複数変数のヒストグラム
plt.figure(figsize=(12, 6))
sns.histplot(data=tips, x="total_bill", hue="time", 
             multiple="dodge", shrink=0.8)
plt.title("Histogram by Time")
plt.show()

# スタック型ヒストグラム
plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x="total_bill", hue="day", 
             multiple="stack", palette="viridis")
plt.title("Stacked Histogram by Day")
plt.show()

# 2次元ヒストグラム
plt.figure(figsize=(10, 8))
sns.histplot(data=tips, x="total_bill", y="tip", 
             bins=20, cbar=True, cmap="YlOrRd")
plt.title("2D Histogram: Total Bill vs Tip")
plt.show()

# 2. カーネル密度推定（KDE Plot）
print("\n--- 2. KDEプロット ---")
plt.figure(figsize=(10, 6))
sns.kdeplot(data=tips, x="total_bill", fill=True, color="purple")
plt.title("KDE of Total Bill")
plt.show()

# 複数グループのKDE
plt.figure(figsize=(10, 6))
for day in ['Thur', 'Fri', 'Sat', 'Sun']:
    subset = tips[tips['day'] == day]
    sns.kdeplot(data=subset, x="total_bill", label=day)
plt.title("KDE by Day")
plt.legend()
plt.show()

# 帯域幅（bandwidth）の比較
plt.figure(figsize=(12, 6))
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

bw_values = [0.5, 1.0, 2.0]
for ax, bw in zip(axes, bw_values):
    sns.kdeplot(data=tips, x="total_bill", bw_adjust=bw, 
                fill=True, ax=ax)
    ax.set_title(f'Bandwidth = {bw}')

plt.tight_layout()
plt.show()

# 2次元KDE
plt.figure(figsize=(10, 8))
sns.kdeplot(data=tips, x="total_bill", y="tip", 
            cmap="Blues", fill=True, levels=10)
plt.title("2D KDE Plot")
plt.show()

# 等高線プロット
plt.figure(figsize=(10, 8))
sns.kdeplot(data=tips, x="total_bill", y="tip", 
            levels=[0.01, 0.05, 0.1, 0.2])
sns.scatterplot(data=tips, x="total_bill", y="tip", 
                alpha=0.3, color="red", s=10)
plt.title("KDE Contour with Scatter")
plt.show()

# 3. 経験的累積分布関数（ECDF）
print("\n--- 3. ECDFプロット ---")
plt.figure(figsize=(10, 6))
sns.ecdfplot(data=tips, x="total_bill")
plt.title("ECDF of Total Bill")
plt.axhline(y=0.5, color='red', linestyle='--', label='Median')
plt.legend()
plt.show()

# 複数グループのECDF
plt.figure(figsize=(10, 6))
sns.ecdfplot(data=tips, x="total_bill", hue="day")
plt.title("ECDF by Day")
plt.show()

# 4. Q-Qプロット（正規性の確認）
print("\n--- 4. Q-Qプロット ---")
plt.figure(figsize=(10, 6))
stats.probplot(tips['total_bill'], dist="norm", plot=plt)
plt.title("Q-Q Plot: Total Bill")
plt.show()

# 5. ディストプロット（非推奨だが参考として）
print("\n--- 5. 分布の詳細分析 ---")
# 新しいAPIを使用した同等の表現
plt.figure(figsize=(10, 6))
ax = sns.histplot(data=tips, x="total_bill", kde=True, stat="density")
plt.title("Distribution Analysis")

# 統計情報を追加
mean = tips['total_bill'].mean()
median = tips['total_bill'].median()
plt.axvline(mean, color='red', linestyle='--', label=f'Mean: {mean:.2f}')
plt.axvline(median, color='green', linestyle='--', label=f'Median: {median:.2f}')
plt.legend()
plt.show()

# 6. リッジプロット風の可視化
print("\n--- 6. リッジプロット風 ---")
# カテゴリ別の分布を重ねて表示
plt.figure(figsize=(10, 8))
days = ['Thur', 'Fri', 'Sat', 'Sun']
colors = sns.color_palette("husl", len(days))

for i, (day, color) in enumerate(zip(days, colors)):
    data = tips[tips['day'] == day]['total_bill']
    
    # KDEを計算
    density = stats.gaussian_kde(data)
    x = np.linspace(data.min(), data.max(), 100)
    y = density(x)
    
    # オフセットを追加して重ねる
    plt.fill_between(x, i*0.5, i*0.5 + y*2, alpha=0.6, color=color, label=day)
    plt.plot(x, i*0.5 + y*2, color=color, linewidth=2)

plt.xlabel("Total Bill")
plt.ylabel("Day (offset)")
plt.title("Ridge Plot Style Distribution")
plt.legend()
plt.yticks([])
plt.show()

# 7. 分布の比較（複数の方法）
print("\n--- 7. 分布の比較 ---")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# ヒストグラム比較
ax = axes[0, 0]
for time in ['Lunch', 'Dinner']:
    subset = tips[tips['time'] == time]
    sns.histplot(data=subset, x="total_bill", kde=False, 
                 alpha=0.5, label=time, ax=ax)
ax.set_title("Histogram Comparison")
ax.legend()

# KDE比較
ax = axes[0, 1]
for time in ['Lunch', 'Dinner']:
    subset = tips[tips['time'] == time]
    sns.kdeplot(data=subset, x="total_bill", fill=True, 
                alpha=0.5, label=time, ax=ax)
ax.set_title("KDE Comparison")

# ECDF比較
ax = axes[1, 0]
sns.ecdfplot(data=tips, x="total_bill", hue="time", ax=ax)
ax.set_title("ECDF Comparison")

# ボックスプロット比較
ax = axes[1, 1]
sns.boxplot(data=tips, x="time", y="total_bill", ax=ax)
ax.set_title("Box Plot Comparison")

plt.tight_layout()
plt.show()

# 統計的要約
print("\n--- 分布の統計的要約 ---")
print("全体の統計:")
print(tips['total_bill'].describe())
print("\n時間帯別の統計:")
print(tips.groupby('time')['total_bill'].describe())

print("\n分布の可視化の例を完了しました！")