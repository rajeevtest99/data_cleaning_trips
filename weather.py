import pandas as pd

source_path = 'C:/Users/rajee/Desktop/data_cleaning/weather_hourly.csv'

df = pd.read_csv(source_path)

df = df.drop(['Unnamed: 0','snow', 'wdir', 'wpgt', 'tsun', 'coco', 'prcp'], axis=1)

df = df.rename({'start_station_id': 'station_id'}, axis=1)

df[['temp', 'dwpt', 'rhum', 'wspd', 'pres']] = df[['temp', 'dwpt', 'rhum', 'wspd', 'pres']].ffill()

print(df.dtypes)

print(df.head)

print((df.isnull().sum()))

print((df.isnull().sum() * 100) / (len(df.index)))

df.to_csv('weather.csv', index=False)