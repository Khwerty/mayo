from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.datastructures import CombinedMultiDict
from werkzeug.utils import secure_filename
from . import app, login_manager

import os

from .forms import AddProductForm, AddQuery, CreateFormLogin, MessagesForm
from .models import Product, Query, QueryList, User, Messages

from .credentials import *

@login_manager.user_loader
def load_user( id ):
  return User.get_by_id( id )

page = Blueprint('page',__name__)

@page.route('/',methods=['GET','POST'])
def index():
  flash("Debes Seleccionar Almenos 1 Producto")
  message = Messages.query.get_or_404( 1 )

  products = Product.query.all()
  form = AddProductForm(CombinedMultiDict((request.files, request.form)))
  fq = AddQuery(request.form)

  if request.method == 'POST':

    if current_user.is_authenticated:
    
      Product.create_product(form)
      f = form.image.data
      if f :
        sfilename = secure_filename(f.filename)
        f.save(os.path.join(app.instance_path,'static/images',sfilename))
      return redirect(url_for('.index'))

    else:        
      datalist = request.form.getlist("data")
      d = datalist[:-2]
      q = 7

      querylist = [d[k:k+q] for k in range(0, len(d), q)]
      totales = datalist[-2:]
      client_id = Query.create_query( fq, totales )
      QueryList.create_queryList( querylist, client_id )

      mm = Messages.query.get_or_404( 1 )
      query = Query.query.get_or_404( client_id )
      products = QueryList.query.filter_by(client_id=client_id).all()

      return(
        render_template(
        'resume/resume.html',
        title = 'Resumen de Pedido',
        query = query,
        lists = products,
        mm = mm
        )
      )

  return(
    render_template(
      'index/index.html',
      title = 'Mayorista',
      products = products,
      form = form,
      fq = fq,
      mm = message
    )
  )

@page.route('/login',methods=['GET','POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('.home'))
  form = CreateFormLogin(request.form)

  if request.method == 'POST':
    if form.user.data == CREDENTIAL_USER and form.passs.data == CREDENTIAL_PASS :

      user = User.get_by_id(1)
      
      login_user( user, remember=True )

      return redirect(url_for('.home'))
    else:
      return redirect(url_for('.login'))

  return(
    render_template(
      'login/login.html',
      title = 'Login',
      form = form)
  )

@page.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('.login'))  

@page.route('/admin/home',methods=['GET','POST'])
@login_required
def home():
  messages = Messages.query.get_or_404( 1 )
  form = MessagesForm(request.form, obj=messages)

  querys = Query.query.all()
  lists = QueryList.query.all()
  
  if request.method == "POST":
    Messages.update( form )

  return(
    render_template(
      'admin/home/home.html',
      title = 'Pedidos',
      querys = querys,
      lists = lists,
      current_page = 'home',
      form = form
    )
  )

@page.route('/admin/delete/query/<int:client_id>')
@login_required
def delete_query( client_id ):
  query = Query.query.get_or_404( client_id )

  QueryList.delete_queryList( query.id )
  Query.delete_query( query.id )
  
  return redirect(url_for('.home'))

@page.route('/admin/delete/product/<int:product_id>')
@login_required
def delete_product( product_id ):
  product = Product.query.get_or_404( product_id )

  if Product.delete_product( product.id ):
    return redirect(url_for('.index'))

@page.route('/admin/edit/product/<int:product_id>',methods=['GET','POST'])
@login_required
def edit_product( product_id ):
  product = Product.query.get_or_404( product_id )
  form = AddProductForm(CombinedMultiDict((request.files, request.form)), obj=product)

  products = Product.query.all()

  if request.method == 'POST':
    Product.update_product(form,product)

    try: 
      f = form.image.data

      if f :
        sfilename = secure_filename(f.filename)
        f.save(os.path.join(app.instance_path,'static/images',sfilename))
    except:
      pass
      
    return redirect(url_for('.index'))

  return(
    render_template(
      'index/index.html',
      title='Mayorista',
      products=products,
      form=form)
    )
