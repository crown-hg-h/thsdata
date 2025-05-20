import pandas as pd
import tushare as ts
import datetime

# Set up tushare token - you need to replace this with your own token
token = '2876ea85cb005fb5fa17c809a98174f2d5aae8b1f830110a5ead6211'
ts.set_token(token)
pro = ts.pro_api()

# Read the stock list from CSV file, ensuring codes are read as strings
df_stocks = pd.read_csv('weak_to_strong_stocks.csv', encoding='utf-8', dtype={'代码': str})

# Get today's date
today = datetime.datetime.now().strftime('%Y%m%d')

# Initialize results dataframe
results = []

# Process each stock
for index, row in df_stocks.iterrows():
    stock_code = row['代码']
    stock_name = row['名称']
    
    # Format stock code for tushare (add market prefix)
    if stock_code.startswith('6'):
        ts_code = f"{stock_code}.SH"
    else:
        ts_code = f"{stock_code}.SZ"
    
    try:
        # Get daily data
        df = pro.daily(ts_code=ts_code, trade_date=today)
        
        if not df.empty:
            # Calculate return rate: (close - open) / open
            open_price = df['open'].values[0]
            close_price = df['close'].values[0]
            return_rate = (close_price - open_price) / open_price * 100
            
            results.append({
                '代码': stock_code,
                '名称': stock_name,
                '开盘价': open_price,
                '收盘价': close_price,
                '收益率(%)': round(return_rate, 2)
            })
            print(f"处理 {stock_name}({stock_code}) 完成, 收益率: {round(return_rate, 2)}%")
        else:
            print(f"未找到 {stock_name}({stock_code}) 的数据")
            
    except Exception as e:
        print(f"处理 {stock_name}({stock_code}) 时出错: {e}")

# Create results dataframe and sort by return rate
if results:
    df_results = pd.DataFrame(results)
    df_results = df_results.sort_values(by='收益率(%)', ascending=False)
    
    # Save to CSV
    result_filename = f"收益率统计_{today}.csv"
    df_results.to_csv(result_filename, index=False, encoding='utf-8-sig')
    print(f"\n结果已保存至 {result_filename}")
    
    # Display top 5 and bottom 5
    print("\n收益率最高的5只股票:")
    print(df_results.head(5))
    
    print("\n收益率最低的5只股票:")
    print(df_results.tail(5))
else:
    print("没有获取到任何股票数据")
