import pandas as pd
import numpy as np

page_001 = pd.read_excel('C:/Users/Administrator/Documents/Python/Students.xlsx', sheet_name='Page_001')
page_002 = pd.read_excel('C:/Users/Administrator/Documents/Python/Students.xlsx', sheet_name='Page_002')
print(page_001)
print(page_002)

students = pd.concat([page_001,page_002]).reset_index(drop=True)
print(students)

# 追加列
students['Age'] = 25
print(students)

# 删除列
students.drop(columns=['Age'],inplace=True)
print(students)

# 插入列
students.insert(1,column='Foo',value=np.repeat('foo',len(students)))
print(students)

# 改列名
students.rename(columns={'Foo':'FOO','Name':'NAME'},inplace=True)
print(students)

# 去无效数据
students.dropna(inplace=True)
print(students)


