import pandas as pd
pd.options.display.max_columns=999

notch = pd.read_excel('C:/Users/Administrator/Documents/Python/Notch.xlsx', index_col='ID')
print(notch)
table = notch.transpose()
print(table)




