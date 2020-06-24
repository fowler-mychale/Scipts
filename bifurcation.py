import pandas as pd
import numpy as np
import time

df = pd.read_csv('C:/Users/Mike_F/Desktop/foo.csv')

df['DOMAIN'] = [x.split('@')[1] for x in df['EMAILADDRESS']]
df['TLD'] = [x.split('.')[1] for x in df['EMAILADDRESS']]

df.drop(df.loc[df['DOMAIN']=='gmail.com'].index, inplace=True)
df.drop(df.loc[df['DOMAIN']=='hotmail.com'].index, inplace=True)
df.drop(df.loc[df['DOMAIN']=='outlook.com'].index, inplace=True)
df.drop(df.loc[df['DOMAIN']=='yahoo.com'].index, inplace=True)
df.drop(df.loc[df['DOMAIN']=='GMAIL.COM'].index, inplace=True)
df.drop(df.loc[df['DOMAIN']=='qq.com'].index, inplace=True)
df.drop(df.loc[df['DOMAIN']=='163.com'].index, inplace=True)


df.drop(df.loc[df['TLD']!='com'].index, inplace=True)
#df.drop(df.loc[df['TLD']=='uk'].index, inplace=True)
#df.drop(df.loc[df['TLD']=='edu'].index, inplace=True)


print(df.head())
print(df.info())

pd.DataFrame.to_csv(df,"bar" + time.strftime('%Y-%m-%d') + ".csv",',')

