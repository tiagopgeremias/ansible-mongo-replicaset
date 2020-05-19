from pymongo import MongoClient
import random


mongo_cluster = [
	'192.168.41.20:27017',
	'192.168.41.21:27017',
	'192.168.41.22:27017'	
]

try:
  print("MongoDB Cluster Info:::")
  client = MongoClient(mongo_cluster,replicaset='rs0')
  cluster_info = client.admin.command('ismaster')
  for host in cluster_info['hosts']:
    if host == cluster_info['primary']:
      print("\tPRIMARY NODE: {}".format(host))
    else:
      print("\tSLAVE NODE: {}".format(host))
except Exception as error:
  print(error)
