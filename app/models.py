#THIS IS AN UNOFFICIAL VERSION

import datetime
import os
from . import app
from werkzeug.utils import secure_filename
from flask_login import UserMixin


from . import db

class Product(db.Model):
  
  __tablename__ = "products"
  id        = db.Column(db.Integer,    primary_key=True)
  typo      = db.Column(db.String(15), nullable=False)
  trademark = db.Column(db.String(30), nullable=False)
  detail    = db.Column(db.String(30), nullable=True)
  price     = db.Column(db.String(5),  nullable=False)
  bulkprice = db.Column(db.String(5),  nullable=False)
  weight    = db.Column(db.String(7),  nullable=False)
  weightype = db.Column(db.String(2),  nullable=False)
  bulk      = db.Column(db.String(3),  nullable=False)
  image     = db.Column(db.String(200),nullable=True)
  hidden    = db.Column(db.Boolean)
  created_at= db.Column(db.DateTime,   default=datetime.datetime.now())
  modified_at=db.Column(db.DateTime,   default=datetime.datetime.now())
  
  """tasks = db.relationship('Task',lazy='dynamic')"""
  
  @classmethod
  def create_product(cls,form):
    img = ""
    if form.image.data : img = secure_filename(form.image.data.filename)

    product = Product(
      typo     =form.typo.data,
      trademark=form.trademark.data,
      detail   =form.detail.data,
      price    =form.price.data,
      bulkprice=form.bulkprice.data,
      weight   =form.weight.data,
      weightype=form.weightype.data,
      bulk     =form.bulk.data,
      hidden   =form.hidden.data,
      image    =img
      )
    db.session.add(product)
    db.session.commit()
    
    return product

  @classmethod
  def get_by_id(cls, id):
    return Product.query.filter_by(id=id).first()

  @classmethod
  def delete_product(cls, id ):
    product = Product.get_by_id( id )

    filepath = os.path.join(app.instance_path,'static/images', product.image)

    if os.path.exists( filepath ):
      os.remove( filepath )
    else:
      print("No se encontro el directorio '"+filepath+"'")
      print("Durante la eliminacion del producto '"+product.typo+" "+product.trademark+"'")

    db.session.delete(product)
    db.session.commit()

    return True
  
  @classmethod
  def update_product(cls,form,product):
    try:
      f = form.image.data
      sfilename = secure_filename(f.filename)
      setattr(product,'image',sfilename)
      
    except:
      pass

    setattr(product, 'typo',form.typo.data )
    setattr(product, 'trademark',form.trademark.data )
    setattr(product, 'detail',form.detail.data )
    setattr(product, 'price',form.price.data )
    setattr(product, 'bulkprice',form.bulkprice.data )
    setattr(product, 'weight',form.weight.data )
    setattr(product, 'weightype',form.weightype.data )
    setattr(product, 'bulk',form.bulk.data )
    setattr(product, 'hidden',form.hidden.data )
    db.session.commit()

class Query(db.Model):
  __tablename__ = "querys"
  id      = db.Column(db.Integer, primary_key=True)
  name    = db.Column(db.String(30))
  contact = db.Column(db.String(30))
  address = db.Column(db.String(30), nullable=True)
  mail    = db.Column(db.String(50), nullable=True)
  total   = db.Column(db.String(10))
  weight  = db.Column(db.String(10))
  created_at=db.Column(db.DateTime , default=datetime.datetime.now())
  desc    = db.Column(db.Text      , nullable=True)
  products = db.relationship('QueryList')

  @classmethod
  def create_query(cls, form, data):

    query = Query(
      name = form.name.data,
      contact = form.contact.data,
      address = form.address.data,
      mail = form.mail.data,
      total = data[0],
      weight = data[1],
      desc = form.desc.data
      )
    db.session.add(query)
    db.session.flush()
    db.session.commit()
    
    return query.id

  @classmethod
  def get_by_id(cls, id):
    return Query.query.filter_by(id=id).first()

  @classmethod
  def delete_query(cls, id ):
    query = Query.get_by_id( id )
    
    db.session.delete(query)
    db.session.commit()

    return True

class QueryList(db.Model):
  __tablename__ = "querylists"
  id        = db.Column(db.Integer,    primary_key=True)
  typo      = db.Column(db.String(30), nullable=True)
  trademark = db.Column(db.String(30), nullable=True)
  detail    = db.Column(db.String(30), nullable=True)
  price     = db.Column(db.String(5),  nullable=True)
  weight    = db.Column(db.String(10), nullable=True)
  quantity  = db.Column(db.String(10), nullable=True)
  bulk      = db.Column(db.String(3),  nullable=True)
  bulks     = db.Column(db.String(3),  nullable=True)
  units     = db.Column(db.String(3),  nullable=True)
  client_id = db.Column(db.Integer, db.ForeignKey("querys.id"))
  
  @classmethod
  def create_queryList(cls,form,client_id):
    for product in form : 
      q = product[6]
      b = int(product[5])

      if q :
        productq = QueryList(
          typo     =product[0],
          trademark=product[1],
          detail   =product[2],
          price    =product[3],
          weight   =product[4],
          bulk     =b,
          quantity =q,
          bulks    =str(int(q) // b),
          units    =str(int(q) % b),
          client_id=client_id
          )
        db.session.add(productq)
        db.session.commit()
      
    return True

  @classmethod
  def delete_queryList(cls, id ):

    querylist = QueryList.query.filter_by(client_id = id).all()
    
    for i in querylist:
      db.session.delete(i)
      db.session.commit()

    return True

class User(db.Model,UserMixin):
  __tablename__ = "data"
  id = db.Column(db.Integer,    primary_key=True)
  name = db.Column(db.String(10), nullable=True)

  @classmethod
  def get_by_id(cls, id):
    return User.query.filter_by(id=id).first()

class Messages(db.Model):
  __tablename__ = "message"
  id = db.Column(db.Integer, primary_key = True)
  message = db.Column(db.Text, nullable=False)
  disc = db.Column(db.Text, nullable=False)

  @classmethod
  def update(cls,form):
    mm = Messages.query.get_or_404( 1 )
    setattr(mm,'message',form.message.data )
    setattr(mm,'disc',form.disc.data )
    db.session.commit()