### NumPy, Pandas, Matplotlib 安装
```
pip install numpy
pip install pandas
pip install matplotlib
```
### 创建Excel文件
```python
import pandas as pd
df=pd.DataFrame({'ID':[1,2,3], 'Name':['Tim','Victor','Nick']})
df=df.set_index('ID')
print(df)
df.to_excel('C:/Users/Administrator/Documents/Python/output.xls')
print('Done!')
```
