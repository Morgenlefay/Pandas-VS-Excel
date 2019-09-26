import pandas as pd
marker = pd.read_excel('C:/Users/Administrator/Documents/Python/Marker.xlsx', index_col='ID')
print(marker)
marker = marker.loc[marker.Mmu_aRG_1.apply(lambda a: a > 0.5)].loc[marker.Mmu_aRG_3.apply(lambda a: a > 0.5)]
print(marker)

