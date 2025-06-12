#!/usr/bin/env python3
"""
Seabornチュートリアル - 例9: 高度な統計プロット
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# スタイル設定
sns.set_theme(style="whitegrid")

# データの準備
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")

print("=== 高度な統計プロット ===\n")

# 1. 統計的推定の可視化
print("--- 1. 統計的推定の可視化 ---")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# ブートストラップ信頼区間
ax = axes[0, 0]
sns.barplot(data=tips, x="day", y="total_bill", 
            errorbar=('ci', 95), n_boot=1000,
            capsize=0.1, ax=ax)
ax.set_title("Bootstrap 95% Confidence Intervals")

# 標準誤差
ax = axes[0, 1]
sns.barplot(data=tips, x="day", y="total_bill", 
            errorbar='se', capsize=0.2, ax=ax)
ax.set_title("Standard Error Bars")

# ポイントプロット（平均と信頼区間）
ax = axes[1, 0]
sns.pointplot(data=tips, x="day", y="total_bill", 
              hue="sex", dodge=True, 
              markers=["o", "s"], linestyles=["-", "--"],
              ax=ax)
ax.set_title("Point Plot with CI")

# カスタム集計関数
ax = axes[1, 1]
def median_and_iqr(x):
    median = np.median(x)
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    return pd.Series([median, q1, q3], index=['median', 'q1', 'q3'])

summary = tips.groupby('day')['total_bill'].apply(median_and_iqr).unstack()
x = np.arange(len(summary))
ax.errorbar(x, summary['median'], 
           yerr=[summary['median'] - summary['q1'], 
                 summary['q3'] - summary['median']],
           fmt='o', capsize=5, capthick=2)
ax.set_xticks(x)
ax.set_xticklabels(summary.index)
ax.set_xlabel('Day')
ax.set_ylabel('Total Bill')
ax.set_title("Median with IQR")

plt.suptitle("Statistical Estimation Visualizations", fontsize=16)
plt.tight_layout()
plt.show()

# 2. 分布の比較と検定
print("\n--- 2. 分布の比較と検定 ---")
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Q-Qプロット
ax = axes[0, 0]
lunch_bills = tips[tips['time'] == 'Lunch']['total_bill']
dinner_bills = tips[tips['time'] == 'Dinner']['total_bill']
stats.probplot(lunch_bills, dist="norm", plot=ax)
ax.set_title("Q-Q Plot: Lunch Bills")

# P-Pプロット
ax = axes[0, 1]
# 累積分布の計算
sorted_data = np.sort(dinner_bills)
n = len(sorted_data)
theoretical = stats.norm.cdf(sorted_data, loc=sorted_data.mean(), scale=sorted_data.std())
empirical = np.arange(1, n + 1) / n
ax.plot(theoretical, empirical, 'o', alpha=0.5)
ax.plot([0, 1], [0, 1], 'r--')
ax.set_xlabel('Theoretical Cumulative Probability')
ax.set_ylabel('Empirical Cumulative Probability')
ax.set_title("P-P Plot: Dinner Bills")

# KDE比較（帯域幅の影響）
ax = axes[0, 2]
for bw in [0.5, 1.0, 2.0]:
    sns.kdeplot(data=tips, x="total_bill", bw_adjust=bw, 
                label=f'bw={bw}', ax=ax)
ax.set_title("KDE with Different Bandwidths")
ax.legend()

# 2標本の分布比較
ax = axes[1, 0]
sns.kdeplot(data=lunch_bills, label='Lunch', fill=True, alpha=0.5, ax=ax)
sns.kdeplot(data=dinner_bills, label='Dinner', fill=True, alpha=0.5, ax=ax)
ax.axvline(lunch_bills.mean(), color='blue', linestyle='--', alpha=0.7)
ax.axvline(dinner_bills.mean(), color='orange', linestyle='--', alpha=0.7)
ax.set_title("Distribution Comparison")
ax.legend()

# 累積分布の比較
ax = axes[1, 1]
sns.ecdfplot(data=tips, x="total_bill", hue="time", ax=ax)
ax.set_title("Empirical CDF Comparison")

# 統計検定の結果表示
ax = axes[1, 2]
# t検定
t_stat, t_pval = stats.ttest_ind(lunch_bills, dinner_bills)
# Mann-Whitney U検定
u_stat, u_pval = stats.mannwhitneyu(lunch_bills, dinner_bills)
# Kolmogorov-Smirnov検定
ks_stat, ks_pval = stats.ks_2samp(lunch_bills, dinner_bills)

test_results = f"""Statistical Tests:

t-test:
  statistic = {t_stat:.3f}
  p-value = {t_pval:.4f}

Mann-Whitney U:
  statistic = {u_stat:.1f}
  p-value = {u_pval:.4f}

Kolmogorov-Smirnov:
  statistic = {ks_stat:.3f}
  p-value = {ks_pval:.4f}
"""
ax.text(0.1, 0.5, test_results, transform=ax.transAxes, 
        fontsize=10, verticalalignment='center',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title("Statistical Test Results")

plt.suptitle("Distribution Comparison and Testing", fontsize=16)
plt.tight_layout()
plt.show()

# 3. 相関と関係性の高度な可視化
print("\n--- 3. 相関と関係性の高度な可視化 ---")
# 相関行列の計算
numeric_cols = tips.select_dtypes(include=[np.number]).columns
corr_matrix = tips[numeric_cols].corr()

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 部分相関
ax = axes[0, 0]
# sizeを制御した場合のtotal_billとtipの相関
from sklearn.linear_model import LinearRegression
X = tips[['size']].values
y_bill = tips['total_bill'].values
y_tip = tips['tip'].values

# 残差の計算
lr = LinearRegression()
resid_bill = y_bill - lr.fit(X, y_bill).predict(X)
resid_tip = y_tip - lr.fit(X, y_tip).predict(X)

ax.scatter(resid_bill, resid_tip, alpha=0.5)
ax.set_xlabel('Total Bill (residuals after size)')
ax.set_ylabel('Tip (residuals after size)')
ax.set_title(f'Partial Correlation\nr = {np.corrcoef(resid_bill, resid_tip)[0,1]:.3f}')

# 共分散楕円
ax = axes[0, 1]
from matplotlib.patches import Ellipse

def plot_cov_ellipse(data, ax, n_std=2, **kwargs):
    mean = data.mean(axis=0)
    cov = np.cov(data.T)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    angle = np.degrees(np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0]))
    width, height = 2 * n_std * np.sqrt(eigenvalues)
    ellipse = Ellipse(mean, width, height, angle=angle, **kwargs)
    ax.add_patch(ellipse)

data = tips[['total_bill', 'tip']].values
ax.scatter(data[:, 0], data[:, 1], alpha=0.5)
plot_cov_ellipse(data, ax, n_std=2, facecolor='none', 
                edgecolor='red', linewidth=2)
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
ax.set_title('Scatter with Covariance Ellipse')

# 条件付き分布
ax = axes[1, 0]
# total_billを区間に分割
tips['bill_category'] = pd.cut(tips['total_bill'], 
                               bins=[0, 15, 25, 50], 
                               labels=['Low', 'Medium', 'High'])
sns.violinplot(data=tips, x='bill_category', y='tip', ax=ax)
ax.set_title('Conditional Distribution of Tips')

# 主成分分析（PCA）
ax = axes[1, 1]
# アイリスデータでPCA
X = iris.iloc[:, :-1].values
y = iris['species']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

for species in y.unique():
    mask = y == species
    ax.scatter(X_pca[mask, 0], X_pca[mask, 1], 
              label=species, alpha=0.7)

ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%} variance)')
ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%} variance)')
ax.set_title('PCA of Iris Dataset')
ax.legend()

plt.suptitle("Advanced Correlation and Relationship Visualizations", fontsize=16)
plt.tight_layout()
plt.show()

# 4. カテゴリデータの高度な分析
print("\n--- 4. カテゴリデータの高度な分析 ---")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# モザイクプロット風
ax = axes[0, 0]
cross_tab = pd.crosstab(tips['day'], tips['time'])
cross_tab_norm = cross_tab.div(cross_tab.sum(1), axis=0)

im = ax.imshow(cross_tab_norm, cmap='Blues', aspect='auto')
ax.set_xticks(range(len(cross_tab.columns)))
ax.set_yticks(range(len(cross_tab.index)))
ax.set_xticklabels(cross_tab.columns)
ax.set_yticklabels(cross_tab.index)
ax.set_xlabel('Time')
ax.set_ylabel('Day')
ax.set_title('Proportion Heatmap')

# テキストアノテーション
for i in range(len(cross_tab.index)):
    for j in range(len(cross_tab.columns)):
        text = ax.text(j, i, f'{cross_tab_norm.iloc[i, j]:.2f}',
                      ha="center", va="center", color="black")

# アソシエーションプロット
ax = axes[0, 1]
# 期待値と観測値の差
expected = cross_tab.values.sum() * np.outer(
    cross_tab.sum(1) / cross_tab.sum().sum(),
    cross_tab.sum(0) / cross_tab.sum().sum()
)
residuals = (cross_tab - expected) / np.sqrt(expected)

im = ax.imshow(residuals, cmap='RdBu_r', center=0, aspect='auto')
ax.set_xticks(range(len(cross_tab.columns)))
ax.set_yticks(range(len(cross_tab.index)))
ax.set_xticklabels(cross_tab.columns)
ax.set_yticklabels(cross_tab.index)
ax.set_xlabel('Time')
ax.set_ylabel('Day')
ax.set_title('Standardized Residuals')
plt.colorbar(im, ax=ax)

# 条件付き確率
ax = axes[1, 0]
# タイタニックデータで生存率
survival_by_class = titanic.groupby(['class', 'sex'])['survived'].mean().unstack()
survival_by_class.plot(kind='bar', ax=ax)
ax.set_title('Survival Rate by Class and Sex')
ax.set_ylabel('Survival Rate')
ax.legend(title='Sex')

# 対応分析風のプロット
ax = axes[1, 1]
# 簡易版：カテゴリの重心をプロット
day_centers = tips.groupby('day')[['total_bill', 'tip']].mean()
time_centers = tips.groupby('time')[['total_bill', 'tip']].mean()

ax.scatter(day_centers['total_bill'], day_centers['tip'], 
          s=200, marker='s', label='Day', alpha=0.7)
for day, row in day_centers.iterrows():
    ax.annotate(day, (row['total_bill'], row['tip']), 
               xytext=(5, 5), textcoords='offset points')

ax.scatter(time_centers['total_bill'], time_centers['tip'], 
          s=200, marker='^', label='Time', alpha=0.7)
for time, row in time_centers.iterrows():
    ax.annotate(time, (row['total_bill'], row['tip']), 
               xytext=(5, 5), textcoords='offset points')

ax.set_xlabel('Average Total Bill')
ax.set_ylabel('Average Tip')
ax.set_title('Category Centers in Feature Space')
ax.legend()

plt.suptitle("Advanced Categorical Data Analysis", fontsize=16)
plt.tight_layout()
plt.show()

# 5. リッジプロットとジョイプロット
print("\n--- 5. リッジプロットとジョイプロット ---")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

# リッジプロット
days = ['Thur', 'Fri', 'Sat', 'Sun']
colors = sns.color_palette("husl", len(days))

for i, (day, color) in enumerate(zip(days, colors)):
    data = tips[tips['day'] == day]['total_bill']
    
    # KDEを計算
    density = stats.gaussian_kde(data)
    x = np.linspace(data.min(), data.max(), 200)
    y = density(x)
    
    # オフセットを追加
    y_offset = i * 0.5
    ax1.fill_between(x, y_offset, y_offset + y * 3, 
                    alpha=0.6, color=color, label=day)
    ax1.plot(x, y_offset + y * 3, color=color, linewidth=2)

ax1.set_xlabel('Total Bill')
ax1.set_ylabel('Day (offset)')
ax1.set_title('Ridge Plot')
ax1.legend()
ax1.set_yticks([])

# ジョイプロット風（複数のKDE）
for i, (day, color) in enumerate(zip(days, colors)):
    data = tips[tips['day'] == day]['total_bill']
    sns.kdeplot(data=data, ax=ax2, fill=True, alpha=0.3, 
               label=day, color=color)

ax2.set_xlabel('Total Bill')
ax2.set_ylabel('Density')
ax2.set_title('Overlapping KDE Plot')
ax2.legend()

plt.suptitle("Ridge and Joy Plots", fontsize=16)
plt.tight_layout()
plt.show()

print("\n高度な統計プロットの例を完了しました！")