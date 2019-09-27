# Data transformation
import pandas as pd
employees = pd.read_excel('C:/Users/Administrator/Documents/Python/Employees.xlsx', index_col='ID')
df = employees['Full Name'].str.split(expand=True)


print(df)
employees['First Name'] = df[0]
employees['Last Name'] = df[1].str.upper()
print(employees)
