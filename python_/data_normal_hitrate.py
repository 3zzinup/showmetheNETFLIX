import numpy as np
import scipy.stats as ss
import pandas as pd
import scipy.stats as ss
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('../csv2_/big_data_zscore.csv')

a = df['hit rate'].to_numpy()

b = a.reshape(-1,1)

scaler = StandardScaler()
scaler.fit(b)
c = scaler.transform(b)

scaler2 = RobustScaler()
scaler2.fit(b)
d = scaler2.transform(b)

scaler2 = MinMaxScaler()
scaler2.fit(b)
e = scaler2.transform(b)

df['zscore'] = c
df['robust'] = d
df['minmax'] = e

df.to_csv('../csv2_/big_data_zscore_nm.csv')