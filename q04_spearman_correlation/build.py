# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
df1=dataframe_1.loc[:,"SalePrice"]
df2=dataframe_2.loc[:,"SalePrice"]

# Your code here
def spearman_correlation():
    scc=df1.corr(df2,method='spearman')
    #print scc
    return scc
#spearman_correlation()
