import pandas as pd
import numpy as np

pd.options.display.max_columns=999
order = pd.read_excel('C:/Users/Administrator/Documents/Python/Orders.xlsx')
print(order.head())
order['Year'] = pd.DatetimeIndex(order.Date).year
print(order.head())
pt1 = order.pivot_table(index='Category', columns="Year", values='Total', aggfunc=np.sum)
print(pt1)

groups = order.groupby(['Category', 'Year'])
s = groups['Total'].sum()
c = groups['ID'].sum()
pt2 = pd.DataFrame({'Sum':s, 'Count':c})
print(pt2)