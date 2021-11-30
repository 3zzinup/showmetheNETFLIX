import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import joblib

# input 정규화해서 넣으려고 만든 함수. 매개변수 : input
def inputChange(input):
    result = {}
    
    data_company = pd.read_csv('./csv_/company_nm1.csv')
    data_company = data_company.drop(columns='Unnamed: 0')
    data_country = pd.read_csv('./csv_/country_nm1.csv')
    data_country = data_country.drop(columns='Unnamed: 0')
    data_director = pd.read_csv('./csv_/director_nm1.csv')
    data_director = data_director.drop(columns='Unnamed: 0')
    data_genre = pd.read_csv('./csv_/genre_nm.csv')
    data_genre = data_genre.drop(columns='Unnamed: 0')
    data_rating = pd.read_csv('./csv_/rating_nm1.csv')
    data_rating = data_rating.drop(columns='Unnamed: 0')
    data_score = pd.read_csv('./csv_/score_nm1.csv')
    data_score = data_score.drop(columns='Unnamed: 0')
    data_writer = pd.read_csv('./csv_/writer_nm1.csv')
    data_writer = data_writer.drop(columns='Unnamed: 0')
    
    data_company['0'] = data_company['0'].str.replace(" ","").str.lower()
    data_country['0'] = data_country['0'].str.replace(" ","").str.lower()
    data_director['0'] = data_director['0'].str.replace(" ","").str.lower()
    data_genre['0'] = data_genre['0'].str.replace(" ","").str.lower()
    data_rating['0'] = data_rating['0'].str.replace(" ","").str.lower()
    data_writer['0'] = data_writer['0'].str.replace(" ","").str.lower()
    
    genre=input.get('genre').strip().lower().replace(' ','')
    if data_genre[data_genre['0'] == genre].empty:
        result['genre'] = 0
    else:
        genre = data_genre[data_genre['0'] == genre]['zscore']
        result['genre'] = genre.values[0]
        
    rating=input.get('rating').strip().lower().replace(' ','')
    if data_rating[data_rating['0'] == rating].empty:
        result['rating'] = 0
    else:
        rating = data_rating[data_rating['0'] == rating]['zscore']
        result['rating'] = rating.values[0]
    
    country=input.get('country').strip().lower().replace(' ','')
    if data_country[data_country['0'] == country].empty:
        result['country'] = 0
    else:
        country = data_country[data_country['0'] == country]['zscore']
        result['country'] = country.values[0]

    score=input.get('score').strip().lower().replace(' ','')
    if data_score[data_score['0'] == float(score)].empty:
        result['score'] = 0
    else:
        score = data_score[data_score['0'] == float(score)]['zscore']
        result['score'] = score.values[0]

    company=input.get('company').strip().lower().replace(' ','')
    # zscore로 정규화하였기때문에 default값은 0으로...
    if data_company[data_company['0'] == company].empty:
        result['company'] = 0
    else:
        company = data_company[data_company['0'] == company]['zscore']
        result['company'] = company.values[0]

    writer=input.get('writer').strip().lower().replace(' ','')
    if data_writer[data_writer['0'] == writer].empty:
        result['writer'] = 0
    else:
        writer = data_writer[data_writer['0'] == writer]['zscore']
        result['writer'] = writer.values[0]

    director=input.get('director').strip().lower().replace(' ','')
    if data_director[data_director['0'] == director].empty:
        result['director'] = 0
    else:
        director = data_director[data_director['0'] == director]['zscore']
        result['director'] = director.values[0]
    
    return result

def randomforest(input):    
    loaded_model = joblib.load('./models_/rfr_model_z_t.pkl')
    
    inputs = pd.DataFrame(inputChange(input), index=[0])
    
    result = loaded_model.predict(inputs)
    
    return result[0]

input = {
    'country':'United States',
    'company':'Daybreak',
    'writer':'Andy Burg',
    'director':'George Huang',
    'genre':'Comedy',
    'rating':'PG-13',
    'score':'5.7'
}

print(randomforest(input))