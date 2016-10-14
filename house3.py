# house3.py
from flask import Flask,jsonify,request
from flask.ext.pymongo import PyMongo
app=Flask(__name__)
app.config["MONGO_DBNAME"]="lvr"
mongo=PyMongo(app)

@app.route("/area/", methods=['POST'])
def getHouse():
    if request.method=='POST':
        area=request.form['area']
        cur=mongo.db.lvrdata.find({'area':area}).limit(30)
        house_list=[{'address':house['address'],
                     'area':house['area'],
                     'total_price':house['total_price']}
                      for house in cur]
        return jsonify({"data":house_list})
    
if __name__=="__main__":
    app.run()
