#!/usr/bin/env python3
"""
Matplotlibチュートリアル - 例8: 画像の保存とエクスポート
"""

import matplotlib.pyplot as plt
import numpy as np
import os

print("=== 画像の保存とエクスポート ===\n")

# 保存用ディレクトリの作成
save_dir = 'matplotlib_outputs'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    print(f"Created directory: {save_dir}")

# 1. 基本的な保存
print("--- 1. 基本的な保存 ---")
# プロットの作成
fig, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
ax.plot(x, np.cos(x), 'r--', linewidth=2, label='cos(x)')
ax.set_title('Basic Save Example')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True, alpha=0.3)

# 様々な形式で保存
fig.savefig(os.path.join(save_dir, 'basic_plot.png'))
fig.savefig(os.path.join(save_dir, 'basic_plot.pdf'))
fig.savefig(os.path.join(save_dir, 'basic_plot.svg'))
fig.savefig(os.path.join(save_dir, 'basic_plot.jpg'), quality=95)

print("Saved: basic_plot.png, .pdf, .svg, .jpg")
plt.close(fig)

# 2. 解像度（DPI）の設定
print("\n--- 2. 解像度（DPI）の設定 ---")
fig, ax = plt.subplots(figsize=(6, 4))
x = np.linspace(0, 2*np.pi, 100)
ax.plot(x, np.sin(x), 'g-', linewidth=2)
ax.set_title('DPI Comparison')
ax.grid(True, alpha=0.3)

# 異なるDPIで保存
dpis = [72, 150, 300, 600]
for dpi in dpis:
    filename = os.path.join(save_dir, f'plot_dpi_{dpi}.png')
    fig.savefig(filename, dpi=dpi)
    filesize = os.path.getsize(filename) / 1024  # KB
    print(f"DPI {dpi}: {filesize:.1f} KB")

plt.close(fig)

# 3. 余白の制御
print("\n--- 3. 余白の制御 ---")
fig, ax = plt.subplots(figsize=(8, 6))
data = np.random.randn(100)
ax.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
ax.set_title('Margin Control Example')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')

# 異なる余白設定で保存
fig.savefig(os.path.join(save_dir, 'plot_default_margin.png'))
fig.savefig(os.path.join(save_dir, 'plot_tight_bbox.png'), bbox_inches='tight')
fig.savefig(os.path.join(save_dir, 'plot_no_padding.png'), 
            bbox_inches='tight', pad_inches=0)
fig.savefig(os.path.join(save_dir, 'plot_extra_padding.png'), 
            bbox_inches='tight', pad_inches=0.5)

print("Saved plots with different margin settings")
plt.close(fig)

# 4. 背景の透明化
print("\n--- 4. 背景の透明化 ---")
fig, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(0, 10, 100)
ax.fill_between(x, 0, np.sin(x), alpha=0.3, label='Area under sin(x)')
ax.plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
ax.set_title('Transparent Background')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True, alpha=0.3)

# 透明背景で保存
fig.savefig(os.path.join(save_dir, 'plot_transparent.png'), 
            transparent=True, dpi=150)
fig.savefig(os.path.join(save_dir, 'plot_opaque.png'), 
            transparent=False, facecolor='white', dpi=150)

print("Saved transparent and opaque versions")
plt.close(fig)

# 5. 複数ページのPDF
print("\n--- 5. 複数ページのPDF ---")
from matplotlib.backends.backend_pdf import PdfPages

pdf_path = os.path.join(save_dir, 'multipage_plots.pdf')
with PdfPages(pdf_path) as pdf:
    # ページ1
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    x = np.linspace(0, 10, 100)
    ax1.plot(x, np.sin(x), 'b-')
    ax1.set_title('Page 1: Sine Wave')
    ax1.grid(True)
    pdf.savefig(fig1)
    plt.close(fig1)
    
    # ページ2
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    data = np.random.normal(100, 15, 1000)
    ax2.hist(data, bins=50, alpha=0.7)
    ax2.set_title('Page 2: Histogram')
    ax2.grid(True, axis='y')
    pdf.savefig(fig2)
    plt.close(fig2)
    
    # ページ3
    fig3, (ax3, ax4) = plt.subplots(2, 1, figsize=(8, 10))
    x = np.linspace(0, 10, 100)
    ax3.plot(x, np.sin(x), 'r-')
    ax3.set_title('Page 3: Multiple Subplots - Top')
    ax4.plot(x, np.cos(x), 'g-')
    ax4.set_title('Page 3: Multiple Subplots - Bottom')
    pdf.savefig(fig3)
    plt.close(fig3)
    
    # PDFメタデータ
    d = pdf.infodict()
    d['Title'] = 'Matplotlib Multi-page PDF Example'
    d['Author'] = 'Matplotlib Tutorial'
    d['Subject'] = 'How to create multi-page PDFs'
    d['Keywords'] = 'Matplotlib, PDF, Tutorial'

print(f"Created multi-page PDF: {pdf_path}")

# 6. カスタムサイズと向き
print("\n--- 6. カスタムサイズと向き ---")
# A4サイズ（インチ単位）
a4_width_inch = 8.27
a4_height_inch = 11.69

# 縦向きA4
fig_portrait = plt.figure(figsize=(a4_width_inch, a4_height_inch))
ax = fig_portrait.add_subplot(111)
ax.text(0.5, 0.5, 'A4 Portrait\n(210 × 297 mm)', 
        ha='center', va='center', fontsize=20, transform=ax.transAxes)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
fig_portrait.savefig(os.path.join(save_dir, 'a4_portrait.pdf'))
plt.close(fig_portrait)

# 横向きA4
fig_landscape = plt.figure(figsize=(a4_height_inch, a4_width_inch))
ax = fig_landscape.add_subplot(111)
ax.text(0.5, 0.5, 'A4 Landscape\n(297 × 210 mm)', 
        ha='center', va='center', fontsize=20, transform=ax.transAxes)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
fig_landscape.savefig(os.path.join(save_dir, 'a4_landscape.pdf'))
plt.close(fig_landscape)

print("Saved A4 portrait and landscape PDFs")

# 7. 高品質エクスポートの設定
print("\n--- 7. 高品質エクスポートの設定 ---")
# 出版品質の図
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.size'] = 12
plt.rcParams['axes.linewidth'] = 1.5

fig, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(0, 10, 1000)
y1 = np.sin(x)
y2 = np.sin(x) * np.exp(-x/10)

ax.plot(x, y1, 'b-', linewidth=2, label='sin(x)')
ax.plot(x, y2, 'r--', linewidth=2, label='sin(x)exp(-x/10)')
ax.fill_between(x, y1, y2, alpha=0.2, color='gray')

ax.set_xlabel('X Axis', fontsize=14)
ax.set_ylabel('Y Axis', fontsize=14)
ax.set_title('Publication Quality Figure', fontsize=16, fontweight='bold')
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3, linestyle='--')

# 高品質設定で保存
fig.savefig(os.path.join(save_dir, 'publication_quality.png'), 
            dpi=300, bbox_inches='tight')
fig.savefig(os.path.join(save_dir, 'publication_quality.pdf'), 
            bbox_inches='tight')
fig.savefig(os.path.join(save_dir, 'publication_quality.svg'), 
            bbox_inches='tight')

print("Saved publication quality figures")
plt.close(fig)

# 8. メタデータの追加
print("\n--- 8. メタデータの追加 ---")
fig, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(0, 2*np.pi, 100)
ax.plot(x, np.sin(x), 'g-', linewidth=2)
ax.set_title('Figure with Metadata')
ax.grid(True)

# メタデータ付きで保存
metadata = {
    'Title': 'Sine Wave Plot',
    'Author': 'Matplotlib Tutorial',
    'Description': 'A simple sine wave demonstration',
    'Copyright': '2024 Tutorial Series',
    'Creation Date': '2024-01-01',
    'Software': 'Matplotlib'
}

fig.savefig(os.path.join(save_dir, 'plot_with_metadata.png'), 
            dpi=150, metadata=metadata)

print("Saved figure with metadata")
plt.close(fig)

# 9. 部分的な保存
print("\n--- 9. 部分的な保存 ---")
fig = plt.figure(figsize=(12, 8))

# 複数のサブプロット
ax1 = plt.subplot(2, 2, 1)
ax1.plot(np.random.randn(100).cumsum())
ax1.set_title('Subplot 1')

ax2 = plt.subplot(2, 2, 2)
ax2.scatter(np.random.randn(50), np.random.randn(50))
ax2.set_title('Subplot 2')

ax3 = plt.subplot(2, 2, 3)
ax3.hist(np.random.randn(100), bins=20)
ax3.set_title('Subplot 3')

ax4 = plt.subplot(2, 2, 4)
ax4.bar(['A', 'B', 'C', 'D'], np.random.randint(1, 10, 4))
ax4.set_title('Subplot 4')

plt.tight_layout()

# 全体を保存
fig.savefig(os.path.join(save_dir, 'all_subplots.png'))

# 特定のサブプロットのみを保存
extent = ax2.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
fig.savefig(os.path.join(save_dir, 'subplot2_only.png'), 
            bbox_inches=extent.expanded(1.1, 1.1))

print("Saved full figure and individual subplot")
plt.close(fig)

# 10. バッチ保存の例
print("\n--- 10. バッチ保存の例 ---")
def create_plot(data, title):
    """プロット作成関数"""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(data)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    return fig

# 複数のプロットを生成して保存
data_sets = {
    'linear': np.linspace(0, 10, 100),
    'quadratic': np.linspace(0, 10, 100)**2,
    'exponential': np.exp(np.linspace(0, 2, 100)),
    'logarithmic': np.log(np.linspace(1, 10, 100))
}

for name, data in data_sets.items():
    fig = create_plot(data, f'{name.capitalize()} Function')
    
    # 複数の形式で保存
    for ext in ['png', 'pdf']:
        filename = os.path.join(save_dir, f'batch_{name}.{ext}')
        fig.savefig(filename, dpi=150, bbox_inches='tight')
    
    plt.close(fig)

print(f"Batch saved {len(data_sets)} plots in multiple formats")

# ファイルサイズの確認
print("\n--- ファイルサイズの比較 ---")
test_files = ['basic_plot.png', 'basic_plot.pdf', 'basic_plot.svg', 'basic_plot.jpg']
for filename in test_files:
    filepath = os.path.join(save_dir, filename)
    if os.path.exists(filepath):
        size = os.path.getsize(filepath) / 1024  # KB
        print(f"{filename}: {size:.1f} KB")

print(f"\n全ての出力ファイルは '{save_dir}' ディレクトリに保存されました。")
print("画像の保存とエクスポートの例を完了しました！")