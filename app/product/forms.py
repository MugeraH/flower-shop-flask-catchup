from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from flask_wtf.file import FileField,FileAllowed
class ProductForm(FlaskForm):
    name=StringField('Name of flower')
    description=StringField('Description')
    price= IntegerField('price')
    pic=FileField('Upload Flower Picture',)
    submit=SubmitField('Add Product')


