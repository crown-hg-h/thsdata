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
              data = quote.download("USHA600519")
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

              time     close    volume      turnover      open      high      low
    0    2001-08-27    35.550  40631800  1.410347e+09    34.509    37.780    32.85
    1    2001-08-28    36.860  12964700  4.634630e+08    34.990    37.000    34.61
    2    2001-08-29    36.380   5325200  1.946890e+08    36.980    37.000    36.10
    3    2001-08-30    37.100   4801300  1.775580e+08    36.280    37.509    36.00
    4    2001-08-31    37.009   2323100  8.623100e+07    37.150    37.620    36.80
    ...         ...       ...       ...           ...       ...       ...      ...
    5658 2025-04-16  1559.170   3115605  4.834881e+09  1552.000  1576.000  1537.00
    5659 2025-04-17  1570.000   2384605  3.733925e+09  1554.000  1576.500  1549.99
    5660 2025-04-18  1565.940   2029848  3.179974e+09  1566.000  1575.000  1556.00
    5661 2025-04-21  1551.000   1805703  2.808158e+09  1565.500  1565.500  1551.00
    5662 2025-04-22  1548.800   1843214  2.857526e+09  1550.000  1556.300  1543.21

   [278 rows x 7 columns]
   Disconnected from the server.

