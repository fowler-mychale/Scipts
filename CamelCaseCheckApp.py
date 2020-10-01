#!/usr/bin/env python
from pandas import pandas as pd
from time import strftime
import PySimpleGUI as sg


def test(newFile):
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
    pd.DataFrame.to_csv(df,"NewFile " + strftime('%Y-%m-%d') + ".csv",',') 
  

#gui setup
sg.theme('Reddit')

layout = [[sg.In(), sg.FileBrowse(file_types=(("Text Files", "*.csv"),))],
         [sg.Text('Select file then press "Run" to complele process.\nPress "Exit" when finished.')], 
         [sg.Button('Run'), sg.Exit()]]

window = sg.Window('Pattern Application',layout)

while True:  # Event Loop
    event, values = window.read()
    #print(values[0]) #For testing  
    if event == sg.WIN_CLOSED or event  == 'Exit':
      break
    if event == 'Run':
         test(values[0])
         sg.popup('Job Completed.')
window.close()
