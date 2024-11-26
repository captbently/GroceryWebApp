from flask import Flask, request, jsonify
from sql import get_sql
import mysql.connector
import json

import products
import orders
import units

app = Flask(__name__)

connection = get_sql

@app.route('/getUnits', methods=['GET'])
def get_units():
    response = units.get_units(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders.get_all_orders(connection)
    reponse = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id,
    })
    response.headers.add('Access-Control-Allow-Origin')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id,
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)