# 多表联合

# 方法1 by merge
import pandas as pd
students = pd.read_excel('C:/Users/Administrator/Documents/Python/Student_score.xlsx', sheet_name='Students')
scores = pd.read_excel('C:/Users/Administrator/Documents/Python/Student_score.xlsx', sheet_name='Scores')
print(students)
print(scores)
table = students.merge(scores, how='left', on='ID').fillna(0)
table.Score = table.Score.astype(int)
print(table)

# 方法2 by join
import pandas as pd
students = pd.read_excel('C:/Users/Administrator/Documents/Python/Student_score.xlsx', sheet_name='Students', index_col='ID')
scores = pd.read_excel('C:/Users/Administrator/Documents/Python/Student_score.xlsx', sheet_name='Scores', index_col='ID')
print(students)
print(scores)
table = students.join(scores, how='left', on='ID').fillna(0)
table.Score = table.Score.astype(int)
print(table)

