import pandas as pd

companys = pd.read_csv('./csv_/company_nm1.csv')
countrys = pd.read_csv('./csv_/country_nm1.csv')

# 이름 소문자로 변환
companys['0'] = companys['0'].str.lower()
countrys['0'] = countrys['0'].str.lower()

company_name = input("Write company name : ")
country_name = input("Write country name : ")

# 입력 또한 소문자로 변환
company_name = company_name.strip().lower().replace(' ','')
country_name = country_name.strip().lower().replace(' ','')

print(company_name, country_name)