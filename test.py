from thsdata import THSData,Interval
from datetime import datetime, time

with THSData() as td:

    now = datetime.now()
    start = datetime.combine(now.date(), time(10, 15, 0))  # 10:15:00
    end = datetime.combine(now.date(), time(10, 25, 0))  # 10:25:00
    print(td.download("600519", start=start, end=end,interval=Interval.MIN_1))
    # print(td.download("600519", count=10,interval=Interval.MIN_1))