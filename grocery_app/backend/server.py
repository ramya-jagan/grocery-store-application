from flask import Flask, request, jsonify
import products_dao
import uom_dao
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

@app.route('/getUOM',methods=['GET'])
def get_uom():
  response=uom_dao.get_uoms(connection) 
  response=jsonify(response) 
  response.headers.add('Access-control-Allow-origin','*')
  return response



@app.route('/deleteProduct',methods=['POST'])
def delete_product():
  return_id=products_dao.delete_product(connection, request.form['product_id'])
  response=jsonify({'product_id': return_id})
  response.headers.add("Access-Control-Allow-Origin","*")
  return response

@app.route('/insertProduct',methods=['POST'])
def insert_product():
  request_payload=request.form['data']
  product_id= product['product_name'],product['uom_id'],product['price_per_unit']
  response=jsonify({'product_id': return_id})
  response.headers.add("Access-Control-Allow-Origin","*")
  return response

if __name__=="__main__":
  print('Starting Python Flask For Grocery Store Management System')
  app.run(port=5000)
