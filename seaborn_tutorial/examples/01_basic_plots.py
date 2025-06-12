#!/usr/bin/env python3
"""
Seabornチュートリアル - 例1: 基本的なプロット
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# スタイル設定
sns.set_theme(style="whitegrid", palette="husl")

# データの準備
tips = sns.load_dataset("tips")
print("=== 基本的なプロット ===\n")
print(f"データセットの形状: {tips.shape}")
print(f"カラム: {list(tips.columns)}\n")

# 1. 散布図（Scatter Plot）
print("--- 1. 散布図 ---")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title("Total Bill vs Tip")
plt.show()

# hueパラメータで色分け
plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
plt.title("Total Bill vs Tip by Time")
plt.show()

# size、style、hueを組み合わせた高度な散布図
plt.figure(figsize=(12, 8))
sns.scatterplot(data=tips, x="total_bill", y="tip", 
                hue="day", size="size", style="sex",
                palette="deep", sizes=(50, 200))
plt.title("Advanced Scatter Plot")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 2. 線グラフ（Line Plot）
print("\n--- 2. 線グラフ ---")
# 時系列データの作成
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=100)
data = pd.DataFrame({
    'date': dates,
    'value': np.cumsum(np.random.randn(100)) + 50,
    'category': np.random.choice(['A', 'B'], 100)
})

plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='date', y='value', hue='category')
plt.title("Time Series Line Plot")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 信頼区間付き線グラフ
fmri = sns.load_dataset("fmri")
plt.figure(figsize=(10, 6))
sns.lineplot(data=fmri, x="timepoint", y="signal", 
             hue="region", style="event", markers=True)
plt.title("Line Plot with Confidence Intervals")
plt.show()

# 3. 棒グラフ（Bar Plot）
print("\n--- 3. 棒グラフ ---")
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x="day", y="total_bill")
plt.title("Average Total Bill by Day")
plt.show()

# hueで分割した棒グラフ
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x="day", y="total_bill", hue="sex")
plt.title("Average Total Bill by Day and Gender")
plt.show()

# 4. カウントプロット（Count Plot）
print("\n--- 4. カウントプロット ---")
plt.figure(figsize=(10, 6))
sns.countplot(data=tips, x="day", hue="time")
plt.title("Count of Observations by Day and Time")
plt.show()

# 5. 基本的な統計情報の表示
print("\n--- 5. 基本的な統計情報 ---")
print(tips.groupby('day')['total_bill'].describe().round(2))

print("\n基本的なプロットの例を完了しました！")