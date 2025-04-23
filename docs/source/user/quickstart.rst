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

              time    close   volume    turnover     open     high      low
    0   2024-01-02  1685.01  3215644  5440082500  1715.00  1718.19  1678.10
    1   2024-01-03  1694.00  2022929  3411400700  1681.11  1695.22  1676.33
    2   2024-01-04  1669.00  2155107  3603970100  1693.00  1693.00  1662.93
    3   2024-01-05  1663.36  2024286  3373155600  1661.33  1678.66  1652.11
    4   2024-01-08  1643.99  2558620  4211918600  1661.00  1662.00  1640.01
    ..         ...      ...      ...         ...      ...      ...      ...
    237 2024-12-25  1530.00  1712339  2621061900  1538.80  1538.80  1526.10
    238 2024-12-26  1527.79  1828651  2798840000  1534.00  1538.78  1523.00
    239 2024-12-27  1528.97  2075932  3170191400  1528.90  1536.00  1519.50
    240 2024-12-30  1525.00  2512982  3849542600  1533.97  1543.96  1525.00
    241 2024-12-31  1524.00  3935445  6033540400  1525.40  1545.00  1522.01

    [242 rows x 7 columns]


证券代码查询
--------------------


.. code-block:: python

      from thsdata import Quote


      def main():
          # 初始化
          quote = Quote()

          try:
              # quote.connect()
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

            try:
                # quote.connect()
                # print(quote.about())
                # data = quote.download("USHA600519")
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

              time    close   volume    turnover     open     high      low
    0   2024-11-21  1545.13  1826179  2810933500  1543.87  1548.99  1532.00
    1   2024-11-22  1507.82  3343611  5107289000  1541.15  1547.77  1507.82
    2   2024-11-25  1498.57  3318556  5011136200  1511.00  1532.00  1496.67
    3   2024-11-26  1509.00  2574479  3876886000  1498.57  1518.88  1488.88
    4   2024-11-27  1519.05  2593417  3927607800  1509.00  1522.15  1505.00
    ..         ...      ...      ...         ...      ...      ...      ...
    96  2025-04-16  1559.17  3115605  4834880600  1552.00  1576.00  1537.00
    97  2025-04-17  1570.00  2384605  3733925000  1554.00  1576.50  1549.99
    98  2025-04-18  1565.94  2029848  3179974300  1566.00  1575.00  1556.00
    99  2025-04-21  1551.00  1805703  2808158200  1565.50  1565.50  1551.00
    100 2025-04-22  1548.80  1843214  2857526000  1550.00  1556.30  1543.21

   [278 rows x 7 columns]
   Disconnected from the server.



行业概念查询
---------------

.. code-block:: python

        from thsdata import Quote

        def main():
            # 初始化
            quote = Quote()

            try:
                # quote.connect()
                # print(quote.about())
                # data = quote.download("USHA600519")
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

