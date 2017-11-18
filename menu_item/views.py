from restaurant import app, db, uploaded_images
from flask import render_template, url_for, redirect, request, flash, session as login_session, abort
from menu_item.models import Menu_items
from menu_item.forms import New_menu
from restaurants.models import Restaurant_name

@app.route('/restaurant/<int:restaurant_id>/menu')
@app.route('/restaurant/<int:restaurant_id>')
def menu(restaurant_id):
	menu_items = Menu_items.query.filter_by(restaurant_id=restaurant_id)
	restaurant = Restaurant_name.query.filter_by(id=restaurant_id).first()
	username = restaurant.user
	return render_template('menu_item/menu_item.html', restaurant_id=restaurant_id, menu_items=menu_items, username=username, name=restaurant.name)

@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def new_menu(restaurant_id):
	form = New_menu()
	if 'username' in login_session:
		restaurant = Restaurant_name.query.filter_by(id=restaurant_id).first()
		if restaurant.user == login_session['username']:
			if request.method == 'POST':
				if form.validate_on_submit():
					image = request.files['image']
					filename = None
					try:
						filename = uploaded_images.save(image)
					except:
						flash('Image was not uploaded')
					menu_item = Menu_items(form.course.data, form.item_name.data, form.description.data, form.price.data, filename, login_session['username'], restaurant_id)
					db.session.add(menu_item)
					db.session.commit()
					flash("Menu item successfully added")
					return redirect(url_for('menu', restaurant_id=restaurant_id))
		else:
			abort(403)
	else:
		return redirect(url_for('login'))

	return render_template('menu_item/new_menu.html', restaurant_id=restaurant_id, form=form)

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit', methods=['GET', 'POST'])
def menu_edit(restaurant_id, menu_id):
	form = New_menu()
	menu_item = Menu_items.query.filter_by(id=menu_id, restaurant_id=restaurant_id).first()
	if 'username' in login_session:
		restaurant = Restaurant_name.query.filter_by(id=restaurant_id).first()
		if restaurant.user == login_session['username']:
			if request.method == 'POST':
				if form.validate_on_submit():
					image = request.files['image']
					filename = None
					try:
						filename = uploaded_images.save(image)
						menu_item.image = filename
					except:
						flash('Image was not updated')
					menu_item.course = form.course.data
					menu_item.menu_name = form.item_name.data
					menu_item.price = form.price.data
					db.session.add(menu_item)
					db.session.commit()
					flash("Menu Item " + menu_item.menu_name + " successfully updated.")
					return redirect(url_for('menu', restaurant_id=restaurant_id))
		else:
			abort(403)
	else:
		return redirect(url_for('login'))

	return render_template('menu_item/menu_edit.html', form=form, name=menu_item.menu_name,
							restaurant_id=restaurant_id, menu_id=menu_id, price=menu_item.price, course=menu_item.course)

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete')
def menu_delete(restaurant_id, menu_id):
	if 'username' in login_session:
		restaurant = Restaurant_name.query.filter_by(id=restaurant_id).first()
		if restaurant.user == login_session['username']:
			menu_item = Menu_items.query.filter_by(id=menu_id, restaurant_id=restaurant_id).first()
			db.session.delete(menu_item)
			db.session.commit()
			flash(menu_item.menu_name + " successfully deleted.")
			return redirect(url_for('menu', restaurant_id=restaurant_id))
		else:
			abort(403)