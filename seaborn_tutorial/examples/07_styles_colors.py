#!/usr/bin/env python3
"""
Seabornチュートリアル - 例7: スタイルとカラーパレット
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# データの準備
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

print("=== スタイルとカラーパレット ===\n")

# 1. Seabornのスタイル
print("--- 1. 利用可能なスタイル ---")
styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for idx, style in enumerate(styles):
    if idx < len(axes):
        with sns.axes_style(style):
            ax = axes[idx]
            tips_sample = tips.sample(50, random_state=42)
            sns.scatterplot(data=tips_sample, x="total_bill", 
                          y="tip", ax=ax)
            ax.set_title(f"Style: {style}", fontsize=14, fontweight='bold')

# 余った軸を削除
if len(styles) < len(axes):
    fig.delaxes(axes[-1])

plt.suptitle("Seaborn Styles Comparison", fontsize=16)
plt.tight_layout()
plt.show()

# 2. スタイルのカスタマイズ
print("\n--- 2. スタイルのカスタマイズ ---")
# カスタムスタイルパラメータ
custom_style = {
    "axes.facecolor": "#f0f0f0",
    "axes.edgecolor": "#333333",
    "axes.linewidth": 2,
    "grid.color": "#cccccc",
    "grid.linestyle": "--",
    "grid.linewidth": 0.5
}

plt.figure(figsize=(10, 6))
with sns.axes_style("whitegrid", custom_style):
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day")
    plt.title("Custom Style Parameters")
plt.show()

# 3. カラーパレット
print("\n--- 3. 組み込みカラーパレット ---")
palettes = ['deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind']
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for idx, palette in enumerate(palettes):
    ax = axes[idx]
    sns.set_palette(palette)
    colors = sns.color_palette(palette)
    
    # パレットの表示
    for i, color in enumerate(colors):
        ax.bar(i, 1, color=color, width=0.8)
    
    ax.set_title(f"Palette: {palette}", fontsize=14)
    ax.set_xlim(-0.5, len(colors) - 0.5)
    ax.set_ylim(0, 1.2)
    ax.set_xticks([])
    ax.set_yticks([])

plt.suptitle("Built-in Color Palettes", fontsize=16)
plt.tight_layout()
plt.show()

# デフォルトに戻す
sns.set_palette("deep")

# 4. カテゴリカルパレット
print("\n--- 4. カテゴリカルパレット ---")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Set1
ax = axes[0, 0]
palette = sns.color_palette("Set1")
sns.barplot(data=tips, x="day", y="total_bill", 
           palette=palette, ax=ax)
ax.set_title("Set1 Palette")

# Set2
ax = axes[0, 1]
palette = sns.color_palette("Set2")
sns.barplot(data=tips, x="day", y="total_bill", 
           palette=palette, ax=ax)
ax.set_title("Set2 Palette")

# Set3
ax = axes[1, 0]
palette = sns.color_palette("Set3")
sns.barplot(data=tips, x="day", y="total_bill", 
           palette=palette, ax=ax)
ax.set_title("Set3 Palette")

# Paired
ax = axes[1, 1]
palette = sns.color_palette("Paired")
sns.barplot(data=tips, x="day", y="total_bill", 
           palette=palette, ax=ax)
ax.set_title("Paired Palette")

plt.suptitle("Categorical Color Palettes", fontsize=16)
plt.tight_layout()
plt.show()

# 5. 連続的なカラーパレット
print("\n--- 5. 連続的なカラーパレット ---")
# グラデーションパレット
fig, axes = plt.subplots(3, 2, figsize=(12, 14))

continuous_palettes = [
    ('Blues', 'Sequential'),
    ('Reds', 'Sequential'),
    ('RdBu', 'Diverging'),
    ('coolwarm', 'Diverging'),
    ('viridis', 'Perceptual'),
    ('plasma', 'Perceptual')
]

# サンプルデータ
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.randn(100) * 0.1
hue = x

for idx, (palette_name, palette_type) in enumerate(continuous_palettes):
    ax = axes[idx // 2, idx % 2]
    
    scatter = ax.scatter(x, y, c=hue, cmap=palette_name, s=50)
    ax.set_title(f"{palette_name} ({palette_type})")
    plt.colorbar(scatter, ax=ax)

plt.suptitle("Continuous Color Palettes", fontsize=16)
plt.tight_layout()
plt.show()

# 6. カスタムカラーパレット
print("\n--- 6. カスタムカラーパレット ---")
# 色のリストからパレットを作成
custom_colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]
custom_palette = sns.color_palette(custom_colors)

plt.figure(figsize=(12, 6))

# カスタムパレットの表示
plt.subplot(1, 2, 1)
sns.palplot(custom_palette)
plt.title("Custom Color Palette")

# カスタムパレットの使用
plt.subplot(1, 2, 2)
sns.barplot(data=tips, x="day", y="total_bill", 
           palette=custom_palette)
plt.title("Using Custom Palette")

plt.tight_layout()
plt.show()

# 7. カラーパレットの生成
print("\n--- 7. カラーパレットの生成 ---")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# husl パレット（均等に分布した色相）
ax = axes[0, 0]
n_colors = 8
palette = sns.color_palette("husl", n_colors)
for i, color in enumerate(palette):
    ax.bar(i, 1, color=color)
ax.set_title(f"HUSL Palette (n={n_colors})")
ax.set_ylim(0, 1.2)

# グラデーションパレット
ax = axes[0, 1]
palette = sns.light_palette("navy", n_colors=8)
for i, color in enumerate(palette):
    ax.bar(i, 1, color=color)
ax.set_title("Light Palette (from navy)")
ax.set_ylim(0, 1.2)

# ダークパレット
ax = axes[1, 0]
palette = sns.dark_palette("green", n_colors=8)
for i, color in enumerate(palette):
    ax.bar(i, 1, color=color)
ax.set_title("Dark Palette (from green)")
ax.set_ylim(0, 1.2)

# 発散パレット
ax = axes[1, 1]
palette = sns.diverging_palette(220, 20, n=8)
for i, color in enumerate(palette):
    ax.bar(i, 1, color=color)
ax.set_title("Diverging Palette")
ax.set_ylim(0, 1.2)

for ax in axes.flat:
    ax.set_xticks([])
    ax.set_yticks([])

plt.suptitle("Generated Color Palettes", fontsize=16)
plt.tight_layout()
plt.show()

# 8. コンテキスト設定
print("\n--- 8. プロットコンテキスト ---")
contexts = ['paper', 'notebook', 'talk', 'poster']
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
axes = axes.flatten()

for idx, context in enumerate(contexts):
    with sns.plotting_context(context):
        ax = axes[idx]
        sns.lineplot(data=tips.groupby('size')['total_bill'].mean().reset_index(),
                    x='size', y='total_bill', ax=ax, marker='o', markersize=8)
        ax.set_title(f"Context: {context}", fontsize=14)
        ax.grid(True, alpha=0.3)

plt.suptitle("Different Plotting Contexts", fontsize=16)
plt.tight_layout()
plt.show()

# 9. テーマの組み合わせ
print("\n--- 9. テーマの組み合わせ ---")
# スタイル、パレット、コンテキストの組み合わせ
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

combinations = [
    ('darkgrid', 'deep', 'notebook'),
    ('whitegrid', 'pastel', 'paper'),
    ('ticks', 'bright', 'talk'),
    ('white', 'muted', 'poster')
]

for idx, (style, palette, context) in enumerate(combinations):
    ax = axes[idx // 2, idx % 2]
    
    with sns.axes_style(style), sns.plotting_context(context):
        sns.set_palette(palette)
        sns.violinplot(data=tips, x="day", y="total_bill", ax=ax)
        ax.set_title(f"Style: {style}, Palette: {palette}, Context: {context}")

plt.suptitle("Theme Combinations", fontsize=16)
plt.tight_layout()
plt.show()

# 10. 実用的な例：出版品質のプロット
print("\n--- 10. 出版品質のプロット ---")
# リセット
sns.set_theme()

# 出版用の設定
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("colorblind")

# フォントサイズの調整
plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'figure.dpi': 150
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# プロット1：回帰プロット
sns.regplot(data=tips, x="total_bill", y="tip", ax=ax1,
           scatter_kws={'alpha': 0.6, 's': 50},
           line_kws={'linewidth': 2})
ax1.set_xlabel("Total Bill ($)", fontweight='bold')
ax1.set_ylabel("Tip ($)", fontweight='bold')
ax1.set_title("Relationship between Bill and Tip", fontweight='bold')
ax1.grid(True, alpha=0.3)

# プロット2：カテゴリプロット
sns.boxplot(data=tips, x="day", y="total_bill", ax=ax2,
           palette="Set2", width=0.6)
ax2.set_xlabel("Day of Week", fontweight='bold')
ax2.set_ylabel("Total Bill ($)", fontweight='bold')
ax2.set_title("Bill Distribution by Day", fontweight='bold')
ax2.grid(True, alpha=0.3, axis='y')

plt.suptitle("Publication-Ready Plots", fontsize=18, fontweight='bold')
plt.tight_layout()
plt.show()

print("\nスタイルとカラーパレットの例を完了しました！")