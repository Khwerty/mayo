from flask_wtf import FlaskForm as Form
from wtforms import StringField,BooleanField,IntegerField,SelectField,TextAreaField
from wtforms import validators
from flask_wtf.file import FileField

class AddProductForm(Form):
  
  typo =      StringField('typo',[
    validators.DataRequired(message='Este campo es obligatorio')
  ])
  trademark = StringField('trademark',[
    validators.DataRequired('Este campo es obligatorio')
  ])
  detail =    StringField('detail')
  price =     StringField('price',[
    validators.DataRequired(message='Este campo es obligatorio')
  ])
  bulkprice = StringField('bulkprice',[
    validators.DataRequired(message='Este campo es obligatorio')
  ])
  weight =    StringField('weight',[
    validators.DataRequired(message='Este campo es obligatorio')
  ])
  weightype = SelectField('weightype',choices=['Kg','g','L','ml'])
  bulk =      StringField('bulk',[
    validators.DataRequired(message='Este campo es obligatorio')
  ])
  image =     FileField('image')
  hidden =    BooleanField('hidden')

class AddQuery(Form):
  name =    StringField('name',[ 
    validators.DataRequired(message='Este campo es obligatorio'),
    validators.length(max=30)
  ])
  contact = StringField('contact',[
    validators.DataRequired(message='Este campo es obligatorio'),
    validators.length(max=30)
  ])
  address = StringField('address',[
    validators.length(max=50)
  ])
  mail =    StringField('mail',[ 
    validators.length(max=50)
  ])
  desc =    TextAreaField('desc',render_kw={'rows': 6})

class CreateFormLogin(Form):

  user = StringField('user')
  passs = StringField('passs')

class MessagesForm(Form):
  message = TextAreaField('desc',[
    validators.length(max=300)],
    render_kw={'rows': 4}
  )
  disc = TextAreaField('disc',[
    validators.length(max=300)],
    render_kw={'rows': 4}
  )