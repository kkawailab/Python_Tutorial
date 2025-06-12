#!/usr/bin/env python3
"""
Seabornチュートリアル - 例10: 実践的な応用例とベストプラクティス
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# スタイル設定
sns.set_theme(style="whitegrid")

print("=== 実践的な応用例とベストプラクティス ===\n")

# 1. 探索的データ分析（EDA）ダッシュボード
print("--- 1. EDAダッシュボード ---")

def create_eda_dashboard(df, target_col, feature_cols, title="EDA Dashboard"):
    """包括的なEDAダッシュボードを作成"""
    
    fig = plt.figure(figsize=(20, 16))
    gs = fig.add_gridspec(4, 4, hspace=0.3, wspace=0.3)
    
    # 1. ターゲット変数の分布
    ax1 = fig.add_subplot(gs[0, :2])
    sns.histplot(data=df, x=target_col, kde=True, ax=ax1)
    ax1.axvline(df[target_col].mean(), color='red', linestyle='--', 
                label=f'Mean: {df[target_col].mean():.2f}')
    ax1.axvline(df[target_col].median(), color='green', linestyle='--', 
                label=f'Median: {df[target_col].median():.2f}')
    ax1.legend()
    ax1.set_title(f"Distribution of {target_col}")
    
    # 2. 相関行列
    ax2 = fig.add_subplot(gs[0, 2:])
    numeric_cols = [col for col in [target_col] + feature_cols 
                    if df[col].dtype in ['int64', 'float64']]
    if len(numeric_cols) > 1:
        corr = df[numeric_cols].corr()
        mask = np.triu(np.ones_like(corr), k=1)
        sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', 
                   center=0, ax=ax2, fmt='.2f')
        ax2.set_title("Correlation Matrix")
    
    # 3. カテゴリ変数との関係（最大4つ）
    cat_cols = [col for col in feature_cols 
                if df[col].dtype == 'object' or df[col].nunique() < 10][:4]
    
    for i, col in enumerate(cat_cols):
        ax = fig.add_subplot(gs[1, i])
        sns.boxplot(data=df, x=col, y=target_col, ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        ax.set_title(f"{target_col} by {col}")
    
    # 4. 数値変数との散布図（最大4つ）
    num_feat_cols = [col for col in feature_cols 
                     if df[col].dtype in ['int64', 'float64'] 
                     and col != target_col][:4]
    
    for i, col in enumerate(num_feat_cols):
        ax = fig.add_subplot(gs[2, i])
        sns.regplot(data=df, x=col, y=target_col, 
                   scatter_kws={'alpha': 0.5}, ax=ax)
        ax.set_title(f"{target_col} vs {col}")
    
    # 5. 統計サマリー
    ax_summary = fig.add_subplot(gs[3, :2])
    summary_text = f"""Statistical Summary for {target_col}:
    
Count: {df[target_col].count()}
Mean: {df[target_col].mean():.2f}
Std: {df[target_col].std():.2f}
Min: {df[target_col].min():.2f}
25%: {df[target_col].quantile(0.25):.2f}
50%: {df[target_col].quantile(0.50):.2f}
75%: {df[target_col].quantile(0.75):.2f}
Max: {df[target_col].max():.2f}
Skewness: {df[target_col].skew():.2f}
Kurtosis: {df[target_col].kurtosis():.2f}"""
    
    ax_summary.text(0.1, 0.9, summary_text, transform=ax_summary.transAxes,
                   fontsize=10, verticalalignment='top',
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    ax_summary.axis('off')
    ax_summary.set_title("Statistical Summary")
    
    # 6. 欠損値パターン
    ax_missing = fig.add_subplot(gs[3, 2:])
    missing_data = df[numeric_cols].isnull().sum()
    if missing_data.sum() > 0:
        missing_data[missing_data > 0].plot(kind='bar', ax=ax_missing)
        ax_missing.set_title("Missing Values Count")
        ax_missing.set_ylabel("Count")
    else:
        ax_missing.text(0.5, 0.5, "No Missing Values", 
                       transform=ax_missing.transAxes,
                       ha='center', va='center', fontsize=14)
        ax_missing.axis('off')
    
    plt.suptitle(title, fontsize=20, fontweight='bold')
    return fig

# 使用例
tips = sns.load_dataset("tips")
fig = create_eda_dashboard(tips, 'tip', 
                          ['total_bill', 'size', 'day', 'time', 'sex', 'smoker'],
                          "Tips Dataset EDA Dashboard")
plt.show()

# 2. カスタム統計可視化関数
print("\n--- 2. カスタム統計可視化関数 ---")

def plot_distribution_analysis(data, variable, hue=None, figsize=(15, 10)):
    """変数の分布を多角的に分析"""
    
    fig, axes = plt.subplots(2, 3, figsize=figsize)
    
    # 1. ヒストグラム
    ax = axes[0, 0]
    if hue:
        for category in data[hue].unique():
            subset = data[data[hue] == category]
            sns.histplot(data=subset, x=variable, kde=False, 
                        label=category, alpha=0.5, ax=ax)
        ax.legend()
    else:
        sns.histplot(data=data, x=variable, kde=True, ax=ax)
    ax.set_title("Histogram")
    
    # 2. 箱ひげ図
    ax = axes[0, 1]
    if hue:
        sns.boxplot(data=data, x=hue, y=variable, ax=ax)
    else:
        sns.boxplot(data=data, y=variable, ax=ax)
    ax.set_title("Box Plot")
    
    # 3. バイオリンプロット
    ax = axes[0, 2]
    if hue:
        sns.violinplot(data=data, x=hue, y=variable, ax=ax)
    else:
        sns.violinplot(data=data, y=variable, ax=ax)
    ax.set_title("Violin Plot")
    
    # 4. Q-Qプロット
    ax = axes[1, 0]
    stats.probplot(data[variable].dropna(), dist="norm", plot=ax)
    ax.set_title("Q-Q Plot")
    
    # 5. ECDF
    ax = axes[1, 1]
    if hue:
        sns.ecdfplot(data=data, x=variable, hue=hue, ax=ax)
    else:
        sns.ecdfplot(data=data, x=variable, ax=ax)
    ax.set_title("Empirical CDF")
    
    # 6. スタッツテーブル
    ax = axes[1, 2]
    if hue:
        stats_df = data.groupby(hue)[variable].describe()
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText=stats_df.round(2).values,
                        rowLabels=stats_df.index,
                        colLabels=stats_df.columns,
                        cellLoc='center',
                        loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(9)
    else:
        stats_text = f"""Statistics for {variable}:
        
Mean: {data[variable].mean():.2f}
Median: {data[variable].median():.2f}
Std: {data[variable].std():.2f}
Skewness: {data[variable].skew():.2f}
Kurtosis: {data[variable].kurtosis():.2f}"""
        ax.text(0.1, 0.5, stats_text, transform=ax.transAxes,
               fontsize=10, verticalalignment='center')
        ax.axis('off')
    ax.set_title("Statistics")
    
    plt.suptitle(f"Distribution Analysis: {variable}" + 
                 (f" by {hue}" if hue else ""), fontsize=16)
    plt.tight_layout()
    return fig

# 使用例
fig = plot_distribution_analysis(tips, 'total_bill', hue='time')
plt.show()

# 3. 時系列分析ダッシュボード
print("\n--- 3. 時系列分析ダッシュボード ---")

def create_timeseries_dashboard(df, date_col, value_col, 
                               category_col=None, figsize=(16, 12)):
    """時系列データの包括的な分析ダッシュボード"""
    
    fig = plt.figure(figsize=figsize)
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # データの準備
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.sort_values(date_col)
    
    # 1. メイン時系列プロット
    ax1 = fig.add_subplot(gs[0, :])
    if category_col:
        sns.lineplot(data=df, x=date_col, y=value_col, 
                    hue=category_col, ax=ax1)
    else:
        sns.lineplot(data=df, x=date_col, y=value_col, ax=ax1)
    ax1.set_title("Time Series Plot")
    ax1.tick_params(axis='x', rotation=45)
    
    # 2. 移動平均
    ax2 = fig.add_subplot(gs[1, :2])
    if not category_col:
        df['MA7'] = df[value_col].rolling(window=7).mean()
        df['MA30'] = df[value_col].rolling(window=30).mean()
        
        ax2.plot(df[date_col], df[value_col], alpha=0.3, label='Original')
        ax2.plot(df[date_col], df['MA7'], label='7-day MA', linewidth=2)
        ax2.plot(df[date_col], df['MA30'], label='30-day MA', linewidth=2)
        ax2.legend()
        ax2.set_title("Moving Averages")
        ax2.tick_params(axis='x', rotation=45)
    
    # 3. 季節性分析
    ax3 = fig.add_subplot(gs[1, 2])
    df['month'] = df[date_col].dt.month
    monthly_avg = df.groupby('month')[value_col].mean()
    sns.barplot(x=monthly_avg.index, y=monthly_avg.values, ax=ax3)
    ax3.set_title("Monthly Average")
    ax3.set_xlabel("Month")
    
    # 4. 曜日別パターン
    ax4 = fig.add_subplot(gs[2, 0])
    df['dayofweek'] = df[date_col].dt.dayofweek
    day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    daily_avg = df.groupby('dayofweek')[value_col].mean()
    sns.barplot(x=daily_avg.index, y=daily_avg.values, ax=ax4)
    ax4.set_xticklabels(day_names)
    ax4.set_title("Day of Week Pattern")
    
    # 5. 分布
    ax5 = fig.add_subplot(gs[2, 1])
    sns.histplot(data=df, x=value_col, kde=True, ax=ax5)
    ax5.set_title("Value Distribution")
    
    # 6. 自己相関
    ax6 = fig.add_subplot(gs[2, 2])
    if not category_col and len(df) > 40:
        from statsmodels.graphics.tsaplots import plot_acf
        plot_acf(df[value_col].dropna(), lags=20, ax=ax6)
        ax6.set_title("Autocorrelation")
    else:
        ax6.text(0.5, 0.5, "ACF not available", 
                transform=ax6.transAxes, ha='center', va='center')
        ax6.axis('off')
    
    plt.suptitle("Time Series Analysis Dashboard", fontsize=16, fontweight='bold')
    return fig

# 時系列データの作成
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=180, freq='D')
ts_data = pd.DataFrame({
    'date': dates,
    'sales': 100 + np.cumsum(np.random.randn(180)) + 
             10 * np.sin(np.arange(180) * 2 * np.pi / 30)
})

fig = create_timeseries_dashboard(ts_data, 'date', 'sales')
plt.show()

# 4. 機械学習結果の可視化
print("\n--- 4. 機械学習結果の可視化 ---")

def plot_ml_results(y_true, y_pred, y_proba=None, figsize=(15, 10)):
    """機械学習の結果を可視化"""
    
    fig, axes = plt.subplots(2, 3, figsize=figsize)
    
    # 1. 混同行列
    ax = axes[0, 0]
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
    ax.set_title("Confusion Matrix")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    
    # 2. 分類レポート
    ax = axes[0, 1]
    from sklearn.metrics import classification_report
    report = classification_report(y_true, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).T[:-3]  # accuracy, macro avg, weighted avgを除外
    
    sns.heatmap(report_df, annot=True, cmap='YlOrRd', ax=ax)
    ax.set_title("Classification Report")
    
    # 3. ROC曲線（2クラス分類の場合）
    ax = axes[0, 2]
    if y_proba is not None and len(np.unique(y_true)) == 2:
        from sklearn.metrics import roc_curve, auc
        fpr, tpr, _ = roc_curve(y_true, y_proba[:, 1])
        roc_auc = auc(fpr, tpr)
        
        ax.plot(fpr, tpr, label=f'ROC (AUC = {roc_auc:.2f})')
        ax.plot([0, 1], [0, 1], 'k--')
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.set_title('ROC Curve')
        ax.legend()
    else:
        ax.text(0.5, 0.5, "ROC not available\n(binary classification only)", 
                transform=ax.transAxes, ha='center', va='center')
        ax.axis('off')
    
    # 4. 予測値の分布
    ax = axes[1, 0]
    pred_df = pd.DataFrame({'True': y_true, 'Predicted': y_pred})
    pred_counts = pred_df.groupby(['True', 'Predicted']).size().unstack(fill_value=0)
    sns.heatmap(pred_counts, annot=True, fmt='d', cmap='Greens', ax=ax)
    ax.set_title("Prediction Distribution")
    
    # 5. エラー分析
    ax = axes[1, 1]
    errors = y_true != y_pred
    error_rate_by_class = pd.Series(y_true[errors]).value_counts() / pd.Series(y_true).value_counts()
    error_rate_by_class.plot(kind='bar', ax=ax)
    ax.set_title("Error Rate by Class")
    ax.set_ylabel("Error Rate")
    ax.set_xlabel("Class")
    
    # 6. 特徴重要度（ダミー）
    ax = axes[1, 2]
    # 実際の特徴重要度がある場合はここで表示
    feature_importance = pd.DataFrame({
        'feature': [f'Feature_{i}' for i in range(5)],
        'importance': np.random.rand(5)
    }).sort_values('importance', ascending=False)
    
    sns.barplot(data=feature_importance, y='feature', x='importance', ax=ax)
    ax.set_title("Feature Importance (Example)")
    
    plt.suptitle("Machine Learning Results Dashboard", fontsize=16, fontweight='bold')
    plt.tight_layout()
    return fig

# シミュレーションデータ
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X, y = make_classification(n_samples=1000, n_features=20, n_classes=3, 
                          n_informative=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
y_proba = clf.predict_proba(X_test)

fig = plot_ml_results(y_test, y_pred, y_proba)
plt.show()

# 5. レポート用の出版品質プロット
print("\n--- 5. 出版品質のプロット ---")

def create_publication_plot(data, x, y, hue=None, 
                           title="", xlabel="", ylabel="",
                           figsize=(10, 6), dpi=300, save_path=None):
    """出版品質のプロットを作成"""
    
    # スタイル設定
    plt.style.use('seaborn-v0_8-whitegrid')
    sns.set_palette("colorblind")
    
    # フォント設定
    plt.rcParams.update({
        'font.size': 14,
        'axes.labelsize': 16,
        'axes.titlesize': 18,
        'xtick.labelsize': 14,
        'ytick.labelsize': 14,
        'legend.fontsize': 14,
        'figure.dpi': dpi,
        'savefig.dpi': dpi,
        'savefig.bbox': 'tight',
        'font.family': 'serif'
    })
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # メインプロット
    if hue:
        # カテゴリごとの回帰線付き散布図
        unique_hues = data[hue].unique()
        colors = sns.color_palette("colorblind", n_colors=len(unique_hues))
        
        for i, category in enumerate(unique_hues):
            subset = data[data[hue] == category]
            ax.scatter(subset[x], subset[y], label=category, 
                      s=60, alpha=0.7, edgecolors='black', 
                      linewidth=0.5, color=colors[i])
            
            # 回帰線
            z = np.polyfit(subset[x], subset[y], 1)
            p = np.poly1d(z)
            x_line = np.linspace(subset[x].min(), subset[x].max(), 100)
            ax.plot(x_line, p(x_line), color=colors[i], linewidth=2, alpha=0.8)
    else:
        # 単一の回帰線付き散布図
        ax.scatter(data[x], data[y], s=60, alpha=0.7, 
                  edgecolors='black', linewidth=0.5)
        
        # 回帰線と信頼区間
        sns.regplot(data=data, x=x, y=y, scatter=False, 
                   ax=ax, color='red', ci=95)
    
    # ラベルとタイトル
    ax.set_xlabel(xlabel or x, fontweight='bold')
    ax.set_ylabel(ylabel or y, fontweight='bold')
    ax.set_title(title, fontweight='bold', pad=20)
    
    # グリッドとスパイン
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    
    # 目盛りの内向き
    ax.tick_params(direction='in', length=6, width=1.5)
    
    # 凡例
    if hue:
        legend = ax.legend(title=hue, frameon=True, fancybox=True, 
                         shadow=True, loc='best', 
                         title_fontsize=14, fontsize=12)
        legend.get_frame().set_alpha(0.9)
    
    plt.tight_layout()
    
    # 保存
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=dpi)
        print(f"Plot saved to {save_path}")
    
    return fig, ax

# 使用例
fig, ax = create_publication_plot(
    tips, 'total_bill', 'tip', hue='day',
    title="Relationship between Total Bill and Tip Amount",
    xlabel="Total Bill (USD)",
    ylabel="Tip Amount (USD)"
)
plt.show()

print("\n実践的な応用例とベストプラクティスの例を完了しました！")