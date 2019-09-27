# Data validation
import pandas as pd
def score_validation(row):
    try:
        assert 0<=row.Score<=100
    except:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}.')

students = pd.read_excel('C:/Users/Administrator/Documents/Python/Students.xlsx')
print(students)
students.apply(score_validation, axis=1)


# Data validation
import pandas as pd
def score_validation(row):
    if not 0<=row.Score<=100:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}.')

students = pd.read_excel('C:/Users/Administrator/Documents/Python/Students.xlsx')
print(students)
students.apply(score_validation, axis=1)
