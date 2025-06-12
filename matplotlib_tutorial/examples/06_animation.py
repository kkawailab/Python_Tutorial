#!/usr/bin/env python3
"""
Matplotlibチュートリアル - 例6: アニメーション
注意: このスクリプトは実際のアニメーションコードを含みますが、
      通常の実行では静的なプロットのみ表示されます。
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

print("=== アニメーション ===\n")
print("注意: 実際のアニメーションを見るには、")
print("Jupyter NotebookやIPythonで実行するか、")
print("animation.save()を使って動画ファイルとして保存してください。\n")

# 1. 基本的なアニメーションの構造
print("--- 1. 基本的なアニメーションの構造 ---")
def create_basic_animation():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1.5, 1.5)
    
    x = np.linspace(0, 2*np.pi, 100)
    line, = ax.plot([], [], 'b-')
    
    def init():
        line.set_data([], [])
        return line,
    
    def animate(frame):
        y = np.sin(x + frame/10)
        line.set_data(x, y)
        return line,
    
    # アニメーションオブジェクトの作成
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                  frames=100, interval=50, blit=True)
    
    ax.set_title('Sine Wave Animation (Static View)')
    ax.set_xlabel('x')
    ax.set_ylabel('sin(x)')
    ax.grid(True)
    
    # 静的な表示のため、最初のフレームを表示
    y = np.sin(x)
    ax.plot(x, y, 'b-')
    plt.show()
    
    return anim

# 基本アニメーションの作成
anim1 = create_basic_animation()

# 2. 成長するプロット
print("\n--- 2. 成長するプロット ---")
def create_growing_plot():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(-2, 2)
    
    x_data, y_data = [], []
    line, = ax.plot([], [], 'r-')
    
    def init():
        line.set_data([], [])
        return line,
    
    def update(frame):
        x_data.append(frame * 0.1)
        y_data.append(np.sin(frame * 0.1))
        line.set_data(x_data, y_data)
        return line,
    
    # 静的表示用
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y, 'r-', alpha=0.5, label='Complete trajectory')
    ax.plot(x[:30], y[:30], 'r-', linewidth=2, label='Growing part')
    
    ax.set_title('Growing Plot Animation (Static View)')
    ax.set_xlabel('x')
    ax.set_ylabel('sin(x)')
    ax.legend()
    ax.grid(True)
    plt.show()

create_growing_plot()

# 3. 散布図アニメーション
print("\n--- 3. 散布図アニメーション ---")
def create_scatter_animation():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    
    # パーティクルの初期化
    n_particles = 100
    positions = np.random.randn(n_particles, 2)
    velocities = np.random.randn(n_particles, 2) * 0.05
    
    scatter = ax.scatter(positions[:, 0], positions[:, 1], c='blue', alpha=0.6)
    
    def update(frame):
        global positions, velocities
        # 位置の更新
        positions += velocities
        # 境界での反射
        velocities[positions > 2] *= -1
        velocities[positions < -2] *= -1
        positions = np.clip(positions, -2, 2)
        scatter.set_offsets(positions)
        return scatter,
    
    ax.set_title('Particle Animation (Static View)')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True, alpha=0.3)
    plt.show()

create_scatter_animation()

# 4. 複数のサブプロットのアニメーション
print("\n--- 4. 複数のサブプロットのアニメーション ---")
def create_multiplot_animation():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))
    
    x = np.linspace(0, 2*np.pi, 100)
    
    # 上のプロット：波形
    ax1.set_xlim(0, 2*np.pi)
    ax1.set_ylim(-2, 2)
    line1, = ax1.plot([], [], 'b-')
    line2, = ax1.plot([], [], 'r--')
    
    # 下のプロット：フーリエ成分
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 1)
    bars = ax2.bar(range(10), np.zeros(10))
    
    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        for bar in bars:
            bar.set_height(0)
        return [line1, line2] + list(bars)
    
    def animate(frame):
        # 波形
        y1 = np.sin(x + frame/10)
        y2 = np.cos(x + frame/10)
        line1.set_data(x, y1)
        line2.set_data(x, y2)
        
        # フーリエ成分（シミュレーション）
        freqs = np.abs(np.random.randn(10)) * np.exp(-np.arange(10)/3)
        for bar, h in zip(bars, freqs):
            bar.set_height(h)
        
        return [line1, line2] + list(bars)
    
    ax1.set_title('Wave Animation')
    ax1.set_xlabel('x')
    ax1.set_ylabel('Amplitude')
    ax1.legend(['sin(x)', 'cos(x)'])
    ax1.grid(True)
    
    ax2.set_title('Frequency Components')
    ax2.set_xlabel('Frequency')
    ax2.set_ylabel('Magnitude')
    ax2.grid(True, axis='y')
    
    # 静的表示
    y1 = np.sin(x)
    y2 = np.cos(x)
    ax1.plot(x, y1, 'b-', label='sin(x)')
    ax1.plot(x, y2, 'r--', label='cos(x)')
    
    freqs = np.abs(np.random.randn(10)) * np.exp(-np.arange(10)/3)
    ax2.bar(range(10), freqs)
    
    plt.tight_layout()
    plt.show()

create_multiplot_animation()

# 5. 3Dアニメーション
print("\n--- 5. 3Dアニメーション ---")
def create_3d_animation():
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # らせんのパラメータ
    t = np.linspace(0, 4*np.pi, 100)
    x = np.sin(t)
    y = np.cos(t)
    z = t / (4*np.pi)
    
    line, = ax.plot([], [], [], 'b-')
    
    def init():
        line.set_data([], [])
        line.set_3d_properties([])
        return line,
    
    def animate(frame):
        # 回転する視点
        ax.view_init(elev=30, azim=frame)
        return line,
    
    # 静的表示
    ax.plot(x, y, z, 'b-', linewidth=2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Helix Animation (Static View)')
    
    plt.show()

create_3d_animation()

# 6. リアルタイムデータのシミュレーション
print("\n--- 6. リアルタイムデータのシミュレーション ---")
def create_realtime_plot():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # 上のプロット：時系列データ
    ax1.set_xlim(0, 100)
    ax1.set_ylim(-3, 3)
    line1, = ax1.plot([], [], 'b-')
    
    # 下のプロット：ヒストグラム
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(0, 50)
    
    x_data, y_data = [], []
    
    def init():
        line1.set_data([], [])
        return line1,
    
    def update(frame):
        # 新しいデータポイント
        x_data.append(frame)
        y_data.append(np.sin(frame/10) + np.random.normal(0, 0.3))
        
        # 最新の100点のみ保持
        if len(x_data) > 100:
            x_data.pop(0)
            y_data.pop(0)
            ax1.set_xlim(frame-100, frame)
        
        line1.set_data(x_data, y_data)
        
        # ヒストグラムの更新
        ax2.clear()
        ax2.hist(y_data, bins=20, alpha=0.7, color='green')
        ax2.set_xlim(-3, 3)
        ax2.set_ylim(0, 50)
        ax2.set_xlabel('Value')
        ax2.set_ylabel('Frequency')
        
        return line1,
    
    ax1.set_title('Real-time Data Stream')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Value')
    ax1.grid(True)
    
    # 静的表示用のデータ
    t = np.linspace(0, 100, 1000)
    signal = np.sin(t/10) + np.random.normal(0, 0.3, 1000)
    ax1.plot(t, signal, 'b-', alpha=0.7)
    ax2.hist(signal, bins=20, alpha=0.7, color='green')
    ax2.set_xlabel('Value')
    ax2.set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()

create_realtime_plot()

# 7. アニメーションの保存方法（コード例）
print("\n--- 7. アニメーションの保存方法 ---")
print("アニメーションを保存するには、以下のコードを使用します：")
print()
print("# MP4として保存")
print("anim.save('animation.mp4', writer='ffmpeg', fps=30)")
print()
print("# GIFとして保存")
print("anim.save('animation.gif', writer='pillow', fps=30)")
print()
print("# HTMLとして保存（JavaScript使用）")
print("anim.save('animation.html', writer='html')")
print()
print("注意: ffmpegやpillowなどの追加ライブラリが必要です。")

# カスタムアニメーション関数クラスの例
print("\n--- 8. カスタムアニメーションクラス ---")
class AnimatedScatter:
    def __init__(self, numpoints=50):
        self.numpoints = numpoints
        self.stream = self.data_stream()
        
        # 図の設定
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.scat = self.ax.scatter([], [])
        
    def data_stream(self):
        """データジェネレーター"""
        data = np.random.randn(self.numpoints, 2)
        while True:
            data += (np.random.randn(self.numpoints, 2) - data) * 0.1
            yield data
    
    def update(self, frame):
        """アップデート関数"""
        data = next(self.stream)
        self.scat.set_offsets(data)
        return self.scat,
    
    def show(self):
        """静的表示"""
        data = np.random.randn(self.numpoints, 2)
        self.ax.scatter(data[:, 0], data[:, 1], alpha=0.6)
        self.ax.set_title('Animated Scatter Class Example')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.grid(True, alpha=0.3)
        plt.show()

# クラスの使用例
animated_scatter = AnimatedScatter(numpoints=100)
animated_scatter.show()

print("\nアニメーションの例を完了しました！")
print("実際のアニメーションを見るには、Jupyter Notebookや")
print("専用の環境で実行してください。")