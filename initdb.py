import pymongo
import os
import json
from dotenv import load_dotenv

load_dotenv()
MONGO_CONNECTION = os.getenv('MONGO_CONNECTION')
myclient = pymongo.MongoClient(MONGO_CONNECTION)
mydb = myclient['planet_db']
planet_col = mydb['planet_collection']

planet_list = {}

with open("planet_template.json", "r") as plFile:
    planet_list = json.load(plFile)
# print(type(planet_list))
x = planet_col.insert_many(planet_list['planets'])