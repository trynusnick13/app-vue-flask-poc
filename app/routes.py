from copy import deepcopy

from flask import jsonify, request

from app import app
from app import db
from models import Shop, Mall


def convert_shops_to_dict(shops: list) -> list:
    row = []
    for shop in shops:
        dict_shop = {
            'id': shop.id,
            'Type': shop.Type,
            'Name': shop.Name,
            'City': '',
            'Mall': '',
            'District': '',
        }
        if not shop.malls:
            row.append(dict_shop)
        else:
            for mall in shop.malls:
                temp_shop = deepcopy(dict_shop)
                temp_shop['City'] = mall.City
                temp_shop['Mall'] = mall.Name
                temp_shop['District'] = mall.District
                row.append(temp_shop)

    return row


def convert_malls_to_dict(malls):
    row = []
    appended = False
    for mall in malls:
        temp_mall = {
            'id': mall.id,
            'Name': mall.Name,
            'City': mall.City,
            'District': mall.District,
            'Shop': '',
        }
        # row.append(temp_mall)
        # if not mall.shops:
        #     row.append(temp_mall)
        # else:

        temp_shop = deepcopy(temp_mall)
        for shop in mall.shops:
            temp_shop = deepcopy(temp_mall)
            temp_shop['Shop'] = shop.Name
            row.append(temp_shop)
            appended = True

        if not appended:
            row.append(temp_shop)

    return row


@app.route('/shops', methods=['GET', 'POST'])
def all_shops():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # SHOPS.append({
        #     'id': post_data.get('id'),
        #     'Mall': post_data.get('Mall'),
        #     'Type': post_data.get('Type'),
        #     'Name': post_data.get('Name'),
        #     'City': post_data.get('City'),
        #     'District': post_data.get('District')
        # })
        shop = Shop.query.filter_by(Name=post_data.get('Name')).first()
        if shop is None:

            shop = Shop(
                Type=post_data.get('Type'),
                Name=post_data.get('Name'),
            )
            db.session.add(shop)

        mall = Mall.query.filter_by(Name=post_data.get('Mall')).first()
        if mall is None:
            mall = Mall(
                Name=post_data.get('Mall'),
                City=post_data.get('City'),
                District=post_data.get('District')
            )
            db.session.add(mall)
        repeated_mall = list(filter(lambda mall: mall.Name == post_data.get('Mall'), shop.malls))
        if not(repeated_mall):
            shop.malls.append(mall)
            db.session.add(shop)
            db.session.add(mall)
            db.session.commit()
            response_object['message'] = 'Shop added!'
        else:
            response_object['message'] = 'Shop is already in the mall!'
    else:
        shops = Shop.query.all()
        row = convert_shops_to_dict(shops)

        return jsonify({
            'status': 'success',
            'shops': row
        })


def remove_shop(shop_id, mall_id):
    # db.session.query(Shop).filter(Shop.id == shop_id).delete()
    shop_to_remove = Shop.query.filter(Shop.id == shop_id).first()
    if (not shop_to_remove.malls and mall_id == "empty") or len(shop_to_remove.malls) == 1:
        db.session.query(Shop).filter(Shop.id == shop_id).delete()
    else:
        for mall in shop_to_remove.malls:
            if mall.Name == mall_id:
                shop_to_remove.malls.remove(mall)
                break
    db.session.commit()


def remove_malls(mall_id):
    db.session.query(Mall).filter(Mall.id == mall_id).delete()
    db.session.commit()


@app.route('/shops/<shop_id>/<mall_id>', methods=['PUT', 'DELETE'])
def single_shop(shop_id, mall_id):
    response_object = {
        'status': 'success',
        'message': 'Shop updated!'
    }
    if request.method == 'PUT':
        post_data = request.get_json()
        # remove_shop(shop_id)
        mall = Mall.query.filter_by(Name=post_data.get('Mall')).first()

        # shop = Shop.query.filter_by(Name=post_data.get('Name')).first()

        shop_by_id = Shop.query.filter_by(id=shop_id).first()
        if shop_by_id.Name == post_data.get('Name'):
            shop_by_id.Type = post_data.get('Type')
        else:
            shop_by_id.Type = post_data.get('Type')
            shop_by_id.Name = post_data.get('Name')

        repeated_mall = list(filter(lambda mall_: mall_.Name == post_data.get('Mall'), shop_by_id.malls))
        if not repeated_mall:
            response_object['message'] = 'Shop was not updated!'
            for mall_in_shop in shop_by_id.malls:
                if mall_in_shop.Name == mall_id:
                    shop_by_id.malls.remove(mall_in_shop)
            if mall is None:
                mall = Mall(
                    Name=post_data.get('Mall'),
                    City=post_data.get('City'),
                    District=post_data.get('District')
                )
                # db.session.add(mall)
            else:
                mall.City = post_data.get('City')
                mall.District = post_data.get('District')
            db.session.add(mall)
            shop_by_id.malls.append(mall)
            db.session.add(shop_by_id)

            #     db.session.add(shop_by_id)
            db.session.commit()
            # remove_shop(shop_id)
            response_object['message'] = 'Shop updated!'
        else:
            mall.City = post_data.get('City')
            mall.District = post_data.get('District')
            response_object['message'] = 'Shop was not updated!'
            db.session.add(shop_by_id)
            db.session.commit()
    if request.method == 'DELETE':
        remove_shop(shop_id, mall_id)
        response_object['message'] = 'Shop removed!'
    return jsonify(response_object)


@app.route('/malls', methods=['GET', 'POST'])
def all_malls():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        mall = Mall.query.filter_by(Name=post_data.get('Name')).first()
        if mall is None:
            mall = Mall(
                Name=post_data.get('Name'),
                City=post_data.get('City'),
                District=post_data.get('District')
            )
            db.session.add(mall)
            db.session.commit()
        response_object['message'] = 'Mall added!'
    else:
        malls = Mall.query.all()
        row = convert_malls_to_dict(malls)

        return jsonify({
                'status': 'success',
                'malls': row
            })


@app.route('/malls/<mall_id>', methods=['PUT', 'DELETE'])
def single_mall(mall_id):
    response_object = {
        'status': 'success',
        'message': 'Mall updated!'
    }
    if request.method == 'PUT':
        post_data = request.get_json()
        mall = Mall.query.filter_by(id=mall_id).first()
        mall.City = post_data.get('City')
        mall.District = post_data.get('District')
        mall.Name = post_data.get('Name')
        db.session.add(mall)
        db.session.commit()
    if request.method == 'DELETE':
        remove_malls(mall_id)
        response_object['message'] = 'Mall removed!'
    return jsonify(response_object)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')
