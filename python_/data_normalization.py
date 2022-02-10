import pandas as pd
import scipy.stats as ss
import csv
import pandas as pd
import scipy.stats as ss
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MinMaxScaler

lis1=[]
df = pd.read_csv('../csv_/movies_dropna1.csv')

for index in range(len(df)):
    cal = df.loc[index]['gross']/df.loc[index]['budget']
    if cal!=cal:
        continue
    lis2 = []   
    lis2.append(df.loc[index]['name'])
    lis2.append(df.loc[index]['genre'])
    lis2.append(df.loc[index]['rating'])
    lis2.append(df.loc[index]['country'])
    lis2.append(df.loc[index]['score'])
    lis2.append(df.loc[index]['company'])
    lis2.append(df.loc[index]['writer'])
    lis2.append(df.loc[index]['director'])
    lis2.append(cal)
    lis1.append(lis2)

dfg = pd.read_csv('../csv2_/genre_nm.csv')
for line in lis1:
    if line[1]!=line[1]:
        continue
    idx = dfg.index[dfg['0']==line[1]].tolist()[0]
    line[1] = dfg.at[idx,'zscore']

dfr = pd.read_csv('../csv2_/rating_nm1.csv')
for line in lis1:
    if line[2]!=line[2]:
        continue
    idx = dfr.index[dfr['0']==line[2]].tolist()[0]
    line[2] = dfr.at[idx,'zscore']

dfc = pd.read_csv('../csv2_/country_nm1.csv')
for line in lis1:
    if line[3]!=line[3]:
        continue
    idx = dfc.index[dfc['0']==line[3]].tolist()[0]
    line[3] = dfc.at[idx,'zscore']

dfs = pd.read_csv('../csv2_/score_nm1.csv')
for line in lis1:
    if line[4]!=line[4]:
        continue
    idx = dfs.index[dfs['0']==line[4]].tolist()[0]
    line[4] = dfs.at[idx,'zscore']

dfco = pd.read_csv('../csv2_/company_nm1.csv')
for line in lis1:
    if line[5]!=line[5]:
        continue
    idx = dfco.index[dfco['0']==line[5]].tolist()[0]
    line[5] = dfco.at[idx,'zscore']

dfw = pd.read_csv('../csv2_/writer_nm1.csv')
for line in lis1:
    if line[6]!=line[6]:
        continue
    idx = dfw.index[dfw['0']==line[6]].tolist()[0]
    line[6] = dfw.at[idx,'zscore']

dfd = pd.read_csv('../csv2_/director_nm1.csv')
for line in lis1:
    if line[7]!=line[7]:
        continue
    idx = dfd.index[dfd['0']==line[7]].tolist()[0]
    line[7] = dfd.at[idx,'zscore']

with open('../csv2_/big_data_zscore.csv','w',newline='',encoding='utf8') as file :
    write = csv.writer(file)
    write.writerows(lis1)