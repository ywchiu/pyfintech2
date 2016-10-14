# house5.py
from flask import Flask,jsonify,request
from flaskext.mysql import MySQL

app=Flask(__name__)
app.config["MYSQL_DATABASE_USER"]="root"
app.config["MYSQL_DATABASE_PASSWORD"]="test"
app.config["MYSQL_DATABASE_DB"]="lvr"

mysql=MySQL()
mysql.init_app(app)

@app.route("/area/")
def getHouse():
    cursor= mysql.get_db().cursor()
    cursor.execute('select address, area, total_price from lvr_data limit 3')
    house_list=[{'address':house[0],
                 'area':house[1],
                 'total_price':house[2]}
                  for house in cursor.fetchall()]
    return jsonify({"data":house_list})
    
if __name__=="__main__":
    app.run()
