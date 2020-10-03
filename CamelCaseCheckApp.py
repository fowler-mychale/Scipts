from pandas import pandas as pd
from time import strftime
import PySimpleGUI as sg
import os
def pget(newFile):
    #read from csv
    df = pd.read_csv(newFile)
    #drop NULL vakue from Answer column
    df.dropna(axis=0, subset=['Check'],inplace = True)
    #function to check CamelCase
    def is_camel_case(s):
      if s != s.lower() and s != s.upper() and "_" not in s and sum(i.isupper() for i in s[1:-1]) == 2:
          return True
      return False
    #run is_camel_case function on column 'Row' in dataframe
    df['Row'] = df['Check'].apply(is_camel_case)
    #drop row if Boolean False
    df.drop(df.loc[df['Row'] == False].index, inplace=True)
    #Save to new csv file
    newFileName = os.path.splitext(newFile)[0]
    pd.DataFrame.to_csv(df,newFileName + '_' + strftime('%Y-%m-%d') + ".csv",',') 
#gui setup
sg.theme('Reddit')
layout = [[sg.Input(), sg.FileBrowse(file_types=(("Csv Files", "*.csv"),("Text Files", "*.txt")))],
         [sg.Text('Select file then press "Run" to complele process.\nPress "Exit" when finished.')],
         [sg.Button('Run'), sg.Exit()]]
window = sg.Window('Pattern Application',layout)
while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event  == 'Exit':
      break
    if event == 'Run':
        try:
        	try:
        		pget(values[0])
        		sg.popup('Job Completed.')
        	except KeyError as err:
        		sg.Print(err, 'Error with the input file. Please check it and try again.')
        except Exception as err:
        	sg.Print(err)
window.close()
