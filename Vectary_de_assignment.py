# import databricks.koalas as koalas
from pyspark.sql import SparkSession
from pandas_profiling import ProfileReport
import pandas as koalas

# import pandas as pd
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
from operator import attrgetter
import matplotlib.colors as mcolors

df = koalas.read_csv('/Users/deepak.sahu/Downloads/data-interview_1.csv')
df['gid'] = df['gid'].fillna('undefined')
df = df[['uuid', 'created', 'source', 'event']].drop_duplicates()
df['order_month'] = koalas.DatetimeIndex(df['created']).month

df_coho = df.groupby('uuid')['created'] \
                 .transform('min')
df['cohort']=koalas.DatetimeIndex(df_coho).month


df_cohort = df.groupby(['cohort', 'order_month']) \
              .agg(n_customers=('uuid', 'nunique')) \
              .reset_index(drop=False)
df_cohort['period_number'] = (df_cohort.order_month - df_cohort.cohort).apply(attrgetter('n'))

with koalas.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df_cohort.head(10))

    #Let’s describe
    #print(df.describe())

    # Let’s check for null values
    # print(df.isnull().sum())


# print(koalas_csv_df['event'].unique())
# prof = ProfileReport(koalas_csv_df)
# prof.to_file(output_file='output.html')

# n_orders = koalas_csv_df.groupby(['uuid'])['InvoiceNo'].nunique()
# mult_orders_perc = koalas_csv_df.sum(n_orders > 1) / df['CustomerID'].nunique()
# print(f'{100 * mult_orders_perc:.2f}% of customers ordered more than once.')

