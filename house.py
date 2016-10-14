# house.py
from flask import Flask,jsonify
from flask.ext.pymongo import PyMongo
app=Flask(__name__)
app.config["MONGO_DBNAME"]="lvr"
mongo=PyMongo(app)

@app.route("/")
def getHouse():
    cur=mongo.db.lvrdata.find().limit(30)
    # house_list = []
    # for house in cur
    #     house_list.append({'address': house['address']})
    house_list=[{'address':house['address'],
                 'area':house['area'],
                 'total_price':house['total_price']}
                  for house in cur]
    return jsonify({"data":house_list})

if __name__=="__main__":
    app.run()