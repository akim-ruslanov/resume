import helper
from flask import Flask, request, Response
import json

app = Flask(__name__)

@ap.route('/')
def home():
    return 'Home Page???'

@app.route('item/new', methods = ['POST'])
def add_item():
    req_data = request.get_json()
    item = req_data['item']

    res_data = helper.add_to_list(item)

    if res_data is None:
        response = Response("{'error': 'Item not added - " + item + "'}", 
        status=400 , mimetype='application/json')
        return response
    
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

# // some changes for commit