#THIS IS AN UNOFFICIAL VERSION
from flask import Flask

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__, instance_path="F:/Projects/webdev/mayzog/app")

db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()

from .views import page

def create_app(config):
  app.config.from_object(config)

  csrf.init_app(app)
  login_manager.init_app(app)
  login_manager.login_view= '.login'
  app.register_blueprint(page)
  
  with app.app_context():
    db.init_app(app)
    db.create_all()
  return app