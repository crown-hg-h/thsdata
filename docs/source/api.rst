.. _api:

Developer Interface
===================
.. module:: thsdata

This part of the documentation covers all the interfaces of Thsdata. For
parts where Thsdata depends on external libraries, we document the most
important right here and provide links to the canonical documentation.


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

