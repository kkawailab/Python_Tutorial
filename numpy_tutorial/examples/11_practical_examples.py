#!/usr/bin/env python3
"""
NumPyチュートリアル - 例11: 実践的な応用例
"""

import numpy as np

print("=== 例1: 画像処理シミュレーション ===\n")

# グレースケール画像のシミュレーション
np.random.seed(42)
image = np.random.randint(0, 256, size=(10, 10), dtype=np.uint8)
print(f"元の画像（10x10）:\n{image}")

# 画像の統計情報
print(f"\n画像の統計情報:")
print(f"最小輝度: {image.min()}")
print(f"最大輝度: {image.max()}")
print(f"平均輝度: {image.mean():.2f}")
print(f"標準偏差: {image.std():.2f}")

# ヒストグラムの計算
hist, bins = np.histogram(image, bins=8, range=(0, 256))
print(f"\n輝度ヒストグラム:")
for i in range(len(hist)):
    print(f"  {int(bins[i]):3d}-{int(bins[i+1]):3d}: {'*' * hist[i]}")

# 画像変換
print("\n--- 画像変換 ---")

# 1. 反転
inverted = 255 - image
print(f"反転画像（最初の5x5）:\n{inverted[:5, :5]}")

# 2. 二値化
threshold = 128
binary = (image > threshold).astype(np.uint8) * 255
print(f"\n二値化（閾値={threshold}）最初の5x5:\n{binary[:5, :5]}")

# 3. コントラスト調整
min_val, max_val = image.min(), image.max()
contrast_stretched = ((image - min_val) / (max_val - min_val) * 255).astype(np.uint8)
print(f"\nコントラスト調整後（最初の5x5）:\n{contrast_stretched[:5, :5]}")

# 4. ガンマ補正
gamma = 2.0
gamma_corrected = (255 * (image / 255) ** gamma).astype(np.uint8)
print(f"\nガンマ補正（γ={gamma}）最初の5x5:\n{gamma_corrected[:5, :5]}")

# 簡単な畳み込みフィルタ
print("\n--- 畳み込みフィルタ ---")

# エッジ検出カーネル（簡略版）
kernel_edge = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]])

# 手動での畳み込み（境界を無視）
filtered = np.zeros((8, 8))
for i in range(1, 9):
    for j in range(1, 9):
        region = image[i-1:i+2, j-1:j+2]
        filtered[i-1, j-1] = np.sum(region * kernel_edge)

filtered = np.clip(filtered, 0, 255).astype(np.uint8)
print(f"エッジ検出結果（8x8）:\n{filtered}")

print("\n=== 例2: 時系列データ分析 ===\n")

# 時系列データの生成（1年分の日次売上データ）
days = 365
time = np.arange(days)

# トレンド + 季節性 + ノイズ
trend = 100 + 0.5 * time
seasonal = 20 * np.sin(2 * np.pi * time / 365) + 10 * np.sin(4 * np.pi * time / 365)
noise = np.random.normal(0, 10, days)
sales = trend + seasonal + noise

print(f"売上データ（最初の10日）: {sales[:10]}")

# 基本統計
print(f"\n年間統計:")
print(f"平均売上: {sales.mean():.2f}")
print(f"標準偏差: {sales.std():.2f}")
print(f"最大売上: {sales.max():.2f}")
print(f"最小売上: {sales.min():.2f}")

# 移動平均
window_sizes = [7, 30]
for window in window_sizes:
    moving_avg = np.convolve(sales, np.ones(window)/window, mode='valid')
    print(f"\n{window}日移動平均（最初の5値）: {moving_avg[:5]}")

# 月ごとの集計
monthly_sales = sales[:360].reshape(12, 30).sum(axis=1)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
print(f"\n月別売上:")
for month, total in zip(months, monthly_sales):
    print(f"  {month}: {total:7.2f}")

# 前年同期比
print(f"\n四半期ごとの分析:")
quarters = sales[:360].reshape(4, 90)
for i in range(4):
    q_mean = quarters[i].mean()
    q_std = quarters[i].std()
    print(f"  Q{i+1}: 平均={q_mean:.2f}, 標準偏差={q_std:.2f}")

# 異常値検出
z_scores = np.abs((sales - sales.mean()) / sales.std())
outliers = np.where(z_scores > 3)[0]
print(f"\n異常値（3σ以上）の日: {outliers}")

print("\n=== 例3: 機械学習の前処理 ===\n")

# データセットの生成
np.random.seed(42)
n_samples = 200
n_features = 4

# 特徴量（異なるスケール）
X = np.random.randn(n_samples, n_features)
X[:, 0] *= 100  # 大きなスケール
X[:, 1] *= 0.01  # 小さなスケール
X[:, 2] += 50    # オフセット

# ラベル（2クラス分類）
true_weights = np.array([0.5, -20, 0.1, 1.0])
y = (X @ true_weights + np.random.randn(n_samples) > 0).astype(int)

print(f"特徴量の統計（変換前）:")
print(f"  平均: {X.mean(axis=0)}")
print(f"  標準偏差: {X.std(axis=0)}")
print(f"  最小値: {X.min(axis=0)}")
print(f"  最大値: {X.max(axis=0)}")

# 1. 標準化（Z-score normalization）
X_mean = X.mean(axis=0)
X_std = X.std(axis=0)
X_standardized = (X - X_mean) / X_std

print(f"\n標準化後:")
print(f"  平均: {X_standardized.mean(axis=0)}")
print(f"  標準偏差: {X_standardized.std(axis=0)}")

# 2. Min-Max正規化
X_min = X.min(axis=0)
X_max = X.max(axis=0)
X_minmax = (X - X_min) / (X_max - X_min)

print(f"\nMin-Max正規化後:")
print(f"  最小値: {X_minmax.min(axis=0)}")
print(f"  最大値: {X_minmax.max(axis=0)}")

# 3. データ分割
train_size = int(0.8 * n_samples)
indices = np.random.permutation(n_samples)
train_idx, test_idx = indices[:train_size], indices[train_size:]

X_train, X_test = X_standardized[train_idx], X_standardized[test_idx]
y_train, y_test = y[train_idx], y[test_idx]

print(f"\nデータ分割:")
print(f"  訓練データ: {X_train.shape}")
print(f"  テストデータ: {X_test.shape}")
print(f"  クラス分布（訓練）: 0={np.sum(y_train==0)}, 1={np.sum(y_train==1)}")
print(f"  クラス分布（テスト）: 0={np.sum(y_test==0)}, 1={np.sum(y_test==1)}")

# 4. 特徴量エンジニアリング
print(f"\n特徴量エンジニアリング:")

# 多項式特徴量（2次）
X_poly = np.column_stack([X_train,
                         X_train[:, 0] * X_train[:, 1],
                         X_train[:, 0] * X_train[:, 2],
                         X_train[:, 1] * X_train[:, 2],
                         X_train[:, 0]**2,
                         X_train[:, 1]**2])

print(f"  元の特徴量数: {X_train.shape[1]}")
print(f"  多項式特徴量追加後: {X_poly.shape[1]}")

# 相関行列
correlation_matrix = np.corrcoef(X_train.T)
print(f"\n特徴量間の相関:")
for i in range(n_features):
    for j in range(i+1, n_features):
        print(f"  特徴量{i} - 特徴量{j}: {correlation_matrix[i, j]:.3f}")

print("\n=== 例4: モンテカルロシミュレーション ===\n")

# 円周率の推定
print("--- 円周率の推定 ---")
n_points = 100000
points = np.random.uniform(-1, 1, size=(n_points, 2))
distances = np.sqrt(np.sum(points**2, axis=1))
inside_circle = np.sum(distances <= 1)
pi_estimate = 4 * inside_circle / n_points

print(f"サンプル数: {n_points}")
print(f"推定された円周率: {pi_estimate:.6f}")
print(f"実際の円周率: {np.pi:.6f}")
print(f"誤差: {abs(pi_estimate - np.pi):.6f}")

# 株価のランダムウォーク
print("\n--- 株価シミュレーション ---")
n_days = 252  # 1年の営業日
n_simulations = 5
initial_price = 100
daily_return_mean = 0.0005  # 0.05%
daily_return_std = 0.02     # 2%

for sim in range(n_simulations):
    returns = np.random.normal(daily_return_mean, daily_return_std, n_days)
    prices = initial_price * np.cumprod(1 + returns)
    final_price = prices[-1]
    total_return = (final_price - initial_price) / initial_price * 100
    print(f"  シミュレーション{sim+1}: 最終価格={final_price:.2f}, リターン={total_return:.1f}%")

# ポートフォリオのリスク分析
print("\n--- ポートフォリオ分析 ---")
n_assets = 3
n_scenarios = 10000

# 各資産の期待リターンとボラティリティ
expected_returns = np.array([0.08, 0.12, 0.06])
volatilities = np.array([0.15, 0.25, 0.10])

# 相関行列
correlation = np.array([[1.0, 0.3, 0.2],
                       [0.3, 1.0, -0.1],
                       [0.2, -0.1, 1.0]])

# 共分散行列
covariance = np.outer(volatilities, volatilities) * correlation

# ランダムなポートフォリオ重み
weights = np.random.dirichlet(np.ones(n_assets), n_scenarios)

# ポートフォリオのリターンとリスク
portfolio_returns = weights @ expected_returns
portfolio_risks = np.sqrt(np.sum((weights @ covariance) * weights, axis=1))

# 最適ポートフォリオ（シャープレシオ最大）
risk_free_rate = 0.02
sharpe_ratios = (portfolio_returns - risk_free_rate) / portfolio_risks
best_idx = np.argmax(sharpe_ratios)

print(f"最適ポートフォリオ:")
print(f"  重み: {weights[best_idx]}")
print(f"  期待リターン: {portfolio_returns[best_idx]:.1%}")
print(f"  リスク（標準偏差）: {portfolio_risks[best_idx]:.1%}")
print(f"  シャープレシオ: {sharpe_ratios[best_idx]:.3f}")

print("\n=== 例5: 数値計算 ===\n")

# ニュートン法による方程式の解
print("--- ニュートン法: x^3 - 2x - 5 = 0 ---")

def f(x):
    return x**3 - 2*x - 5

def df(x):
    return 3*x**2 - 2

x0 = 2.0  # 初期値
tolerance = 1e-6
max_iterations = 20

x = x0
for i in range(max_iterations):
    fx = f(x)
    if abs(fx) < tolerance:
        break
    x = x - fx / df(x)
    print(f"  反復{i+1}: x = {x:.6f}, f(x) = {fx:.6e}")

print(f"解: x = {x:.6f}")
print(f"検証: f({x:.6f}) = {f(x):.6e}")

# 数値積分（台形則）
print("\n--- 数値積分: ∫sin(x)dx from 0 to π ---")

def integrate_trapezoidal(func, a, b, n):
    x = np.linspace(a, b, n)
    y = func(x)
    dx = (b - a) / (n - 1)
    return np.trapz(y, dx=dx)

result = integrate_trapezoidal(np.sin, 0, np.pi, 1000)
exact = 2.0  # -cos(π) - (-cos(0)) = 2

print(f"数値積分結果: {result:.6f}")
print(f"厳密解: {exact}")
print(f"誤差: {abs(result - exact):.6e}")

# 固有値問題の応用（主成分分析の簡略版）
print("\n--- 主成分分析（PCA）の例 ---")

# データ生成（2次元、相関あり）
n_points = 100
mean = [0, 0]
cov = [[1, 0.8], [0.8, 1]]
data = np.random.multivariate_normal(mean, cov, n_points)

# 中心化
data_centered = data - np.mean(data, axis=0)

# 共分散行列
cov_matrix = np.cov(data_centered.T)
print(f"共分散行列:\n{cov_matrix}")

# 固有値分解
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
idx = eigenvalues.argsort()[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print(f"\n固有値: {eigenvalues}")
print(f"主成分1の寄与率: {eigenvalues[0]/eigenvalues.sum():.1%}")
print(f"主成分2の寄与率: {eigenvalues[1]/eigenvalues.sum():.1%}")

# 第1主成分への射影
pc1 = data_centered @ eigenvectors[:, 0]
print(f"\n第1主成分スコア（最初の5つ）: {pc1[:5]}")