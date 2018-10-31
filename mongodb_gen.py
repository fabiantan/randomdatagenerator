import pymongo
from pymongo import MongoClient
import datetime
from random import *
import string
import time


location = [
        "selangor",
        "kedah",
        "kuala lumpur",
        "perlis",
        "sabah",
        "sarawak",
        "negeri sembilan",
        "pahang",
        "perak",
        "kelantan",
        "terrengganu",
        "penang",
        "melaka",
        "johor",
]


min_char = 8
max_char = 12
allchar = string.ascii_letters + string.digits
domain = [
    "@gmail.com",
    "@ymail.com",
    "@yahoo.com",

]

name = [ "".join(choice(allchar) for x in range(randint(min_char, max_char))) ]
for i in range(999):
    name.append("".join(choice(allchar) for x in range(randint(min_char, max_char))))

client = MongoClient('mongodb://localhost:27017/',username='',password='')
db = client['testdb']
collection = db['purchase']

import random
   
while True:
    item_array=[]

    product_type = [
            10000,
            10001,
            10002,
            10003,
            10004,
            10005,
            10006,
    ]

    for z in range(0,random.randint(1,4)):
        item={}
        product= product_type.pop(random.randint(0,6-z))
        item.update(type = product )
        item.update(quantity = random.randint(1,2))
        item_array.append(item)
        

    post = {"email": string.lower(name[random.randint(0,999)])+ domain[random.randint(0,2)],
            "state": location[random.randint(0,13)],
            "timestamp": datetime.datetime.utcnow().strftime('%s'),
            "items": item_array }
    post_id = collection.insert(post)
    print(post)
    time.sleep(1)

