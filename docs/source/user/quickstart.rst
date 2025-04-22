.. _quickstart:

快速开始
==========

下面是如何使用 `thsdata` 包的简单示例：


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



日k数据查询
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

