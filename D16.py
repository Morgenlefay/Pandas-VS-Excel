# 去除重复数据
import pandas as pd
marker = pd.read_excel('C:/Users/Administrator/Documents/Python/Marker.xlsx')
print(marker)
marker.drop_duplicates(subset='ID',inplace=True, keep='first')
print(marker)

# 定位重复数据
import pandas as pd
marker = pd.read_excel('C:/Users/Administrator/Documents/Python/Marker.xlsx')
print(marker)
dupe = marker.duplicated(subset="ID")
dupe = dupe[dupe == True]
print(dupe)
print(marker.iloc[dupe.index])
