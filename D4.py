import pandas as pd
from datetime import date, timedelta

def add_month(d, md):
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m//12
        m = m % 12
        return date(d.year+yd, m, d.day)    

books = pd.read_excel('C:/Users/Administrator/Documents/Python/Books.xlsx',skiprows=3, usecols="D:G",index_col=None, dtype={'ID':str, 'InStore':str, 'Date':str})
start = date(2018,1,1)
for i in books.index:
    books['ID'].at[i] = i+1
    books['InStore'].at[i] = 'Yes' if i%2==0 else 'No'
    books['Date'].at[i] = add_month(start, i)
    # books['Date'].at[i] = start + timedelta(days=i) #天
    # books['Date'].at[i] = date(start.year+i,start.month,start.day) #年

print(books)
books.set_index('ID', inplace=True)
books.to_excel('C:/Users/Administrator/Documents/Python/Books.xlsx')
print('Done!')
