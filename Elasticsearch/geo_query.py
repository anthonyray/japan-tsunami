from elasticsearch import Elasticsearch


es = Elasticsearch()

res = es.search(index="japan", body={"filtered" : {"query" : {"match_all" : {}},"filter" : {"geo_distance" : {"distance" : "200km","location" : {"lat" : 40,"lon" : -70}}}}})
