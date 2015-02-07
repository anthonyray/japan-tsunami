import pandas as pd
import sys
import csv

csvfile= sys.argv[1]
data =  pd.read_csv(csvfile,sep=';',names=['timestamp','codegsm','latitude','longitude','phone'])
data['timestamp'] = data['timestamp'].apply(lambda x: x.split(',')[0])

data.to_csv('extract.csv',header=False,index=False,sep=",",quoting=csv.QUOTE_ALL)
