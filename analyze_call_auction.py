import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

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
    volume_increased = second_half_avg_vol > first_half_avg_vol * 1.2  # 成交量至少增加20%
    
    # 3. 后半段价格上升
    price_finally_up = final_price > mid_price
    
    # 判断是否符合弱转强模式
    is_weak_to_strong = price_initially_down and volume_increased and price_finally_up
    
    # 找到价格最低点
    min_price_idx = df['price'].idxmin()
    min_price_time = df.loc[min_price_idx, 'time']
    min_price = df.loc[min_price_idx, 'price']
    
    # 可视化分析结果
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    
    # 价格图
    ax1.plot(df['time'], df['price'], 'b-', linewidth=2)
    ax1.set_title(f'{code_name}集合竞价价格走势' if code_name else '集合竞价价格走势')
    ax1.set_ylabel('价格')
    ax1.axvline(df['time'].iloc[mid_point], color='red', linestyle='--', alpha=0.5, label='数据中点')
    ax1.scatter(min_price_time, min_price, color='red', s=100, marker='v', label='最低价格点')
    ax1.grid(True)
    ax1.legend()
    
    # 成交量图
    ax2.bar(df['time'], df['live_vol'], color='g', alpha=0.6)
    ax2.set_title('成交量')
    ax2.set_ylabel('成交量')
    ax2.set_xlabel('时间')
    ax2.axvline(df['time'].iloc[mid_point], color='red', linestyle='--', alpha=0.5)
    ax2.axvline(min_price_time, color='red', alpha=0.5)
    ax2.grid(True)
    
    # 格式化x轴时间
    fmt = mdates.DateFormatter('%H:%M:%S')
    ax2.xaxis.set_major_formatter(fmt)
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    
    # 显示分析结果
    result_text = f"弱转强分析结果:\n"
    result_text += f"初始价格: {initial_price}, 中间价格: {mid_price}, 最终价格: {final_price}\n"
    result_text += f"初始价格下跌: {'是' if price_initially_down else '否'}\n"
    result_text += f"前半段平均成交量: {first_half_avg_vol:.2f}, 后半段平均成交量: {second_half_avg_vol:.2f}\n"
    result_text += f"成交量增加: {'是' if volume_increased else '否'}\n"
    result_text += f"后期价格上升: {'是' if price_finally_up else '否'}\n"
    result_text += f"综合判断-弱转强: {'是' if is_weak_to_strong else '否'}"
    
    # 如果价格存在明显的"V"形反转，标记出来
    if min_price_idx > 0 and min_price_idx < len(df) - 1:
        # 计算从最低点到结束的上涨幅度
        recovery_pct = (final_price - min_price) / min_price * 100
        result_text += f"\n\n最低价格点: {min_price}元 (时间: {min_price_time.strftime('%H:%M:%S')})"
        result_text += f"\n最低点到结束上涨幅度: {recovery_pct:.2f}%"
    
    plt.figtext(0.5, 0.01, result_text, ha='center', bbox={'facecolor': 'yellow', 'alpha': 0.5, 'pad': 5})
    
    return is_weak_to_strong, fig, result_text

# 主程序
if __name__ == "__main__":
    print("分析call_auction.csv数据...")
    try:
        # 读取数据
        df = pd.read_csv("call_auction.csv")
        
        # 打印基本数据信息
        print(f"数据点数量: {len(df)}")
        print(f"开始时间: {df['time'].iloc[0]}")
        print(f"结束时间: {df['time'].iloc[-1]}")
        print(f"起始价格: {df['price'].iloc[0]}")
        print(f"结束价格: {df['price'].iloc[-1]}")
        print(f"价格变化: {df['price'].iloc[-1] - df['price'].iloc[0]}")
        print(f"价格变化百分比: {(df['price'].iloc[-1] / df['price'].iloc[0] - 1) * 100:.2f}%")
        
        # 进行弱转强分析
        is_weak_to_strong, fig, result_text = analyze_weak_to_strong(df, "集合竞价分析")
        
        # 打印详细结果
        print("\n" + result_text.replace("\n\n", "\n"))
        
        # 保存并显示图表
        plt.savefig("call_auction_analysis.png")
        plt.show()
        
    except Exception as e:
        print(f"分析失败: {e}") 