.. thsdata documentation master file, created by
   sphinx-quickstart on Sat Mar  1 15:22:41 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

data documentation
=====================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage/quickstart

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

   from thsdata import BlockThsQuote

   def main():
       quote = BlockThsQuote()
       login_reply = quote.connect()
       if login_reply.err_code != 0:
           print(f"Login error: {login_reply.err_code}, message: {login_reply.err_message}")
           return
       reply = quote.get_block_data(0xCE5F)
       if reply.err_code != 0:
           print(f"Query error: {reply.err_code}, message: {reply.err_message}")
           return
       df = pd.DataFrame(reply.resp.data)
       print(df)
       quote.disconnect()

   if __name__ == "__main__":
       main()