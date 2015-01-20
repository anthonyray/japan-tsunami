import csv
import pandas as pd
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()


# Reading the csv file
data = pd.read_csv('data/data_1MB.csv',delimiter=";",names=["date","gsm","lat","lon","phone"])


for index,row in data.iterrows():
    doc = {
        'timestamp' : row['date'],
        'lon' : row['lon'],
        'lat' : row['lat'],
        'phone': row['phone'],
        'gsm': row['gsm']
    }
    es.index(index="japan", doc_type='locatron', id=index, body=doc)
