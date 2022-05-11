from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import Product


@main.route('/')
def index():
    product=Product.query.all()

    return render_template('index.html',products=product)
