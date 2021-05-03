import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(Configuration)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# SHOPS = [
#     {
#         'id': uuid.uuid4().hex,
#         'Mall': 'Gulliver',
#         'Type': 'Clothes',
#         'Name': 'H&M',
#         'City': 'Kyiv',
#         'District': 'Podil'
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'Mall': 'Dream Town',
#         'Type': 'Technologies',
#         'Name': 'MOYO',
#         'City': 'Kyiv',
#         'District': 'Obolon'
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'Mall': 'Dream Town 2',
#         'Type': 'Toys',
#         'Name': 'Budinok igrashok',
#         'City': 'Kyiv',
#         'District': 'Obolon'
#     }
# ]
#
# MALLS = [
#     {
#         'id': uuid.uuid4().hex,
#         'Name': 'Gulliver',
#         'City': 'Kyiv',
#         'District': 'Podil'
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'Name': 'Dream Town',
#         'City': 'Kyiv',
#         'District': 'Obolon'
#     }
# ]
#
#
#
#
# @app.route('/shops', methods=['GET', 'POST'])
# def all_shops():
#     response_object = {'status': 'success'}
#     if request.method == 'POST':
#         post_data = request.get_json()
#         SHOPS.append({
#             'id': post_data.get('id'),
#             'Mall': post_data.get('Mall'),
#             'Type': post_data.get('Type'),
#             'Name': post_data.get('Name'),
#             'City': post_data.get('City'),
#             'District': post_data.get('District')
#         })
#         response_object['message'] = 'Shop added!'
#     else:
#         return jsonify({
#             'status': 'success',
#             'shops': SHOPS
#         })
#
#
# def remove_shop(shop_id):
#     for shop in SHOPS:
#         if shop['id'] == shop_id:
#             SHOPS.remove(shop)
#             return True
#     return False
#
#
# @app.route('/shops/<shop_id>', methods=['PUT', 'DELETE'])
# def single_shop(shop_id):
#     response_object = {'status': 'success'}
#     if request.method == 'PUT':
#         post_data = request.get_json()
#         remove_shop(shop_id)
#         SHOPS.append({
#             'id': uuid.uuid4().hex,
#             'Mall': post_data.get('Mall'),
#             'Type': post_data.get('Type'),
#             'Name': post_data.get('Name'),
#             'City': post_data.get('City'),
#             'District': post_data.get('District')
#         })
#         response_object['message'] = 'Shop updated!'
#     if request.method == 'DELETE':
#         remove_shop(shop_id)
#         response_object['message'] = 'Shop removed!'
#     return jsonify(response_object)
#
#
# @app.route('/malls', methods=['GET', 'POST'])
# def all_malls():
#     response_object = {'status': 'success'}
#     if request.method == 'POST':
#         post_data = request.get_json()
#         MALLS.append({
#             'id': uuid.uuid4().hex,
#             'Name': post_data.get('Name'),
#             'City': post_data.get('City'),
#             'District': post_data.get('District')
#         })
#         response_object['message'] = 'Mall added!'
#     else:
#         return jsonify({
#             'status': 'success',
#             'malls': MALLS
#         })
#
#
# def remove_malls(mall_id):
#     for mall in MALLS:
#         if mall['id'] == mall_id:
#             MALLS.remove(mall)
#             return True
#     return False
#
#
# @app.route('/malls/<mall_id>', methods=['PUT', 'DELETE'])
# def single_mall(mall_id):
#     response_object = {'status': 'success'}
#     if request.method == 'PUT':
#         post_data = request.get_json()
#         remove_shop(mall_id)
#         MALLS.append({
#             'id': uuid.uuid4().hex,
#             'Name': post_data.get('Name'),
#             'City': post_data.get('City'),
#             'District': post_data.get('District')
#         })
#         response_object['message'] = 'Mall updated!'
#     if request.method == 'DELETE':
#         remove_malls(mall_id)
#         response_object['message'] = 'Mall removed!'
#     return jsonify(response_object)
#
# # sanity check route
# @app.route('/ping', methods=['GET'])
# def ping_pong():
#     return jsonify('pong!')

if __name__ == '__main__':
    app.run()