# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 16:17:43 2015

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

'''
Create a special table into Cassandra database
'''
def createTableCassandra(session,table=""):    
    session.execute("CREATE TABLE "+table+"(timestamp timestamp, latitude float, longitude float, codegsm text, phone text, PRIMARY KEY((timestamp,latitude,longitude)));") 
    print "Table "+table+" created !";
  
'''
Insert one row into special table
'''  
def insertCassandra(session,timestamp,latitude,longitude,table="",codegsm="",phone=""):
    session.execute("insert into "+table+"(timestamp,latitude,longitude,codegsm,phone) VALUES('"+str(timestamp)+"',"+str(latitude)+","+str(longitude)+",'"+str(codegsm)+"','"+str(phone)+"');")

'''
Insert all rows from panda dataframe to Cassandra table
'''
def fillTable(session,data,table=""):
    for i in range(0,len(data.index)):
        timestamp = data.iloc[i][0]
        codegsm = data.iloc[i][1]
        latitude = data.iloc[i][2]
        longitude = data.iloc[i][3]
        phone = data.iloc[i][4]
        insertCassandra(session,timestamp,latitude,longitude,table,codegsm,phone)
        print i

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
Square box around coordinates given distance
d : distance (in km)
'''
def boundingBox(d,lat,lon):
     lat1sup = lat + (d*3.531426/500)
     lon1sup = lon + (d*3.531426/500)
     lat1inf = lat - (d*3.531426/500)
     lon1inf = lon - (d*3.531426/500)     
     return lat1inf,lat1sup,lon1inf,lon1sup

'''
Tell if a date is in a range of 2 dates
'''
def timestampInterval(date,dat_inf,dat_sup):
    if(dat_inf<date<=dat_sup):
        return True
    else:
        return False

'''
Get people datas to prevent from the tsunami
'''
def alertPhones(dat_inf,dat_sup,lat,lon,radius,request_size=100000,table="bigtable4",keyspace="japantsunami"):
    cluster = Cluster()
    session = cluster.connect(keyspace)
    session.default_fetch_size = request_size
    box = boundingBox(radius,lon,lat)
    res_coor = session.execute("select latitude,longitude,timestamp,phone from "+table+" where token(timestamp,latitude,longitude)>=token('"+str(dat_inf)+"',"+str(box[0])+","+str(box[2])+") and token(timestamp,latitude,longitude)<token('"+str(dat_sup)+"',"+str(box[1])+","+str(box[3])+");")   
    phonelist = list()
    for i in range(0,len(res_coor)):
        lat2 = res_coor[i][0]
        lon2 = res_coor[i][1]
        date = res_coor[i][2]    
        phone = str(res_coor[i][3]).split('.')[0]     
        if(haversine(lon,lat,lon2,lat2)<=radius and timestampInterval(date,dat_inf,dat_sup)):
            phonelist.append((lat2,lon2,date,phone))
    return phonelist

#cluster = Cluster()
#session = cluster.connect('japantsunami')
#session.default_fetch_size = 20000
#datinf=datetime(2015, 1, 5, 10, 32)
#datsup=datetime(2015, 1, 10, 10, 32)
#suplat = 36.05522918701172 + 3.531426
#suplon =  140.06179809570312 + 3.531426
#testhaversineinverse = haversine(suplon,suplat,140.06179809570312,36.05522918701172)
#box = boundingBox(500,140.06179809570312,36.05522918701172)
#plop = session.execute("select latitude,longitude,timestamp,phone from bigtable4 where token(timestamp,latitude,longitude)>=token('"+str(datinf)+"',"+str(box[0])+","+str(box[2])+") and token(timestamp,latitude,longitude)<token('"+str(datsup)+"',"+str(box[1])+","+str(box[3])+");")
#data =  pd.read_csv('datajapan.csv',sep=';',names=['timestamp','codegsm','latitude','longitude','phone'])
#res = alertPhones(datinf,datsup,34.241238,137.433197,500)
