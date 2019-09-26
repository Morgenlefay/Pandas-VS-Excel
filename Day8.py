# 柱状图 by pandas
import pandas as pd
import matplotlib.pyplot as plt
notch = pd.read_excel('C:/Users/Administrator/Documents/Python/Notch.xlsx')
notch.sort_values(by='aRG', inplace=True)
print(notch)
notch.plot.bar(x='ID', y='aRG', color='red', title='FPKM')
plt.tight_layout()
plt.show()

# 柱状图 by matplotlib
import pandas as pd
import matplotlib.pyplot as plt
notch = pd.read_excel('C:/Users/Administrator/Documents/Python/Notch.xlsx')
notch.sort_values(by='aRG', inplace=True)
print(notch)
plt.bar(notch.ID, notch.aRG, color="red")
plt.xticks(notch.ID, rotation='90')
plt.xlabel('ID')
plt.ylabel('FPKM')
plt.title('FPKM by ID', fontsize=14)
plt.tight_layout()
plt.show()

# 分组柱图 by pandas
import pandas as pd
import matplotlib.pyplot as plt
notch = pd.read_excel('C:/Users/Administrator/Documents/Python/Notch.xlsx')
notch.sort_values(by='aRG', inplace=True)
notch.plot.bar(x='ID', y=['aRG','bRG', 'bIP', 'N'], color=['red', 'blue', 'black', 'green'])
plt.title('FPKM by genes', fontsize=14, fontweight='bold')
plt.xlabel('ID')
plt.ylabel('FPKM')
f=plt.gcf()
f.subplots_adjust(left=0.2, bottom=0.42)
# plt.tight_layout()
plt.show()

# 叠加柱状图 by pandas
import pandas as pd
import matplotlib.pyplot as plt
notch = pd.read_excel('C:/Users/Administrator/Documents/Python/Notch.xlsx')
print(notch)
notch['Total'] = notch['aRG'] + notch['bRG'] + notch['bIP'] + notch['N']
print(notch)
notch.sort_values(by='Total', inplace=True)
notch.plot.bar(x='ID', y=['aRG','bRG', 'bIP', 'N'], stacked=True)
plt.tight_layout()
plt.show()

# 水平叠加柱状图 by pandas
import pandas as pd
import matplotlib.pyplot as plt
notch = pd.read_excel('C:/Users/Administrator/Documents/Python/Notch.xlsx')
print(notch)
notch['Total'] = notch['aRG'] + notch['bRG'] + notch['bIP'] + notch['N']
print(notch)
notch.sort_values(by='Total', inplace=True, ascending=True)
notch.plot.barh(x='ID', y=['aRG','bRG', 'bIP', 'N'], stacked=True)
plt.tight_layout()
plt.show()


