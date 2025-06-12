#!/usr/bin/env python3
"""
NumPyチュートリアル - 例5: 配列の演算
"""

import numpy as np

print("=== 基本的な算術演算 ===\n")

a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

print(f"配列a: {a}")
print(f"配列b: {b}")
print(f"\na + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}  # 整数除算")
print(f"a % b = {a % b}   # 剰余")
print(f"a ** 2 = {a ** 2}")
print(f"b ** 0.5 = {b ** 0.5}")

# スカラーとの演算
print("\n--- スカラーとの演算 ---")
print(f"a * 2 = {a * 2}")
print(f"a + 10 = {a + 10}")
print(f"a / 2 = {a / 2}")
print(f"2 ** a = {2 ** a}")

print("\n=== ユニバーサル関数（ufunc） ===\n")

# 三角関数
print("--- 三角関数 ---")
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
print(f"角度（ラジアン）: {angles}")
print(f"角度（度）: {np.degrees(angles)}")
print(f"\nsin: {np.sin(angles)}")
print(f"cos: {np.cos(angles)}")
print(f"tan: {np.tan(angles)}")

# 逆三角関数
values = np.array([0, 0.5, 0.707, 0.866, 1])
print(f"\n値: {values}")
print(f"arcsin: {np.arcsin(values)}")
print(f"arcsin（度）: {np.degrees(np.arcsin(values))}")

# 指数・対数
print("\n--- 指数・対数 ---")
arr = np.array([1, 2, 3, 4, 5])
print(f"配列: {arr}")
print(f"e^x: {np.exp(arr)}")
print(f"2^x: {np.power(2, arr)}")
print(f"ln(x): {np.log(arr)}")
print(f"log2(x): {np.log2(arr)}")
print(f"log10(x): {np.log10(arr)}")

# 平方根・累乗
print("\n--- 平方根・累乗 ---")
arr = np.array([1, 4, 9, 16, 25])
print(f"配列: {arr}")
print(f"√x: {np.sqrt(arr)}")
print(f"∛x: {np.cbrt(arr)}")
print(f"x^2: {np.square(arr)}")
print(f"x^3: {np.power(arr, 3)}")

# 丸め
print("\n--- 丸め関数 ---")
arr_float = np.array([1.2, 2.7, -3.5, 4.8, -5.3])
print(f"元の配列: {arr_float}")
print(f"floor: {np.floor(arr_float)}")
print(f"ceil: {np.ceil(arr_float)}")
print(f"round: {np.round(arr_float)}")
print(f"round(1桁): {np.round(arr_float, 1)}")
print(f"trunc: {np.trunc(arr_float)}")

# 符号関数
print("\n--- 符号関数 ---")
arr = np.array([-5, -2, 0, 3, 7])
print(f"配列: {arr}")
print(f"abs: {np.abs(arr)}")
print(f"sign: {np.sign(arr)}")

print("\n=== 配列同士の演算 ===\n")

# ベクトルの内積
print("--- ベクトルの内積 ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"ベクトルa: {a}")
print(f"ベクトルb: {b}")
print(f"内積 (dot): {np.dot(a, b)}")
print(f"内積 (@): {a @ b}")

# 行列の積
print("\n--- 行列の積 ---")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"行列A:\n{A}")
print(f"行列B:\n{B}")
print(f"\n要素ごとの積 (*):\n{A * B}")
print(f"\n行列積 (dot):\n{np.dot(A, B)}")
print(f"\n行列積 (@):\n{A @ B}")

# 外積
print("\n--- 外積 ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"ベクトルa: {a}")
print(f"ベクトルb: {b}")
print(f"外積:\n{np.outer(a, b)}")

# クロス積（3次元ベクトル）
print("\n--- クロス積 ---")
a = np.array([1, 0, 0])
b = np.array([0, 1, 0])
print(f"ベクトルa: {a}")
print(f"ベクトルb: {b}")
print(f"クロス積: {np.cross(a, b)}")

print("\n=== 比較演算 ===\n")

a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 3, 3, 3, 3])

print(f"配列a: {a}")
print(f"配列b: {b}")
print(f"\na == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a < b: {a < b}")
print(f"a <= b: {a <= b}")
print(f"a > b: {a > b}")
print(f"a >= b: {a >= b}")

# 配列全体の比較
print(f"\n全要素が等しい: {np.array_equal(a, b)}")
print(f"全要素が等しい: {np.array_equal(a, a)}")

# 近似的な等価性
a = np.array([1.0, 2.0, 3.0])
b = np.array([1.0000001, 2.0000001, 3.0000001])
print(f"\n厳密に等しい: {np.array_equal(a, b)}")
print(f"ほぼ等しい: {np.allclose(a, b)}")

print("\n=== 論理演算 ===\n")

a = np.array([True, True, False, False])
b = np.array([True, False, True, False])

print(f"配列a: {a}")
print(f"配列b: {b}")
print(f"\na & b: {a & b}")
print(f"a | b: {a | b}")
print(f"a ^ b: {a ^ b}  # XOR")
print(f"~a: {~a}")

# 論理関数
print("\n--- 論理関数 ---")
print(f"logical_and: {np.logical_and(a, b)}")
print(f"logical_or: {np.logical_or(a, b)}")
print(f"logical_xor: {np.logical_xor(a, b)}")
print(f"logical_not: {np.logical_not(a)}")

# any と all
arr = np.array([1, 2, 0, 4, 5])
print(f"\n配列: {arr}")
print(f"いずれかが0より大きい: {np.any(arr > 0)}")
print(f"すべてが0より大きい: {np.all(arr > 0)}")
print(f"いずれかが0: {np.any(arr == 0)}")
print(f"すべてが10未満: {np.all(arr < 10)}")