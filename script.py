import pandas as pd
import pymongo as pm

# se configura el puerto del servicio de mongo | la base de datos | la colección  ||  se insertan los docs | se transforman los datos de csv a json
pm.MongoClient("mongodb://localhost:27017/")["tennis_tournaments"]["tournaments"].insert_many(pd.read_csv("./atp_tennis.csv").to_dict("records"))




# llst data:
for x in pm.MongoClient("mongodb://localhost:27017/")["tennis_tournaments"]["tournaments"].find():
	print(x)