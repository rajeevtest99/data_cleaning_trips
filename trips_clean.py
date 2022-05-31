import pandas as pd

source_path = 'C:/Users/rajee/Desktop/data_cleaning/trips_first_pass_clean.csv'

df = pd.read_csv(source_path)

print(df.isnull().sum())



df = df.drop(['Unnamed: 0', 'start_station_name' , 'end_station_name' ,'rental_access_method', 'start_station_latitude', 'start_station_longitude' , 'end_station_latitude', 'end_station_longitude'], axis=1)


df[['ride_id', 'bike_type']] = df[['ride_id', 'bike_type']].fillna('NA')
df[['bike_id']] = df[['bike_id']].fillna(0)


df = df.astype({'duration_sec': int})
df = df.astype({'bike_id': int})



print((df.isnull().sum() * 100) / (len(df.index)))

df.to_csv('trips.csv', index=False)






