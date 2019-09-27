import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = 999
homes = pd.read_excel('C:/Users/Administrator/Documents/Python/home_data.xlsx')
print(homes.head())
print(homes.corr())

# 散点图
homes.plot.scatter(x='sqft_living', y='price')
plt.show()

# 面积直方图
homes.sqft_living.plot.kde()
homes.sqft_living.plot.hist(bins=100)
plt.xticks(range(0, max(homes.sqft_living), 500), fontsize=8, rotation=90)
plt.show()

# 价格直方图
homes.price.plot.hist(bins=200)
plt.xticks(range(0, max(homes.price), 100000), fontsize=8, rotation=90)
plt.show()

# 密度图
homes.sqft_living.plot.kde()
plt.xticks(range(0, max(homes.sqft_living), 500), fontsize=8, rotation=90)
plt.show()






