import pandas as pd
import numpy as np
import time

#read csv file
df = pd.read_csv('/Users/Mike_F/Desktop/Crime_Data_2010_2017.csv',dtype={'Time Occurred': np.int16, 'Area ID': np.int16,'Reporting District': np.int16, 'Crime Code': np.float16, 'Victim Age': np.float16, 'Premise Code': np.float16, 'Crime Code 1': np.float16})

#convert to datetime formatsns.heatmap(df, yticklabels=False, cbar=False,cmap='summer')
df['Date Occurred'] = pd.to_datetime(df['Date Occurred'])
df['Date Reported'] = pd.to_datetime(df['Date Reported'])

#get the difference in date occurred - date reported
df['Difference'] = (df['Date Reported'] - df['Date Occurred']).dt.days

#drop unsued columns or cloumns with too many blank values
df.drop(['Premise Description','Weapon Description','Victim Descent','Weapon Used Code','Crime Code 3','Crime Code 2','Crime Code 4','Address','Cross Street','DR Number','Status Description','Crime Code Description','MO Codes','Status Code'], axis=1,inplace=True)

#select start and end dates to filter out
start_date = '01-01-2017'
end_date = '01-05-2017'

#set the mask dataframe
bool_mask = (df['Date Occurred'] > start_date) & (df['Date Occurred'] <= end_date)

#assign mask to df
df = df.loc[bool_mask]

#create new columns for lat and long
new = df['Location '].str.split(", ", n = 1, expand = True)
df['Latitude']= new[0] 
df['Longitude']= new[1]

#remove the consolidated Location column
df.drop(columns = ['Location '], inplace = True) 

#create two seperate columns for location
cols = ['Latitude', 'Longitude']

#remove the parenthesis from lat and long
def removeparen():
    for col in cols:
        df[col] = df[col].map(lambda x: str(x).lstrip('(').rstrip(')')).astype(float)
removeparen()

#fill null data with 0
df.fillna(0, inplace=True)

#assign gender
def converter(gender):
     if gender == 'M':
         return 1
     else:
         return 0

#save to file
pd.DataFrame.to_csv(df,"" + time.strftime('%Y-%m-%d') + ".csv",',')
