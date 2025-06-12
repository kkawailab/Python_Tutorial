#!/usr/bin/env python3
"""
NumPyチュートリアル - 例2: 配列の作成と初期化
"""

import numpy as np

print("=== 配列の作成方法 ===\n")

# ゼロで初期化
print("--- ゼロ配列 ---")
zeros = np.zeros((3, 4))
print(f"zeros((3, 4)):\n{zeros}")

zeros_int = np.zeros((2, 3), dtype=int)
print(f"\nzeros((2, 3), dtype=int):\n{zeros_int}")

# 1で初期化
print("\n--- 1の配列 ---")
ones = np.ones((2, 3))
print(f"ones((2, 3)):\n{ones}")

# 特定の値で初期化
print("\n--- 特定の値で初期化 ---")
full = np.full((2, 2), 7)
print(f"full((2, 2), 7):\n{full}")

full_float = np.full((3, 3), 3.14)
print(f"\nfull((3, 3), 3.14):\n{full_float}")

# 単位行列
print("\n--- 単位行列 ---")
eye = np.eye(3)
print(f"eye(3):\n{eye}")

identity = np.identity(4)
print(f"\nidentity(4):\n{identity}")

# 対角行列
print("\n--- 対角行列 ---")
diag = np.diag([1, 2, 3, 4])
print(f"diag([1, 2, 3, 4]):\n{diag}")

# 既存の配列から対角要素を抽出
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
diag_elements = np.diag(matrix)
print(f"\n行列:\n{matrix}")
print(f"対角要素: {diag_elements}")

print("\n=== 連続した値の配列 ===\n")

# arange
print("--- arange ---")
arr1 = np.arange(10)
print(f"arange(10): {arr1}")

arr2 = np.arange(2, 10, 2)
print(f"arange(2, 10, 2): {arr2}")

arr3 = np.arange(1.0, 2.0, 0.1)
print(f"arange(1.0, 2.0, 0.1): {arr3}")

# linspace
print("\n--- linspace ---")
lin1 = np.linspace(0, 1, 5)
print(f"linspace(0, 1, 5): {lin1}")

lin2 = np.linspace(0, 10, 11)
print(f"linspace(0, 10, 11): {lin2}")

# endpoint引数
lin3 = np.linspace(0, 1, 5, endpoint=False)
print(f"linspace(0, 1, 5, endpoint=False): {lin3}")

# logspace
print("\n--- logspace ---")
log1 = np.logspace(0, 2, 4)
print(f"logspace(0, 2, 4): {log1}")
print(f"（10^0から10^2まで4要素）")

log2 = np.logspace(0, 3, 4, base=2)
print(f"\nlogspace(0, 3, 4, base=2): {log2}")
print(f"（2^0から2^3まで4要素）")

# meshgrid（格子点の生成）
print("\n--- meshgrid ---")
x = np.arange(0, 3)
y = np.arange(0, 4)
X, Y = np.meshgrid(x, y)
print(f"x: {x}")
print(f"y: {y}")
print(f"\nX:\n{X}")
print(f"\nY:\n{Y}")

# empty（未初期化配列）
print("\n--- empty（未初期化） ---")
empty = np.empty((2, 2))
print(f"empty((2, 2)):\n{empty}")
print("※ 値は不定（メモリの既存の値）")

# like関数（同じ形状の配列を作成）
print("\n--- like関数 ---")
original = np.array([[1, 2, 3], [4, 5, 6]])
zeros_like = np.zeros_like(original)
ones_like = np.ones_like(original)
full_like = np.full_like(original, 9)

print(f"元の配列:\n{original}")
print(f"\nzeros_like:\n{zeros_like}")
print(f"\nones_like:\n{ones_like}")
print(f"\nfull_like(original, 9):\n{full_like}")