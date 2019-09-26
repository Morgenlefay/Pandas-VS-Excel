import pandas as pd
notch = pd.read_excel('C:/Users/Administrator/Documents/Python/Notch.xlsx', index_col='ID')
print(notch)

# 排序
notch.sort_values(by='ID', inplace=True) # 从小到大排
notch.sort_values(by='ID', inplace=True, ascending=False) #从大到小排
print(notch)

# 多重排序
notch.sort_values(by=['aRG', 'ID'], inplace=True, ascending=[False, False])
print(notch)
