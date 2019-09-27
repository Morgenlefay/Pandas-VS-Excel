# 条件格式化
import pandas as pd

def low_score_red(s):
    color = 'red' if s<60 else 'black'
    return f'color:{color}'

def highest_score_green(col):
    return ['background-color:lime' if v==col.max() else 'background-color:white' for v in col]

students = pd.read_excel('C:/Users/Administrator/Documents/Python/Students.xlsx')
students.style.applymap(low_score_red, subset=['Test_1','Test_2','Test_3']).apply(highest_score_green, subset=['Test_1','Test_2','Test_3'])


# Heatmap
import pandas as pd
import seaborn as sns

color_map = sns.light_palette('green', as_cmap=True)

students = pd.read_excel('c:/Temp/Students.xlsx')
students.style.background_gradient(cmap=color_map, subset=['Test_1','Test_2','Test_3'])
