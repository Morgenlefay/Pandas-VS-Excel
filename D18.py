import pandas as pd

# 读取CSV文件
students1 = pd.read_csv('C:/Users/Administrator/Documents/Python/Students.csv')
print(students1)

# 读取TSV文件
students2 = pd.read_csv('C:/Users/Administrator/Documents/Python/Students.tsv', sep='\t')
print(students2)

# 读取TXT文件
students3 = pd.read_csv('C:/Users/Administrator/Documents/Python/Students.txt', sep='|')
print(students3)