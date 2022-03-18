import os

directory = os.getcwd()

# PATHS
customer_path = f"{directory}\datasets\dateset_1\customer.tbl\customer.tbl"
orders_path = f"{directory}\datasets\dateset_1\orders.tbl\orders.tbl"
lineitem_path = f"{directory}\datasets\dateset_1\lineitem.tbl\lineitem.tbl"
query_example_path = f"{directory}\datasets\dateset_1\query_example.txt"

# COLUMNS
customer_columns = ['CUSTKEY', 'NAME',
                    'ADDRESS', 'NATIONKEY', 'PHONE', 'ACCTBAL', 'MKTSEGMENT', 'COMMENT']
lineitem_columns = ['ORDERKEY', 'PARTKEY', 'SUPPKEY', 'LINENUMBER', 'QUANTITY', 'EXTENDEDPRICE', 'DISCOUNT', 'TAX',
                    'RETURNFLAG', 'LINESTATUS', 'SHIPDATE', 'COMMITDATE', 'RECEIPTDATE', 'SHIPINSTRUCT', 'SHIPMODE', 'COMMENT']
orders_columns = ['ORDERKEY', 'CUSTKEY',
                  'ORDERSTATUS', 'TOTALPRICE', 'ORDERDATE', 'ORDERPRIORITY', 'CLERK', 'SHIPPRIORITY', 'COMMENT']
