#!/bin/sh

s3cmd get s3://bigdata-paristech/projet2014/data/$3 $3

python creationProcess.py $1 $2

