from thsdk import ZhuThsQuote, FuThsQuote, InfoThsQuote, BlockThsQuote
from thsdk.constants import *
import pandas as pd
import datetime


class Quote:
    def __init__(self, ops: dict = None):
        self.ops = ops
        self._zhuQuote = None
        self._fuQuote = None
        self._infoQuote = None
        self._blockQuote = None

    @property
    def zhuQuote(self):
        if self._zhuQuote is None:
            self._zhuQuote = ZhuThsQuote(self.ops)
            self._zhuQuote.connect()
        return self._zhuQuote

    @property
    def fuQuote(self):
        if self._fuQuote is None:
            self._fuQuote = FuThsQuote(self.ops)
            self._fuQuote.connect()
        return self._fuQuote

    @property
    def infoQuote(self):
        if self._infoQuote is None:
            self._infoQuote = InfoThsQuote(self.ops)
            self._infoQuote.connect()
        return self._infoQuote

    @property
    def blockQuote(self):
        if self._blockQuote is None:
            self._blockQuote = BlockThsQuote(self.ops)
            self._blockQuote.connect()
        return self._blockQuote

    def connect(self):
        self.zhuQuote.connect()
        self.fuQuote.connect()
        self.infoQuote.connect()
        self.blockQuote.connect()

    def disconnect(self):
        if self._zhuQuote:
            self._zhuQuote.disconnect()
        if self._fuQuote:
            self._fuQuote.disconnect()
        if self._infoQuote:
            self._infoQuote.disconnect()
        if self._blockQuote:
            self._blockQuote.disconnect()

    def _block_data(self, block_id: int):
        reply = self.blockQuote.get_block_data(block_id)
        if reply.err_code != 0:
            print(f"查询错误:{reply.err_code}, 信息:{reply.err_message}")
            return
        resp = reply.resp
        df = pd.DataFrame(resp.data)
        return df

    def stock_codes(self):
        """
        获取股票市场代码

        :return: DataFrame

            - **code** (str): 代码，格式为市场标识+数字
            - **name** (str): 名称

            示例::

                code        name
                USHA600519  贵州茅台
                USZA300750  宁德时代
                USTM832566    梓橦宫
        """
        return self._block_data(0xC6A6)

    def cbond_codes(self):
        """
        获取可转债市场代码
         :return: DataFrame

            - **code** (str): 代码，格式为市场标识+数字
            - **name** (str): 名称

            示例::

                code        name
                USHD113037   紫银转债
                USZD123158   宙邦转债
                USHD110094   众和转债
        """
        return self._block_data(0xCE14)

    def etf_codes(self):
        """
        获取ETF基金市场代码
         :return: DataFrame

            - **code** (str): 代码，格式为市场标识+数字
            - **name** (str): 名称

            示例::

                code        name
                USHJ589660       综指科创
                USZJ159201   自由现金流ETF
                USHJ510410      资源ETF
        """
        return self._block_data(0xCFF3)

    def security_bars_daily(self, code: str, start: datetime.datetime, end: datetime.datetime, adjust: str):
        """
        获取指定证券的日K线数据

        :param code: 证券代码，例如 'USHA600619'
        :type code: str
        :param start: 开始时间，格式为 datetime 对象
        :type start: datetime.datetime
        :param end: 结束时间，格式为 datetime 对象
        :type end: datetime.datetime
        :param adjust: 调整类型，例如 'Q'（前复权）、'B'（后复权）或 ''（不复权） Fuquanqian/Fuquanhou/FuquanNo
        :type adjust: str
        :return: pandas.DataFrame

            示例::

                        time    close   volume    turnover     open     high      low
                0   2024-01-02  1685.01  3215644  5440082500  1715.00  1718.19  1678.10
                1   2024-01-03  1694.00  2022929  3411400700  1681.11  1695.22  1676.33
                2   2024-01-04  1669.00  2155107  3603970100  1693.00  1693.00  1662.93
        """
        start_int = int(start.strftime('%Y%m%d'))
        end_int = int(end.strftime('%Y%m%d'))

        reply = self.zhuQuote.security_bars(code, start_int, end_int, adjust, KlineDay)
        if reply.err_code != 0:
            print(f"查询错误:{reply.err_code}, 信息:{reply.err_message}")
            return

        resp = reply.resp
        return pd.DataFrame(resp.data)
