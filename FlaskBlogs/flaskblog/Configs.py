import os



class Config:
    SECRET_KEY = '123456789987456321'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'idreesrehan234@gmail.com'
    MAIL_PASSWORD = 'salmanmayo321'