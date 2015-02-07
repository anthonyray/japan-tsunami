#!/usr/bin/env python

"""
reated on Tue Jan 20 16:17:43 2015
@author: Paco
"""
"""
------------------------------------------------
--- Japan Tsunami Project
--- Process 1
------------------------------------------------
"""

import sys
import cassandraTest as ca
from cassandra.cluster import Cluster

# sys.argv[1]

crea_keyspace = sys.argv[1]
crea_table = sys.argv[2]

print sys.argv[1],sys.argv[2]

cluster = Cluster()
session = cluster.connect()
ca.createKeyspaceCassandra(session,keyspace=crea_keyspace)

session = cluster.connect(crea_keyspace)
ca.createTableCassandra(session,table=crea_table)
ca.createTableCassandra(session,table=str(crea_table+'bis'))

'''
datacsv = ca.fromCSVtoDataframe(crea_file)

offset = int(crea_offset)
for i in range(0,int(crea_loop)):
    if(i == 0):
        test = ca.multipleInsertCreation(data=datacsv[0:offset],table=crea_table)
        ca.multipleInsertExec(keyspace=crea_keyspace,cmd=test)
        print "-------------------------------------------------"
    else:
        u = i*offset
        uu = u + offset
        test = ca.multipleInsertCreation(data=datacsv[u:uu],table=crea_table)
        ca.multipleInsertExec(keyspace=crea_keyspace,cmd=test)
        print "-------------------------------------------------"
'''

