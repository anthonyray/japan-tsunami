# MongoDB configuration for Japan Tsunami project


###0. Problématique

* Rechercher des personnes dans un périmètre autour de l'épicentre
* Prévenir ces personnes par ordre croissant de distance à l'épicentre
* Les prévenir le plus vite possible, dans l'idéal, avant d'avoir été touché par l'épicentre

  -> Indexer les données par temps

* Selectionner les personnes présente dans la zone pendant un interval de temps déterminé


###1. Install MongoDB

Follow those steps from the official website http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/
Rq: At least 3Gb memory space will be needed.

###2. Configurate mongoDB

Run MongoDB:
```
sudo service mongod start
```
Create a folder for the database:
```
mkdir -p /db/mongo```

**In this folder**, connect DataBase:
```
mongo```
Use a new database, that we will call "japan_tsunami"
```
>use japan_tsunami
```


###3. Populate the database

We will create a new collection like this json.
```
phone_loc = {
date:2015-01-16 01:02:16,
gsm_cell_code:Yok_19,
latitude:35.462635,
longitude:139.774854,
phone_num:593071
}
```
Install _pymongo_


###X. Increase performances

####1. Using index

Indexes sort the database, we will sort the database by date, as we will be looking within a specific range of dates
To create this index, enter this code in the mongo shell
```
>db.phones.ensureIndex({date:1})
```

For this query
```
>db.phones.find({ date:{ $gte: new Date("2015-01-25T13:00:00.000Z"), $lt: new Date("2015-01-25T13:00:30.000Z") } }).explain()
```
The performance with and without index
```
"n" : 94,
"nscannedObjects" : 18200000,
"nYields" : 142195,
"millis" : 110559

"n" : 94,
"nscannedObjects" : 94,
"nYields" : 43,
"millis" : 1242
```
