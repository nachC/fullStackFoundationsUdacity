from flask import Flask, json, render_template, request, url_for, redirect, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

### Database connection ###
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
print "Created database session"
### End ###

### JSON - API Endpoints (GET requests) ###
"""
Method: restaurantsJSON()
    - responds with a list of all restaurants, in JSON format
route:
    '/restaurants/JSON/'
"""
@app.route('/restaurants/JSON/')
def restaurantsJSON():
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurants=[r.serialize for r in restaurants])

"""
Method: restaurantMenuJSON()
    - responds with the menu items for the given restaurant, in JSON format
Route:
    '/restaurants/restaurant_id/menu/JSON/'
Params:
    @ (int) restaurant_id
"""
@app.route('/restaurants/<int:restaurant_id>/menu/JSON/')
def restaurantMenuJSON(restaurant_id):
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return jsonify(MenuItems=[i.serialize for i in items])

"""
Method: restaurantsJSON()
    - responds with a the requested menu item, in JSON format
Route:
    '/restaurants/restaurant_id/menu/menu_id/JSON/'
Params:
    @ (int) restaurant_id
    @ (int) menu_id
"""
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON/')
def menuItemJSON(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(restaurant_id=restaurant_id, id=menu_id).one()
    return jsonify(MenuItem=item.serialize)

### END API ###

### ROUTING ###
"""
Method: showRestaurants()
    - Shows all the restaurants in the DB
Route:
    '/'
    '/restaurants'
"""
@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)

"""
Method: newRestaurant()
    - Allows to create a new restaurant
Route:
    '/restaurant/new'
"""
@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        restaurant = Restaurant(name = request.form['name'])
        try:
            session.add(restaurant)
            session.commit()
            return redirect(url_for('showRestaurants'))
        except:
            session.rollback()
            raise
    return render_template('newRestaurant.html')

"""
Method: editRestaurant()
    - Allows to edit a restaurant
Route:
    '/restaurant/restaurant_id/edit'
Params:
    @ (int) restaurant_id
"""
@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        restaurant.name = request.form['name']
        try:
            session.add(restaurant)
            session.commit()
            return redirect(url_for('showRestaurants'))
        except:
            session.rollback()
            raise
    return render_template('editRestaurant.html', restaurant=restaurant)

"""
Method: deleteRestaurant()
    - Allows to delete a restaurant
Route:
    '/restaurant/restaurant_id/delete'
Params:
    @ (int) restaurant_id
"""
@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        try:
            session.delete(restaurant)
            session.commit()
            return redirect(url_for('showRestaurants'))
        except:
            session.rollback()
            raise
    return render_template('deleteRestaurant.html', restaurant=restaurant)

"""
Method: showMenu()
    - Shows the menu for a given restaurant
Route:
    '/restaurant/restaurant_id/'
    '/restaurant/restaurant_id/menu'
Params:
    @ (int) restaurant_id
"""
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template('menu.html', restaurant=restaurant, items=items)

"""
Method: newMenuItem
    - Allows to create a new menu item for the given restaurant
Route:
    '/restaurant/restaurant_id/menu/new'
Params:
    @ (int) restaurant_id
"""
@app.route('/restaurant/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        course = request.form['course']
        newItem = MenuItem(name=name, price=price, description=description, course=course, restaurant_id=restaurant_id)
        try:
            session.add(newItem)
            session.commit()
            return redirect(url_for('showMenu', restaurant_id=restaurant_id))
        except:
            session.rollback()
            print 'exception thrown'
            raise
    return render_template('newMenuItem.html', restaurant_id=restaurant_id)

"""
Method: editMenuItem()
    - Allows to edit a given menu item for a given restaurant
Route:
    '/restaurant/restaurant_id/menu/menu_id/edit'
Params:
    @ (int) restaurant_id
    @ (int) menu_id
"""
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        item.name = request.form['name']
        try:
            session.add(item)
            session.commit()
            return redirect(url_for('showMenu', restaurant_id=restaurant_id))
        except:
            session.rollback()
            raise
    return render_template('editMenuItem.html', restaurant_id=restaurant_id, item=item)

"""
Method: deleteMenuItem()
    - Allows to delete a given menu item for a given restaurant
Route:
    '/restaurant/restaurant_id/menu/menu_id/delete'
Params:
    @ (int) restaurant_id
    @ (int) menu_id
"""
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        try:
            session.delete(item)
            session.commit()
            return redirect(url_for('showMenu', restaurant_id=restaurant_id))
        except:
            session.rollback()
            raise
    return render_template('deleteMenuItem.html', restaurant_id=restaurant_id, item=item)

### END ROUTING ###

if __name__ == '__main__':
    app.secret_key = 'testSecretKey'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)