import pandas as pd
import pprint
import csv

dfo = pd.read_csv('../csv2_/big_data.csv')
dft = pd.read_csv('../csv2_/last.csv')

final_list = []
for index in range(len(dfo)):
    lis = []
    lis.append(dfo.loc[index][8])
    lis.append(dft.loc[index][0])
    final_list.append(lis)

with open('../csv2_/final_real.csv','w',newline='',encoding='utf8') as file :
    write = csv.writer(file)
    write.writerows(final_list)