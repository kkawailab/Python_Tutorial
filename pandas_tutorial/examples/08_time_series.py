#!/usr/bin/env python3
"""
Pandasチュートリアル - 例8: 時系列データの処理
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("=== 時系列データの処理 ===\n")

# 1. 日付時刻データの作成
print("--- 1. 日付時刻データの作成 ---")

# 様々な方法で日付を作成
dates1 = pd.date_range('2023-01-01', periods=10, freq='D')
dates2 = pd.date_range('2023-01-01', '2023-01-10', freq='D')
dates3 = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')

print("日次データ（10日間）:")
print(dates1)
print("\n月次データ（2023年）:")
print(dates3)

# 営業日
business_days = pd.bdate_range('2023-01-01', periods=10)
print("\n営業日（10日間）:")
print(business_days)

# カスタム頻度
custom_dates = pd.date_range('2023-01-01', periods=10, freq='2D')  # 2日ごと
print("\n2日ごとのデータ:")
print(custom_dates)

# 2. 時系列データフレームの作成
print("\n--- 2. 時系列データフレームの作成 ---")

# 時系列データの作成
np.random.seed(42)
ts_data = pd.DataFrame({
    'date': pd.date_range('2023-01-01', periods=365, freq='D'),
    'sales': np.random.randint(100, 1000, 365) + np.sin(np.arange(365) * 2 * np.pi / 365) * 200,
    'customers': np.random.randint(50, 200, 365),
    'temperature': 20 + 10 * np.sin(np.arange(365) * 2 * np.pi / 365) + np.random.randn(365) * 2
})

# 日付をインデックスに設定
ts_data = ts_data.set_index('date')
print("時系列データ（最初の10日）:")
print(ts_data.head(10))

# 3. 日付時刻の属性
print("\n--- 3. 日付時刻の属性 ---")

# 日付属性の抽出
ts_data['year'] = ts_data.index.year
ts_data['month'] = ts_data.index.month
ts_data['day'] = ts_data.index.day
ts_data['dayofweek'] = ts_data.index.dayofweek
ts_data['dayname'] = ts_data.index.day_name()
ts_data['quarter'] = ts_data.index.quarter
ts_data['is_month_start'] = ts_data.index.is_month_start
ts_data['is_month_end'] = ts_data.index.is_month_end

print("日付属性を追加（一部）:")
print(ts_data[['sales', 'year', 'month', 'dayname', 'quarter']].head(10))

# 元に戻す（分析用）
ts_data = ts_data[['sales', 'customers', 'temperature']]

# 4. 時系列の選択とスライス
print("\n--- 4. 時系列の選択とスライス ---")

# 特定の日付
print("2023年1月15日のデータ:")
print(ts_data.loc['2023-01-15'])

# 日付範囲
print("\n2023年1月の最初の週:")
print(ts_data.loc['2023-01-01':'2023-01-07'])

# 月での選択
print("\n2023年3月のデータ（最初の5日）:")
print(ts_data.loc['2023-03'].head())

# 年での選択
print("\n2023年のデータ（統計）:")
print(ts_data.loc['2023'].describe())

# 5. リサンプリング
print("\n--- 5. リサンプリング ---")

# 週次リサンプリング
weekly = ts_data.resample('W').agg({
    'sales': ['sum', 'mean'],
    'customers': 'sum',
    'temperature': 'mean'
})
print("週次集計（最初の5週）:")
print(weekly.head())

# 月次リサンプリング
monthly = ts_data.resample('M').agg({
    'sales': ['sum', 'mean', 'std'],
    'customers': ['sum', 'mean'],
    'temperature': ['mean', 'max', 'min']
})
print("\n月次集計:")
print(monthly)

# カスタム期間でのリサンプリング
biweekly = ts_data.resample('2W').mean()
print("\n隔週の平均:")
print(biweekly.head())

# 6. 移動窓関数
print("\n--- 6. 移動窓関数 ---")

# 移動平均
ts_data['sales_ma7'] = ts_data['sales'].rolling(window=7).mean()
ts_data['sales_ma30'] = ts_data['sales'].rolling(window=30).mean()

print("移動平均を追加（一部）:")
print(ts_data[['sales', 'sales_ma7', 'sales_ma30']].head(35).tail(10))

# 移動統計
rolling_stats = ts_data['sales'].rolling(window=30).agg(['mean', 'std', 'min', 'max'])
print("\n30日移動統計（一部）:")
print(rolling_stats.tail(10))

# エクスパンディング（累積）
ts_data['sales_cumsum'] = ts_data['sales'].expanding().sum()
ts_data['sales_cummax'] = ts_data['sales'].expanding().max()

print("\n累積統計（最後の10日）:")
print(ts_data[['sales', 'sales_cumsum', 'sales_cummax']].tail(10))

# 7. シフトと差分
print("\n--- 7. シフトと差分 ---")

# シフト（ラグ）
ts_data['sales_lag1'] = ts_data['sales'].shift(1)
ts_data['sales_lag7'] = ts_data['sales'].shift(7)

# 前期比
ts_data['sales_change'] = ts_data['sales'].diff()
ts_data['sales_pct_change'] = ts_data['sales'].pct_change() * 100

print("シフトと差分（一部）:")
print(ts_data[['sales', 'sales_lag1', 'sales_change', 'sales_pct_change']].head(10))

# 前年同期比（簡易版）
ts_data['sales_yoy'] = ts_data['sales'].pct_change(periods=365) * 100

# 8. 時系列の分解
print("\n--- 8. 時系列の分解 ---")

# 簡易的な分解
# トレンド（30日移動平均）
trend = ts_data['sales'].rolling(window=30, center=True).mean()

# 季節性（トレンドを除いた後の月別平均）
detrended = ts_data['sales'] - trend
seasonal = detrended.groupby(detrended.index.month).transform('mean')

# 残差
residual = ts_data['sales'] - trend - seasonal

# 結果をまとめる
decomposition = pd.DataFrame({
    'original': ts_data['sales'],
    'trend': trend,
    'seasonal': seasonal,
    'residual': residual
})

print("時系列分解（一部）:")
print(decomposition.dropna().head(10))

# 9. 日付の操作
print("\n--- 9. 日付の操作 ---")

# 日付の加算・減算
sample_date = pd.Timestamp('2023-01-15')
print(f"基準日: {sample_date}")
print(f"1週間後: {sample_date + pd.Timedelta(weeks=1)}")
print(f"30日前: {sample_date - pd.Timedelta(days=30)}")

# 月末・月初の取得
print(f"月末: {sample_date + pd.offsets.MonthEnd()}")
print(f"月初: {sample_date - pd.offsets.MonthBegin()}")

# 営業日の計算
print(f"5営業日後: {sample_date + pd.offsets.BDay(5)}")

# 10. 実践的な時系列分析
print("\n--- 10. 実践的な時系列分析 ---")

# 包括的な時系列レポート
def create_time_series_report(df, value_col):
    """時系列データの包括的なレポートを作成"""
    report = {}
    
    # 基本統計
    report['basic_stats'] = df[value_col].describe()
    
    # トレンド分析
    df['trend'] = df[value_col].rolling(window=30).mean()
    df['trend_change'] = df['trend'].pct_change(periods=30) * 100
    
    # 季節性分析
    monthly_avg = df.groupby(df.index.month)[value_col].mean()
    report['seasonal_pattern'] = monthly_avg
    
    # 曜日パターン
    dow_avg = df.groupby(df.index.dayofweek)[value_col].mean()
    report['day_of_week_pattern'] = dow_avg
    
    # 異常値検出（四分位範囲法）
    Q1 = df[value_col].quantile(0.25)
    Q3 = df[value_col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[value_col] < Q1 - 1.5 * IQR) | 
                  (df[value_col] > Q3 + 1.5 * IQR)]
    report['outliers_count'] = len(outliers)
    
    return report

# レポート作成
report = create_time_series_report(ts_data.copy(), 'sales')

print("時系列分析レポート:")
print("\n基本統計:")
print(report['basic_stats'])
print("\n月別平均売上:")
print(report['seasonal_pattern'])
print("\n曜日別平均売上:")
print(report['day_of_week_pattern'])
print(f"\n異常値の数: {report['outliers_count']}")

# 予測用のデータ準備（ラグ特徴量）
forecast_data = ts_data[['sales']].copy()
for lag in [1, 7, 30]:
    forecast_data[f'sales_lag{lag}'] = forecast_data['sales'].shift(lag)

forecast_data['month'] = forecast_data.index.month
forecast_data['dayofweek'] = forecast_data.index.dayofweek
forecast_data['is_weekend'] = forecast_data['dayofweek'].isin([5, 6]).astype(int)

print("\n予測用データ（最後の5行）:")
print(forecast_data.dropna().tail())

print("\n時系列データの処理の例を完了しました！")