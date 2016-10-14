# house2.py
from flask import Flask,jsonify
from flask.ext.pymongo import PyMongo
app=Flask(__name__)
app.config["MONGO_DBNAME"]="lvr"
mongo=PyMongo(app)

@app.route("/area/<area>")
def getHouse(area):
    cur=mongo.db.lvrdata.find({'area':area}).limit(30)
    house_list=[{'address':house['address'],
                 'area':house['area'],
                 'total_price':house['total_price']}
                  for house in cur]
    return jsonify({"data":house_list})
if __name__=="__main__":
    app.run()