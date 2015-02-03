'''
Make sure mongo is running
'''

import pymongo, datetime
from pymongo import MongoClient

#client mongodb
client = MongoClient('Localhost',27017)
db = client.japan_tsunami #use the japan_tsunami database
collection = db.phones  #phone collection


def get_phones(epi_long, epi_lat, radius=500000, time, duration_min=30):
	time_min = datetime.datetime.strptime(time,"%Y-%m-%d %H:%M:%S,%f")
	time_max = time_min + datetime.timedelta(minutes=duration_min)
	collection.find({
		$and:[
			date:{
				$gte: time_min,
				$lt: time_max
			},
			loc:{
				$near:{
					$geometry: {type: "Point", coordiantes:[epi_lat,epi_long]},
					$maxDistance: radius
				}
			}
		]
	})






db.phones.find({
	$and:[
	{
		loc:{
			$near:[142.103302,31.111784],
			$maxDistance:500
		}
	},
	{
		date:{	
			$gte: new Date("2015-01-25T00:00:00.000Z"),
			$lt: new Date("2015-01-25T00:01:00.000Z")	
		}
	}]	
})

