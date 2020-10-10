# https://wiki.grab.com/pages/viewpage.action?spaceKey=GRABPAY&title=How-tos+with+jupyter
# from pyspark.sql import SparkSession
#
# conf = sc._conf.setAll([("hive.metastore.uris", "thrift://prod-presto-hive-thift.gfg.pr:443")])
# spark = SparkSession.builder.config(conf=conf).enableHiveSupport().getOrCreate()
#
# import requests
# import pandas as pd
# from datetime import datetime as dt
# from dateutil.relativedelta import relativedelta
# from pyspark.sql.types import *
#
# today = dt.now()
# start_month = dt(today.year, today.month, 1)
# end_month = start_month + relativedelta(months=1, days=-1)
#
# '''
# Current one used (Some dates are missing though):
# https://exchangeratesapi.io/
#
# Test:
# response = requests.get("https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2020-07-01&base=SGD")
# df = pd.DataFrame(response.json()['rates']).T.reset_index().sort_values(by=['index'])
# df.head()
# df.tail()
# df['SGD'].unique() # returns 1
#
# =======================
# Lists of other currency exchanage sites as backup:
# https://docs.openexchangerates.org/docs/historical-json
# https://fixer.io/documentation
# '''
#
# url = 'https://api.exchangeratesapi.io/'
# query = url + str(end_month)[
#               :10] + "?base=SGD"  # Will get latest avail date if end month not available; some historical end month dates are missing
# response = requests.get(query)
#
# cur = pd.DataFrame(response.json()).reset_index()
# cur.rename(columns={
#     'index': 'currency',
#     'rates': 'exchange_one_sgd'
# }, inplace=True)
#
# cur['base'] = 'SGD'
# cur = cur[['base', 'currency', 'date', 'exchange_one_sgd']]
# cur
#
# # We actually only need the start & end.
# # The below is only for looping purposes, or in cases where API returns complate dates without missing gaps
# # , it can be used to join and filter only dates we need
# month_ends = pd.date_range(start='1950-01-01', end='2020-09-20', freq='M')
#
# url = 'https://api.exchangeratesapi.io/history?'
# start = str(month_ends.min())[:10]
# end = str(month_ends.max())[:10]
# query = url + "start_at=" + start + "&end_at=" + end + "&base=SGD"
#
# r = requests.get(query)
# df = pd.DataFrame(r.json()['rates']).reset_index()
# df
#
# df2 = pd.melt(df, id_vars='index')
# df2.rename(columns={
#     'index': 'currency',
#     'variable': 'date',
#     'value': 'exchange_one_sgd'
# }, inplace=True)
#
# df2['base'] = 'SGD'
# df2['month'] = df2['date'].str[:7]
# df2['exchange_one_sgd'] = df2['exchange_one_sgd'].astype('float64')
# df2.head()
#
# df3 = df2.sort_values(by=['date']).drop_duplicates(subset=['currency', 'base', 'month'], keep='last')
#
# df3.head()
#
# # In[121]:
#
#
# cols_order = ['base', 'currency', 'month', 'date', 'exchange_one_sgd']
# df3 = df3.where(pd.notnull(df3), None).reset_index()[cols_order]
# df3.head()
#
# # In[123]:
#
#
# schema = StructType([
#     StructField('base', StringType(), True)
#     , StructField('currency', StringType(), True)
#     , StructField('month', StringType(), True)
#     , StructField('date', StringType(), True)
#     , StructField('exchange_one_sgd', DoubleType(), True)
# ])
#
# # In[124]:
#
#
# cur_sp = spark.createDataFrame(df3, schema=schema)
# cur_sp.show(vertical=True)
#
# # In[125]:
#
#
# cur_pth = 's3://dsplatform-data/datalake/gfsa_lending_loan_datamart/mex/currencies'
# cur_sp.write.mode('overwrite').partitionBy('date').parquet(cur_pth)
#
# # In[126]:
#
#
# cur_sp.printSchema()
#
# # In[128]:
#
#
# spark.sql('''
#     CREATE TABLE gfsa_lending_loan_datamart.mex_currencies (
#         base STRING
#         , currency STRING
#         , month STRING
#         , exchange_one_sgd DOUBLE
#     )
#     PARTITIONED BY (date STRING)
#     STORED AS PARQUET
#     LOCATION "s3://dsplatform-data/datalake/gfsa_lending_loan_datamart/mex/currencies/"
# ''')
#
# # In[129]:
#
#
# spark.sql("MSCK REPAIR TABLE gfsa_lending_loan_datamart.mex_currencies")
#
# # ***
#
# # In[102]:
#
#
# # Quick Checks
# df3.groupby('currency').count()
# df3.query('currency == "CNY"')
# df3.groupby(['month', 'currency']).count()  # No dupes
#
# # In[49]:
#
#
# '''
# # Some dates are missing from API so can't use this method
# month_ends_df = pd.DataFrame(month_ends)
# month_ends_df.columns = ['date']
# month_ends_df['date'] = month_ends_df['date'].astype(str)
# month_ends_df
#
# df3 = df2.merge(month_ends_df, how='inner', left_on='date', right_on='date')
# df3.head()
# '''
#
# # In[16]:
#
#
# # Quick Checks
# pd.set_option('display.max_rows', None)
# df3.query('currency == "USD"').sort_values(by='date')
#
# # In[ ]:
#
#
# '''currencies = []
#
# for m in month_ends:
#     month_end = str(m)[:10]
#     print(month_end)
#     query = url + month_end + "?base=SGD" # Will get latest avail date if end month not available; some historical end month dates are missing
#     response = requests.get(query)
#     currencies.append(response.json())'''
#
# SDR,AUD,SKK,JPY,MYR,SIN,SGD,EUR,KRW,CNY,HKD,XEU,USD,CHF,REN,SAR,SEK,XDR,INR,ILS,OTH,KGS,RIN,MAL
# US
# HK
#
# {6 items
# "success":true
# "timestamp":1357084799
# "historical":true
# "base":"SGD"
# "date":"2013-01-01"
# "rates":{16 items
# "AUD":0.789042
# "JPY":70.876685
# "MYR":2.502614
# "SGD":1
# "EUR":0.619807
# "KRW":870.734433
# "CNY":5.116818
# "HKD":6.344971
# "USD":0.818603
# "CHF":0.749066
# "SAR":3.070035
# "SEK":5.332761
# "XDR":0.532133
# "INR":44.787632
# "ILS":3.054759
# "KGS":38.798869
# }
# }


import requests
import pprint

url = "https://openexchangerates.org/api/historical/2020-08-27.json?app_id=251803cdbb994fe2813635578dacbd0a&base=USD"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

pprint(response)


# import requests
#
# url = "https://fixer-fixer-currency-v1.p.rapidapi.com/symbols"
#
# headers = {
#     'x-rapidapi-host': "fixer-fixer-currency-v1.p.rapidapi.com",
#     'x-rapidapi-key': "d7f3d6edaemsh4140d996ecfe6cbp1e46e0jsn2b1b514e0acc"
#     }
#
# response = requests.request("GET", url, headers=headers)
#
# print(response.text)