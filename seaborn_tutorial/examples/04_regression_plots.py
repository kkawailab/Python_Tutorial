#!/usr/bin/env python3
"""
Seabornチュートリアル - 例4: 回帰プロット
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score

# スタイル設定
sns.set_theme(style="whitegrid")

# データの準備
tips = sns.load_dataset("tips")
anscombe = sns.load_dataset("anscombe")

print("=== 回帰プロット ===\n")

# 1. 基本的な回帰プロット
print("--- 1. 基本的な回帰プロット ---")
plt.figure(figsize=(10, 6))
sns.regplot(data=tips, x="total_bill", y="tip")
plt.title("Linear Regression: Total Bill vs Tip")
plt.show()

# 信頼区間のカスタマイズ
plt.figure(figsize=(12, 6))
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# 95%信頼区間（デフォルト）
sns.regplot(data=tips, x="total_bill", y="tip", 
            ci=95, ax=axes[0])
axes[0].set_title("95% Confidence Interval")

# 99%信頼区間
sns.regplot(data=tips, x="total_bill", y="tip", 
            ci=99, color="red", ax=axes[1])
axes[1].set_title("99% Confidence Interval")

plt.tight_layout()
plt.show()

# 散布図のカスタマイズ
plt.figure(figsize=(10, 6))
sns.regplot(data=tips, x="total_bill", y="tip",
            scatter_kws={'alpha': 0.5, 's': 80, 'color': 'blue'},
            line_kws={'color': 'red', 'linewidth': 2})
plt.title("Customized Regression Plot")
plt.show()

# 2. 多項式回帰
print("\n--- 2. 多項式回帰 ---")
# サンプルデータの作成
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = 2 * x - x**2 + 10 + np.random.normal(0, 2, 100)
poly_data = pd.DataFrame({'x': x, 'y': y})

plt.figure(figsize=(15, 5))
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

orders = [1, 2, 3]
colors = ['blue', 'green', 'red']

for ax, order, color in zip(axes, orders, colors):
    sns.regplot(data=poly_data, x='x', y='y', 
                order=order, ax=ax, color=color,
                scatter_kws={'alpha': 0.5})
    ax.set_title(f'Polynomial Regression (order={order})')

plt.tight_layout()
plt.show()

# 3. ロバスト回帰
print("\n--- 3. ロバスト回帰 ---")
# 外れ値を含むデータ
tips_outliers = tips.copy()
# いくつかの外れ値を追加
tips_outliers.loc[tips_outliers.index[:5], 'tip'] = 25

plt.figure(figsize=(12, 6))
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# 通常の回帰
sns.regplot(data=tips_outliers, x="total_bill", y="tip", 
            ax=axes[0])
axes[0].set_title("Standard Regression")

# ロバスト回帰
sns.regplot(data=tips_outliers, x="total_bill", y="tip", 
            robust=True, ax=axes[1], color="green")
axes[1].set_title("Robust Regression")

plt.tight_layout()
plt.show()

# 4. ローカル回帰（LOWESS）
print("\n--- 4. ローカル回帰（LOWESS） ---")
plt.figure(figsize=(10, 6))
sns.regplot(data=tips, x="total_bill", y="tip", 
            lowess=True, color="orange")
plt.title("LOWESS (Locally Weighted Regression)")
plt.show()

# 5. 残差プロット
print("\n--- 5. 残差プロット ---")
plt.figure(figsize=(12, 6))
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# 通常のプロット
sns.regplot(data=tips, x="total_bill", y="tip", ax=axes[0])
axes[0].set_title("Regression Plot")

# 残差プロット
sns.residplot(data=tips, x="total_bill", y="tip", 
              lowess=True, color="g", ax=axes[1])
axes[1].set_title("Residual Plot")
axes[1].axhline(0, color='red', linestyle='--')

plt.tight_layout()
plt.show()

# 6. カテゴリ別回帰（lmplot）
print("\n--- 6. カテゴリ別回帰 ---")
# hueパラメータで分割
g = sns.lmplot(data=tips, x="total_bill", y="tip", 
               hue="smoker", height=6, aspect=1.5)
g.fig.suptitle("Regression by Smoker Status", y=1.02)
plt.show()

# col/rowパラメータで分割
g = sns.lmplot(data=tips, x="total_bill", y="tip", 
               col="time", row="sex", height=4)
g.fig.suptitle("Regression by Time and Sex", y=1.02)
plt.show()

# 7. Anscombeの四重奏
print("\n--- 7. Anscombeの四重奏 ---")
# 同じ統計量だが異なるパターンを示すデータセット
g = sns.lmplot(data=anscombe, x="x", y="y", col="dataset", 
               col_wrap=2, height=4, scatter_kws={'s': 50})
g.fig.suptitle("Anscombe's Quartet - Same Statistics, Different Patterns", y=1.02)

# 各データセットの統計量を計算
for dataset in ['I', 'II', 'III', 'IV']:
    subset = anscombe[anscombe['dataset'] == dataset]
    corr = subset[['x', 'y']].corr().iloc[0, 1]
    print(f"Dataset {dataset}: correlation = {corr:.3f}")

plt.show()

# 8. 回帰の診断プロット
print("\n--- 8. 回帰の診断 ---")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. 散布図と回帰線
ax = axes[0, 0]
sns.regplot(data=tips, x="total_bill", y="tip", ax=ax)
ax.set_title("Scatter Plot with Regression Line")

# 2. 残差 vs 予測値
ax = axes[0, 1]
# 簡単な線形回帰を実行
from sklearn.linear_model import LinearRegression
X = tips[['total_bill']].values
y = tips['tip'].values
model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)
residuals = y - predictions

ax.scatter(predictions, residuals, alpha=0.5)
ax.axhline(0, color='red', linestyle='--')
ax.set_xlabel("Fitted Values")
ax.set_ylabel("Residuals")
ax.set_title("Residuals vs Fitted")

# 3. Q-Qプロット（残差の正規性）
ax = axes[1, 0]
from scipy import stats
stats.probplot(residuals, dist="norm", plot=ax)
ax.set_title("Q-Q Plot of Residuals")

# 4. スケール-位置プロット
ax = axes[1, 1]
standardized_residuals = residuals / np.std(residuals)
ax.scatter(predictions, np.sqrt(np.abs(standardized_residuals)), alpha=0.5)
ax.set_xlabel("Fitted Values")
ax.set_ylabel("√|Standardized Residuals|")
ax.set_title("Scale-Location Plot")

plt.tight_layout()
plt.show()

# 9. 複数変数の関係（ペアプロット with 回帰）
print("\n--- 9. 複数変数の回帰関係 ---")
# 数値変数のみを選択
numeric_cols = tips.select_dtypes(include=[np.number]).columns.tolist()
g = sns.pairplot(tips[numeric_cols], kind="reg", 
                 plot_kws={'scatter_kws': {'alpha': 0.5}})
g.fig.suptitle("Pairwise Regression Plots", y=1.02)
plt.show()

# 統計情報の表示
print("\n--- 回帰統計 ---")
print(f"R² score: {r2_score(y, predictions):.3f}")
print(f"Slope: {model.coef_[0]:.3f}")
print(f"Intercept: {model.intercept_:.3f}")

print("\n回帰プロットの例を完了しました！")