#! /usr/bin/env python

import subprocess
import math

class ClusterManager:

	nodes_info = [
		("Tokyo",35.732727,139.722404),
		("Yokohama",35.462635,139.774854),
		("Osaka",34.705359,135.500729),
		("Nagoya",35.193866,136.907394),
		("Sapporo",43.179025,141.388028)
	]


	def __init__(self):
		print "prout"



	def get_closest_node(self, lon, lat):
		lon = float(lon)
		lat = float(lat)
		min_v = None 
		min_d = None

		for city in self.nodes_info:
			d = math.sqrt( (float(city[2])-lon)**2 + (float(city[1]))**2 )
			if min_v == None or min_d > d:
				min_v = city
				min_d = d

		status = self.node_status(disable)
		print status

		return min_v




	def node_status(self, status="disable"):
		if status == "disable":
			bashCommand = "nodetool -h 172.31.60.189 disablegossip"
		else: 
			bashCommand = "nodetool -h 172.31.60.189 enablegossip"

		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output = process.communicate()[0]





