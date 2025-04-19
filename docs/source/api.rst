.. _api:

API文档
===================
.. module:: thsdata

本部分文档涵盖了 Thsdata 的所有接口。对于 Thsdata 依赖外部库的部分，我们在此记录了最重要的部分，并提供了规范文档的链接。


基础数据
--------------------

.. automethod:: thsdata.Quote.stock_codes
.. automethod:: thsdata.Quote.cbond_codes
.. automethod:: thsdata.Quote.etf_codes


行业概念板块
--------------------

.. automethod:: thsdata.Quote.ths_industry_block
.. automethod:: thsdata.Quote.ths_industry_sub_block
.. automethod:: thsdata.Quote.ths_concept_block
.. automethod:: thsdata.Quote.ths_block_components


行情数据
--------------------

.. automethod:: thsdata.Quote.security_bars
.. automethod:: thsdata.Quote.call_auction
.. automethod:: thsdata.Quote.corporate_action
.. automethod:: thsdata.Quote.level5_order_book
.. automethod:: thsdata.Quote.transaction_history
.. automethod:: thsdata.Quote.stock_cur_market_data
.. automethod:: thsdata.Quote.cbond_cur_market_data


特色数据
--------------------
.. automethod:: thsdata.Quote.wencai