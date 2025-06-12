# NumPy完全チュートリアル

## 目次
1. [NumPyとは](#1-numpyとは)
2. [NumPyのインストールと基本設定](#2-numpyのインストールと基本設定)
3. [NumPy配列（ndarray）の基礎](#3-numpy配列ndarrayの基礎)
4. [配列の作成と初期化](#4-配列の作成と初期化)
5. [配列の操作とインデックス](#5-配列の操作とインデックス)
6. [配列の演算](#6-配列の演算)
7. [配列の形状変換](#7-配列の形状変換)
8. [統計関数と集約](#8-統計関数と集約)
9. [ブロードキャスティング](#9-ブロードキャスティング)
10. [線形代数](#10-線形代数)
11. [ファイル入出力](#11-ファイル入出力)
12. [実践的な応用例](#12-実践的な応用例)

## 1. NumPyとは

NumPyは「Numerical Python」の略で、Pythonで科学計算を行うための基礎的なライブラリです。高速な多次元配列操作と、それらの配列を操作するための高度な関数を提供します。

### NumPyの特徴

- **高速な配列処理**: C言語で実装されており、Pythonのリストよりも高速
- **多次元配列**: 1次元から多次元まで柔軟に扱える
- **数学関数**: 三角関数、統計関数など豊富な数学関数
- **ブロードキャスティング**: 異なる形状の配列同士の演算を効率的に実行
- **メモリ効率**: 連続したメモリ領域に配列を格納

### なぜNumPyを使うのか？

```python
# Pythonリストでの計算（遅い）
python_list = list(range(1000000))
result = [x * 2 for x in python_list]

# NumPyでの計算（高速）
import numpy as np
numpy_array = np.arange(1000000)
result = numpy_array * 2
```

## 2. NumPyのインストールと基本設定

### インストール

```bash
pip install numpy
```

### インポートと基本設定

```python
import numpy as np

# バージョン確認
print(np.__version__)

# 表示設定
np.set_printoptions(precision=3)  # 小数点以下3桁表示
np.set_printoptions(suppress=True)  # 科学的記数法を抑制
```

## 3. NumPy配列（ndarray）の基礎

### ndarrayオブジェクト

NumPyの中核となるのは`ndarray`（N-dimensional array）オブジェクトです。

```python
import numpy as np

# 1次元配列
arr1d = np.array([1, 2, 3, 4, 5])
print(f"1次元配列: {arr1d}")
print(f"形状: {arr1d.shape}")
print(f"次元数: {arr1d.ndim}")
print(f"データ型: {arr1d.dtype}")

# 2次元配列
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2次元配列:\n{arr2d}")
print(f"形状: {arr2d.shape}")
print(f"次元数: {arr2d.ndim}")

# 3次元配列
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"\n3次元配列:\n{arr3d}")
print(f"形状: {arr3d.shape}")
print(f"次元数: {arr3d.ndim}")
```

### データ型（dtype）

```python
# 整数型
int_array = np.array([1, 2, 3], dtype=np.int32)
print(f"int32: {int_array.dtype}")

# 浮動小数点型
float_array = np.array([1.0, 2.0, 3.0], dtype=np.float64)
print(f"float64: {float_array.dtype}")

# 複素数型
complex_array = np.array([1+2j, 3+4j], dtype=np.complex128)
print(f"complex128: {complex_array.dtype}")

# ブール型
bool_array = np.array([True, False, True], dtype=np.bool_)
print(f"bool: {bool_array.dtype}")
```

## 4. 配列の作成と初期化

### 基本的な配列作成

```python
# ゼロで初期化
zeros = np.zeros((3, 4))
print(f"ゼロ配列:\n{zeros}")

# 1で初期化
ones = np.ones((2, 3))
print(f"\n1の配列:\n{ones}")

# 特定の値で初期化
full = np.full((2, 2), 7)
print(f"\n7で満たされた配列:\n{full}")

# 単位行列
eye = np.eye(3)
print(f"\n単位行列:\n{eye}")

# 対角行列
diag = np.diag([1, 2, 3, 4])
print(f"\n対角行列:\n{diag}")
```

### 連続した値の配列

```python
# arange（範囲指定）
arr1 = np.arange(10)
print(f"0から9: {arr1}")

arr2 = np.arange(2, 10, 2)
print(f"2から9まで2刻み: {arr2}")

# linspace（要素数指定）
arr3 = np.linspace(0, 1, 5)
print(f"0から1まで5要素: {arr3}")

# logspace（対数スケール）
arr4 = np.logspace(0, 2, 4)
print(f"10^0から10^2まで4要素: {arr4}")
```

### ランダム配列

```python
# 乱数のシード設定（再現性のため）
np.random.seed(42)

# 一様分布（0から1）
uniform = np.random.rand(3, 3)
print(f"一様分布:\n{uniform}")

# 正規分布
normal = np.random.randn(3, 3)
print(f"\n正規分布:\n{normal}")

# 整数の乱数
integers = np.random.randint(0, 10, size=(3, 3))
print(f"\n整数乱数:\n{integers}")

# 配列のシャッフル
arr = np.arange(10)
np.random.shuffle(arr)
print(f"\nシャッフル後: {arr}")
```

## 5. 配列の操作とインデックス

### 基本的なインデックス

```python
# 1次元配列
arr1d = np.array([10, 20, 30, 40, 50])
print(f"3番目の要素: {arr1d[2]}")
print(f"最後の要素: {arr1d[-1]}")

# 2次元配列
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2行3列目: {arr2d[1, 2]}")
print(f"2行目全体: {arr2d[1]}")
print(f"3列目全体: {arr2d[:, 2]}")
```

### スライシング

```python
# 1次元スライシング
arr = np.arange(10)
print(f"インデックス2から5: {arr[2:6]}")
print(f"偶数インデックス: {arr[::2]}")
print(f"逆順: {arr[::-1]}")

# 2次元スライシング
arr2d = np.arange(20).reshape(4, 5)
print(f"\n元の配列:\n{arr2d}")
print(f"\n左上2x2:\n{arr2d[:2, :2]}")
print(f"\n右下2x2:\n{arr2d[-2:, -2:]}")
```

### ブールインデックス

```python
arr = np.array([1, -2, 3, -4, 5])

# 条件に基づく選択
mask = arr > 0
print(f"正の要素のマスク: {mask}")
print(f"正の要素: {arr[mask]}")

# 複数条件
arr2d = np.random.randint(-10, 10, size=(5, 5))
print(f"\n元の配列:\n{arr2d}")

# -5から5の間の要素
mask = (arr2d > -5) & (arr2d < 5)
print(f"\n-5<x<5の要素: {arr2d[mask]}")
```

### ファンシーインデックス

```python
arr = np.arange(10) * 10
print(f"元の配列: {arr}")

# インデックスの配列で選択
indices = [1, 3, 5, 7]
print(f"選択された要素: {arr[indices]}")

# 2次元配列での例
arr2d = np.arange(20).reshape(4, 5)
print(f"\n元の2次元配列:\n{arr2d}")

# 行と列を指定
rows = [0, 1, 2]
cols = [1, 2, 3]
print(f"選択された要素: {arr2d[rows, cols]}")
```

## 6. 配列の演算

### 基本的な算術演算

```python
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a ** 2 = {a ** 2}")
print(f"√a = {np.sqrt(a)}")
```

### ユニバーサル関数（ufunc）

```python
angles = np.array([0, np.pi/4, np.pi/2, np.pi])

# 三角関数
print(f"sin: {np.sin(angles)}")
print(f"cos: {np.cos(angles)}")

# 指数・対数
arr = np.array([1, 2, 3])
print(f"\ne^x: {np.exp(arr)}")
print(f"ln(x): {np.log(arr)}")
print(f"log10(x): {np.log10(arr)}")

# 丸め
arr_float = np.array([1.2, 2.7, 3.5, 4.8])
print(f"\n元の配列: {arr_float}")
print(f"floor: {np.floor(arr_float)}")
print(f"ceil: {np.ceil(arr_float)}")
print(f"round: {np.round(arr_float)}")
```

### 配列同士の演算

```python
# 行列の積
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"要素ごとの積:\n{A * B}")
print(f"\n行列積:\n{np.dot(A, B)}")
print(f"\n行列積（@演算子）:\n{A @ B}")

# 内積と外積
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(f"\n内積: {np.dot(a, b)}")
print(f"外積:\n{np.outer(a, b)}")
```

## 7. 配列の形状変換

### reshape

```python
# 1次元から2次元へ
arr = np.arange(12)
print(f"元の配列: {arr}")

reshaped = arr.reshape(3, 4)
print(f"\n3x4に変形:\n{reshaped}")

# -1を使った自動計算
auto_reshape = arr.reshape(2, -1)
print(f"\n2x?に変形:\n{auto_reshape}")
```

### 次元の追加・削除

```python
# 1次元配列
arr = np.array([1, 2, 3, 4])
print(f"元の形状: {arr.shape}")

# newaxisで次元追加
col_vec = arr[:, np.newaxis]
print(f"\n列ベクトル形状: {col_vec.shape}")
print(f"列ベクトル:\n{col_vec}")

row_vec = arr[np.newaxis, :]
print(f"\n行ベクトル形状: {row_vec.shape}")

# squeezeで次元削除
arr3d = np.array([[[1, 2, 3]]])
print(f"\n3次元配列形状: {arr3d.shape}")
squeezed = np.squeeze(arr3d)
print(f"squeeze後: {squeezed.shape}")
```

### 転置と軸の入れ替え

```python
# 転置
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"元の配列:\n{arr}")
print(f"\n転置:\n{arr.T}")

# 3次元配列の軸入れ替え
arr3d = np.arange(24).reshape(2, 3, 4)
print(f"\n3次元配列形状: {arr3d.shape}")

transposed = np.transpose(arr3d, (1, 0, 2))
print(f"軸入れ替え後: {transposed.shape}")
```

### 配列の結合と分割

```python
# 結合
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# 垂直結合
v_stack = np.vstack((a, b))
print(f"垂直結合:\n{v_stack}")

# 水平結合
h_stack = np.hstack((a, b))
print(f"\n水平結合:\n{h_stack}")

# concatenate
concat_axis0 = np.concatenate((a, b), axis=0)
concat_axis1 = np.concatenate((a, b), axis=1)

# 分割
arr = np.arange(16).reshape(4, 4)
print(f"\n元の配列:\n{arr}")

# 垂直分割
v_split = np.vsplit(arr, 2)
print(f"\n垂直分割:")
for i, part in enumerate(v_split):
    print(f"Part {i+1}:\n{part}")

# 水平分割
h_split = np.hsplit(arr, 2)
print(f"\n水平分割:")
for i, part in enumerate(h_split):
    print(f"Part {i+1}:\n{part}")
```

## 8. 統計関数と集約

### 基本的な統計量

```python
# データの準備
data = np.random.normal(100, 15, 1000)

print(f"平均: {np.mean(data):.2f}")
print(f"中央値: {np.median(data):.2f}")
print(f"標準偏差: {np.std(data):.2f}")
print(f"分散: {np.var(data):.2f}")
print(f"最小値: {np.min(data):.2f}")
print(f"最大値: {np.max(data):.2f}")

# パーセンタイル
print(f"\n25パーセンタイル: {np.percentile(data, 25):.2f}")
print(f"75パーセンタイル: {np.percentile(data, 75):.2f}")
```

### 軸に沿った集約

```python
# 2次元配列での集約
arr = np.random.randint(0, 10, size=(4, 5))
print(f"元の配列:\n{arr}")

print(f"\n行ごとの合計: {np.sum(arr, axis=1)}")
print(f"列ごとの合計: {np.sum(arr, axis=0)}")
print(f"行ごとの平均: {np.mean(arr, axis=1)}")
print(f"列ごとの平均: {np.mean(arr, axis=0)}")

# 累積和と累積積
arr1d = np.array([1, 2, 3, 4, 5])
print(f"\n累積和: {np.cumsum(arr1d)}")
print(f"累積積: {np.cumprod(arr1d)}")
```

### 条件付き集約

```python
arr = np.random.randint(-10, 10, size=20)
print(f"配列: {arr}")

# 条件を満たす要素の数
positive_count = np.sum(arr > 0)
print(f"\n正の要素数: {positive_count}")

# 条件を満たす要素の位置
positive_indices = np.where(arr > 0)
print(f"正の要素の位置: {positive_indices[0]}")

# 条件を満たす要素の抽出
positive_values = arr[arr > 0]
print(f"正の要素: {positive_values}")
```

## 9. ブロードキャスティング

### ブロードキャスティングの基本

ブロードキャスティングは、異なる形状の配列間で演算を行うためのNumPyの強力な機能です。

```python
# スカラーとの演算
arr = np.array([1, 2, 3, 4])
print(f"配列 * 2: {arr * 2}")

# 異なる形状の配列
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
print(f"\n2D配列:\n{a}")
print(f"1D配列: {b}")
print(f"ブロードキャスト結果:\n{a + b}")
```

### ブロードキャスティングのルール

```python
# ルール1: 次元数を合わせる
a = np.ones((3, 4))
b = np.ones(4)
print(f"形状 {a.shape} + {b.shape} = {(a + b).shape}")

# ルール2: 各次元のサイズが1または同じ
a = np.ones((3, 1))
b = np.ones((1, 4))
print(f"\n形状 {a.shape} + {b.shape} = {(a + b).shape}")
print(f"結果:\n{a + b}")

# 実用例：正規化
data = np.random.randint(0, 100, size=(5, 3))
print(f"\n元のデータ:\n{data}")

# 列ごとの平均と標準偏差
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

# 正規化
normalized = (data - mean) / std
print(f"\n正規化後:\n{normalized}")
print(f"確認（平均）: {np.mean(normalized, axis=0)}")
print(f"確認（標準偏差）: {np.std(normalized, axis=0)}")
```

## 10. 線形代数

### 基本的な行列演算

```python
# 行列の作成
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"行列A:\n{A}")
print(f"行列B:\n{B}")

# 行列積
print(f"\n行列積 A @ B:\n{A @ B}")

# 転置
print(f"\nAの転置:\n{A.T}")

# トレース（対角和）
print(f"\nAのトレース: {np.trace(A)}")

# 行列式
print(f"Aの行列式: {np.linalg.det(A):.2f}")
```

### 逆行列と連立方程式

```python
# 逆行列
A = np.array([[2, 1], [1, 3]])
A_inv = np.linalg.inv(A)
print(f"A:\n{A}")
print(f"\nAの逆行列:\n{A_inv}")
print(f"\n確認 A @ A_inv:\n{A @ A_inv}")

# 連立方程式を解く
# 2x + y = 5
# x + 3y = 7
A = np.array([[2, 1], [1, 3]])
b = np.array([5, 7])
x = np.linalg.solve(A, b)
print(f"\n連立方程式の解: x={x[0]:.2f}, y={x[1]:.2f}")

# 検証
print(f"検証: A @ x = {A @ x}")
```

### 固有値と固有ベクトル

```python
# 対称行列
A = np.array([[4, -2], [-2, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)

print(f"行列A:\n{A}")
print(f"\n固有値: {eigenvalues}")
print(f"\n固有ベクトル:\n{eigenvectors}")

# 検証
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    λ = eigenvalues[i]
    print(f"\n固有値{λ:.2f}の検証:")
    print(f"A @ v = {A @ v}")
    print(f"λ * v = {λ * v}")
```

### 特異値分解（SVD）

```python
# 行列の作成
A = np.array([[1, 2, 3], [4, 5, 6]])
U, s, VT = np.linalg.svd(A)

print(f"元の行列A:\n{A}")
print(f"\nU:\n{U}")
print(f"\n特異値: {s}")
print(f"\nV^T:\n{VT}")

# 再構成
S = np.zeros(A.shape)
S[:len(s), :len(s)] = np.diag(s)
reconstructed = U @ S @ VT
print(f"\n再構成:\n{reconstructed}")
```

## 11. ファイル入出力

### NumPy形式での保存・読み込み

```python
# 配列の作成
arr = np.random.rand(5, 5)
print(f"元の配列:\n{arr}")

# バイナリ形式で保存（.npy）
np.save('array.npy', arr)

# 読み込み
loaded_arr = np.load('array.npy')
print(f"\n読み込んだ配列:\n{loaded_arr}")

# 複数の配列を保存（.npz）
arr1 = np.array([1, 2, 3])
arr2 = np.array([[4, 5], [6, 7]])
np.savez('arrays.npz', x=arr1, y=arr2)

# 読み込み
data = np.load('arrays.npz')
print(f"\nx: {data['x']}")
print(f"y:\n{data['y']}")

# 圧縮保存
np.savez_compressed('arrays_compressed.npz', arr1=arr1, arr2=arr2)
```

### テキスト形式での保存・読み込み

```python
# CSVとして保存
arr = np.random.rand(4, 3)
np.savetxt('data.csv', arr, delimiter=',', fmt='%.3f')

# CSVから読み込み
loaded = np.loadtxt('data.csv', delimiter=',')
print(f"CSVから読み込み:\n{loaded}")

# ヘッダー付きCSV
header = "x,y,z"
np.savetxt('data_with_header.csv', arr, delimiter=',', 
           header=header, fmt='%.3f', comments='')

# より複雑なデータの読み込み
# genfromtxtは欠損値や異なるデータ型に対応
data = np.genfromtxt('data_with_header.csv', delimiter=',', 
                     names=True, dtype=None, encoding='utf-8')
```

## 12. 実践的な応用例

### 例1: 画像処理

```python
# 画像をグレースケールとして扱う
# 仮想的な画像データ（実際はPILやOpenCVで読み込む）
image = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)

# 画像の統計情報
print(f"画像サイズ: {image.shape}")
print(f"最小輝度: {image.min()}")
print(f"最大輝度: {image.max()}")
print(f"平均輝度: {image.mean():.2f}")

# 画像の変換
# 反転
inverted = 255 - image

# 二値化
threshold = 128
binary = (image > threshold).astype(np.uint8) * 255

# フィルタリング（簡単な平滑化）
kernel = np.ones((3, 3)) / 9
# 実際の畳み込みはscipy.ndimageやOpenCVを使用
```

### 例2: 時系列データ分析

```python
# 時系列データの生成
np.random.seed(42)
days = 365
trend = np.linspace(100, 200, days)
seasonal = 10 * np.sin(2 * np.pi * np.arange(days) / 365)
noise = np.random.normal(0, 5, days)
sales = trend + seasonal + noise

# 移動平均
window = 7
moving_avg = np.convolve(sales, np.ones(window)/window, mode='valid')

# 統計量
print(f"年間売上統計:")
print(f"平均: {sales.mean():.2f}")
print(f"標準偏差: {sales.std():.2f}")
print(f"最大値: {sales.max():.2f}")
print(f"最小値: {sales.min():.2f}")

# 月ごとの集計（30日を1ヶ月と仮定）
monthly_sales = sales[:360].reshape(12, 30).sum(axis=1)
print(f"\n月別売上: {monthly_sales}")
```

### 例3: 機械学習の前処理

```python
# データセットの準備
np.random.seed(42)
n_samples = 1000
n_features = 5

# 特徴量の生成
X = np.random.randn(n_samples, n_features)
# ターゲット（線形関係 + ノイズ）
true_weights = np.array([1.5, -2.0, 0.5, 1.0, -0.5])
y = X @ true_weights + np.random.randn(n_samples) * 0.1

# データの標準化
X_mean = X.mean(axis=0)
X_std = X.std(axis=0)
X_normalized = (X - X_mean) / X_std

print(f"元のデータ統計:")
print(f"平均: {X.mean(axis=0)}")
print(f"標準偏差: {X.std(axis=0)}")

print(f"\n標準化後:")
print(f"平均: {X_normalized.mean(axis=0)}")
print(f"標準偏差: {X_normalized.std(axis=0)}")

# 訓練・テストデータの分割
train_size = int(0.8 * n_samples)
indices = np.random.permutation(n_samples)
train_idx = indices[:train_size]
test_idx = indices[train_size:]

X_train, X_test = X[train_idx], X[test_idx]
y_train, y_test = y[train_idx], y[test_idx]

print(f"\n訓練データサイズ: {X_train.shape}")
print(f"テストデータサイズ: {X_test.shape}")
```

### 例4: 数値シミュレーション

```python
# モンテカルロ法による円周率の推定
n_points = 1000000
points = np.random.uniform(-1, 1, size=(n_points, 2))

# 原点からの距離
distances = np.sqrt(np.sum(points**2, axis=1))

# 単位円内の点の数
inside_circle = np.sum(distances <= 1)

# 円周率の推定
pi_estimate = 4 * inside_circle / n_points
print(f"推定された円周率: {pi_estimate}")
print(f"実際の円周率: {np.pi}")
print(f"誤差: {abs(pi_estimate - np.pi):.6f}")

# ランダムウォーク
steps = 1000
walk = np.random.choice([-1, 1], size=steps)
position = np.cumsum(walk)

print(f"\nランダムウォーク:")
print(f"最終位置: {position[-1]}")
print(f"最大到達点: {position.max()}")
print(f"最小到達点: {position.min()}")
```

## まとめ

NumPyは科学計算の基礎となるライブラリで、以下の重要な機能を提供します：

1. **高速な配列演算**: C言語実装による高速処理
2. **ブロードキャスティング**: 異なる形状の配列間での効率的な演算
3. **豊富な数学関数**: 統計、線形代数、フーリエ変換など
4. **メモリ効率**: 連続したメモリ配置による効率的なデータ管理
5. **他のライブラリとの連携**: pandas、scikit-learn、TensorFlowなど

### 学習のポイント

- まずは基本的な配列操作（作成、インデックス、スライス）を習得
- ブロードキャスティングの理解は必須
- 実際のデータで練習を重ねる
- 他のライブラリ（pandas、matplotlib）と組み合わせて使用

### 次のステップ

- **pandas**: データ分析のためのライブラリ
- **matplotlib/seaborn**: データ可視化
- **scikit-learn**: 機械学習
- **scipy**: 科学計算の拡張機能

NumPyをマスターすることで、Pythonでのデータサイエンスや科学計算の基礎が身につきます。実際のプロジェクトで使いながら、徐々に高度な機能も習得していきましょう。