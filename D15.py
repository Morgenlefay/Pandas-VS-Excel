import pandas as pd
marker = pd.read_excel('C:/Users/Administrator/Documents/Python/Marker.xlsx',index_col='ID')
print(marker)

aRG = marker[['Mmu_aRG_1','Mmu_aRG_2','Mmu_aRG_3','Mmu_aRG_4']]
print(aRG)
marker['aRG'] = aRG.mean(axis=1) #求平均值
print(marker)

bRG = marker[['Mmu_bRG_1','Mmu_bRG_2','Mmu_bRG_3','Mmu_bRG_4']]
print(bRG)
marker['bRG'] = bRG.mean(axis=1) #求平均值
print(marker)

bIP = marker[['Mmu_bIP_1','Mmu_bIP_2','Mmu_bIP_3','Mmu_bIP_4']]
print(bIP)
marker['bIP'] = bIP.mean(axis=1) #求平均值
print(marker)

n = marker[['Mmu_N_1','Mmu_N_2','Mmu_N_3','Mmu_N_4']]
print(n)
marker['N'] = n.mean(axis=1) #求平均值
print(marker)

marker.to_excel('C:/Users/Administrator/Documents/Python/Output.xlsx')
print('Done!')
