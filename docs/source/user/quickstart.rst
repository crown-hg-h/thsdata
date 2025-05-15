.. _quickstart:

快速开始
==========

下面是如何使用 `thsdata` 包的简单示例：

快速入门使用
--------------------

.. code-block:: python

        from thsdata import THSData

        with THSData() as td:
            data = td.download("600519", start=20240101, end=20250101)
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

      from thsdata import THSData

      with THSData() as td:
        data = td.stock_codes()
        print(data)




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



查询日k数据
---------------

.. code-block:: python

        from thsdata import THSData

        with THSData() as td:
            data = td.download("USHA600519", count=100)
            print(data)





.. code-block:: text

                  time     open     high      low    close   volume    turnover
        0   2024-12-11  1540.00  1555.00  1530.98  1535.60  2967112  4569662600
        1   2024-12-12  1532.02  1566.00  1529.00  1565.80  4193652  6510547800
        2   2024-12-13  1550.01  1554.99  1518.88  1519.00  4951197  7580908300
        3   2024-12-16  1521.00  1529.00  1510.71  1527.20  3253710  4945298800
        4   2024-12-17  1525.99  1569.00  1521.01  1558.00  5417163  8398945400
        ..         ...      ...      ...      ...      ...      ...         ...
        96  2025-05-09  1578.99  1597.45  1575.05  1591.18  2367190  3757574500
        97  2025-05-12  1598.00  1618.93  1596.61  1604.50  2473533  3967785800
        98  2025-05-13  1608.92  1608.92  1585.11  1590.30  2125829  3386617800
        99  2025-05-14  1590.00  1645.00  1588.18  1634.99  3946012  6394735100
        100 2025-05-15  1634.80  1643.59  1624.13  1634.04  1750022  2861327900

        [101 rows x 7 columns]



行业概念查询
---------------

.. code-block:: python

        from thsdata import THSData

        with THSData() as td:
            data = td.ths_industry_block()
            print(data)





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


行业成份股案例
---------------

.. code-block:: python

        import pandas as pd
        from thsdata import THSData

        with THSData() as td:
            result = td.ths_industry_block()
            if not result.empty:
                formatted_data = []  # List to store formatted rows

                for _, row in result.iterrows():
                    block_code = row['code']  # Get the block code
                    block_name = row['name']  # Get the block name
                    components = td.ths_block_components(block_code)  # Get components for the block
                    if not components.empty:
                        stock_codes = components['code'].tolist()  # Extract stock codes as a list
                        formatted_data.append({
                            'block_code': block_code,
                            'block_name': block_name,
                            'components': stock_codes
                        })

                    print(block_code, block_name,f"成份数量:{len(components)}")

                # Convert to DataFrame and save to CSV
                formatted_df = pd.DataFrame(formatted_data)
                formatted_df.to_csv('all_block_components.csv', index=False, encoding='utf-8')
                print("All block components saved to 'all_block_components.csv'.")
            else:
                print("No industry block data found.")





.. code-block:: text

    URFI881165 综合 成份数量:22
    URFI881171 自动化设备 成份数量:92
    URFI881118 专用设备 成份数量:191
    URFI881141 中药 成份数量:71
    ...
    URFI881156 保险 成份数量:6
    URFI881138 包装印刷 成份数量:46
    URFI881121 半导体 成份数量:160
    URFI881131 白色家电 成份数量:43
    URFI881273 白酒 成份数量:20
    URFI881271 IT服务 成份数量:126
    All block components saved to 'all_block_components.csv'.



问财查询
---------------

.. code-block:: python

        from thsdata import THSData

        with THSData() as td:
            data = td.wencai_base("所属概念;所属行业")
            print(data)



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


问财NLP
---------------

.. code-block:: python

        from thsdata import THSData

        def main():
            # 初始化
            td = THSData()
            td.connect()

            try:
                data = td.wencai_nlp("涨停;涨停原因")
                print(data)

            except Exception as e:
                print("An error occurred:", e)

            finally:
                # 断开连接
                td.disconnect()
                print("Disconnected from the server.")


        if __name__ == "__main__":
            main()



.. code-block:: text

              最新价         最新涨跌幅 涨停[20250514]      涨停原因类别[20250514]       股票代码   股票简称
        0     6.1   4.991394148           涨停                    其它  600421.SH  *ST华嵘
        1   19.54   4.997313272           涨停                    其它  603261.SH  *ST立航
        2     3.7  10.119047619           涨停          港口航运+一带一路+国企  600798.SH   宁波海运
        3    3.74   5.056179775           涨停                    其它  000638.SZ  *ST万方
        4     8.6   9.974424552           涨停                    其它  002774.SZ   快意电梯
        5    6.92  10.015898251           涨停   涂料+有机硅胶粘剂+跨境电商+一带一路  002909.SZ   集泰股份
        6    6.82            10           涨停                  None  600530.SH   交大昂立
        7    3.02   4.861111111           涨停                    其它  002141.SZ  *ST贤丰
        8   10.68   9.989701339           涨停                    其它  600410.SH   华胜天成
        9   70.56            20           涨停                    其它  300946.SZ    恒而达
        10  14.36  10.038314176           涨停         涤纶+化学纤维+一季报增长  603332.SH   苏州龙杰
        11  11.89   9.990749306           涨停      航空零部件+大飞机+军工+机器人  002651.SZ   利君股份
        12   2.08  10.052910053           涨停        PTA+瓶级聚酯切片+低价股  600370.SH    三房巷
        13   3.03   4.844290657           涨停                  None  000889.SZ   ST中嘉
        14  52.01  10.004230118           涨停  半导体光掩膜版+国产替代+半导体显示器件  605588.SH   冠石科技
        15   9.63  10.057142857           涨停                    其它  002383.SZ   合众思壮
        16   4.39  10.025062657           涨停          出口美国+外销+医疗器械  002551.SZ   尚荣医疗
        17   4.51            10           涨停       拟取得吉莱微控制权+功率半导体  600770.SH   综艺股份
        18  29.66  10.014836795           涨停    成飞概念+军工+汽车零部件+国企改革  002190.SZ   成飞集成
        19   3.69  10.149253731           涨停                    其它  002421.SZ   达实智能
        20  10.44  10.010537408           涨停                    其它  603803.SH   瑞斯康达
        21   3.81   4.958677686           涨停                    其它  603959.SH   ST百利
        22  29.16   9.996227839           涨停                    其它  002943.SZ   宇晶股份
        23  12.68   4.966887417           涨停                    其它  002289.SZ  *ST宇顺
        24  10.11  10.010881393           涨停            航运+海洋+浙江国资  601022.SH   宁波远洋
        25   1.48   4.964539007           涨停                  None  600568.SH   ST中珠
        26   8.61             5           涨停                    其它  603389.SH  *ST亚振
        27   7.81            10           涨停                  None  002427.SZ   尤夫股份
        28  18.34  10.017996401           涨停                  None  002809.SZ   红墙股份
        29  10.07  10.054644809           涨停           军工+特种电源+钨合金  000576.SZ   甘化科工
        30  10.33  10.010649627           涨停                  None  002136.SZ    安纳达
        31   8.45  10.026041667           涨停                  None  002040.SZ    南京港
        32   8.12   5.045278137           涨停                    其它  002650.SZ   ST加加


