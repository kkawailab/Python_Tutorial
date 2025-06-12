#!/usr/bin/env python3
"""
NumPyチュートリアル - 例6: 配列の形状変換
"""

import numpy as np

print("=== reshape ===\n")

# 基本的なreshape
arr = np.arange(12)
print(f"元の配列: {arr}")
print(f"形状: {arr.shape}")

reshaped1 = arr.reshape(3, 4)
print(f"\n3x4に変形:\n{reshaped1}")

reshaped2 = arr.reshape(4, 3)
print(f"\n4x3に変形:\n{reshaped2}")

reshaped3 = arr.reshape(2, 2, 3)
print(f"\n2x2x3に変形:\n{reshaped3}")

# -1を使った自動計算
print("\n--- -1を使った自動計算 ---")
auto1 = arr.reshape(2, -1)
print(f"reshape(2, -1):\n{auto1}")
print(f"形状: {auto1.shape}")

auto2 = arr.reshape(-1, 3)
print(f"\nreshape(-1, 3):\n{auto2}")
print(f"形状: {auto2.shape}")

# reshapeとビューの関係
print("\n--- reshapeとビュー ---")
original = np.arange(6)
reshaped = original.reshape(2, 3)
print(f"元の配列: {original}")
print(f"reshape後:\n{reshaped}")

reshaped[0, 0] = 99
print(f"\nreshape後の配列を変更:")
print(f"元の配列: {original}")
print(f"reshape後:\n{reshaped}")
print("※ reshapeは可能な場合ビューを返す")

print("\n=== 次元の追加・削除 ===\n")

# newaxisで次元追加
arr = np.array([1, 2, 3, 4])
print(f"元の配列: {arr}")
print(f"形状: {arr.shape}")

# 列ベクトルに変換
col_vec = arr[:, np.newaxis]
print(f"\n列ベクトル:\n{col_vec}")
print(f"形状: {col_vec.shape}")

# 行ベクトルに変換
row_vec = arr[np.newaxis, :]
print(f"\n行ベクトル: {row_vec}")
print(f"形状: {row_vec.shape}")

# 複数の次元を追加
multi_newaxis = arr[:, np.newaxis, np.newaxis]
print(f"\n複数の次元追加後の形状: {multi_newaxis.shape}")

# expandの使用
print("\n--- expand_dims ---")
expanded1 = np.expand_dims(arr, axis=0)
print(f"axis=0で拡張: {expanded1.shape}")

expanded2 = np.expand_dims(arr, axis=1)
print(f"axis=1で拡張: {expanded2.shape}")

expanded3 = np.expand_dims(arr, axis=-1)
print(f"axis=-1で拡張: {expanded3.shape}")

# squeeze
print("\n--- squeeze（次元削除） ---")
arr = np.array([[[1, 2, 3]]])
print(f"元の配列形状: {arr.shape}")
print(f"配列:\n{arr}")

squeezed = np.squeeze(arr)
print(f"\nsqueeze後: {squeezed}")
print(f"形状: {squeezed.shape}")

# 特定の軸だけsqueeze
arr2 = np.zeros((1, 3, 1, 4))
print(f"\n元の形状: {arr2.shape}")
squeezed_axis0 = np.squeeze(arr2, axis=0)
print(f"axis=0をsqueeze: {squeezed_axis0.shape}")
squeezed_axis2 = np.squeeze(arr2, axis=2)
print(f"axis=2をsqueeze: {squeezed_axis2.shape}")

print("\n=== 転置と軸の入れ替え ===\n")

# 2次元配列の転置
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"元の配列:\n{arr2d}")
print(f"形状: {arr2d.shape}")

transposed = arr2d.T
print(f"\n転置:\n{transposed}")
print(f"形状: {transposed.shape}")

# transposeメソッド
transposed2 = np.transpose(arr2d)
print(f"\ntranspose():\n{transposed2}")

# 3次元配列の軸入れ替え
print("\n--- 3次元配列の軸入れ替え ---")
arr3d = np.arange(24).reshape(2, 3, 4)
print(f"元の形状: {arr3d.shape}")
print(f"配列:\n{arr3d}")

# 軸の順序を指定
transposed3d = np.transpose(arr3d, (1, 0, 2))
print(f"\n軸を(1, 0, 2)に並べ替え: {transposed3d.shape}")

# swapaxes
swapped = np.swapaxes(arr3d, 0, 1)
print(f"\naxis 0と1を交換: {swapped.shape}")

# moveaxis
moved = np.moveaxis(arr3d, 0, -1)
print(f"axis 0を最後に移動: {moved.shape}")

print("\n=== 配列の結合 ===\n")

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(f"配列a:\n{a}")
print(f"配列b:\n{b}")

# vstack（垂直結合）
v_stack = np.vstack((a, b))
print(f"\nvstack:\n{v_stack}")

# hstack（水平結合）
h_stack = np.hstack((a, b))
print(f"\nhstack:\n{h_stack}")

# concatenate
concat_axis0 = np.concatenate((a, b), axis=0)
print(f"\nconcatenate(axis=0):\n{concat_axis0}")

concat_axis1 = np.concatenate((a, b), axis=1)
print(f"\nconcatenate(axis=1):\n{concat_axis1}")

# stack（新しい軸で結合）
stacked = np.stack((a, b))
print(f"\nstack:\n{stacked}")
print(f"形状: {stacked.shape}")

stacked_axis1 = np.stack((a, b), axis=1)
print(f"\nstack(axis=1):\n{stacked_axis1}")
print(f"形状: {stacked_axis1.shape}")

# dstack（深さ方向の結合）
d_stack = np.dstack((a, b))
print(f"\ndstack:\n{d_stack}")
print(f"形状: {d_stack.shape}")

print("\n=== 配列の分割 ===\n")

arr = np.arange(16).reshape(4, 4)
print(f"元の配列:\n{arr}")

# vsplit（垂直分割）
v_parts = np.vsplit(arr, 2)
print(f"\nvsplit(2):")
for i, part in enumerate(v_parts):
    print(f"Part {i+1}:\n{part}")

# hsplit（水平分割）
h_parts = np.hsplit(arr, 2)
print(f"\nhsplit(2):")
for i, part in enumerate(h_parts):
    print(f"Part {i+1}:\n{part}")

# split（軸を指定）
split_axis0 = np.split(arr, 2, axis=0)
print(f"\nsplit(2, axis=0):")
for i, part in enumerate(split_axis0):
    print(f"Part {i+1}:\n{part}")

# 不均等な分割
uneven_split = np.split(arr, [1, 3], axis=0)
print(f"\nsplit([1, 3], axis=0):")
for i, part in enumerate(uneven_split):
    print(f"Part {i+1}:\n{part}")

# array_split（要素数が割り切れない場合も対応）
arr2 = np.arange(10)
splits = np.array_split(arr2, 3)
print(f"\narray_split(10要素を3分割):")
for i, part in enumerate(splits):
    print(f"Part {i+1}: {part}")

# flatten と ravel
print("\n=== flatten と ravel ===\n")

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"元の配列:\n{arr}")

# flatten（コピーを返す）
flattened = arr.flatten()
print(f"\nflatten: {flattened}")

# ravel（可能な場合ビューを返す）
raveled = arr.ravel()
print(f"ravel: {raveled}")

# 違いの確認
arr[0, 0] = 99
print(f"\n元の配列を変更後:")
print(f"元の配列:\n{arr}")
print(f"flatten: {flattened}")
print(f"ravel: {raveled}")