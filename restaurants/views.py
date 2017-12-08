from restaurant import app, db
from flask import render_template, url_for, redirect, request, flash, session as login_session, make_response, abort  # NOQA
from restaurants.forms import New_restaurantForm
from restaurants.models import Restaurant_name
from menu_item.models import Menu_items
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import requests


CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']  # NOQA


@app.route('/')
@app.route('/restaurants')
def restaurants():
    all_names = Restaurant_name.query.all()
    return render_template('restaurants/restaurants.html',
                           all_names=all_names)


@app.route('/myrestaurants')
def my_restaurants():
    myrestaurants = Restaurant_name.query.filter_by(user=login_session['username']).all()  # NOQA
    return render_template('restaurants/my_restaurants.html',
                           myrestaurants=myrestaurants)


@app.route('/restaurant/new', methods=['GET', 'POST'])
def new():
    form = New_restaurantForm()
    if 'username' in login_session:
        if request.method == 'POST':
            if form.validate_on_submit():
                restaurant_name = Restaurant_name(form.restaurant_name.data,
                                                  login_session['username'])
                db.session.add(restaurant_name)
                db.session.commit()
                flash(restaurant_name.name + " successfully created")
                return redirect(url_for('my_restaurants'))
    else:
        return redirect(url_for('login'))
    return render_template('restaurants/new.html', form=form)


@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def edit(restaurant_id):
    form = New_restaurantForm()
    restaurant_name = Restaurant_name.query.filter_by(id=restaurant_id).first()  # NOQA
    if 'username' in login_session:
        restaurant = Restaurant_name.query.filter_by(id=restaurant_id).first()
        if restaurant.user == login_session['username']:
            if request.method == 'POST':
                if form.restaurant_name.data:
                    restaurant_name.name = form.restaurant_name.data
                    db.session.add(restaurant_name)
                    db.session.commit()
                    flash(restaurant_name.name + " successfully updated")
                    return redirect(url_for('my_restaurants'))
        else:
            abort(403)

    else:
        return redirect(url_for('login'))
    return render_template('restaurants/edit.html',
                           form=form,
                           value=restaurant_name.name,
                           restaurant_id=restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/delete')
def delete(restaurant_id):
    if 'username' in login_session:
        restaurant = Restaurant_name.query.filter_by(id=restaurant_id).first()
        if restaurant.user == login_session['username']:
            menu_item = Menu_items.query.filter_by(restaurant_id=restaurant_id).delete()  # NOQA
            restaurant = Restaurant_name.query.filter_by(id=restaurant_id).first()  # NOQA
            name = restaurant.name
            db.session.delete(restaurant)
            db.session.commit()
            flash(name+" successfully deleted")
            return redirect(url_for('my_restaurants'))
        else:
            abort(403)


@app.route('/login')
def login():
    state = ''.join(random.choice(string.ascii_uppercase+string.digits) for x in range(32))  # NOQA
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'), 200)  # NOQA
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    flash("You are now logged in as %s" % login_session['username'])
    return '<h4>Redirecting...</h4>'


@app.route('/logout')
def logout():
    if 'username' in login_session:
        login_session.pop('username')
        login_session.pop('picture')
        login_session.pop('email')
        login_session.pop('access_token')
        login_session.pop('gplus_id')
        flash('You are now logged out')
        return redirect(url_for('restaurants'))
    else:
        abort(401)
