import sys
sys.path.append('/usr/local/lib/python3.4/dist-packages')
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
Data_session = sessionmaker(bind=engine)
session = Data_session()
app = Flask(__name__)


@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def restaurant_menu_json(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])


@app.route('/')
@app.route('/restaurant')
def restaurant():
    output = '<html><body>'
    output += '<h1>Bellow are the Restaurants</h1>'
    for i in session.query(Restaurant).all():
        output += '<h3> %s </h3>' % i.name
        tmp = i.id
        lis = session.query(MenuItem).filter_by(restaurant_id=tmp)
        for j in lis:
            output += '<p> %s </p>' % j.name
            output += '<p> %s </p>' % j.price
        output += "<a href='/restaurant/%d/delete'>delete </a></br>" % int(tmp)
        output += "<a href='/restaurant/%s/edit'> edit</a>" % tmp
        output += '\n\n'
    output += "<form method='POST' enctype='multipart/form-data' action='/restaurant/new/'>" \
              "<h2> Add your restaurant</h2><input name='name' type='text'>" \
              "<input type='submit' value='Submit'> </form>"
    output += "<a href='/restaurant/new'>new</a>"
    output += "</body></html>"
    return output


@app.route('/restaurant/<int:rest_id>/')
def restaurant_id(rest_id):
    restau = session.query(Restaurant).filter_by(id=rest_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=rest_id)

    return render_template('menu.html', restaurant=restau, items=items)


@app.route('/restaurant/new/', methods=['GET', 'POST'])
def new_menu_item():
    if request.method == 'POST':
        new_item = Restaurant(name=request.form['name'])
        session.add(new_item)
        session.commit()
        return redirect(url_for('restaurant'))
    elif request.method == 'GET':
        return render_template('new_menu.html')


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def edit_menu_item(restaurant_id):
    return "page found on edit url"


@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def delete_menu_item(restaurant_id):
    return "page found on delete url"


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)