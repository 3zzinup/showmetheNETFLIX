import pandas as pd
import numpy as np

companys = pd.read_csv('../csv_/company.csv')   # 회사 
contrys = pd.read_csv('../csv_/country.csv')    # 나라
directors = pd.read_csv('../csv_/director.csv') # 감독
genres = pd.read_csv('../csv_/genre.csv')       # 장르
ratings = pd.read_csv('../csv_/rating.csv')     # 상영등급
scores = pd.read_csv('../csv_/score.csv')       # 평점
writers = pd.read_csv('../csv_/writer.csv')     # 작가

# 이름 소문자로 변환
companys['0'] = companys['0'].str.lower()
contrys['0'] = contrys['0'].str.lower()
directors['0'] = directors['0'].str.lower()
genres['0'] = genres['0'].str.lower()
ratings['0'] = ratings['0'].str.lower()
# 평점은 알파벳이아니라서 제외
writers['0'] = writers['0'].str.lower()

# 입력받기
company_, country_ = input("Write info of movie(company) : ")
# country_, director_, genre_, rating_, score_, writer_
# , country, director, genre, rating, score, writer)
# 입력 또한 소문자로 변환
# company_ = company_.lower()
# country_ = country_.lower()
# director_ = director_.lower()
# genre_ = genre_.lower()
# rating_ = rating_.lower()
# 평점은 알파벳이아니라서 제외
# writer_ = writer_.lower()

# movie_info = [company_, country_, director_, genre_, rating_, score_, writer_]


rank_company = companys[companys['0']==company_].index
if rank_company.tolist()[0]+1 > 0:
    its_sum = float(companys['1'].sum())
    rate = float(companys[companys['0']==company_]['1']) / its_sum
    print(f'rank_company : {rank_company.tolist()[0]+1}')
    print(f'{company_}\'s rate is {rate}%')
else:
    print("it's not in data")

rank_company = companys[companys['0']==company_].index
if rank_company.tolist()[0]+1 > 0:
    its_sum = float(companys['1'].sum())
    rate = float(companys[companys['0']==company_]['1']) / its_sum
    print(f'rank_company : {rank_company.tolist()[0]+1}')
    print(f'{company_}\'s rate is {rate}%')
else:
    print("it's not in data")

# its_sum = float(companys['1'].sum())
# rate = float(companys[companys['0']==company_]['1']) / its_sum
# if rate > 0:
#     print(f'{company_}\'s rate is {rate}%')
# else:
#     print("it's not in data")