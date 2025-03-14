.. thsdata documentation master file, created by
   sphinx-quickstart on Sat Mar  1 15:22:41 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Thsdata 文档说明
=====================


**Thsdata** 是基于Python开发的ths数据接口实现。

-------------------

**Python使用Thsdata**::

      >>> from thsdata import Quote
      >>> quote = Quote()
      >>> quote.stock_codes()
      2025/03/14 09:11:30 Hello thsdk!
                  code   name
      0     USTM832566    梓橦宫
      1     USZA002346   柘中股份
      2     USZA002069    獐子岛
      3     USZA300181   佐力药业
      4     USZA003030   祖名股份
      ...          ...    ...
      5404  USZA300167  *ST迪威
      5405  USHT688282  *ST导航
      5406  USHT603963  *ST大药
      5407  USZA300301  *ST长方
      5408  USHT603363  *ST傲农

      [5409 rows x 2 columns]
      >>> quote.disconnect()


**Thsdata** 提供ths的查询金融数据和行情数据.基于thsdk上的二次开发.thanks to `thsdk <https://pypi.org/project/thsdk/>`_.


功能速阅
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
次代码用于个人对网络协议的研究和习作，不对外提供服务，任何人使用本代码遇到问题请自行解决，也可以在github提issue给我，但是我不保证能即时处理。 由于我们连接的是既有的行情软件兼容行情服务器，机构请不要使用次代码，对此造成的任何问题本人概不负责
