import  pandas as pd
from time import strftime
import sys
import os   

newFile = sys.argv[1]
#read from csv
df = pd.read_csv(newFile, sep='\,',engine='python')# change this

df['result'] = df['Pts'].map(lambda x: x.lstrip('"').rstrip('"'))

df['result'] = pd.to_numeric(df['result'])

newFileName = os.path.splitext(newFile)[0]
pd.DataFrame.to_csv(df,newFileName + '_' + strftime('%Y-%m-%d') + ".csv",',')