from flask_wtf import Form 
from wtforms import validators, StringField

class New_restaurantForm(Form):
	restaurant_name = StringField('Restaurant Name', [validators.Required()])