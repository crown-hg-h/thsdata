from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from thsdata import THSData, Interval
from datetime import datetime, time
import pandas as pd
import numpy as np
import matplotlib as mpl

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

def analyze_call_auction(df):
    # 计算价格变化率
    df['price_change'] = df['price'].pct_change()
    
    # 将数据分为前期和后期（以9:20为分界点）
    early_period = df[df['time'].dt.time < time(9, 20)]
    late_period = df[df['time'].dt.time >= time(9, 20)]
    
    # 计算前后期成交量比值
    early_volume_sum = early_period['live_vol'].sum() if len(early_period) > 0 else 1
    late_volume_sum = late_period['live_vol'].sum() if len(late_period) > 0 else 0
    volume_ratio = late_volume_sum / early_volume_sum if early_volume_sum > 0 else 0
    
    # 判断条件
    conditions = {
        '前期下跌': early_period['price_change'].mean() < 0,
        '后期上涨': late_period['price_change'].mean() > 0,
        '弱转强': early_period['price_change'].mean() < late_period['price_change'].mean()
    }
    
    # 返回结果
    results = {
        '前期下跌': conditions['前期下跌'],
        '后期上涨': conditions['后期上涨'],
        '成交量比值': volume_ratio,
        '弱转强': conditions['弱转强']
    }
    
    return results

# 判断是否为ST股票
def is_st_stock(stock_name):
    return 'ST' in stock_name or 'st' in stock_name or '*' in stock_name

# 判断是否为科创板或创业板
def is_special_board(code):
    # 科创板以688开头
    if code[4:7] == '688':
        return True
    # 创业板以300开头
    if code[4:7] == '300':
        return True
    return False

# 创建结果DataFrame
results_df = pd.DataFrame(columns=['股票代码', '股票名称', '今日收益率', '前期下跌', '后期上涨', '成交量比值', '弱转强'])

try:
    with THSData() as td:
        # 获取集合竞价数据，排除ST、科创板和创业板
        try:
            codes = list(td.wencai_select_codes("今日竞价抢筹,高开板块，非ST，非科创板，非创业板")[0])
            print("获取到的股票代码:", codes)
        except Exception as e:
            print(f"获取股票代码时出错: {e}")
            codes = []
        
        try:
            # 获取沪深股票代码和名称映射
            stock_info = td.stock_codes()
            stock_dict = dict(zip(stock_info['code'], stock_info['name']))
        except Exception as e:
            print(f"获取股票信息时出错: {e}")
            stock_dict = {}
        
        # 获取当前日期
        today = datetime.now()
        
        for code in codes:
            try:
                # 获取股票名称
                stock_name = stock_dict.get(code, "未知")
                
                # 跳过ST股票
                if is_st_stock(stock_name):
                    print(f"跳过ST股票: {code} ({stock_name})")
                    continue
                    
                # 跳过科创板和创业板股票
                if is_special_board(code):
                    print(f"跳过科创板/创业板股票: {code} ({stock_name})")
                    continue
                
                # 获取今日收益率
                today_return_rate = 0.0
                try:
                    # 获取今日K线数据
                    start_date = datetime(today.year, today.month, today.day)
                    end_date = datetime(today.year, today.month, today.day, 23, 59, 59)
                    today_data = td.security_bars(code, start_date, end_date, "", Interval.DAY)
                    
                    if not today_data.empty:
                        # 计算收益率 = (收盘价 - 开盘价) / 开盘价
                        today_return_rate = (today_data['close'].iloc[0] - today_data['open'].iloc[0]) / today_data['open'].iloc[0] * 100
                    else:
                        # 如果无法获取日K线，尝试使用当前市场数据
                        market_data = td.stock_cur_market_data([code])
                        if not market_data.empty and 'price' in market_data.columns and 'open' in market_data.columns:
                            open_price = market_data['open'].iloc[0]
                            if open_price > 0:
                                today_return_rate = (market_data['price'].iloc[0] - open_price) / open_price * 100
                except Exception as e:
                    print(f"获取 {code} 今日收益率时出错: {e}")
                
                # 获取集合竞价数据
                try:
                    df = td.call_auction(code)
                    if df.empty:
                        print(f"股票 {code} 无集合竞价数据，跳过")
                        continue
                        
                    # 将时间列转换为datetime类型
                    df['time'] = pd.to_datetime(df['time'])
                    
                    # 分析集合竞价数据
                    results = analyze_call_auction(df)
                    
                    # 打印分析结果
                    print(f"\n股票代码: {code} ({stock_name})")
                    print(f"今日收益率: {today_return_rate:.2f}%")
                    print("分析结果:")
                    for key, value in results.items():
                        print(f"{key}: {value}")
                    
                    # 将结果添加到DataFrame
                    results_df = pd.concat([results_df, pd.DataFrame({
                        '股票代码': [code],
                        '股票名称': [stock_name],
                        '今日收益率': [today_return_rate],
                        '前期下跌': [results['前期下跌']],
                        '后期上涨': [results['后期上涨']],
                        '成交量比值': [results['成交量比值']],
                        '弱转强': [results['弱转强']]
                    })], ignore_index=True)
                except Exception as e:
                    print(f"处理 {code} 集合竞价数据时出错: {e}")
                    continue
            except Exception as e:
                print(f"处理股票 {code} 时出错: {e}")
                continue
        
        try:
            # 组合筛选条件：弱转强、前期下跌和后期上涨
            filtered_stocks = results_df[
                (results_df['弱转强'] == True) & 
                (results_df['前期下跌'] == True) & 
                (results_df['后期上涨'] == True)
            ]
            
            # 按照成交量比值从高到低排序
            filtered_stocks = filtered_stocks.sort_values(by='成交量比值', ascending=False)
            
            # 保存筛选后的结果
            filtered_stocks.to_csv("weak_to_strong_stocks.csv", index=False, encoding='utf-8-sig')
            print(f"\n筛选结果：共找到 {len(filtered_stocks)} 只符合条件的股票")
            print("结果已保存到 weak_to_strong_stocks.csv")
            print("结果已按照成交量比值从高到低排序")
        except Exception as e:
            print(f"筛选和保存结果时出错: {e}")
except Exception as e:
    print(f"程序运行时发生错误: {e}")
 