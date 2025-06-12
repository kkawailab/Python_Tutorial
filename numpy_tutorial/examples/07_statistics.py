#!/usr/bin/env python3
"""
NumPyチュートリアル - 例7: 統計関数と集約
"""

import numpy as np

# データの準備
np.random.seed(42)

print("=== 基本的な統計量 ===\n")

# 1次元データ
data = np.random.normal(100, 15, 100)
print(f"データの最初の10要素: {data[:10]}")
print(f"\n統計量:")
print(f"平均: {np.mean(data):.2f}")
print(f"中央値: {np.median(data):.2f}")
print(f"標準偏差: {np.std(data):.2f}")
print(f"分散: {np.var(data):.2f}")
print(f"最小値: {np.min(data):.2f}")
print(f"最大値: {np.max(data):.2f}")
print(f"範囲: {np.ptp(data):.2f}")  # peak to peak

# パーセンタイルと分位数
print(f"\nパーセンタイル:")
print(f"25パーセンタイル: {np.percentile(data, 25):.2f}")
print(f"50パーセンタイル: {np.percentile(data, 50):.2f}")
print(f"75パーセンタイル: {np.percentile(data, 75):.2f}")

# 四分位範囲
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1
print(f"四分位範囲 (IQR): {iqr:.2f}")

print("\n=== 軸に沿った集約 ===\n")

# 2次元配列での集約
arr = np.random.randint(0, 10, size=(4, 5))
print(f"元の配列:\n{arr}")

print(f"\n全体の統計:")
print(f"合計: {np.sum(arr)}")
print(f"平均: {np.mean(arr):.2f}")

print(f"\n行ごとの統計 (axis=1):")
print(f"合計: {np.sum(arr, axis=1)}")
print(f"平均: {np.mean(arr, axis=1)}")
print(f"最大値: {np.max(arr, axis=1)}")
print(f"最小値: {np.min(arr, axis=1)}")

print(f"\n列ごとの統計 (axis=0):")
print(f"合計: {np.sum(arr, axis=0)}")
print(f"平均: {np.mean(arr, axis=0)}")
print(f"標準偏差: {np.std(arr, axis=0)}")

# keepdimsオプション
print("\n--- keepdims ---")
mean_keepdims = np.mean(arr, axis=1, keepdims=True)
print(f"平均 (keepdims=True):\n{mean_keepdims}")
print(f"形状: {mean_keepdims.shape}")

# 正規化の例
normalized = (arr - mean_keepdims) / np.std(arr, axis=1, keepdims=True)
print(f"\n行ごとに正規化:\n{normalized}")

print("\n=== 累積関数 ===\n")

arr1d = np.array([1, 2, 3, 4, 5])
print(f"配列: {arr1d}")
print(f"累積和: {np.cumsum(arr1d)}")
print(f"累積積: {np.cumprod(arr1d)}")

# 2次元での累積
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2次元配列:\n{arr2d}")
print(f"\n行方向の累積和 (axis=1):\n{np.cumsum(arr2d, axis=1)}")
print(f"\n列方向の累積和 (axis=0):\n{np.cumsum(arr2d, axis=0)}")

print("\n=== 条件付き集約 ===\n")

arr = np.random.randint(-10, 10, size=20)
print(f"配列: {arr}")

# whereを使った条件付き選択
positive_indices = np.where(arr > 0)[0]
negative_indices = np.where(arr < 0)[0]
zero_indices = np.where(arr == 0)[0]

print(f"\n正の要素の位置: {positive_indices}")
print(f"負の要素の位置: {negative_indices}")
print(f"ゼロの位置: {zero_indices}")

print(f"\n正の要素: {arr[positive_indices]}")
print(f"正の要素の合計: {np.sum(arr[arr > 0])}")
print(f"正の要素の平均: {np.mean(arr[arr > 0]):.2f}")

# argmax, argmin
print("\n--- 最大値・最小値の位置 ---")
print(f"最大値: {np.max(arr)}")
print(f"最大値の位置: {np.argmax(arr)}")
print(f"最小値: {np.min(arr)}")
print(f"最小値の位置: {np.argmin(arr)}")

# 2次元での例
arr2d = np.random.randint(0, 100, size=(4, 5))
print(f"\n2次元配列:\n{arr2d}")
print(f"最大値: {np.max(arr2d)}")
print(f"最大値の位置（フラット）: {np.argmax(arr2d)}")
print(f"最大値の位置（2D）: {np.unravel_index(np.argmax(arr2d), arr2d.shape)}")

print("\n=== ソートと順位 ===\n")

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(f"元の配列: {arr}")

# ソート
sorted_arr = np.sort(arr)
print(f"ソート後: {sorted_arr}")

# argsort（ソートのインデックス）
sort_indices = np.argsort(arr)
print(f"ソートのインデックス: {sort_indices}")
print(f"確認: {arr[sort_indices]}")

# 降順ソート
descending = np.sort(arr)[::-1]
print(f"降順: {descending}")

# 2次元配列のソート
arr2d = np.random.randint(0, 10, size=(3, 4))
print(f"\n2次元配列:\n{arr2d}")

sorted_axis0 = np.sort(arr2d, axis=0)
print(f"\n列ごとにソート:\n{sorted_axis0}")

sorted_axis1 = np.sort(arr2d, axis=1)
print(f"\n行ごとにソート:\n{sorted_axis1}")

# partition（部分的なソート）
print("\n--- partition ---")
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(f"元の配列: {arr}")

# 3番目に小さい要素まで正しく配置
partitioned = np.partition(arr, 3)
print(f"partition(3): {partitioned}")
print(f"最小3要素: {partitioned[:3]}")

print("\n=== ユニークな要素 ===\n")

arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(f"配列: {arr}")

# ユニークな要素
unique = np.unique(arr)
print(f"ユニークな要素: {unique}")

# カウント付き
unique_counts = np.unique(arr, return_counts=True)
print(f"要素: {unique_counts[0]}")
print(f"出現回数: {unique_counts[1]}")

# インデックス付き
arr2 = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5])
unique_with_index = np.unique(arr2, return_index=True, return_inverse=True)
print(f"\n元の配列: {arr2}")
print(f"ユニークな要素: {unique_with_index[0]}")
print(f"最初の出現位置: {unique_with_index[1]}")
print(f"逆インデックス: {unique_with_index[2]}")

print("\n=== ヒストグラムと頻度 ===\n")

# 正規分布データ
data = np.random.normal(100, 15, 1000)

# ヒストグラム
hist, bins = np.histogram(data, bins=10)
print(f"ヒストグラムの頻度: {hist}")
print(f"ビンの境界: {bins}")

# bincount（整数の頻度）
integers = np.random.randint(0, 10, size=100)
counts = np.bincount(integers)
print(f"\n0-9の出現回数: {counts}")

# digitize（どのビンに属するか）
data_points = np.array([85, 95, 105, 115, 125])
bins = np.array([80, 90, 100, 110, 120, 130])
bin_indices = np.digitize(data_points, bins)
print(f"\nデータ: {data_points}")
print(f"ビン: {bins}")
print(f"所属ビン: {bin_indices}")

print("\n=== 相関と共分散 ===\n")

# 2つの変数
x = np.random.normal(0, 1, 100)
y = 2 * x + np.random.normal(0, 0.5, 100)

# 相関係数
correlation = np.corrcoef(x, y)
print(f"相関行列:\n{correlation}")
print(f"相関係数: {correlation[0, 1]:.3f}")

# 共分散
covariance = np.cov(x, y)
print(f"\n共分散行列:\n{covariance}")

# 多変数の場合
data = np.random.randn(3, 100)  # 3変数、100サンプル
corr_matrix = np.corrcoef(data)
print(f"\n3変数の相関行列:\n{corr_matrix}")