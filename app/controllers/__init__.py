from app import app, ia, db
from app.ia import costumer, pd, encode_transform, untransform_product, model
from flask import Flask, jsonify, request,render_template,url_for,redirect,abort,flash
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from flask_cors import CORS, cross_origin
from sqlalchemy import select
from app.models.models_spc import Spc_Raw_Data, Customers, Customers_Products, Kaggle_Raw_Data, Transactions, Products, Schema_Migrations

import secrets
import os


# tela inicial
@app.route("/")
def index():
    customer = Customers.query.all()
    transactions= Transactions.query.all()
    customers_products = Customers_Products.query.all()
    products = Products.query.all()
    kaggle_raw_data = Kaggle_Raw_Data.query.all()
    return render_template('home.html', kaggle_raw_data=kaggle_raw_data, products=products, customers_products=customers_products, customer=customer, transactions=transactions)


@app.route("/api")
def showdata():
    customer = Customers.query.all()
    page = request.args.get('page', 1, type=int)
    posts = Customers.query.order_by(Customers.id.desc()).paginate(page=page, per_page=5)
    transactions= Transactions.query.all()
    customers_products = Customers_Products.query.all()
    products = Products.query.all()
    spc_raw_data=Spc_Raw_Data.query.all()
    posts2 = Kaggle_Raw_Data.query.all()
   
    posts3 = Customers.query.all()
   
    return render_template('api.html', posts3=posts3, page=page, posts=posts,customer=customer)

@app.route("/api/<id>", methods=["GET","POST"])
def api(id):
    # breakpoint()
    customers = Customers.query.get_or_404(id)
    cp = Customers_Products.query.filter_by(customer_id=customers.id).all()
    if len(cp) > 0:
        ct = cp[0].active
    else:
        ct = False

    teste=encode_transform({
        "customer_state":customers.state,
        "customer_city": customers.city,
        "customer_age": customers.age,
        "customer_avg_income": customers.avg_income,
        "customer_products_active": ct ,
        "transactions_total_limit": 7626.014464,
        "transactions_category": 'Não Especificado'
    })
    teste2 = teste.reshape(1,-1)
    teste3 =model.predict(teste2)
    teste4= untransform_product(teste3)


        
    products= Products.query.filter_by(id=teste4).first()
    return render_template('recomendacao.html', products=products,teste4=teste4, customers=customers)