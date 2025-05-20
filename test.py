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

with THSData() as td:
    # 获取集合竞价数据
    df = td.call_auction("USHA600519")
    df.to_csv("call_auction.csv", index=False)
    
    # 确保时间列为datetime类型
    df['time'] = pd.to_datetime(df['time'])
    
    # 创建样式更好的图表
    plt.style.use('ggplot')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True, gridspec_kw={'height_ratios': [2, 1]})
    
    # 第一个子图：价格走势
    line_price = ax1.plot(df['time'], df['price'], 'b-', linewidth=2.5, label='价格')
    ax1.set_ylabel('价格 (元)', fontsize=14, fontweight='bold')
    ax1.set_title('贵州茅台(600519)集合竞价数据', fontsize=16, fontweight='bold', pad=15)
    ax1.grid(True, linestyle='--', alpha=0.5)
    
    # 美化价格图
    ax1.fill_between(df['time'], df['price'].min(), df['price'], alpha=0.1, color='blue')
    
    # 添加最新价格辅助线和标签
    if not df.empty:
        last_price = df['price'].iloc[-1]
        first_price = df['price'].iloc[0]
        percent_change = (last_price - first_price) / first_price * 100
        
        color = 'red' if last_price >= first_price else 'green'
        
        ax1.axhline(y=last_price, color=color, linestyle='--', alpha=0.7, linewidth=1.5)
        ax1.text(df['time'].iloc[-1], last_price, 
                 f'最新: {last_price:.2f} ({percent_change:+.2f}%)', 
                 color=color, va='bottom', ha='right', fontweight='bold')
    
    # 第二个子图：成交量和买卖委托量
    volume_bars = ax2.bar(df['time'], df['live_vol'], width=np.timedelta64(20, 's'), 
              color='forestgreen', alpha=0.7, label='成交量')
    ax2.set_ylabel('成交量', fontsize=14, fontweight='bold')
    
    # 添加委托量信息（如果存在）
    if 'bid2_vol' in df.columns and 'ask2_vol' in df.columns:
        ax3 = ax2.twinx()
        bid_line = ax3.plot(df['time'], df['bid2_vol'], 'r-', linewidth=2, label='买二量')
        ask_line = ax3.plot(df['time'], df['ask2_vol'], 'b-', linewidth=2, label='卖二量')
        ax3.set_ylabel('委托量', fontsize=14, fontweight='bold')
        
        # 合并图例
        lines = line_price + bid_line + ask_line
        labels = [l.get_label() for l in lines]
        ax1.legend(lines, labels, loc='upper left', frameon=True, fontsize=12)
    else:
        ax1.legend(loc='upper left', frameon=True, fontsize=12)
    
    # 格式化X轴日期显示
    date_format = mdates.DateFormatter('%H:%M:%S')
    ax2.xaxis.set_major_formatter(date_format)
    ax2.xaxis.set_major_locator(mdates.MinuteLocator(interval=1))
    ax2.set_xlabel('时间', fontsize=14, fontweight='bold')
    
    # 旋转日期标签
    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')
    
    # 添加网格线
    ax2.grid(True, linestyle='--', alpha=0.5)
    
    # 紧凑布局
    fig.tight_layout()
    
    # 保存图片
    plt.savefig('maotai_call_auction.png', dpi=300, bbox_inches='tight')
    
    # 显示图形
    plt.show()

