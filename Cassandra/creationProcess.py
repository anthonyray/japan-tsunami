#!/usr/bin/env python

"""
------------------------------------------------
--- Japan Tsunami Project
--- Process 1
------------------------------------------------
"""

import sys
import cassandraTest as ca
from cassandra.cluster import Cluster


crea_keyspace = sys.argv[1]
crea_table = sys.argv[2]

print sys.argv[1],sys.argv[2]

cluster = Cluster()
session = cluster.connect()
ca.createKeyspaceCassandra(session,keyspace=crea_keyspace)

session = cluster.connect(crea_keyspace)
ca.createTableCassandra(session,table=crea_table)
ca.createTableCassandra(session,table=str(crea_table+'bis'))
