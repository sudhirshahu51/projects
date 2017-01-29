from Find_Restaurant import find_restaurant
from models import Base, Restaurant
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///restaruants.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


@app.route('/restaurants', methods=['GET', 'POST'])
def all_restaurants_handler():
    if request.method == 'GET':
        # RETURN ALL RESTAURANTS IN DATABASE
        restaurants = session.query(Restaurant).all()
        return jsonify(restaurants=[i.serialize for i in restaurants])
    elif request.method == 'POST':
        # MAKE A NEW RESTAURANT AND STORE IT IN DATABASE
        location = request.form.get('location', '')
        meal_type = request.form.get('meal_type', '')
        restaurant_info = find_restaurant(meal_type, location)
        if restaurant_info != "No Restaurants Found" and restaurant_info != 'No such place found':
            restaurant = Restaurant(restaurant_name=str(restaurant_info['name']),
                                    restaurant_address=str(restaurant_info['address']),
                                    restaurant_image=restaurant_info['image'])
            session.add(restaurant)
            session.commit()
            return jsonify(restaurant=restaurant.serialize)
        else:
            return jsonify({"error": "No Restaurants Found for %s in %s" % (meal_type, location)})


@app.route('/restaurants/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def restaurant_handler(id):
    restaurant = session.query(Restaurant).filter_by(id=id).one()
    if request.method == 'GET':
        # RETURN A SPECIFIC RESTAURANT
        return jsonify(restaurant=restaurant.serialize)
    elif request.method == 'PUT':
        # UPDATE A SPECIFIC RESTAURANT
        address = request.form.get('address')
        image = request.form.get('image')
        name = request.form.get('name')
        if address:
            restaurant.restaurant_address = address
        if image:
            restaurant.restaurant_image = image
        if name:
            restaurant.restaurant_name = name
        session.commit()
        return jsonify(restaurant=restaurant.serialize)
    elif request.method == 'DELETE':
        # DELETE A SPECIFIC RESTAURANT
        session.delete(restaurant)
        session.commit()
        return jsonify("Restaurant Deleted")


if __name__ == '__main__':
    app.debug = True
    app.run()
