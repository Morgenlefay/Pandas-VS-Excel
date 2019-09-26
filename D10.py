import pandas as pd
import matplotlib.pyplot as plt
notch = pd.read_excel('C:/Users/Administrator/Documents/Python/Notch.xlsx', index_col='Time')
print(notch)

# 折线图
notch.plot(y=['Notch1', 'Notch2', 'Notch3', 'Notch4'])
plt.xlabel('Time')
plt.ylabel('FPKM')
plt.show()

# 叠加区域图
notch.plot.area(y=['Notch1', 'Notch2', 'Notch3', 'Notch4'])
plt.xlabel('Time')
plt.ylabel('FPKM')
plt.show()



