from .. import db
from .forms import ProductForm
from .import product
from flask import render_template,redirect
from ..models import Product

@product.route('/addproduct', methods=['GET','POST'])
def add_product():
    form=ProductForm()
    if form.validate_on_submit():
       name=form.name.data
       decription=form.description.data 
       price=form.price.data
       new_product=Product(name=name,decription=decription,price=price)
       db.session.add(new_product)
       db.session.commit()
    return render_template("product/product.html",form=form)