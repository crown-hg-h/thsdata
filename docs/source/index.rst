.. thsdata documentation master file, created by
   sphinx-quickstart on Sat Mar  1 15:22:41 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

thsdata documentation
=====================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction
   installation
   usage/quickstart
   api

Introduction
============

Welcome to the `thsdata` documentation. This package provides tools to interact with the `thsdata` API, allowing you to retrieve and analyze financial data.

Features:

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


Installation
============

To install the package, use pip:

.. code-block:: bash

   pip install --upgrade thsdata

Usage
=====

Quickstart
----------

Here is a quick example of how to use the `thsdata` package:

.. code-block:: python

   from thsdata import ZhuThsQuote, FuquanNo, KlineDay
   import pandas as pd


   def main():
       # 初始化
       quote = ZhuThsQuote()

       try:
           # 连接到行情服务器
           login_reply = quote.connect()
           if login_reply.err_code != 0:
               print(f"登录错误:{login_reply.err_code}, 信息:{login_reply.err_message}")
               return
           else:
               print("Connected to the server.")

           # 获取历史日级别数据
           reply = quote.security_bars("USHA600519", 20240101, 20250228, FuquanNo, KlineDay)

           if reply.err_code != 0:
               print(f"查询错误:{reply.err_code}, 信息:{reply.err_message}")
               return

           resp = reply.resp
           df = pd.DataFrame(resp.data)
           print(df)

           print("查询成功 数量:", len(resp.data))

       except Exception as e:
           print("An error occurred:", e)

       finally:
           # 断开连接
           quote.disconnect()
           print("Disconnected from the server.")


   if __name__ == "__main__":
       main()


Output
------

.. code-block:: text

   Connected to the server.
             time    close   volume    turnover     open     high      low
   0   2024-01-02  1685.01  3215644  5440082500  1715.00  1718.19  1678.10
   1   2024-01-03  1694.00  2022929  3411400700  1681.11  1695.22  1676.33
   2   2024-01-04  1669.00  2155107  3603970100  1693.00  1693.00  1662.93
   3   2024-01-05  1663.36  2024286  3373155600  1661.33  1678.66  1652.11
   4   2024-01-08  1643.99  2558620  4211918600  1661.00  1662.00  1640.01
   ..         ...      ...      ...         ...      ...      ...      ...
   273 2025-02-24  1479.07  3474373  5157907300  1488.00  1499.52  1474.00
   274 2025-02-25  1454.00  2838743  4142814500  1470.01  1473.39  1452.00
   275 2025-02-26  1460.01  2636609  3835949000  1455.45  1464.96  1445.00
   276 2025-02-27  1485.56  4976217  7368002400  1460.02  1489.90  1454.00
   277 2025-02-28  1500.79  5612895  8475738200  1485.50  1528.38  1482.00

   [278 rows x 7 columns]
   查询成功 数量: 278
   Disconnected from the server.

API
===

The `thsdata` package provides the following modules and functions:

.. automodule:: thsdata
   :members:
   :undoc-members:
   :show-inheritance: