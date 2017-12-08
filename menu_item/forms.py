from flask_wtf import Form
from wtforms import validators, StringField, RadioField, IntegerField
from flask_wtf.file import FileField, FileAllowed


class New_menu(Form):
    course = RadioField('Course', [validators.Required()],
                        choices=[('Appetizers', 'Appetizers'),
                                 ('Beverages', 'Beverages'),
                                 ('Main Course', 'Main Course'),
                                 ('Dessert', 'Dessert')])
    item_name = StringField('Item Name', [validators.Required()])
    image = FileField('Image', validators=[
            FileAllowed(['jpg', 'png', 'jpeg'], 'Images only')])
    description = StringField('Description')
    price = IntegerField('Price', [validators.NumberRange(min=0, max=1000)])
