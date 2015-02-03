'''
Make sure mongo is running
'''

import pymongo, csv, datetime
from pymongo import MongoClient

#client mongodb
client = MongoClient('Localhost',27017)
db = client.japan_tsunami #use the japan_tsunami database
collection = db.phones  #phone collection

#populate the mongodb, pass as argument the path to the csv file
#Rq: longitude then latitude
def populate_mongo(file_path='/db/mongo/data_tsunami.csv'):
	with open(file_path) as csvfile:
		spamreader = csv.reader(csvfile, delimiter=';')
		count = 0
		for row in spamreader:
			proper_date = datetime.datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S,%f") #translate into an understandable time format
			collection.insert({
				"date":proper_date,
				"gsm_cell_code":row[1],
				 "loc":[float(row[3]),float(row[2])],
				  "phone_num":row[4]
			})
			count = count + 1 
			print count

 

#drop the phones collection
def remove_phones():
	collection.drop()


if __name__ == "__main__":
	populate_mongo()

