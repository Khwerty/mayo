import urllib.parse

d = urllib.parse.quote_plus("EseCuEler@1")

class Config:
  SECRET_KEY = 'W4r3h0u$3'

class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:'+str(d)+'@localhost/mayo'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ENGINE_OPTIONS = {'pool_pre_ping':True}

config = {
  'development': DevelopmentConfig,
  'default': DevelopmentConfig
}