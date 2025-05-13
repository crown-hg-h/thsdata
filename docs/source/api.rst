.. _api:

API文档
===================
.. module:: thsdata

本部分文档涵盖了 Thsdata 的所有接口。对于 Thsdata 依赖外部库的部分，我们在此记录了最重要的部分，并提供了规范文档的链接。


导出历史
--------------------

.. autofunction:: thsdata.download


基础数据
--------------------

.. automethod:: thsdata.THSData.stock_codes
.. automethod:: thsdata.THSData.conbond_codes
.. automethod:: thsdata.THSData.etf_codes


行业概念板块
--------------------

.. automethod:: thsdata.THSData.ths_industry_block
.. automethod:: thsdata.THSData.ths_industry_sub_block
.. automethod:: thsdata.THSData.ths_concept_block
.. automethod:: thsdata.THSData.ths_block_components


行情数据
--------------------

.. automethod:: thsdata.THSData.download
.. automethod:: thsdata.THSData.security_bars
.. automethod:: thsdata.THSData.call_auction
.. automethod:: thsdata.THSData.corporate_action
.. automethod:: thsdata.THSData.order_book
.. automethod:: thsdata.THSData.transaction_history
.. automethod:: thsdata.THSData.stock_cur_market_data
.. automethod:: thsdata.THSData.conbond_cur_market_data


特色数据
--------------------
.. automethod:: thsdata.THSData.wencai_select_codes
.. automethod:: thsdata.THSData.wencai_base
.. automethod:: thsdata.THSData.attention
.. automethod:: thsdata.THSData.getshape