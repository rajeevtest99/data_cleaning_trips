import pandas as pd

source_path = 'C:/Users/rajee/Desktop/data_cleaning/station_info.csv'

df = pd.read_csv(source_path)

df = df.drop(['index', 'legacy_id', 'station_id', 'region_id'], axis=1)

region_id = []

df2 = df['short_name']

for i in df2:
    region_id.append(i[:2])

df['region_id'] = region_id 

df.to_csv('station.csv', index=False)

print(df.head)







