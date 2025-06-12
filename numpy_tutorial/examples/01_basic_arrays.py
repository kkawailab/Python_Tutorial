#!/usr/bin/env python3
"""
NumPyチュートリアル - 例1: 基本的な配列操作
"""

import numpy as np

print("=== NumPy配列の基礎 ===\n")

# 1次元配列の作成
arr1d = np.array([1, 2, 3, 4, 5])
print(f"1次元配列: {arr1d}")
print(f"形状: {arr1d.shape}")
print(f"次元数: {arr1d.ndim}")
print(f"データ型: {arr1d.dtype}")
print(f"要素数: {arr1d.size}")

# 2次元配列の作成
print("\n--- 2次元配列 ---")
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2次元配列:\n{arr2d}")
print(f"形状: {arr2d.shape}")
print(f"次元数: {arr2d.ndim}")

# 3次元配列の作成
print("\n--- 3次元配列 ---")
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"3次元配列:\n{arr3d}")
print(f"形状: {arr3d.shape}")
print(f"次元数: {arr3d.ndim}")

# データ型の指定
print("\n=== データ型の指定 ===\n")

int_array = np.array([1, 2, 3], dtype=np.int32)
print(f"整数配列 (int32): {int_array}, dtype: {int_array.dtype}")

float_array = np.array([1.0, 2.0, 3.0], dtype=np.float64)
print(f"浮動小数点配列 (float64): {float_array}, dtype: {float_array.dtype}")

complex_array = np.array([1+2j, 3+4j], dtype=np.complex128)
print(f"複素数配列: {complex_array}, dtype: {complex_array.dtype}")

bool_array = np.array([True, False, True], dtype=np.bool_)
print(f"ブール配列: {bool_array}, dtype: {bool_array.dtype}")

# 配列の属性
print("\n=== 配列の属性 ===\n")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"配列:\n{arr}")
print(f"形状 (shape): {arr.shape}")
print(f"次元数 (ndim): {arr.ndim}")
print(f"データ型 (dtype): {arr.dtype}")
print(f"要素数 (size): {arr.size}")
print(f"要素のバイトサイズ (itemsize): {arr.itemsize}")
print(f"全体のバイトサイズ (nbytes): {arr.nbytes}")

# 配列のメモリレイアウト
print("\n=== メモリレイアウト ===\n")
print(f"C順序（行優先）: {arr.flags['C_CONTIGUOUS']}")
print(f"Fortran順序（列優先）: {arr.flags['F_CONTIGUOUS']}")
print(f"書き込み可能: {arr.flags['WRITEABLE']}")