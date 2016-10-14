# house4.py
from flask import Flask,jsonify,request
from flask.ext.pymongo import PyMongo
app=Flask(__name__)
app.config["MONGO_DBNAME"]="lvr"
mongo=PyMongo(app)

@app.route("/area/<area>/<page>")
def getHouse(area, page):
    cnt=mongo.db.lvrdata.find({'area':area}).count()
    cur=mongo.db.lvrdata.find({'area':area}).skip(30*(int(page)-1)).limit(30)
    house_list=[{'address':house['address'],
                 'area':house['area'],
                 'total_price':house['total_price']}
                  for house in cur]
    return jsonify({"data":house_list,'count':cnt})
    
if __name__=="__main__":
    app.run()
