#!/usr/bin/env python3
"""
NumPyチュートリアル - 例3: ランダム配列の生成
"""

import numpy as np

# 乱数のシード設定（再現性のため）
np.random.seed(42)

print("=== ランダム配列の生成 ===\n")

# 一様分布（0から1）
print("--- 一様分布 [0, 1) ---")
uniform = np.random.rand(3, 3)
print(f"rand(3, 3):\n{uniform}")

uniform_1d = np.random.rand(5)
print(f"\nrand(5): {uniform_1d}")

# 一様分布（範囲指定）
print("\n--- 一様分布（範囲指定） ---")
uniform_range = np.random.uniform(low=-1, high=1, size=(3, 3))
print(f"uniform(-1, 1, size=(3, 3)):\n{uniform_range}")

uniform_int = np.random.uniform(low=10, high=20, size=5)
print(f"\nuniform(10, 20, size=5): {uniform_int}")

# 正規分布
print("\n--- 正規分布 ---")
normal = np.random.randn(3, 3)
print(f"randn(3, 3):\n{normal}")

# 平均と標準偏差を指定
normal_custom = np.random.normal(loc=100, scale=15, size=10)
print(f"\nnormal(mean=100, std=15, size=10):\n{normal_custom}")

# 整数の乱数
print("\n--- 整数の乱数 ---")
integers = np.random.randint(0, 10, size=(3, 3))
print(f"randint(0, 10, size=(3, 3)):\n{integers}")

integers_1d = np.random.randint(1, 7, size=10)  # サイコロの目
print(f"\nrandint(1, 7, size=10) [サイコロ]: {integers_1d}")

# 二項分布
print("\n--- 二項分布 ---")
binomial = np.random.binomial(n=10, p=0.5, size=20)
print(f"binomial(n=10, p=0.5, size=20):\n{binomial}")
print(f"（10回のコイン投げで表が出る回数）")

# ポアソン分布
print("\n--- ポアソン分布 ---")
poisson = np.random.poisson(lam=3, size=20)
print(f"poisson(λ=3, size=20):\n{poisson}")
print(f"（平均3回のイベント発生）")

# 指数分布
print("\n--- 指数分布 ---")
exponential = np.random.exponential(scale=2, size=10)
print(f"exponential(scale=2, size=10):\n{exponential}")

# choice（選択）
print("\n--- choice（選択） ---")
arr = np.array(['A', 'B', 'C', 'D', 'E'])
choice = np.random.choice(arr, size=10, replace=True)
print(f"元の配列: {arr}")
print(f"choice(arr, size=10, replace=True): {choice}")

# 重み付き選択
weights = [0.1, 0.1, 0.3, 0.3, 0.2]
weighted_choice = np.random.choice(arr, size=20, p=weights)
print(f"\n重み: {weights}")
print(f"重み付き選択: {weighted_choice}")

# 配列のシャッフル
print("\n--- シャッフル ---")
arr = np.arange(10)
print(f"元の配列: {arr}")

# shuffle（元の配列を変更）
arr_copy1 = arr.copy()
np.random.shuffle(arr_copy1)
print(f"shuffle後: {arr_copy1}")

# permutation（新しい配列を返す）
shuffled = np.random.permutation(arr)
print(f"permutation: {shuffled}")
print(f"元の配列（不変）: {arr}")

# 2次元配列の行をシャッフル
matrix = np.arange(12).reshape(4, 3)
print(f"\n元の2次元配列:\n{matrix}")

indices = np.random.permutation(matrix.shape[0])
shuffled_matrix = matrix[indices]
print(f"\n行をシャッフル:\n{shuffled_matrix}")

# 乱数生成器の状態管理
print("\n--- 乱数生成器の状態 ---")
# 状態を保存
state = np.random.get_state()

# 乱数を生成
random1 = np.random.rand(5)
print(f"最初の乱数: {random1}")

# 状態を復元
np.random.set_state(state)

# 同じ乱数が生成される
random2 = np.random.rand(5)
print(f"状態復元後: {random2}")
print(f"同じ値か: {np.array_equal(random1, random2)}")

# 新しい乱数生成器（推奨される方法）
print("\n--- Generator（新しい方法） ---")
rng = np.random.default_rng(seed=42)
new_random = rng.random((2, 3))
print(f"Generator.random((2, 3)):\n{new_random}")

new_integers = rng.integers(0, 10, size=(3, 3))
print(f"\nGenerator.integers(0, 10, size=(3, 3)):\n{new_integers}")