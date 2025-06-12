#!/usr/bin/env python3
"""
Seabornチュートリアル - 例2: カテゴリカルプロット
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# スタイル設定
sns.set_theme(style="whitegrid")

# データの準備
tips = sns.load_dataset("tips")
titanic = sns.load_dataset("titanic")

print("=== カテゴリカルプロット ===\n")

# 1. 箱ひげ図（Box Plot）
print("--- 1. 箱ひげ図 ---")
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

# 2. バイオリンプロット（Violin Plot）
print("\n--- 2. バイオリンプロット ---")
plt.figure(figsize=(10, 6))
sns.violinplot(data=tips, x="day", y="total_bill")
plt.title("Total Bill Distribution by Day (Violin Plot)")
plt.show()

# 分割バイオリンプロット
plt.figure(figsize=(12, 6))
sns.violinplot(data=tips, x="day", y="total_bill", 
               hue="sex", split=True, palette="pastel")
plt.title("Split Violin Plot by Gender")
plt.show()

# 内部の分布表示オプション
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# クォータイル
sns.violinplot(data=tips, x="day", y="total_bill", 
               inner="quartiles", ax=axes[0])
axes[0].set_title("Inner: Quartiles")

# ボックス
sns.violinplot(data=tips, x="day", y="total_bill", 
               inner="box", ax=axes[1])
axes[1].set_title("Inner: Box")

# ポイント
sns.violinplot(data=tips, x="size", y="total_bill", 
               inner="point", ax=axes[2])
axes[2].set_title("Inner: Points")

plt.tight_layout()
plt.show()

# 3. スウォームプロット（Swarm Plot）
print("\n--- 3. スウォームプロット ---")
# サンプルサイズを制限（計算時間の節約）
tips_sample = tips.sample(n=100, random_state=42)

plt.figure(figsize=(10, 6))
sns.swarmplot(data=tips_sample, x="day", y="total_bill")
plt.title("Swarm Plot of Total Bill by Day")
plt.show()

# カテゴリプロットの組み合わせ
plt.figure(figsize=(12, 8))
sns.violinplot(data=tips, x="day", y="total_bill", 
               inner=None, alpha=0.3, palette="muted")
sns.swarmplot(data=tips_sample, x="day", y="total_bill", 
              color="black", alpha=0.5, size=3)
plt.title("Violin + Swarm Plot Combination")
plt.show()

# 4. ストリッププロット（Strip Plot）
print("\n--- 4. ストリッププロット ---")
plt.figure(figsize=(10, 6))
sns.stripplot(data=tips, x="day", y="total_bill", 
              jitter=True, alpha=0.7)
plt.title("Strip Plot with Jitter")
plt.show()

# 5. ポイントプロット（Point Plot）
print("\n--- 5. ポイントプロット ---")
plt.figure(figsize=(10, 6))
sns.pointplot(data=tips, x="day", y="total_bill", 
              hue="sex", dodge=True)
plt.title("Point Plot with Confidence Intervals")
plt.show()

# 6. カテゴリプロットのグリッド
print("\n--- 6. カテゴリプロットのグリッド ---")
g = sns.catplot(data=tips, x="day", y="total_bill", 
                hue="sex", col="time", kind="box",
                height=4, aspect=1.2)
g.fig.suptitle("Box Plots by Multiple Categories", y=1.02)
plt.show()

# 7. 複数のプロットタイプの比較
print("\n--- 7. プロットタイプの比較 ---")
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

plot_types = [
    ('box', 'Box Plot'),
    ('violin', 'Violin Plot'),
    ('strip', 'Strip Plot'),
    ('swarm', 'Swarm Plot'),
    ('bar', 'Bar Plot'),
    ('point', 'Point Plot')
]

for idx, (plot_type, title) in enumerate(plot_types):
    ax = axes[idx // 3, idx % 3]
    
    if plot_type == 'box':
        sns.boxplot(data=tips, x="day", y="total_bill", ax=ax)
    elif plot_type == 'violin':
        sns.violinplot(data=tips, x="day", y="total_bill", ax=ax)
    elif plot_type == 'strip':
        sns.stripplot(data=tips, x="day", y="total_bill", ax=ax)
    elif plot_type == 'swarm':
        sns.swarmplot(data=tips_sample, x="day", y="total_bill", ax=ax)
    elif plot_type == 'bar':
        sns.barplot(data=tips, x="day", y="total_bill", ax=ax)
    elif plot_type == 'point':
        sns.pointplot(data=tips, x="day", y="total_bill", ax=ax)
    
    ax.set_title(title)
    ax.set_xlabel('')
    if idx % 3 != 0:
        ax.set_ylabel('')

plt.suptitle("Comparison of Categorical Plot Types", fontsize=16)
plt.tight_layout()
plt.show()

# 統計サマリー
print("\n--- カテゴリ別統計サマリー ---")
summary = tips.groupby(['day', 'time'])['total_bill'].agg(['mean', 'std', 'count'])
print(summary.round(2))

print("\nカテゴリカルプロットの例を完了しました！")