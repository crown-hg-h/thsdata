from thsdata import THSData, Interval
from datetime import datetime, time, timedelta
import pandas as pd
import numpy as np

def analyze_weak_to_strong(df, code_name=""):
    """分析集合竞价数据，识别弱转强的股票模式"""
    # 确保时间列是datetime类型
    df['time'] = pd.to_datetime(df['time'])
    
    # 计算价格变化百分比
    df['price_change_pct'] = df['price'].pct_change() * 100
    
    # 计算成交量变化
    df['vol_change'] = df['live_vol'].diff()
    
    # 将数据分为前半段和后半段
    mid_point = len(df) // 2
    first_half = df.iloc[:mid_point]
    second_half = df.iloc[mid_point:]
    
    # 检查是否符合弱转强模式
    # 1. 初始价格走低 - 检查前半段是否整体下跌
    initial_price = df['price'].iloc[0]
    mid_price = df['price'].iloc[mid_point]
    final_price = df['price'].iloc[-1]
    
    price_initially_down = mid_price < initial_price
    
    # 2. 后半段成交量放大
    first_half_avg_vol = first_half['live_vol'].mean()
    second_half_avg_vol = second_half['live_vol'].mean()
    volume_increased = second_half_avg_vol > first_half_avg_vol * 3  # 成交量至少增加20%
    
    # 3. 后半段价格上升
    price_finally_up = final_price > mid_price
    
    # 判断是否符合弱转强模式
    is_weak_to_strong = price_initially_down and volume_increased and price_finally_up
    
    return is_weak_to_strong

def get_daily_return(td, code):
    """获取股票当日收益率"""
    try:
        # 获取当前市场数据
        market_data = td.stock_cur_market_data([code])
        if market_data.empty:
            print(f"无法获取 {code} 的市场数据")
            return None
        
        # 打印列名用于调试
        print(f"股票 {code} 市场数据列: {list(market_data.columns)}")
        
        # 直接检查涨跌幅字段是否存在
        # 常见可能的涨跌幅字段名
        possible_change_fields = ['涨跌幅', 'price_change_pct', 'change_pct', 'price_change_rate', 
                            'chg', 'change', 'change_rate', 'increase_rate']
        
        for field in possible_change_fields:
            if field in market_data.columns:
                return round(market_data[field].iloc[0], 2)
        
        # 如果没有直接的涨跌幅字段，检查是否有当前价和昨收价
        price_fields = {'当前价': ['price', 'last_price', 'close', '现价', '最新价', 'current_price']}
        pre_close_fields = {'昨收价': ['pre_close', 'previous_close', 'yesterday_close', '昨收', '昨日收盘价']}
        
        # 找到价格字段
        current_price = None
        for key, alternatives in price_fields.items():
            for field in [key] + alternatives:
                if field in market_data.columns:
                    current_price = market_data[field].iloc[0]
                    print(f"当前价格({field}): {current_price}")
                    break
            if current_price is not None:
                break
                
        # 找到昨收价字段
        pre_close = None
        for key, alternatives in pre_close_fields.items():
            for field in [key] + alternatives:
                if field in market_data.columns:
                    pre_close = market_data[field].iloc[0]
                    print(f"昨收价({field}): {pre_close}")
                    break
            if pre_close is not None:
                break
        
        # 计算涨跌幅
        if current_price is not None and pre_close is not None and pre_close != 0:
            return round((current_price / pre_close - 1) * 100, 2)
        
        print(f"无法计算 {code} 的涨跌幅：找不到必要字段")
        return None
    except Exception as e:
        print(f"获取 {code} 当日收益率时出错: {e}")
        return None

with THSData() as td:
    # 获取股票代码和名称映射
    stock_info = td.stock_codes()
    stock_name_map = dict(zip(stock_info['code'], stock_info['name']))
    
    # 获取集合竞价数据
    codes = list(td.wencai_select_codes("今日竞价抢筹，股价在5-20之间")[0])
    print(f"分析 {len(codes)} 只今日竞价弱转强股票的集合竞价数据")
    
    weak_to_strong_stocks = []
    
    for code in codes:
        stock_name = stock_name_map.get(code, code)
        
        # 排除ST股票, 科创板(688开头), 创业板(300开头), 北交所(8开头)
        if "ST" in stock_name or code.startswith(("688", "30", "8")):
            print(f"跳过 {code} {stock_name} (ST股或科创板/创业板/北交所)")
            continue
            
        print(f"分析 {code} {stock_name}")
        
        # 获取集合竞价数据
        df = td.call_auction(code)
        
        # 保存数据到CSV (只保存第一个股票的数据，避免覆盖)
        if code == codes[0]:
            df.to_csv("call_auction.csv", index=False)
        
        # 分析是否为弱转强模式
        is_weak_to_strong = analyze_weak_to_strong(df, f"{code} {stock_name}")
        
        if is_weak_to_strong:
            weak_to_strong_stocks.append((code, stock_name))
    
    # 输出弱转强股票列表
    if weak_to_strong_stocks:
        print(f"\n找到 {len(weak_to_strong_stocks)} 只符合弱转强模式的股票:")
        for code, name in weak_to_strong_stocks:
            print(f"{code} {name}")
        
        # 保存筛选出的股票到CSV表格
        result_data = []
        for code, name in weak_to_strong_stocks:
            # 提取股票代码中的6位数字
            numeric_code = ''.join(filter(str.isdigit, code))[-6:]
            # 再次确认不包含ST股票、科创板和创业板
            if "ST" in name or numeric_code.startswith(("688", "30")):
                continue
            result_data.append((numeric_code, name))
            
        df_result = pd.DataFrame(result_data, columns=['代码', '名称'])
        df_result['日期'] = datetime.now().strftime('%Y-%m-%d')
        df_result.to_csv("weak_to_strong_stocks.csv", index=False, encoding='utf-8-sig')
        print(f"已将筛选结果保存至 weak_to_strong_stocks.csv")
    else:
        print("\n没有找到符合弱转强模式的股票")
