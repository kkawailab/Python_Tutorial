#!/usr/bin/env python3
"""
Matplotlibチュートリアル - 例10: パフォーマンスとベストプラクティス
"""

import matplotlib.pyplot as plt
import numpy as np
import time

print("=== パフォーマンスとベストプラクティス ===\n")

# 1. 大量データの効率的なプロット
print("--- 1. 大量データの効率的なプロット ---")

# データサイズの比較
sizes = [100, 1000, 10000, 100000]
times_normal = []
times_optimized = []

for size in sizes:
    data = np.random.randn(size)
    
    # 通常のプロット
    start_time = time.time()
    fig, ax = plt.subplots()
    ax.plot(data)
    plt.close(fig)
    times_normal.append(time.time() - start_time)
    
    # 最適化されたプロット（ダウンサンプリング）
    start_time = time.time()
    fig, ax = plt.subplots()
    step = max(1, size // 1000)
    ax.plot(data[::step])
    plt.close(fig)
    times_optimized.append(time.time() - start_time)

print("データサイズ | 通常 (秒) | 最適化 (秒)")
print("-" * 40)
for i, size in enumerate(sizes):
    print(f"{size:>10} | {times_normal[i]:>9.4f} | {times_optimized[i]:>11.4f}")

# 実際の最適化例を表示
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 大量データ
n_points = 100000
x = np.linspace(0, 100, n_points)
y = np.sin(x) + np.random.normal(0, 0.1, n_points)

# 全データをプロット（非効率）
ax1.plot(x, y, 'b-', linewidth=0.5, alpha=0.5)
ax1.set_title(f'All {n_points} points (Slow)')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')

# ダウンサンプリング（効率的）
step = 100
ax2.plot(x[::step], y[::step], 'r-', linewidth=1)
ax2.set_title(f'Downsampled (1/{step}, Fast)')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')

plt.tight_layout()
plt.show()

# 2. メモリ効率的なプロット
print("\n--- 2. メモリ効率的なプロット ---")

# ラスタライズの使用
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 多数の線をプロット
n_lines = 100
x = np.linspace(0, 10, 100)

# ベクター形式（メモリ使用量大）
for i in range(n_lines):
    y = np.sin(x + i * 0.1)
    ax1.plot(x, y, alpha=0.3)
ax1.set_title('Vector Format (Large file size)')

# ラスター形式（メモリ効率的）
for i in range(n_lines):
    y = np.sin(x + i * 0.1)
    ax2.plot(x, y, alpha=0.3, rasterized=True)
ax2.set_title('Rasterized (Small file size)')

plt.tight_layout()
plt.show()

# 3. インタラクティブプロットの最適化
print("\n--- 3. インタラクティブプロットの最適化 ---")

# blittingの使用例
class OptimizedAnimation:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.ax.set_xlim(0, 2*np.pi)
        self.ax.set_ylim(-1.5, 1.5)
        
        self.x = np.linspace(0, 2*np.pi, 100)
        self.line, = self.ax.plot([], [], 'b-')
        
        self.ax.set_title('Optimized Animation with Blitting')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.grid(True)
        
        # 背景を保存（blitting用）
        self.fig.canvas.draw()
        self.background = self.fig.canvas.copy_from_bbox(self.ax.bbox)
        
    def update(self, frame):
        # 背景を復元
        self.fig.canvas.restore_region(self.background)
        
        # データを更新
        y = np.sin(self.x + frame * 0.1)
        self.line.set_data(self.x, y)
        
        # 変更部分のみ再描画
        self.ax.draw_artist(self.line)
        self.fig.canvas.blit(self.ax.bbox)

# 静的表示
anim = OptimizedAnimation()
anim.update(0)
plt.show()

# 4. ベストプラクティス：再利用可能な関数
print("\n--- 4. ベストプラクティス：再利用可能な関数 ---")

def create_publication_plot(x, y, xlabel='', ylabel='', title='', 
                          figsize=(8, 6), style='seaborn'):
    """出版品質のプロットを作成する再利用可能な関数"""
    with plt.style.context(style):
        fig, ax = plt.subplots(figsize=figsize)
        
        # メインプロット
        ax.plot(x, y, 'b-', linewidth=2)
        
        # ラベルとタイトル
        ax.set_xlabel(xlabel, fontsize=14)
        ax.set_ylabel(ylabel, fontsize=14)
        ax.set_title(title, fontsize=16, fontweight='bold')
        
        # グリッドとスパイン
        ax.grid(True, alpha=0.3)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        # タイトレイアウト
        plt.tight_layout()
        
        return fig, ax

# 使用例
x = np.linspace(0, 10, 100)
y = np.sin(x) * np.exp(-x/10)
fig, ax = create_publication_plot(x, y, 
                                xlabel='Time (s)', 
                                ylabel='Amplitude',
                                title='Damped Oscillation')
plt.show()

# 5. カラーマップの選択ガイド
print("\n--- 5. カラーマップの選択ガイド ---")

# データの種類別推奨カラーマップ
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# 連続データ
ax = axes[0, 0]
im = ax.imshow(Z, cmap='viridis')
ax.set_title('Sequential: viridis (Recommended)')
plt.colorbar(im, ax=ax)

# 発散データ
ax = axes[0, 1]
Z_div = X * Y
im = ax.imshow(Z_div, cmap='RdBu_r')
ax.set_title('Diverging: RdBu_r')
plt.colorbar(im, ax=ax)

# カテゴリデータ
ax = axes[0, 2]
Z_cat = np.random.randint(0, 10, (20, 20))
im = ax.imshow(Z_cat, cmap='tab10')
ax.set_title('Categorical: tab10')
plt.colorbar(im, ax=ax)

# 知覚的に均一
ax = axes[1, 0]
im = ax.imshow(Z, cmap='cividis')
ax.set_title('Perceptually Uniform: cividis')
plt.colorbar(im, ax=ax)

# 色覚多様性対応
ax = axes[1, 1]
im = ax.imshow(Z, cmap='viridis')
ax.set_title('Colorblind Safe: viridis')
plt.colorbar(im, ax=ax)

# 印刷対応
ax = axes[1, 2]
im = ax.imshow(Z, cmap='gray')
ax.set_title('Print Friendly: gray')
plt.colorbar(im, ax=ax)

plt.tight_layout()
plt.show()

# 6. 効率的なサブプロット作成
print("\n--- 6. 効率的なサブプロット作成 ---")

def create_subplot_grid(data_list, titles, figsize=(12, 8), ncols=3):
    """複数のデータを効率的にサブプロットする"""
    n_plots = len(data_list)
    nrows = (n_plots + ncols - 1) // ncols
    
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize, squeeze=False)
    axes = axes.flatten()
    
    for i, (data, title) in enumerate(zip(data_list, titles)):
        if i < n_plots:
            ax = axes[i]
            ax.plot(data)
            ax.set_title(title)
            ax.grid(True, alpha=0.3)
        else:
            fig.delaxes(axes[i])
    
    plt.tight_layout()
    return fig, axes

# 使用例
data_list = [np.sin(np.linspace(0, 10, 100) + i) for i in range(7)]
titles = [f'Signal {i+1}' for i in range(7)]
fig, axes = create_subplot_grid(data_list, titles)
plt.show()

# 7. エラー処理とバリデーション
print("\n--- 7. エラー処理とバリデーション ---")

def safe_plot(x, y, ax=None, **kwargs):
    """エラー処理を含む安全なプロット関数"""
    # 入力検証
    if len(x) != len(y):
        raise ValueError(f"x and y must have same length: {len(x)} vs {len(y)}")
    
    # NaNやInfのチェック
    if np.any(np.isnan(x)) or np.any(np.isnan(y)):
        print("Warning: NaN values detected, removing them")
        mask = ~(np.isnan(x) | np.isnan(y))
        x, y = x[mask], y[mask]
    
    if np.any(np.isinf(x)) or np.any(np.isinf(y)):
        print("Warning: Inf values detected, removing them")
        mask = ~(np.isinf(x) | np.isinf(y))
        x, y = x[mask], y[mask]
    
    # プロット
    if ax is None:
        fig, ax = plt.subplots()
    
    line = ax.plot(x, y, **kwargs)
    return ax, line

# テスト
x = np.linspace(0, 10, 100)
y = np.sin(x)
y[50:55] = np.nan  # NaNを挿入

fig, ax = plt.subplots()
safe_plot(x, y, ax=ax, label='Safe Plot')
ax.set_title('Plot with Error Handling')
ax.legend()
ax.grid(True)
plt.show()

# 8. メモリとパフォーマンスのモニタリング
print("\n--- 8. メモリとパフォーマンスのモニタリング ---")

import psutil
import os

def plot_with_monitoring(plot_func, *args, **kwargs):
    """プロット関数のメモリ使用量とパフォーマンスを監視"""
    process = psutil.Process(os.getpid())
    
    # 初期メモリ
    mem_before = process.memory_info().rss / 1024 / 1024  # MB
    
    # 実行時間計測
    start_time = time.time()
    result = plot_func(*args, **kwargs)
    end_time = time.time()
    
    # 終了時メモリ
    mem_after = process.memory_info().rss / 1024 / 1024  # MB
    
    print(f"実行時間: {end_time - start_time:.4f} 秒")
    print(f"メモリ使用量: {mem_after - mem_before:.2f} MB")
    
    return result

# テスト関数
def test_plot():
    fig, ax = plt.subplots()
    x = np.linspace(0, 100, 10000)
    for i in range(10):
        ax.plot(x, np.sin(x + i))
    plt.close(fig)
    return fig

# モニタリング付き実行
print("プロットのパフォーマンス測定:")
plot_with_monitoring(test_plot)

# 9. プロットテンプレート
print("\n--- 9. プロットテンプレート ---")

class PlotTemplate:
    """再利用可能なプロットテンプレートクラス"""
    
    def __init__(self, style='seaborn', figsize=(10, 6)):
        self.style = style
        self.figsize = figsize
        self.colors = plt.cm.get_cmap('tab10')
    
    def setup_axes(self, ax, title='', xlabel='', ylabel=''):
        """共通の軸設定"""
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel(xlabel, fontsize=14)
        ax.set_ylabel(ylabel, fontsize=14)
        ax.grid(True, alpha=0.3, linestyle='--')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        return ax
    
    def time_series(self, data, labels=None, title='Time Series Plot'):
        """時系列プロットテンプレート"""
        with plt.style.context(self.style):
            fig, ax = plt.subplots(figsize=self.figsize)
            
            if isinstance(data, list):
                for i, d in enumerate(data):
                    label = labels[i] if labels else f'Series {i+1}'
                    ax.plot(d, color=self.colors(i), label=label, linewidth=2)
                ax.legend()
            else:
                ax.plot(data, color=self.colors(0), linewidth=2)
            
            self.setup_axes(ax, title=title, xlabel='Time', ylabel='Value')
            plt.tight_layout()
            return fig, ax

# テンプレートの使用
template = PlotTemplate()
data = [np.sin(np.linspace(0, 10, 100) + i) for i in range(3)]
labels = ['Signal A', 'Signal B', 'Signal C']
fig, ax = template.time_series(data, labels, title='Multiple Time Series')
plt.show()

print("\nパフォーマンスとベストプラクティスの例を完了しました！")