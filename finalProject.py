from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
app = Flask(__name__)

### ROUTING ###
"""
Method: showRestaurants()
    - Shows all the restaurants in the DB
route:
    '/'
    '/restaurants'
"""
@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    return 'This page will show all the restaurants'

"""
Method: newRestaurant()
    - Allows to create a new restaurant
Route:
    '/restaurant/new'
"""
@app.route('/restaurant/new/')
def newRestaurant():
    return 'This page will be for making a new restaurant'

"""
Method: editRestaurant()
    - Allows to edit a restaurant
Route:
    '/restaurant/restaurant_id/edit'
Params:
    @ (int) restaurant_id
"""
@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    return 'This page will be for editing restaurant %s' % restaurant_id

"""
Method: deleteRestaurant()
    - Allows to delete a restaurant
Route:
    '/restaurant/restaurant_id/delete'
Params:
    @ (int) restaurant_id
"""
@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return 'This page will be for deleting restaurant %s' % restaurant_id

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
    return 'This page is the menu for restaurant %s' % restaurant_id

"""
Method: newMenuItem
    - Allows to create a new menu item for the given restaurant
Route:
    '/restaurant/restaurant_id/menu/new'
Params:
    @ (int) restaurant_id
"""
@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):
    return 'This page is for making a new Menu Item for restaurant %s' % restaurant_id

"""
Method: editMenuItem()
    - Allows to edit a given menu item for a given restaurant
Route:
    '/restaurant/restaurant_id/menu/menu_id/edit'
Params:
    @ (int) restaurant_id
    @ (int) menu_id
"""
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return 'This page is for editing menu item %s' % menu_id

"""
Method: deleteMenuItem()
    - Allows to delete a given menu item for a given restaurant
Route:
    '/restaurant/restaurant_id/menu/menu_id/delete'
Params:
    @ (int) restaurant_id
    @ (int) menu_id
"""
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return 'This page is for deleting menu item %s' % menu_id

if __name__ == '__main__':
    # app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)