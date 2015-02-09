#!/usr/bin/env python

"""
reated on Tue Jan 20 16:17:43 2015
@author: Paco
"""
"""
------------------------------------------------
--- Japan Tsunami Project
--- Cassandra drivers and phone alert
------------------------------------------------
"""

import pandas as pd
from datetime import datetime
from math import radians, cos, sin, asin, sqrt
from cassandra.cluster import Cluster

def createKeyspaceCassandra(session,keyspace=""):
    session.execute("CREATE KEYSPACE "+keyspace+" WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor' : 5};")
    print "Keyspace "+keyspace+" created !";

'''
Create a special table into Cassandra database
'''
def createTableCassandra(session,table=""):
    session.execute("CREATE TABLE "+table+"(timestamp timestamp, codegsm text, latitude float, longitude float, phone text, PRIMARY KEY((codegsm),timestamp));")
    print "Table "+table+" created !";

'''
Insert one row into a table
'''
def insertCassandra(session,timestamp,latitude,longitude,table="",codegsm="",phone=""):
    session.execute("insert into "+table+"(timestamp,latitude,longitude,codegsm,phone) VALUES('"+str(timestamp)+"',"+str(latitude)+","+str(longitude)+",'"+str(codegsm)+"','"+str(phone)+"');")

'''
Calculate Haversine distance of 2 points
'''
def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c  # 6367 km is the radius of the Earth
    return km

'''
Get people datas to prevent from the tsunami
'''
def alertPhones(dat_inf,dat_sup,lat,lon,radius,request_size=100000,table="bigtable4",keyspace="japantsunami"):
    cluster = Cluster()
    session = cluster.connect(keyspace)
    session.default_timeout = 30
    session.default_fetch_size = request_size
    res_coor = session.execute("select latitude,longitude,timestamp,phone from "+table+" where timestamp>='"+str(dat_inf)+"' and timestamp<'"+str(dat_sup)+"' allow filtering;")
    phonelist = list()
    for i in range(0,len(res_coor)):
	lon2 = res_coor[i][0]
        lat2 = res_coor[i][1]
        date = res_coor[i]
        phone = str(res_coor[i][3])
        if(haversine(lon,lat,lon2,lat2)<=radius):
            phonelist.append((lat2,lon2,date,phone))
    return phonelist

def multipleInsertCreation(data,table="bigtable"):
    begin = "BEGIN BATCH \n "
    end = " APPLY BATCH;"
    cmd = ""
    for i in range(0,len(data)-1):
        timestamp = data[i][2]
        phone = data[i][3]
        latitude = data[i][0]
        longitude = data[i][1]
        temp = "insert into "+table+"(timestamp,latitude,longitude,phone) VALUES('"+str(timestamp)+"',"+str(latitude)+","+str(longitude)+",'"+str(phone)+"')"
        cmd = cmd + " " + temp + " \n "
    return begin + cmd + end

def multipleInsertExec(keyspace="",cmd=""):
    cluster = Cluster()
    session = cluster.connect(keyspace)
    session.execute(cmd)

