# MongoDB configuration for Japan Tsunami project

1. Install MongoDB

Follow those steps from the official website http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/
Rq: At least 3Gb memory space will be needed.

2. Configurate mongoDB

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
