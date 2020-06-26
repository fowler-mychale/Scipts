#Convert plain text to csv 
import os
import pandas as pd
from datetime import datetime
import sys
newFile = sys.argv[1]
save_path = pd.read_csv(newFile)

in_filename = os.path.join(save_path,'New Text Document.txt')
out_filename = os.path.join(save_path, datetime.now().strftime("%Y_%m_%d.csv"))

df = pd.read_csv(in_filename, sep=",")
df.to_csv(out_filename, index=False)
