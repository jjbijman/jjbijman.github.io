
import csv
import os, glob
import pandas as pd


path ='C:/Users/dvanleent/Deloitte (O365D)/Knowledge Graphs AICE BUILD 2020 - General/data/'
all_files = glob.glob(os.path.join(path, "*.csv"))
dfs = []
for f in all_files:    
    dfs.append(pd.read_csv(f))
df_merged   = pd.concat(dfs, ignore_index=False)
df_merged.to_csv( "merged.csv")


