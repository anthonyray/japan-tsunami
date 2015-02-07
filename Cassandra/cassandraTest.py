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
    session.execute("CREATE TABLE "+table+"(timestamp timestamp, codegsm text, latitude float, longitude float, phone text, PRIMARY KEY((timestamp,latitude,longitude)));") 
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
    print "Connexion Ok"
    session.default_fetch_size = request_size
    print "size ok"
    box = boundingBox(radius,lon,lat)
    print "box ok"
    res_coor = session.execute("select latitude,longitude,timestamp,phone from "+table+" where token(timestamp,latitude,longitude)>=token('"+str(dat_inf)+"',"+str(box[0])+","+str(box[2])+") and token(timestamp,latitude,longitude)<token('"+str(dat_sup)+"',"+str(box[1])+","+str(box[3])+");")   
    print "Session ok"
    phonelist = list()
    for i in range(0,len(res_coor)):
	lat2 = res_coor[i][0]
        lon2 = res_coor[i][1]
        date = res_coor[i][2]    
        phone = str(res_coor[i][3]).split('.')[0]     
        if(haversine(lon,lat,lon2,lat2)<=radius and timestampInterval(date,dat_inf,dat_sup)):
            phonelist.append((lat2,lon2,date,phone))
    print phonelist[1]
    return phonelist

'''
Convert CSV file into dataframe
'''
def fromCSVtoDataframe(csvfile=''):
    data =  pd.read_csv(csvfile,sep=';',names=['timestamp','codegsm','latitude','longitude','phone'])   
    data['timestamp'] = data['timestamp'].apply(lambda x: x.split(',')[0])
    return data

def multipleInsertCreation(data,table="bigtable"):
    begin = "BEGIN BATCH \n "
    end = " APPLY BATCH;"
    cmd = ""
    for i in range(0,len(data.index)-1):
        timestamp = data.iloc[i][0]
        codegsm = data.iloc[i][1]
        latitude = data.iloc[i][2]
        longitude = data.iloc[i][3]
        phone = data.iloc[i][4]    
        temp = "insert into "+table+"(timestamp,latitude,longitude,codegsm,phone) VALUES('"+str(timestamp)+"',"+str(latitude)+","+str(longitude)+",'"+str(codegsm)+"','"+str(phone)+"')"
        cmd = cmd + " " + temp + " \n " 
        print i
    return begin + cmd + end

def multipleInsertCreation2(data,table="bigtable"):
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
        print i
    return begin + cmd + end


def multipleInsertExec(keyspace="",cmd=""):
    cluster = Cluster()
    session = cluster.connect(keyspace)   
    session.execute(cmd)

#####################################################################

yop = list((12,11,'yop','po'))
yop.append((13,1313,'fsf','gdg'))
yop.append((4648,456,'gfdg','ff'))

print yop[0:1]

'''
cluster = Cluster()
session = cluster.connect()
createKeyspaceCassandra(session,keyspace="japtest2")

session = cluster.connect('japtest2')
createTableCassandra(session,table='bigtable')

datacsv = fromCSVtoDataframe('data1MB.csv')
#insertion = multipleInsertCreation(datas,table='bigtable')
#multipleInsertExec(keyspace='japtest2',cmd=insertion)
offset = 1000
for i in range(0,100):
    if(i == 0):
        test = multipleInsertCreation(data=datacsv[0:offset],table="bigtable")
        multipleInsertExec(keyspace="japtest2",cmd=test)
        print "-------------------------------------------------"
    else:
        u = i*offset
        uu = u + offset
        test = multipleInsertCreation(data=datacsv[u:uu],table="bigtable")
        multipleInsertExec(keyspace="japtest2",cmd=test)
        print "-------------------------------------------------"
'''

