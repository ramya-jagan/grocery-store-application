from flask import Flask, request, jsonify
import products_dao
from sql_connection import get_connection  
from flask_cors import CORS  

app=Flask(__name__)
CORS(app)

connection=get_connection()
@app.route('/getProducts',methods=['GET'])
def get_products():
  products=products_dao.get_all_products(connection)
  response=jsonify(products)
  response.headers.add("Access-Control-Allow-Origin","*")
  return response


if __name__=="__main__":
  print('Starting Python Flask For Grocery Store Management System')
  app.run(port=5000)
