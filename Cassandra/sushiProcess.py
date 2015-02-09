#!/usr/bin/env python

import cassandraTest as ca
from datetime import datetime
import sys

'''
alertPhones(dat_inf,dat_sup,lat,lon,radius,request_size=100000,table="bigtable4",keyspace="japantsunami")
'''

# list : ((lat2,lon2,date,phone))
dateinfrecup = sys.argv[7].split('-')
date_inf_t = datetime(int(dateinfrecup[0]),int(dateinfrecup[1]),int(dateinfrecup[2]),int(dateinfrecup[3]),int(dateinfrecup[4]))
datesuprecup = sys.argv[8].split('-')
date_sup_t = datetime(int(datesuprecup[0]),int(datesuprecup[1]),int(datesuprecup[2]),int(datesuprecup[3]),int(datesuprecup[4]))
lat_t = float(sys.argv[5])
lon_t = float(sys.argv[6])
radius_t = int(sys.argv[9])
size_req_t = 1000000
table_t = sys.argv[2]
keyspace_t = sys.argv[1]

hop = ca.alertPhones(date_inf_t,date_sup_t,lat_t,lon_t,radius_t,size_req_t,table_t,keyspace_t)
print hop[0]
print hop[1]
print "----------------------- "+str(len(hop))+" -----------------------"

crea_offset = sys.argv[3]
crea_loop = sys.argv[4]
offset = int(crea_offset)
for i in range(0,int(crea_loop)):
    if(i == 0):
        test = ca.multipleInsertCreation(data=hop[0:offset],table=str(table_t+'bis'))
        ca.multipleInsertExec(keyspace=keyspace_t,cmd=test)
        print "-------------------------------------------------"
    else:
        u = i*offset
        uu = u + offset
        test = ca.multipleInsertCreation(data=hop[u:uu],table=str(table_t+'bis'))
        ca.multipleInsertExec(keyspace=keyspace_t,cmd=test)
	print "-------------------------------------------------"


