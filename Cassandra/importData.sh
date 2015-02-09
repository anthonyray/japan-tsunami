#!/bin/sh

#touch cqlcom
#chmod 777 cqlcom
#echo "DROP KEYSPACE japtest;" > cqlcom
#cqlsh -f cqlcom 

#python creationProcess.py japtest bigtable
python creationProcess.py $1 $2

#python format_csv.py data_1GB.csv 
python format_csv.py $3