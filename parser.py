import pandas
import constants


def get_customers():
    customer_list = pandas.read_table(
        constants.customer_path, delimiter='|', names=constants.customer_columns, index_col=False)
    return customer_list


def get_orders():
    orders_list = pandas.read_table(
        constants.orders_path, delimiter='|', names=constants.orders_columns, index_col=False)
    return orders_list


def get_lineitems():
    lineitem_list = pandas.read_table(
        constants.lineitem_path, delimiter='|', names=constants.lineitem_columns, index_col=False)
    return lineitem_list


def get_query_example():
    with open(constants.query_example_path) as f:
        lines = f.readlines()
        clean_lines = []
        for line in lines:
            line = line.replace("\n", "")
            clean_lines.append(line)
        print(f"Query Example List: {clean_lines}")
        return clean_lines
