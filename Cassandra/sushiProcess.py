#!/usr/bin/env python

import cassandraTest as ca
from datetime import datetime
import sys

'''
alertPhones(dat_inf,dat_sup,lat,lon,radius,request_size=100000,table="bigtable4",keyspace="japantsunami")
'''

# list : ((lat2,lon2,date,phone))
date_inf_t = datetime(2015,1,5,10,32)
date_sup_t = datetime(2015,1,10,10,30)
lat_t = 36.055
lon_t = 140.061
radius_t = 500
size_req_t = 1000000
table_t = 'bigtable'
keyspace_t = 'japjapo'

hop = ca.alertPhones(date_inf_t,date_sup_t,lat_t,lon_t,radius_t,size_req_t,table_t,keyspace_t)
print hop[0]
print hop[12]
print "----------------------- "+str(len(hop))+" -----------------------"

print "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
print hop[0:2]
print "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"


crea_offset = sys.argv[1]
crea_loop = sys.argv[2]
offset = int(crea_offset)
for i in range(0,int(crea_loop)):
    if(i == 0):
        test = ca.multipleInsertCreation2(data=hop[0:offset],table=str(table_t+'bis'))
        ca.multipleInsertExec(keyspace=keyspace_t,cmd=test)
        print "-------------------------------------------------"
    else:
        u = i*offset
        uu = u + offset
        test = ca.multipleInsertCreation2(data=hop[u:uu],table=str(table_t+'bis'))
        ca.multipleInsertExec(keyspace=keyspace_t,cmd=test)
	print "-------------------------------------------------"


