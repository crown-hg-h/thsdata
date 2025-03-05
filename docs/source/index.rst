.. thsdata documentation master file, created by
   sphinx-quickstart on Sat Mar  1 15:22:41 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Thsdata documentation
=====================


**Thsdata** is a Python library designed for querying and retrieving financial data.

-------------------

**Behold, the power of Requests**::

      >>> from thsdata import Quote
      >>> quote = Quote()
      >>> quote.stock_codes()
      2025/03/05 08:13:48 hello thsdata!
            code   name
      0     USTM832566    梓橦宫
      1     USZA002346   柘中股份
      2     USZA002069    獐子岛
      3     USZA300181   佐力药业
      4     USZA003030   祖名股份
      ...          ...    ...
      5399  USHT688282  *ST导航
      5400  USHT603963  *ST大药
      5401  USZA300301  *ST长方
      5402  USHT600083  *ST博信
      5403  USHT603363  *ST傲农
      [5404 rows x 2 columns]
      >>> quote.disconnect()


**Thsdata** provides an easy-to-use interface for accessing a wide range of financial information, including stock prices, market indices, historical data, and more. Whether you're a developer, data analyst, or financial researcher, Thsdata simplifies the process of integrating financial data into your applications or analyses.thanks to `thsdk <https://pypi.org/project/thsdata/>`_.


Beloved Features
----------------

- 支持股票，可转债，基金市场行情数据
- 集合竞价数据，成交明细数据，分时数据
- 获取个股年，季度，月度，周度，日度，分钟行情数据
- 获取同花顺行业，同花顺概念，同花顺地域，同花顺板块行情数据
- 获取个股资金流向数据
- 获取个股财务数据
- 获取个股新闻数据
- 获取个股公告数据
- 获取个股研报数据
- 获取个股龙虎榜数据
- 获取个股大宗交易数据


The User Guide
--------------

This part of the documentation, which is mostly prose, begins with some
background information about Requests, then focuses on step-by-step
instructions for getting the most out of Requests.

.. toctree::
   :maxdepth: 2

   user/install
   user/quickstart

The API Documentation / Guide
-----------------------------

If you are looking for information on a specific function, class, or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 3

   api