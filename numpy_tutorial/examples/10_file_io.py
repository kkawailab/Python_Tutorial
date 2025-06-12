#!/usr/bin/env python3
"""
NumPyチュートリアル - 例10: ファイル入出力
"""

import numpy as np
import os

print("=== NumPy形式での保存・読み込み ===\n")

# 作業ディレクトリの作成
os.makedirs('numpy_data', exist_ok=True)

# 配列の作成
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.random.rand(3, 4)
arr3d = np.random.randint(0, 10, size=(2, 3, 4))

print(f"1次元配列: {arr1d}")
print(f"2次元配列:\n{arr2d}")
print(f"3次元配列の形状: {arr3d.shape}")

# .npy形式で保存（単一配列）
print("\n--- .npy形式での保存 ---")
np.save('numpy_data/array1d.npy', arr1d)
np.save('numpy_data/array2d.npy', arr2d)
print("array1d.npy と array2d.npy を保存しました")

# 読み込み
loaded1d = np.load('numpy_data/array1d.npy')
loaded2d = np.load('numpy_data/array2d.npy')
print(f"\n読み込んだ1次元配列: {loaded1d}")
print(f"読み込んだ2次元配列:\n{loaded2d}")
print(f"元の配列と同じか: {np.array_equal(arr1d, loaded1d)}")

# .npz形式で複数配列を保存
print("\n--- .npz形式での保存（複数配列） ---")
np.savez('numpy_data/arrays.npz', 
         one_d=arr1d, 
         two_d=arr2d, 
         three_d=arr3d,
         labels=['A', 'B', 'C'])
print("arrays.npz を保存しました")

# 読み込み
data = np.load('numpy_data/arrays.npz')
print(f"\n保存されているキー: {list(data.keys())}")
print(f"one_d: {data['one_d']}")
print(f"labels: {data['labels']}")
data.close()  # npzファイルは明示的にcloseする

# 圧縮保存
print("\n--- 圧縮保存 (.npz) ---")
large_array = np.random.rand(1000, 1000)
np.savez_compressed('numpy_data/large_array_compressed.npz', data=large_array)

# ファイルサイズの比較
uncompressed_size = os.path.getsize('numpy_data/array2d.npy')
compressed_size = os.path.getsize('numpy_data/large_array_compressed.npz')
print(f"非圧縮サイズ（小さい配列）: {uncompressed_size} bytes")
print(f"圧縮サイズ（大きい配列）: {compressed_size} bytes")

print("\n=== テキスト形式での保存・読み込み ===\n")

# CSVとして保存
arr = np.random.rand(5, 3)
print(f"保存する配列:\n{arr}")

# 基本的な保存
np.savetxt('numpy_data/data.csv', arr, delimiter=',')
print("\ndata.csv を保存しました")

# フォーマット指定
np.savetxt('numpy_data/data_formatted.csv', arr, 
           delimiter=',', fmt='%.3f', 
           header='col1,col2,col3', comments='')
print("data_formatted.csv を保存しました（3桁精度、ヘッダー付き）")

# 読み込み
loaded_csv = np.loadtxt('numpy_data/data.csv', delimiter=',')
print(f"\nCSVから読み込み:\n{loaded_csv}")
print(f"元の配列と近いか: {np.allclose(arr, loaded_csv)}")

# ヘッダー付きCSVの読み込み
loaded_with_header = np.loadtxt('numpy_data/data_formatted.csv', 
                               delimiter=',', skiprows=1)
print(f"\nヘッダー付きCSVから読み込み:\n{loaded_with_header}")

print("\n--- 整数データの保存 ---")
int_array = np.random.randint(0, 100, size=(4, 5))
print(f"整数配列:\n{int_array}")

np.savetxt('numpy_data/integers.txt', int_array, fmt='%d', delimiter='\t')
loaded_int = np.loadtxt('numpy_data/integers.txt', dtype=int, delimiter='\t')
print(f"\n読み込んだ整数配列:\n{loaded_int}")

print("\n--- 複雑なデータの保存 ---")
# 構造化配列
dtype = np.dtype([('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
structured = np.array([('Alice', 25, 55.5), 
                      ('Bob', 30, 70.2), 
                      ('Charlie', 35, 68.9)], dtype=dtype)
print(f"構造化配列:\n{structured}")

# 構造化配列の保存
np.save('numpy_data/structured.npy', structured)
loaded_structured = np.load('numpy_data/structured.npy')
print(f"\n読み込んだ構造化配列:\n{loaded_structured}")

print("\n=== genfromtxtの使用 ===\n")

# 欠損値を含むデータの作成
csv_content = """# サンプルデータ
# x, y, z
1.0, 2.0, 3.0
4.0, , 6.0
7.0, 8.0, 9.0
, 11.0, 12.0
"""

with open('numpy_data/missing_data.csv', 'w') as f:
    f.write(csv_content)

# genfromtxtで読み込み
data_with_missing = np.genfromtxt('numpy_data/missing_data.csv', 
                                  delimiter=',', skip_header=2,
                                  filling_values=np.nan)
print(f"欠損値を含むデータ:\n{data_with_missing}")

# 列名付きで読み込み
data_with_names = np.genfromtxt('numpy_data/missing_data.csv', 
                                delimiter=',', skip_header=1,
                                names=['x', 'y', 'z'],
                                filling_values={'x': -1, 'y': -2, 'z': -3})
print(f"\n列名付きデータ:\n{data_with_names}")
print(f"列 'x': {data_with_names['x']}")

print("\n=== メモリマップファイル ===\n")

# 大きな配列をメモリマップとして作成
shape = (1000, 1000)
memmap_array = np.memmap('numpy_data/large_memmap.dat', 
                        dtype='float32', mode='w+', shape=shape)

# 一部だけ書き込み
memmap_array[:10, :10] = np.random.rand(10, 10)
print(f"メモリマップ配列の形状: {memmap_array.shape}")
print(f"最初の5x5:\n{memmap_array[:5, :5]}")

# フラッシュして保存
del memmap_array  # ファイルを閉じる

# 読み込みモードで開く
memmap_readonly = np.memmap('numpy_data/large_memmap.dat', 
                           dtype='float32', mode='r', shape=shape)
print(f"\n読み込んだメモリマップの5x5:\n{memmap_readonly[:5, :5]}")

print("\n=== バイナリファイルの直接操作 ===\n")

# tofileでバイナリ保存
arr = np.array([1.5, 2.5, 3.5, 4.5], dtype=np.float32)
arr.tofile('numpy_data/binary_data.bin')
print(f"バイナリファイルに保存: {arr}")

# fromfileで読み込み
loaded_binary = np.fromfile('numpy_data/binary_data.bin', dtype=np.float32)
print(f"バイナリファイルから読み込み: {loaded_binary}")

# 複数のデータ型
mixed_types = np.array([(1, 2.5), (3, 4.5)], 
                      dtype=[('int_val', 'i4'), ('float_val', 'f4')])
mixed_types.tofile('numpy_data/mixed_types.bin')

loaded_mixed = np.fromfile('numpy_data/mixed_types.bin', 
                          dtype=[('int_val', 'i4'), ('float_val', 'f4')])
print(f"\n複合型データ: {loaded_mixed}")

print("\n=== 実用例: データセットの保存と読み込み ===\n")

# 機械学習用のデータセットを想定
np.random.seed(42)
n_samples = 100
n_features = 5

# 特徴量とラベルの生成
X = np.random.randn(n_samples, n_features)
y = np.random.randint(0, 3, n_samples)  # 3クラス分類

# データセットの情報
metadata = {
    'n_samples': n_samples,
    'n_features': n_features,
    'n_classes': 3,
    'feature_names': [f'feature_{i}' for i in range(n_features)],
    'class_names': ['class_0', 'class_1', 'class_2']
}

# すべてを一つのファイルに保存
np.savez_compressed('numpy_data/dataset.npz',
                   X=X, y=y, 
                   metadata=metadata,
                   feature_names=metadata['feature_names'],
                   class_names=metadata['class_names'])

print("データセットを保存しました")
print(f"特徴量の形状: {X.shape}")
print(f"ラベルの形状: {y.shape}")
print(f"メタデータ: {metadata}")

# データセットの読み込み
dataset = np.load('numpy_data/dataset.npz', allow_pickle=True)
X_loaded = dataset['X']
y_loaded = dataset['y']
metadata_loaded = dataset['metadata'].item()

print(f"\n読み込んだデータ:")
print(f"特徴量の形状: {X_loaded.shape}")
print(f"ラベルの形状: {y_loaded.shape}")
print(f"メタデータ: {metadata_loaded}")

dataset.close()

# クリーンアップ（オプション）
print("\n生成されたファイル:")
for filename in os.listdir('numpy_data'):
    filepath = os.path.join('numpy_data', filename)
    size = os.path.getsize(filepath)
    print(f"{filename}: {size} bytes")