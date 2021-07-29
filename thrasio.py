# Input
#
# 1. A list or array of records representing a stream of sales data
# [
#   { 'channel' : 'Amazon', 'id' : 'AMZ123', 'sales' : 10, 'returns' : 0 },
#   { 'channel' : 'Amazon', 'id' : 'AMZ123', 'sales' : 5, 'returns' : 2 },
#   { 'channel' : 'Shopify', 'id' : '1234', 'sales' : 15, 'returns' : 0 },
#   { 'channel' : 'Target', 'id' : 'TGT456', 'sales' : 23, 'returns' : 5 }
# ]
#
# 2. A map of channel specific external ids to Thrasio internal ids
# {
#   'AMAZON' : {'AMZ123' : 'THRASIO-987', 'AMZ456' : 'THRASIO-456' },
#   'SHOPIFY' : {'1234' : 'THRASIO-987', '5678' : 'THRASIO-321' }
# }
#
## Expected Output
#
# The aggregated performance data of products across all channels showing the net sales and total number of returns.
#
# [
#   {“id”:“THRASIO-987”, “net_sales”:28, “returns”:2},
#   {“id”:“THRASIO-456”, “net_sales”:18, “returns”:5},
# ]


# --------------
# import pprint
sales = [
    {'channel': 'Amazon', 'id': 'AMZ123', 'sales': 10, 'returns': 0},
    {'channel': 'Amazon', 'id': 'AMZ123', 'sales': 5, 'returns': 2},
    {'channel': 'Shopify', 'id': '1234', 'sales': 15, 'returns': 0}
]

mapping = {
    'AMAZON': {'AMZ123': 'THRASIO-987', 'AMZ456': 'THRASIO-456'},
    'SHOPIFY': {'1234': 'THRASIO-987', '5678': 'THRASIO-321'}
}

def thrasio_sales(mappings,sales):
    result={}
    for mapping_keys,mapping_vals in mappings.items():
        for sale in sales:
            print("-____-____-")
            if mapping_keys==sale['channel'].upper():
                result["id"] = mapping_vals[sale['id']]
                result["net_sales"] += sale.get('sales',0)
                result["returns"] += sale.get('returns',0)
                print(result)






# [{ 'channel' : 'Amazon', 'id' : 'THRASIO-987', 'sales' : 10, 'returns' : 0 },{ 'channel' : 'Amazon', 'id' : 'THRASIO-987', 'sales' : 5, 'returns' : 2 }]

# [
#   {“id”:“THRASIO-987”, “net_sales”:28, “returns”:2},
#   {“id”:“THRASIO-456”, “net_sales”:18, “returns”:5},
# ]
from collections import defaultdict, Counter
#
# def thrasio_sales(sales, mapping):
#     results = []
#
#     for sale in sales:
#         # res=sale
#         sale['id'] = mapping[sale['channel'].upper()].get(sale['id'])
#         # print(sale)
#         results.append(sale)
#     # print(results)
#     answer=[]
#     final = defaultdict(Counter)
    # for result in results:
    #     if result['channel'] in final.values() and result['id'] in final.values():
    #         final.update('net_sales')=final['net_return'] + result['sales']
    #         final['net_return'] += result['returns']
    #
    #     else:
    #         final['channel']=result['channel']
    #         final['id'] = result['id']
    #         final['net_sales'] = result['sales']
    #         final['net_return'] = result['returns']
    #     print(final)
    #     answer.append(final)
    # print(answer)
    # sum_value_keys=['sales','returns']
    # for item in results:
    #     key = item['id']+"-"+item["channel"]
    #     values = {k: item[k] for k in sum_value_keys}
    #     final[key].update(values)
    #
    #
    # print(final)






    # final = []
    # dict = {}
    # for result in results:
    #     if result.get('id') in dict['id']:
    #         dict['net_sales'] += result.get('sales')
    #         dict['return'] += result.get('return')
    #     else:
    #         dict['id'] = result.get('id')
    #         dict['net_sales'] = result.get('sales')
    #         dict['return'] = result.get('return')
    #
    #     final.append(dict)
    # print(results)


thrasio_sales( mapping,sales)

