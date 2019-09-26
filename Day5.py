import pandas as pd
books = pd.read_excel('C:/Users/Administrator/Documents/Python/Books.xlsx', index_col=None, dtype={'ID':str, 'ListPrice':str, 'Price':str})

for i in books.index:
    books['ID'].at[i] = i+1
    books['ListPrice'].at[i] = (i+1)*10

print(books)

for i in range(5, 16): # 左闭右开区间
    books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]
print(books)

# books['Price'] = books['ListPrice'] * books['Discount']
# books['ListPrice'] = books['ListPrice'] + 2
# books['ListPrice'] = books['ListPrice'].apply(lambda x: x+2)

print(books)

books.set_index('ID', inplace=True)
books.to_excel('C:/Users/Administrator/Documents/Python/Book.xlsx')
print('Done!')


