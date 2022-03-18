from parser import get_customers, get_orders, get_lineitems, get_query_example
import pandas
import concurrent.futures


def get_calculated_revenue_list(mktsegment, customers, orders, lineitems):
    orderkey_list = get_merged_orderkey_list(
        mktsegment, customers, orders, lineitems)
    merged_list = pandas.merge(lineitems, orderkey_list, on=["ORDERKEY"])
    merged_list = merged_list[["EXTENDEDPRICE", "DISCOUNT"]]
    merged_list["REVENUE"] = merged_list["EXTENDEDPRICE"] * \
        (1-merged_list["DISCOUNT"])
    revenue_list = merged_list[["REVENUE"]]
    print(f"Revenue List Length for {mktsegment}: {revenue_list.shape}")
    return revenue_list


def get_merged_orderkey_list(mktsegment, customers, orders, lineitems):
    merged_list = pandas.merge(customers, orders, on=["CUSTKEY"])
    merged_list = merged_list[["ORDERKEY", "MKTSEGMENT"]]
    mktsegment_list = merged_list.loc[merged_list['MKTSEGMENT'] == mktsegment]
    orderkey_list = mktsegment_list[["ORDERKEY"]]
    print(f"Orderkey List Length for {mktsegment}: {orderkey_list.shape}")
    return orderkey_list


def get_average_customer_revenue(mktsegment, customers, orders, lineitems):
    revenue_list = get_calculated_revenue_list(
        mktsegment, customers, orders, lineitems)
    total_sum = revenue_list['REVENUE'].sum()
    average_revenue = total_sum / len(revenue_list)
    print(f"Total Revenue for {mktsegment}: {total_sum}")
    print(f"Average Customer Revenue for {mktsegment}: {average_revenue}")


def main():
    query_example_list = get_query_example()
    customers = get_customers()
    orders = get_orders()
    lineitems = get_lineitems()
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=None)
    for mktsegment in query_example_list:
        executor.submit(get_average_customer_revenue,
                        mktsegment, customers, orders, lineitems)


if __name__ == '__main__':
    main()
