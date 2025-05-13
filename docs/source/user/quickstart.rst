.. _quickstart:

快速开始
==========

下面是如何使用 `thsdata` 包的简单示例：

快速入门使用
--------------------

.. code-block:: python

        import thsdata as td

        data = td.download("USHA600519", start="2024-01-01", end="2025-01-01")
        print(data)





.. code-block:: text

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


证券代码查询
--------------------


.. code-block:: python

      from thsdata import Quote


      def main():
          # 初始化
          quote = Quote()
          quote.connect()

          try:
              data = quote.stock_codes()
              print(data)

          except Exception as e:
              print("An error occurred:", e)

          finally:
              # 断开连接
              quote.disconnect()
              print("Disconnected from the server.")


      if __name__ == "__main__":
          main()





.. code-block:: text

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
   Disconnected from the server.



quote查询日k数据
---------------

.. code-block:: python

        from thsdata import Quote

        def main():
            # 初始化
            quote = Quote()
            quote.connect()

            try:
                # print(quote.about())
                data = quote.download("USHA600519", count=100)
                print(data)

            except Exception as e:
                print("An error occurred:", e)

            finally:
                # 断开连接
                quote.disconnect()
                print("Disconnected from the server.")


        if __name__ == "__main__":
            main()






.. code-block:: text

              time     open     high      low    close   volume    turnover
    0   2024-12-09  1522.02  1529.72  1513.20  1518.80  1979986  3008173600
    1   2024-12-10  1570.00  1579.73  1545.18  1546.59  6031210  9421340700
    2   2024-12-11  1540.00  1555.00  1530.98  1535.60  2967112  4569662600
    3   2024-12-12  1532.02  1566.00  1529.00  1565.80  4193652  6510547800
    4   2024-12-13  1550.01  1554.99  1518.88  1519.00  4951197  7580908300
    ..         ...      ...      ...      ...      ...      ...         ...
    96  2025-05-07  1570.00  1570.00  1550.20  1555.00  2746221  4275142600
    97  2025-05-08  1553.00  1592.78  1549.83  1578.19  3348106  5265446400
    98  2025-05-09  1578.99  1597.45  1575.05  1591.18  2367190  3757574500
    99  2025-05-12  1598.00  1618.93  1596.61  1604.50  2473533  3967785800
    100 2025-05-13  1608.92  1608.92  1585.11  1590.78  1917953  3055813300

   [278 rows x 7 columns]
   Disconnected from the server.



行业概念查询
---------------

.. code-block:: python

        from thsdata import Quote

        def main():
            # 初始化
            quote = Quote()
            quote.connect()

            try:
                # print(quote.about())
                data = quote.ths_industry_block()
                print(data)

            except Exception as e:
                print("An error occurred:", e)

            finally:
                # 断开连接
                quote.disconnect()
                print("Disconnected from the server.")


        if __name__ == "__main__":
            main()






.. code-block:: text

              code   name
    0   URFI881165     综合
    1   URFI881171  自动化设备
    2   URFI881118   专用设备
    3   URFI881141     中药
    4   URFI881157     证券
    ..         ...    ...
    85  URFI881138   包装印刷
    86  URFI881121    半导体
    87  URFI881131   白色家电
    88  URFI881273     白酒
    89  URFI881271   IT服务

    [90 rows x 2 columns]
    Disconnected from the server.



问财查询
---------------

.. code-block:: python

        from thsdata import Quote

        def main():
            # 初始化
            quote = Quote()
            quote.connect()

            try:
                data = quote.wencai_base("所属概念;所属行业")
                print(data)

            except Exception as e:
                print("An error occurred:", e)

            finally:
                # 断开连接
                quote.disconnect()
                print("Disconnected from the server.")


        if __name__ == "__main__":
            main()



.. code-block:: text

                     code           所属同花顺行业                                        所属概念
        0     USZP300630    医药生物-化学制药-化学制剂                                           -
        1     USHA603110    基础化工-化学制品-涂料油墨     石墨烯;算力租赁;数据中心;PCB概念;东数西算(算力);DeepSeek概念
        2     USHA600085       医药生物-中药-中药Ⅲ       超级品牌;融资融券;流感;沪股通;国企改革;证金持股;DeepSeek概念
        3     USHA603477     农林牧渔-养殖业-生猪养殖        养鸡;比亚迪概念;融资融券;沪股通;西部大开发;猪肉;回购增持再贷款概念
        4     USHA688603   电子-电子化学品-电子化学品Ⅲ                        PCB概念;融资融券;先进封装;芯片概念
        ...          ...               ...                                         ...
        5412  USHT600287       商贸零售-贸易-贸易Ⅲ  参股保险;期货概念;参股券商;国企改革;参股银行;跨境电商;ST板块;人民币贬值受益
        5413  USHT605081    环保-环境治理-水务及水治理           污水处理;雄安新区;电子商务;乡村振兴;东数西算(算力);ST板块
        5414  USHT600608       商贸零售-贸易-贸易Ⅲ                                   ST板块;国企改革
        5415  USHT603559   通信-通信服务-通信工程及服务                      数据中心;5G;时空大数据;ST板块;云计算
        5416  USHT600381  食品饮料-食品加工制造-其他食品                             白酒概念;ST板块;西部大开发

        [5417 rows x 3 columns]
        Disconnected from the server.


