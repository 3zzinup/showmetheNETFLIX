from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
import time
import tensorflow as tf
import csv

df = pd.read_csv('../csv2_/big_data.csv')
lis1 = []
trX=[]
trY=[]
for index in range(len(df)):
    lis2 = []
    a=df.loc[index][1]
    if a!=a:
        continue
    b=df.loc[index][2]
    if b!=b:
        continue
    c=df.loc[index][3]
    if c!=c:
        continue
    d=df.loc[index][4]
    if d!=d:
        continue
    e=df.loc[index][5]
    if e!=e:
        continue
    f=df.loc[index][6]
    if f!=f:
        continue
    g=df.loc[index][7]
    if g!=g:
        continue
    h=df.loc[index][8]
    lis2.append(a)
    lis2.append(b)
    lis2.append(c)
    lis2.append(d)
    lis2.append(e)
    lis2.append(f)
    lis2.append(g)
    trX.append(lis2)
    trY.append(h)

seed = 0
np.random.seed(seed)
tf.random.set_seed(seed)

model = Sequential()
model.add(Dense(7, input_dim= 7, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(3, activation='tanh'))
model.add(Dense(1))

model.compile(loss='mean_squared_logarithmic_error', optimizer='adam')
model.fit(trX, trY, epochs=100, batch_size=3)

loss = model.evaluate(trX, trY, verbose=0)

last_list = model.predict(trX)

print("테스트데이터 loss 값 : ", loss)

with open('../csv2_/last.csv','w',newline='',encoding='utf8') as file :
    write = csv.writer(file)
    write.writerows(last_list)