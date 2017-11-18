from restaurant import app, db, uploaded_images
from restaurants.models import Restaurant_name

class Menu_items(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	course = db.Column(db.String(80))
	menu_name = db.Column(db.String(80), nullable=False)
	description = db.Column(db.String(250))
	price = db.Column(db.Integer)
	image = db.Column(db.String(80))
	user = db.Column(db.String(80), nullable=False)
	restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant_name.id'))

	@property
	def imgsrc(self):
		return uploaded_images.url(self.image)

	def __init__(self, course, menu_name, description, price, image, user, restaurant_id):
		self.course = course
		self.menu_name = menu_name
		self.description = description
		self.price = price
		self.image = image
		self.user = user
		self.restaurant_id = restaurant_id

	def __repr__(self):
		return '<Menu item %r>' %self.menu_name



