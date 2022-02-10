import pandas as pd
import numpy as np

companys = pd.read_csv('../csv_/company.csv')
countrys = pd.read_csv('../csv_/country.csv')

# 이름 소문자로 변환
companys['0'] = companys['0'].str.lower()
countrys['0'] = countrys['0'].str.lower()

company_name = input("Write company name : ")
country_name = input("Write country name : ")

# 입력 또한 소문자로 변환
company_name = company_name.lower()
country_name = country_name.lower()

rank = companys[companys['0']==company_name].index
print(f'{company_name} rank : {rank.tolist()[0]+1}')

its_sum = float(companys['1'].sum())

rate = float(companys[companys['0']==company_name]['1']) / its_sum

if rate > 0:
    print(f'company: {company_name}\'s rate is {rate*100}%')
else:
    print("it's not in data")

rank_country = countrys[countrys['0']==country_name].index
print(f'{country_name} rank : {rank_country.tolist()[0]+1}')

its_sum = float(countrys['1'].sum())

rate = float(countrys[countrys['0']==country_name]['1']) / its_sum

if rate > 0:
    print(f'country: {country_name}\'s rate is {rate*100}%')
else:
    print("it's not in data")