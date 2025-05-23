.. thsdata documentation master file, created by
   sphinx-quickstart on Sat Mar  1 15:22:41 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Thsdata 文档说明
=====================


**Thsdata** 是基于Python开发的ths数据接口实现。

-------------------

**Python使用Thsdata**::

      >>> from thsdata import THSData
      >>> with THSData() as td:
      ...     data = td.download("600519", start=20240101, end=20250101)
      ...     print(data)
      ...
      Hello thsdk!
      2025-05-15 13:17:19,379 [INFO] thsdk.ths_api: Connected to THS server successfully
                time     open     high      low    close   volume    turnover
      0   2024-01-02  1715.00  1718.19  1678.10  1685.01  3215644  5440082500
      1   2024-01-03  1681.11  1695.22  1676.33  1694.00  2022929  3411400700
      2   2024-01-04  1693.00  1693.00  1662.93  1669.00  2155107  3603970100
      3   2024-01-05  1661.33  1678.66  1652.11  1663.36  2024286  3373155600
      4   2024-01-08  1661.00  1662.00  1640.01  1643.99  2558620  4211918600
      ..         ...      ...      ...      ...      ...      ...         ...
      237 2024-12-25  1538.80  1538.80  1526.10  1530.00  1712339  2621061900
      238 2024-12-26  1534.00  1538.78  1523.00  1527.79  1828651  2798840000
      239 2024-12-27  1528.90  1536.00  1519.50  1528.97  2075932  3170191400
      240 2024-12-30  1533.97  1543.96  1525.00  1525.00  2512982  3849542600
      241 2024-12-31  1525.40  1545.00  1522.01  1524.00  3935445  6033540400

      [242 rows x 7 columns]
      2025-05-15 13:17:19,661 [INFO] thsdk.ths_api: Disconnected from THS server


**Thsdata** 提供ths的查询金融数据和行情数据.基于thsdk上的二次开发.thanks to `thsdk <https://pypi.org/project/thsdk/>`_.


功能速阅
----------------

- 支持股票，可转债，基金市场行情数据
- 集合竞价数据，成交明细数据，分时数据
- 获取个股年，季度，月度，周度，日度，分钟行情数据
- 获取行业，概念，地域，板块行情数据
- 获取个股舆情监控
- 获取个股资金流向数据
- 获取个股财务数据
- 获取个股新闻数据
- 获取个股公告数据
- 获取个股研报数据
- 获取个股龙虎榜数据
- 获取个股大宗交易数据
- 权息资料


用户指南
--------------

这部分内容为安装于案例使用。

.. toctree::
   :maxdepth: 2

   user/install
   user/quickstart

API文档
-----------------------------

If you are looking for information on a specific function, class, or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 3

   api

声明
----------------
当前项目代码用于个人对网络协议的研究和习作，不对外提供服务，任何人使用本代码遇到问题请自行解决，也可以在github提issue给我，但是我不保证能即时处理。 由于我们连接的是既有的行情软件兼容行情服务器，机构请不要使用此代码，对此造成的任何问题本人概不负责。
