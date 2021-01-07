from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
app = Flask(__name__)


### Fake data as placeholder until DB implementation ###
#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}
restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]
#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}
### End fake data ###

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
    return render_template('restaurants.html', restaurants=restaurants)

"""
Method: newRestaurant()
    - Allows to create a new restaurant
Route:
    '/restaurant/new'
"""
@app.route('/restaurant/new/')
def newRestaurant():
    return render_template('newRestaurant.html')

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
    return render_template('editRestaurant.html', restaurant_id=restaurant_id)

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
    return render_template('menu.html', restaurant=restaurant, items=items)

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
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
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
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return render_template('deleteMenuItem.html', restaurant_id=restaurant_id, item=item)

### END ROUTING ###

if __name__ == '__main__':
    # app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)