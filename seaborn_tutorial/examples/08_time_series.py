#!/usr/bin/env python3
"""
Seabornチュートリアル - 例8: 時系列データの可視化
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.dates as mdates

# スタイル設定
sns.set_theme(style="whitegrid")

print("=== 時系列データの可視化 ===\n")

# 1. 時系列データの作成
print("--- 1. 時系列データの準備 ---")
# 基本的な時系列データ
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=365, freq='D')
values = np.cumsum(np.random.randn(365)) + 100
ts_data = pd.DataFrame({
    'date': dates,
    'value': values,
    'month': dates.month,
    'day_of_week': dates.day_name(),
    'quarter': dates.quarter
})

# カテゴリ別時系列データ
categories = ['Product A', 'Product B', 'Product C']
multi_ts_data = []
for cat in categories:
    base = 100 if cat == 'Product A' else 80 if cat == 'Product B' else 60
    values = base + np.cumsum(np.random.randn(365) * 2)
    for i, date in enumerate(dates):
        multi_ts_data.append({
            'date': date,
            'product': cat,
            'sales': max(0, values[i]),
            'month': date.month,
            'quarter': f'Q{date.quarter}'
        })

multi_ts_df = pd.DataFrame(multi_ts_data)

print(f"データ形状: {ts_data.shape}")
print(ts_data.head())

# 2. 基本的な時系列プロット
print("\n--- 2. 基本的な時系列プロット ---")
plt.figure(figsize=(14, 6))
sns.lineplot(data=ts_data, x='date', y='value')
plt.title("Basic Time Series Plot")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. 複数系列の時系列プロット
print("\n--- 3. 複数系列の時系列プロット ---")
plt.figure(figsize=(14, 6))
sns.lineplot(data=multi_ts_df, x='date', y='sales', 
             hue='product', style='product', markers=False)
plt.title("Multiple Time Series")
plt.xticks(rotation=45)
plt.legend(title='Product', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 4. 移動平均とトレンド
print("\n--- 4. 移動平均とトレンド ---")
# 移動平均の計算
for window in [7, 30]:
    ts_data[f'ma_{window}'] = ts_data['value'].rolling(window=window).mean()

plt.figure(figsize=(14, 8))
plt.plot(ts_data['date'], ts_data['value'], 
         alpha=0.3, label='Original', color='gray')
plt.plot(ts_data['date'], ts_data['ma_7'], 
         label='7-day MA', linewidth=2, color='blue')
plt.plot(ts_data['date'], ts_data['ma_30'], 
         label='30-day MA', linewidth=2, color='red')

# トレンドライン
z = np.polyfit(range(len(ts_data)), ts_data['value'], 1)
p = np.poly1d(z)
plt.plot(ts_data['date'], p(range(len(ts_data))), 
         "--", label='Trend', linewidth=2, color='green')

plt.title("Time Series with Moving Averages and Trend")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. 季節性の可視化
print("\n--- 5. 季節性の可視化 ---")
# 月別集計
monthly_avg = ts_data.groupby('month')['value'].mean().reset_index()

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 月別平均
ax = axes[0, 0]
sns.barplot(data=monthly_avg, x='month', y='value', ax=ax)
ax.set_title("Average by Month")
ax.set_xlabel("Month")

# 曜日別パターン
daily_pattern = multi_ts_df.groupby(['product', multi_ts_df['date'].dt.day_name()])['sales'].mean().reset_index()
daily_pattern['date'] = pd.Categorical(daily_pattern['date'], 
                                       categories=['Monday', 'Tuesday', 'Wednesday', 
                                                  'Thursday', 'Friday', 'Saturday', 'Sunday'],
                                       ordered=True)

ax = axes[0, 1]
sns.lineplot(data=daily_pattern.sort_values('date'), 
             x='date', y='sales', hue='product', 
             marker='o', ax=ax)
ax.set_title("Weekly Pattern")
ax.set_xlabel("Day of Week")
ax.tick_params(axis='x', rotation=45)

# 四半期別トレンド
ax = axes[1, 0]
sns.boxplot(data=multi_ts_df, x='quarter', y='sales', 
            hue='product', ax=ax)
ax.set_title("Quarterly Distribution")

# ヒートマップ形式の月別日別集計
pivot_data = ts_data.pivot_table(
    values='value',
    index=ts_data['date'].dt.day,
    columns=ts_data['date'].dt.month,
    aggfunc='mean'
)

ax = axes[1, 1]
sns.heatmap(pivot_data, cmap='RdYlBu_r', ax=ax,
            cbar_kws={'label': 'Average Value'})
ax.set_title("Day-Month Heatmap")
ax.set_xlabel("Month")
ax.set_ylabel("Day of Month")

plt.suptitle("Seasonality Analysis", fontsize=16)
plt.tight_layout()
plt.show()

# 6. 時系列の分解
print("\n--- 6. 時系列の分解 ---")
# 簡易的な分解（実際はstatsmodelsを使用することが多い）
fig, axes = plt.subplots(4, 1, figsize=(14, 12))

# 元のデータ
ax = axes[0]
ax.plot(ts_data['date'], ts_data['value'])
ax.set_title("Original Time Series")
ax.set_ylabel("Value")

# トレンド
ax = axes[1]
trend = ts_data['value'].rolling(window=30, center=True).mean()
ax.plot(ts_data['date'], trend, color='red')
ax.set_title("Trend Component")
ax.set_ylabel("Trend")

# 季節性（簡易版）
ax = axes[2]
detrended = ts_data['value'] - trend
seasonal = detrended.groupby(ts_data['date'].dt.dayofyear).transform('mean')
ax.plot(ts_data['date'], seasonal, color='green')
ax.set_title("Seasonal Component")
ax.set_ylabel("Seasonal")

# 残差
ax = axes[3]
residual = ts_data['value'] - trend - seasonal
ax.plot(ts_data['date'], residual, color='blue', alpha=0.5)
ax.set_title("Residual Component")
ax.set_ylabel("Residual")
ax.set_xlabel("Date")

for ax in axes:
    ax.tick_params(axis='x', rotation=45)

plt.suptitle("Time Series Decomposition", fontsize=16)
plt.tight_layout()
plt.show()

# 7. リサンプリングと集計
print("\n--- 7. リサンプリングと集計 ---")
# 異なる頻度でのリサンプリング
ts_data_indexed = ts_data.set_index('date')

fig, axes = plt.subplots(3, 1, figsize=(14, 10))

# 週次集計
ax = axes[0]
weekly = ts_data_indexed['value'].resample('W').mean()
weekly.plot(ax=ax, marker='o')
ax.set_title("Weekly Aggregation (Mean)")
ax.set_ylabel("Value")

# 月次集計（複数の統計量）
ax = axes[1]
monthly = ts_data_indexed['value'].resample('M').agg(['mean', 'min', 'max'])
monthly['mean'].plot(ax=ax, label='Mean', linewidth=2)
ax.fill_between(monthly.index, monthly['min'], monthly['max'], 
                alpha=0.3, label='Min-Max Range')
ax.set_title("Monthly Aggregation with Range")
ax.set_ylabel("Value")
ax.legend()

# 四半期集計（棒グラフ）
ax = axes[2]
quarterly = ts_data_indexed['value'].resample('Q').sum()
quarterly.plot(kind='bar', ax=ax)
ax.set_title("Quarterly Sum")
ax.set_ylabel("Total Value")
ax.set_xlabel("Quarter")
ax.tick_params(axis='x', rotation=45)

plt.suptitle("Resampling at Different Frequencies", fontsize=16)
plt.tight_layout()
plt.show()

# 8. 時系列の比較
print("\n--- 8. 時系列の比較 ---")
# 年度比較用のデータ作成
years_data = []
for year in [2021, 2022, 2023]:
    dates = pd.date_range(f'{year}-01-01', f'{year}-12-31', freq='D')
    values = 100 + np.cumsum(np.random.randn(len(dates))) + (year - 2021) * 20
    for i, date in enumerate(dates):
        years_data.append({
            'date': date,
            'value': values[i],
            'year': year,
            'day_of_year': date.dayofyear
        })

years_df = pd.DataFrame(years_data)

plt.figure(figsize=(14, 8))
for year in [2021, 2022, 2023]:
    data = years_df[years_df['year'] == year]
    plt.plot(data['day_of_year'], data['value'], 
             label=f'Year {year}', linewidth=2)

plt.title("Year-over-Year Comparison")
plt.xlabel("Day of Year")
plt.ylabel("Value")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 9. イベントとアノテーション
print("\n--- 9. イベントとアノテーション ---")
# イベントの追加
events = [
    ('2023-03-15', 'Product Launch'),
    ('2023-06-01', 'Summer Campaign'),
    ('2023-09-10', 'System Update'),
    ('2023-11-24', 'Black Friday')
]

plt.figure(figsize=(14, 8))
sns.lineplot(data=ts_data, x='date', y='value')

# イベントをマーク
for event_date, event_name in events:
    event_date = pd.to_datetime(event_date)
    event_value = ts_data[ts_data['date'] == event_date]['value'].values[0]
    
    plt.axvline(x=event_date, color='red', linestyle='--', alpha=0.5)
    plt.annotate(event_name, 
                xy=(event_date, event_value),
                xytext=(10, 20), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.title("Time Series with Events")
plt.xlabel("Date")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 10. 時系列予測の可視化
print("\n--- 10. 時系列予測の可視化 ---")
# 簡単な予測（最後の30日の平均とトレンドから）
train_end = '2023-11-30'
train_data = ts_data[ts_data['date'] <= train_end]
test_data = ts_data[ts_data['date'] > train_end]

# 予測（単純な方法）
last_30_mean = train_data.tail(30)['value'].mean()
trend = (train_data.tail(30)['value'].iloc[-1] - train_data.tail(30)['value'].iloc[0]) / 30

forecast_dates = test_data['date']
forecast_values = [last_30_mean + trend * i for i in range(len(forecast_dates))]

# 信頼区間（仮想的）
std = train_data.tail(30)['value'].std()
upper_bound = [f + 2*std for f in forecast_values]
lower_bound = [f - 2*std for f in forecast_values]

plt.figure(figsize=(14, 8))
# 実績データ
plt.plot(train_data['date'], train_data['value'], 
         label='Historical', color='blue')
plt.plot(test_data['date'], test_data['value'], 
         label='Actual', color='green')

# 予測
plt.plot(forecast_dates, forecast_values, 
         label='Forecast', color='red', linestyle='--')

# 信頼区間
plt.fill_between(forecast_dates, lower_bound, upper_bound, 
                alpha=0.2, color='red', label='95% CI')

# 境界線
plt.axvline(x=pd.to_datetime(train_end), 
           color='black', linestyle=':', linewidth=2)

plt.title("Time Series Forecast Visualization")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n時系列データの可視化の例を完了しました！")