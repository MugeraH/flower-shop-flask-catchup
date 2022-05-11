import os

class Config:
  
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    


# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'

class ProdConfig(Config):
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/flowerdb'
    pass
    


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost:5432/flowerdb'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
