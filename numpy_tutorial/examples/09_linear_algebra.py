#!/usr/bin/env python3
"""
NumPyチュートリアル - 例9: 線形代数
"""

import numpy as np

print("=== 基本的な行列演算 ===\n")

# 行列の作成
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"行列A:\n{A}")
print(f"行列B:\n{B}")

# 要素ごとの演算
print(f"\n要素ごとの積 (A * B):\n{A * B}")
print(f"要素ごとの除算 (A / B):\n{A / B}")

# 行列積
print(f"\n行列積 (A @ B):\n{A @ B}")
print(f"行列積 (np.dot):\n{np.dot(A, B)}")
print(f"行列積 (np.matmul):\n{np.matmul(A, B)}")

# 転置
print(f"\nAの転置:\n{A.T}")
print(f"Bの転置:\n{B.T}")

# トレース（対角和）
print(f"\nAのトレース: {np.trace(A)}")
print(f"Bのトレース: {np.trace(B)}")

# 行列式
print(f"\nAの行列式: {np.linalg.det(A):.2f}")
print(f"Bの行列式: {np.linalg.det(B):.2f}")

print("\n=== 逆行列 ===\n")

# 逆行列の計算
A = np.array([[2, 1], [1, 3]])
print(f"行列A:\n{A}")

A_inv = np.linalg.inv(A)
print(f"\nAの逆行列:\n{A_inv}")

# 検証
identity = A @ A_inv
print(f"\nA @ A_inv:\n{identity}")
print(f"単位行列に近いか: {np.allclose(identity, np.eye(2))}")

# 特異行列（逆行列が存在しない）
singular = np.array([[1, 2], [2, 4]])
print(f"\n特異行列:\n{singular}")
print(f"行列式: {np.linalg.det(singular):.2f}")

try:
    inv = np.linalg.inv(singular)
except np.linalg.LinAlgError as e:
    print(f"エラー: {e}")

# 擬似逆行列
pinv = np.linalg.pinv(singular)
print(f"\n擬似逆行列:\n{pinv}")

print("\n=== 連立方程式を解く ===\n")

# Ax = b を解く
# 2x + y = 5
# x + 3y = 7
A = np.array([[2, 1], [1, 3]])
b = np.array([5, 7])

print(f"係数行列A:\n{A}")
print(f"定数ベクトルb: {b}")

# 解を求める
x = np.linalg.solve(A, b)
print(f"\n解: x = {x[0]:.2f}, y = {x[1]:.2f}")

# 検証
print(f"検証 A @ x: {A @ x}")
print(f"正しいか: {np.allclose(A @ x, b)}")

# 過剰決定系（方程式が多い）
A_over = np.array([[1, 2], [3, 4], [5, 6]])
b_over = np.array([5, 11, 17])
print(f"\n過剰決定系:")
print(f"A:\n{A_over}")
print(f"b: {b_over}")

# 最小二乗解
x_lstsq, residuals, rank, s = np.linalg.lstsq(A_over, b_over, rcond=None)
print(f"\n最小二乗解: {x_lstsq}")
print(f"残差: {residuals}")

print("\n=== 固有値と固有ベクトル ===\n")

# 対称行列
A = np.array([[4, -2], [-2, 3]])
print(f"行列A:\n{A}")

# 固有値と固有ベクトル
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"\n固有値: {eigenvalues}")
print(f"固有ベクトル:\n{eigenvectors}")

# 検証
for i in range(len(eigenvalues)):
    λ = eigenvalues[i]
    v = eigenvectors[:, i]
    Av = A @ v
    λv = λ * v
    print(f"\n固有値 λ = {λ:.2f}")
    print(f"A @ v = {Av}")
    print(f"λ * v = {λv}")
    print(f"等しいか: {np.allclose(Av, λv)}")

# 実対称行列の固有値分解
symmetric = np.array([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
print(f"\n実対称行列:\n{symmetric}")

eigenvalues_sym, eigenvectors_sym = np.linalg.eigh(symmetric)
print(f"\n固有値: {eigenvalues_sym}")
print(f"固有ベクトル:\n{eigenvectors_sym}")

# 対角化
D = np.diag(eigenvalues_sym)
P = eigenvectors_sym
reconstructed = P @ D @ P.T
print(f"\n再構成:\n{reconstructed}")
print(f"元の行列と等しいか: {np.allclose(reconstructed, symmetric)}")

print("\n=== 特異値分解（SVD） ===\n")

# 非正方行列
A = np.array([[1, 2, 3], [4, 5, 6]])
print(f"行列A:\n{A}")

# SVD
U, s, VT = np.linalg.svd(A)
print(f"\nU:\n{U}")
print(f"特異値: {s}")
print(f"V^T:\n{VT}")

# 再構成
S = np.zeros(A.shape)
S[:len(s), :len(s)] = np.diag(s)
reconstructed = U @ S @ VT
print(f"\n再構成:\n{reconstructed}")
print(f"元の行列と等しいか: {np.allclose(reconstructed, A)}")

# 低ランク近似
print("\n--- 低ランク近似 ---")
k = 1  # ランク1近似
S_k = np.zeros(A.shape)
S_k[0, 0] = s[0]
A_k = U @ S_k @ VT
print(f"ランク{k}近似:\n{A_k}")

print("\n=== ノルム ===\n")

# ベクトルのノルム
v = np.array([3, 4])
print(f"ベクトル: {v}")
print(f"L2ノルム: {np.linalg.norm(v)}")
print(f"L1ノルム: {np.linalg.norm(v, ord=1)}")
print(f"L∞ノルム: {np.linalg.norm(v, ord=np.inf)}")

# 行列のノルム
A = np.array([[1, 2], [3, 4]])
print(f"\n行列A:\n{A}")
print(f"フロベニウスノルム: {np.linalg.norm(A, 'fro'):.2f}")
print(f"2ノルム: {np.linalg.norm(A, 2):.2f}")
print(f"1ノルム: {np.linalg.norm(A, 1):.2f}")
print(f"∞ノルム: {np.linalg.norm(A, np.inf):.2f}")

print("\n=== QR分解 ===\n")

A = np.array([[1, 2], [3, 4], [5, 6]])
print(f"行列A:\n{A}")

# QR分解
Q, R = np.linalg.qr(A)
print(f"\nQ（直交行列）:\n{Q}")
print(f"\nR（上三角行列）:\n{R}")

# 検証
print(f"\nQ @ R:\n{Q @ R}")
print(f"元の行列と等しいか: {np.allclose(Q @ R, A)}")

# Qが直交行列か確認
print(f"\nQ^T @ Q:\n{Q.T @ Q}")
print(f"単位行列に近いか: {np.allclose(Q.T @ Q, np.eye(2))}")

print("\n=== 行列の条件数とランク ===\n")

# 条件数
A = np.array([[1, 2], [3, 4]])
cond = np.linalg.cond(A)
print(f"行列A:\n{A}")
print(f"条件数: {cond:.2f}")

# 悪条件行列
ill_conditioned = np.array([[1, 1], [1, 1.0001]])
cond_ill = np.linalg.cond(ill_conditioned)
print(f"\n悪条件行列:\n{ill_conditioned}")
print(f"条件数: {cond_ill:.2f}")

# ランク
A = np.array([[1, 2, 3], [2, 4, 6], [1, 1, 1]])
rank = np.linalg.matrix_rank(A)
print(f"\n行列A:\n{A}")
print(f"ランク: {rank}")

print("\n=== 実用例: 最小二乗法による直線フィッティング ===\n")

# データ点
np.random.seed(42)
x = np.linspace(0, 10, 20)
y_true = 2 * x + 1
y_noise = y_true + np.random.normal(0, 2, len(x))

print(f"x: {x[:5]}...")
print(f"y（ノイズ付き）: {y_noise[:5]}...")

# 行列形式で設定: y = ax + b
A = np.column_stack([x, np.ones(len(x))])
print(f"\n計画行列A（最初の5行）:\n{A[:5]}")

# 最小二乗法で係数を求める
coeffs, residuals, rank, s = np.linalg.lstsq(A, y_noise, rcond=None)
a_fit, b_fit = coeffs

print(f"\nフィッティング結果:")
print(f"傾き a = {a_fit:.2f} (真値: 2)")
print(f"切片 b = {b_fit:.2f} (真値: 1)")
print(f"残差の二乗和: {residuals[0]:.2f}")

# 予測値
y_fit = a_fit * x + b_fit
error = np.mean((y_fit - y_noise)**2)
print(f"平均二乗誤差: {error:.2f}")