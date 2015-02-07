````
cqlsh> DROP KEYSPACE japtest;
cqlsh> exit
````

```
python creationProcess.py japtest bigtable
python format_csv.py data_1GB.csv 
```

```
cqlsh> use japtest;
cqlsh> COPY bigtable ("timestamp",codegsm,longitude,latitude,phone) FROM 'extract.csv' WITH HEADER='false' AND DELIMITER=','; 

