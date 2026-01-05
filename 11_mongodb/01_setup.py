from pymongo import MongoClient

client=MongoClient("mongodb://admin:admin123@localhost:27017/")
#  mongodb url-> mongodb://username:password@localhost:port/agar uske koi specific document etc 
# is bare me aur depth me badme padh liyo 

print(client.list_database_names())