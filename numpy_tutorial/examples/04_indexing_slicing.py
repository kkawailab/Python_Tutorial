#!/usr/bin/env python3
"""
NumPyチュートリアル - 例4: インデックスとスライシング
"""

import numpy as np

print("=== 基本的なインデックス ===\n")

# 1次元配列
arr1d = np.array([10, 20, 30, 40, 50])
print(f"1次元配列: {arr1d}")
print(f"arr1d[0]: {arr1d[0]}")
print(f"arr1d[2]: {arr1d[2]}")
print(f"arr1d[-1]: {arr1d[-1]}")
print(f"arr1d[-2]: {arr1d[-2]}")

# 2次元配列
print("\n--- 2次元配列のインデックス ---")
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"2次元配列:\n{arr2d}")
print(f"arr2d[0, 0]: {arr2d[0, 0]}")
print(f"arr2d[1, 2]: {arr2d[1, 2]}")
print(f"arr2d[2, 1]: {arr2d[2, 1]}")
print(f"arr2d[1]: {arr2d[1]}  # 2行目全体")
print(f"arr2d[:, 1]: {arr2d[:, 1]}  # 2列目全体")

# 3次元配列
print("\n--- 3次元配列のインデックス ---")
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"3次元配列:\n{arr3d}")
print(f"形状: {arr3d.shape}")
print(f"arr3d[0, 1, 0]: {arr3d[0, 1, 0]}")
print(f"arr3d[1, :, 1]:\n{arr3d[1, :, 1]}")

print("\n=== スライシング ===\n")

# 1次元スライシング
print("--- 1次元スライシング ---")
arr = np.arange(10)
print(f"元の配列: {arr}")
print(f"arr[2:6]: {arr[2:6]}")
print(f"arr[:5]: {arr[:5]}")
print(f"arr[5:]: {arr[5:]}")
print(f"arr[::2]: {arr[::2]}  # 偶数インデックス")
print(f"arr[1::2]: {arr[1::2]}  # 奇数インデックス")
print(f"arr[::-1]: {arr[::-1]}  # 逆順")
print(f"arr[::-2]: {arr[::-2]}  # 逆順で2つおき")

# 2次元スライシング
print("\n--- 2次元スライシング ---")
arr2d = np.arange(20).reshape(4, 5)
print(f"元の配列:\n{arr2d}")
print(f"\n左上2x2:\n{arr2d[:2, :2]}")
print(f"\n右下2x2:\n{arr2d[-2:, -2:]}")
print(f"\n中央部分:\n{arr2d[1:3, 1:4]}")
print(f"\n偶数行:\n{arr2d[::2, :]}")
print(f"\n奇数列:\n{arr2d[:, 1::2]}")

print("\n=== ブールインデックス ===\n")

# 基本的なブールインデックス
arr = np.array([1, -2, 3, -4, 5, -6])
print(f"元の配列: {arr}")

mask = arr > 0
print(f"正の要素のマスク: {mask}")
print(f"正の要素: {arr[mask]}")
print(f"負の要素: {arr[~mask]}")

# 条件を直接使用
print(f"\n絶対値が3より大きい要素: {arr[np.abs(arr) > 3]}")

# 複数条件
print("\n--- 複数条件 ---")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"元の配列: {arr}")
mask = (arr > 3) & (arr < 7)
print(f"3 < x < 7: {arr[mask]}")

mask = (arr < 3) | (arr > 7)
print(f"x < 3 or x > 7: {arr[mask]}")

# 2次元配列でのブールインデックス
print("\n--- 2次元配列でのブールインデックス ---")
arr2d = np.random.randint(-10, 10, size=(5, 5))
print(f"元の配列:\n{arr2d}")

# 0より大きい要素を0に置き換え
arr2d_copy = arr2d.copy()
arr2d_copy[arr2d_copy > 0] = 0
print(f"\n正の要素を0に置換:\n{arr2d_copy}")

print("\n=== ファンシーインデックス ===\n")

# 1次元配列
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(f"元の配列: {arr}")

indices = [1, 3, 5, 7]
print(f"インデックス {indices}: {arr[indices]}")

indices = [0, 2, -1]
print(f"インデックス {indices}: {arr[indices]}")

# 2次元配列
print("\n--- 2次元配列でのファンシーインデックス ---")
arr2d = np.arange(20).reshape(4, 5)
print(f"元の配列:\n{arr2d}")

# 特定の行を選択
rows = [0, 2, 3]
print(f"\n行 {rows}:\n{arr2d[rows]}")

# 特定の要素を選択
rows = [0, 1, 2, 3]
cols = [1, 2, 3, 4]
print(f"\n対角要素の右側: {arr2d[rows, cols]}")

# meshgridを使った選択
row_indices = np.array([0, 2])
col_indices = np.array([1, 3])
selected = arr2d[np.ix_(row_indices, col_indices)]
print(f"\n行[0, 2]と列[1, 3]の交差:\n{selected}")

print("\n=== 値の代入 ===\n")

# スライスへの代入
arr = np.arange(10)
print(f"元の配列: {arr}")

arr[2:5] = 99
print(f"arr[2:5] = 99: {arr}")

arr[::2] = -1
print(f"arr[::2] = -1: {arr}")

# ブールインデックスでの代入
arr = np.array([1, -2, 3, -4, 5, -6])
print(f"\n元の配列: {arr}")

arr[arr < 0] = 0
print(f"負の値を0に: {arr}")

# 2次元配列での代入
arr2d = np.zeros((5, 5), dtype=int)
print(f"\n5x5のゼロ配列:\n{arr2d}")

# 対角線に値を代入
np.fill_diagonal(arr2d, 1)
print(f"\n対角線を1に:\n{arr2d}")

# 特定の領域に値を代入
arr2d[1:4, 1:4] = 2
print(f"\n中央部分を2に:\n{arr2d}")

# 条件付き代入
arr2d[arr2d == 0] = -1
print(f"\n0を-1に:\n{arr2d}")