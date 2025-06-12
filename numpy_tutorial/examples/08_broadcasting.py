#!/usr/bin/env python3
"""
NumPyチュートリアル - 例8: ブロードキャスティング
"""

import numpy as np

print("=== ブロードキャスティングの基本 ===\n")

# スカラーとの演算
print("--- スカラーとの演算 ---")
arr = np.array([1, 2, 3, 4])
print(f"配列: {arr}")
print(f"配列 * 2: {arr * 2}")
print(f"配列 + 10: {arr + 10}")

# 異なる形状の配列
print("\n--- 1次元と2次元の演算 ---")
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([10, 20, 30])
print(f"2D配列 a:\n{a}")
print(f"1D配列 b: {b}")
print(f"\na + b:\n{a + b}")
print(f"\na * b:\n{a * b}")

# 列ベクトルとの演算
print("\n--- 列ベクトルとの演算 ---")
col_vec = np.array([[100], [200], [300]])
print(f"列ベクトル:\n{col_vec}")
print(f"\na + col_vec:\n{a + col_vec}")

print("\n=== ブロードキャスティングのルール ===\n")

# ルール1: 次元数を合わせる
print("--- ルール1: 次元数の調整 ---")
a = np.ones((3, 4))
b = np.ones(4)
print(f"形状 {a.shape} + 形状 {b.shape}")
print(f"bは(1, 4)として扱われる")
result = a + b
print(f"結果の形状: {result.shape}")

# ルール2: 各次元のサイズが1または同じ
print("\n--- ルール2: サイズの互換性 ---")
a = np.ones((3, 1))
b = np.ones((1, 4))
print(f"形状 {a.shape} + 形状 {b.shape}")
result = a + b
print(f"結果の形状: {result.shape}")
print(f"結果:\n{result}")

# より複雑な例
print("\n--- 複雑な例 ---")
a = np.arange(6).reshape(2, 3, 1)
b = np.arange(4).reshape(1, 1, 4)
print(f"a の形状: {a.shape}")
print(f"b の形状: {b.shape}")
result = a + b
print(f"結果の形状: {result.shape}")

print("\n=== 実用的な例 ===\n")

# データの正規化
print("--- データの正規化 ---")
np.random.seed(42)
data = np.random.randint(0, 100, size=(5, 3))
print(f"元のデータ:\n{data}")

# 列ごとの平均と標準偏差
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
print(f"\n列ごとの平均: {mean}")
print(f"列ごとの標準偏差: {std}")

# 正規化（ブロードキャスティングを使用）
normalized = (data - mean) / std
print(f"\n正規化後:\n{normalized}")
print(f"\n確認:")
print(f"正規化後の平均: {np.mean(normalized, axis=0)}")
print(f"正規化後の標準偏差: {np.std(normalized, axis=0)}")

# 外れ値の検出
print("\n--- 外れ値の検出 ---")
threshold = 2  # 2標準偏差以上を外れ値とする
outliers = np.abs(normalized) > threshold
print(f"外れ値のマスク:\n{outliers}")
print(f"外れ値の位置: {np.where(outliers)}")

# 行列の各行を正規化
print("\n--- 行ごとの正規化 ---")
matrix = np.random.rand(4, 5)
print(f"元の行列:\n{matrix}")

# 各行のノルムで正規化
row_norms = np.linalg.norm(matrix, axis=1, keepdims=True)
normalized_rows = matrix / row_norms
print(f"\n行ごとに正規化:\n{normalized_rows}")
print(f"\n各行のノルム: {np.linalg.norm(normalized_rows, axis=1)}")

print("\n=== 距離計算 ===\n")

# ユークリッド距離の計算
points = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
print(f"点の座標:\n{points}")

# すべての点間の距離を計算
# points[:, np.newaxis, :] の形状: (4, 1, 2)
# points[np.newaxis, :, :] の形状: (1, 4, 2)
diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
print(f"\n差の形状: {diff.shape}")

distances = np.sqrt(np.sum(diff**2, axis=2))
print(f"\n距離行列:\n{distances}")

print("\n=== グリッド演算 ===\n")

# 2次元グリッドでの関数評価
x = np.linspace(-2, 2, 5)
y = np.linspace(-2, 2, 5)
print(f"x: {x}")
print(f"y: {y}")

# ブロードキャスティングを使ったグリッド作成
X = x[:, np.newaxis]
Y = y[np.newaxis, :]
print(f"\nX の形状: {X.shape}")
print(f"Y の形状: {Y.shape}")

# 関数 f(x, y) = x² + y² の評価
Z = X**2 + Y**2
print(f"\nf(x, y) = x² + y²:\n{Z}")

# より複雑な関数
Z2 = np.sin(X) * np.cos(Y)
print(f"\nf(x, y) = sin(x) * cos(y):\n{Z2}")

print("\n=== カラー画像の処理 ===\n")

# RGB画像のシミュレーション（高さ×幅×チャンネル）
image = np.random.randint(0, 256, size=(4, 5, 3), dtype=np.uint8)
print(f"画像の形状: {image.shape}")
print(f"画像データ:\n{image}")

# 各チャンネルの重み
weights = np.array([0.299, 0.587, 0.114])  # RGB to グレースケール
print(f"\nRGB重み: {weights}")

# グレースケール変換（ブロードキャスティング使用）
grayscale = np.sum(image * weights, axis=2)
print(f"\nグレースケール画像:\n{grayscale}")

# 明度調整
brightness_factor = 1.2
brightened = np.clip(image * brightness_factor, 0, 255).astype(np.uint8)
print(f"\n明度調整後（最初のピクセル）:")
print(f"元: {image[0, 0]}")
print(f"調整後: {brightened[0, 0]}")

print("\n=== エラーになる例 ===\n")

# ブロードキャストできない例
a = np.ones((3, 4))
b = np.ones((3, 5))
print(f"形状 {a.shape} と {b.shape} はブロードキャストできません")

try:
    result = a + b
except ValueError as e:
    print(f"エラー: {e}")

# 解決方法
print("\n解決方法: 形状を調整する")
b_reshaped = b[:, :4]  # 最初の4列だけ使用
result = a + b_reshaped
print(f"調整後: {a.shape} + {b_reshaped.shape} = {result.shape}")

print("\n=== パフォーマンスの利点 ===\n")

# ループを使った方法（遅い）
size = 1000
a = np.random.rand(size, size)
b = np.random.rand(size)

print("ループを使った加算（最初の5x5のみ表示）:")
result_loop = np.zeros_like(a)
for i in range(size):
    for j in range(size):
        result_loop[i, j] = a[i, j] + b[j]
print(result_loop[:5, :5])

print("\nブロードキャスティングを使った加算（最初の5x5のみ表示）:")
result_broadcast = a + b
print(result_broadcast[:5, :5])

print("\n結果が同じか確認:", np.allclose(result_loop, result_broadcast))