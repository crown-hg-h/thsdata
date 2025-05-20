from matplotlib import pyplot as plt
from thsdata import THSData,Interval
from datetime import datetime, time

import pandas as pd
with THSData() as td:
    df = td.call_auction("USHA600519")
    df.to_csv("call_auction.csv", index=False)
    df.plot(x="time", y="price", kind="line")
    plt.show()

