import pandas as pd

page_001 = pd.read_excel('C:/Users/Administrator/Documents/Python/Students.xlsx', sheet_name='Page_001')
page_002 = pd.read_excel('C:/Users/Administrator/Documents/Python/Students.xlsx', sheet_name='Page_002')
print(page_001)
print(page_002)

# 追加行
students = page_001.append(page_002).reset_index(drop=True)
print(students)

# 增加行
stu = pd.Series({'ID':41, 'Name':'Abel', 'Score':99})
students = students.append(stu, ignore_index=True)

# 单元格更改数据
students.at[39, 'Name'] = 'Bailey'
students
# 行替换
stu = pd.Series({'ID':40, 'Name':'Bailey', 'Score':120})
students.iloc[39] = stu
print(students)

# 行插入
stu = pd.Series({'ID':101, 'Name':'Danny', 'Score':101})
part1 = students[:20]
part2 = students[20:]
students = part1.append(stu, ignore_index=True).append(part2).reset_index(drop=True)
print(students)

# 行删除
students.drop(index=[0,1,2], inplace=True)
print(students)
students.drop(index=range(3,10), inplace=True)
print(students)

# 删除空行
for i in range(10,15):
    students['Name'].at[i] = ''
print(students)
missing = students.loc[students['Name'] =='']
students.drop(index=missing.index, inplace=True)
students = students.reset_index(drop=True)
print(students)