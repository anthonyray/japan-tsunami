#!/usr/bin/env python

import cassandraTest as ca
from datetime import datetime

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
keyspace_t = 'dodo'

hop = ca.alertPhones(date_inf_t,date_sup_t,lat_t,lon_t,radius_t,size_req_t,table_t,keyspace_t)
print hop[0]


