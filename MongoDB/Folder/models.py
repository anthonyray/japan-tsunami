from django.db import models
import datetime

# Create your models here.
class Japan:
	japan_cities = list()
	position_list = list()

	def __init__(self):
		self.japan_cities.append(("Tokyo","9 128 090","http://en.wikipedia.org/wiki/Tokyo",35.732727,139.722404))
		self.japan_cities.append(("Yokohama","3 709 777","http://en.wikipedia.org/wiki/Yokohama",35.462635,139.774854))
		self.japan_cities.append(("Osaka","2 685 218","http://en.wikipedia.org/wiki/Osaka",34.705359,135.500729))
		self.japan_cities.append(("Nagoya","2 275 428","http://en.wikipedia.org/wiki/Nagoya",35.193866,136.907394))
		self.japan_cities.append(("Sapporo","1 919 684","http://en.wikipedia.org/wiki/Sapporo",43.179025,141.388028))
		self.japan_cities.append(("Kobe","1 538 281","http://en.wikipedia.org/wiki/Kobe",34.699714,135.187619))
		self.japan_cities.append(("Fukuoka","1 516 575","http://en.wikipedia.org/wiki/Fukuoka",33.643127,130.355035))
		self.japan_cities.append(("Kyoto","1 469 912","http://en.wikipedia.org/wiki/Kyoto",35.043493,135.771593))
		self.japan_cities.append(("Kawasaki","1 459 191","http://en.wikipedia.org/wiki/Kawasaki",35.557485,139.698357))
		self.japan_cities.append(("Saitama","1 250 407","http://en.wikipedia.org/wiki/Saitama",35.867481,139.642576))

		self.position_list.append((35.932727,139.722404))
		self.position_list.append((34.205359,136.580729))
		self.position_list.append((35.032727,139.522404))
		self.position_list.append((33.243127,130.455035))

	def get_cities(self):
		return self.japan_cities

	def get_people(self):
		return self.position_list



class RequestCassandra:
	date, longitude, latitude = (None,None,None)

	def __init__(self, longitude, latitude, date):
		self.date = datetime.datetime.strptime(date,"%Y-%m-%d %H:%M:%S,%f")
		self.longitude = longitude
		self.latitude = latitude

	def search_people(self):
		print "Write a request"