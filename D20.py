import pandas as import pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

sales = pd.read_excel('C:/Users/Administrator/Documents/Python/Sales.xlsx', dtype={'Month':str})
print(sales)

slope, intercept, r, p, std_err = linregress(sales.index, sales.Revenue)

exp = sales.index * slope + intercept
print(slope*35+intercept)

plt.scatter(sales.index, sales.Revenue)
plt.plot(sales.index, exp, color='orange')
plt.title(f"y={slope}*x+{intercept}")
plt.xticks(sales.index, sales.Month, rotation=90)
plt.tight_layout()
plt.show()
