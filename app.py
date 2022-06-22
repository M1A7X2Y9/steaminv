from flask import Flask
from flask_restful import Api, Resource, reqparse
from addict import Dict
import requests
import json
from urllib.request import urlopen


app = Flask(__name__)
api = Api(app)

plush = "https://steamcommunity.com/profiles/76561198342081700/inventory/json/730/2"
# PLUSHBERRY
responsep = requests.request("GET", plush)
# print(response.text)
datap = Dict(responsep.json())

tradable = ""

k1p = datap.rgDescriptions['4365582890_188530139']
knife1p = k1p['market_hash_name']
# trade1 = k1['tradable']
# if(trade1 == 1):
#     tradable = "tradable"
# else:
#     tradable = "Not tradable"
k2p = datap.rgDescriptions['4878981359_188530139']
knife2p = k2p['market_hash_name']
# trade2 = k2['tradable']
# if(trade2 == 0):
#     tradable = "tradable"
# else:
#     tradable = "Not tradable"
k3p = datap.rgDescriptions['4887874194_188530139']
knife3p = k3p['market_hash_name']
# trade3 = k3['tradable']
# if(trade3 == 0):
#     tradable = "tradable"
# else:
#     tradable = "Not tradable"

falcon = "https://steamcommunity.com/id/rohangundaliya/inventory/json/730/2"
# FALCON
response = requests.request("GET", falcon)
# print(response.text)
data = Dict(response.json())

tradable = ""

k1f = data.rgDescriptions['4887988744_188530139']
knife1f = k1f['market_hash_name']
# trade1 = k1['tradable']
# if(trade1 == 1):
#     tradable = "tradable"
# else:
#     tradable = "Not tradable"

# k2 = data.rgDescriptions['4878981359_188530139']
# knife2 = k2['market_hash_name']
# trade2 = k2['tradable']
# if(trade2 == 0):
#     tradable = "tradable"
# else:
#     tradable = "Not tradable"

# k3 = data.rgDescriptions['4887874194_188530139']
# knife3 = k3['market_hash_name']
# trade3 = k3['tradable']
# if(trade3 == 0):
#     tradable = "tradable"
# else:
#     tradable = "Not tradable"


# ONLY PUBG
opubg = "https://steamcommunity.com/id/krutarthchovatiya4/inventory/json/730/2"
# FALCON
response = requests.request("GET", opubg)
# print(response.text)
data = Dict(response.json())

tradable = ""

k1o = data.rgDescriptions['4878981360_188530721']
knife1o = k1o['market_hash_name']


# 0
zero = "https://steamcommunity.com/id/krishnapandeyu124//inventory/json/730/2"
# FALCON
response = requests.request("GET", zero)
# print(response.text)
data = Dict(response.json())

tradable = ""

k1z = data.rgDescriptions['4878981360_188530721']
knife1z = k1z['market_hash_name']


# Happymice
happymice = "https://steamcommunity.com/id/Happymice81/inventory/json/730/2"
# FALCON
response = requests.request("GET", happymice)
# print(response.text)
data = Dict(response.json())

tradable = ""

k1h = data.rgDescriptions['3608122587_188530139']
knife1h = k1h['market_hash_name']


# Maverik
maverik = "https://steamcommunity.com/id/ismailcaptain/inventory/json/730/2"
# FALCON
response = requests.request("GET", maverik)
# print(response.text)
data = Dict(response.json())

tradable = ""

k1m = data.rgDescriptions['3608107027_188530139']
knife1m = k1m['market_hash_name']


knives = [

    # plushberry
    {
        
        "id": 1,
        "knifeName": knife1p,
        "owner": "plushberry",

        "url": plush
    },
    {
        "knifeName": knife2p,
        "id": 2,
        "owner": "plushberry",
        "url": plush
    },
    {
        "knifeName": knife3p,
        "id": 3,
        
        "owner": "plushberry",
        "url": plush
    },


    # falcon
    {
        "id": 4,
        "owner": "falcon",
        "knifeName": knife1f,
        "url": falcon
    },
    # {
    #     "id": 5,
    #     "owner": "falcon",
    #     "knifeName": knife2f,
    #     "url": falcon
    # },
    # {
    #     "id": 6,
    #     "owner": "falcon",
    #     "knifeName": knife3f,
    #     "url": falcon
    # },


    # onlypubg
    {
        "id": 5,
        "knifeName": knife1o,
        "owner": "onlypubg",
        "url": opubg
    },
    # {
    #     "id": 8,
    #     "owner": "falcon",
    #     "knifeName": knife2f,
    #     "url": falcon
    # },
    # {
    #     "id": 9,
    #     "owner": "falcon",
    #     "knifeName": knife3f,
    #     "url": falcon
    # },



    # zero
    {
        "knifeName": knife1z,
        "id": 6,
                
        "owner": "0",

        "url": zero
    },

    # {
    #     "id": 7,
    #     "owner": "plushberry",
    #     "knifeName": knife2p,
    #     "url": plush
    # },
    # {
    #     "id": 8,
    #     "owner": "plushberry",
    #     "knifeName": knife3p,
    #     "url": plush
    # },


    # Happymice
    {
        "url": happymice,
        "id": 8,
        "owner": "Happymice",
        "knifeName": knife1h
        
    },
    # {
    #     "id": 2,
    #     "owner": "0",
    #     "knifeName": knife2z,
    #     "url": plush
    # },
    # {
    #     "id": 3,
    #     "owner": "0",
    #     "knifeName": knife3z,
    #     "url": plush
    # },

    # Maverik
    {
        "id": 9,
        "knifeName": knife1m,
        "owner": "Maverik",
        
        "url": maverik
    }
    # {
    #     "id": 2,
    #     "owner": "0",
    #     "knifeName": knife2z,
    #     "url": plush
    # },
    # {
    #     "id": 3,
    #     "owner": "0",
    #     "knifeName": knife3z,
    #     "url": plush
    # }
]


class message(Resource):

    def get(self, owner):

        for message in knives:
            # for filter
            userf = ["falcon"]
            for sub in knives:
                if owner == "falcon":
                    res = next(
                        (sub for sub in knives if sub["owner"] == "falcon"), None)
                    return res, 200
                elif owner == "plushberry":
                    res = next(
                        (sub2 for sub2 in knives if sub2["owner"] == "plushberry"), None)
                    return res, 200
                elif owner == "opubg":
                    res = next(
                        (sub2 for sub2 in knives if sub2["owner"] == "opubg"), None)
                    return res, 200
                elif owner == "0":
                    res = next(
                        (sub2 for sub2 in knives if sub2["owner"] == "0"), None)
                    return res, 200

                elif owner == "Happymice":
                    res = next(
                        (sub2 for sub2 in knives if sub2["owner"] == "Happymice"), None)
                    return res, 200
                elif owner == "Maverik":
                    res = next(
                        (sub2 for sub2 in knives if sub2["owner"] == "Maverik"), None)
                    return res, 200
                elif app.route('/all'):
                    return knives, 200
                else:
                    return "Knife not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("owner")
        parser.add_argument("knifeName")
        # parser.add_argument("tradable")
        params = parser.parse_args()

        for message in knives:
            if(id == message["id"]):
                return f"message with id {id} already exists", 400

        message = {
            "id": int(id),
            "knifeName": params["knifeName"]
            # "tradable": params["tradable"]
        }

        knives.append(message)
        return message, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("knifeName")
        # parser.add_argument("tradable")
        params = parser.parse_args()

        for message in knives:
            if(id == message["id"]):
                message["owner"] = params["owner"]
                message["knifeName"] = params["knifeName"]
                message["tradable"] = params["tradable"]
                return message, 200

        message = {
            "id": id,
            "owner": "owner",
            "knifeName": params["knifeName"]
            # "tradable": params["tradable"]
        }

        knives.append(message)
        return message, 201

    def delete(self, id):
        global knives
        knives = [message for message in knives if message["id"] != id]
        return f"knife with id {id} is deleted.", 200


api.add_resource(message, "/getknife",
                 "/getknife/", "/getknife/<string:owner>")
if __name__ == '__main__':
    app.run(debug=True)
