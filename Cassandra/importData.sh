#!/bin/sh


# Argument 1 : keyspace to create 
# Argument 2 : table to create
# Argument 3 : name of the data to import in the cluster

#touch cqlcom
#chmod 777 cqlcom
#echo "DROP KEYSPACE japtest;" > cqlcom
#cqlsh -f cqlcom 

#python creationProcess.py japtest bigtable
python creationProcess.py $1 $2

#python format_csv.py data_1GB.csv 
python format_csv.py $3

touch cqlcom
chmod 777 cqlcom
echo "COPY bigtable (\"timestamp\",codegsm,longitude,latitude,phone) FROM 'extract.csv' WITH HEADER='false' AND DELIMITER=',';" > cqlcom
cqlsh -k $1 -f cqlcom

