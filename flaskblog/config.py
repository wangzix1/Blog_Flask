import os

class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    #SECRET_KEY = os.environ.get('SECRET_KEY')#'5791628bb0b13ce0c676dfde280ba245'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER= 'smtp.googlemail.com'
    MAIL_PORT= 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "zoey.wang.zixuan@gmail.com"#os.environ.get('EMAIL_USER') #"zoey.wang.zixuan@gmail.com"
    MAIL_PASSWORD = "Wutong1luo!"#os.environ.get('EMAIL_PASS') #"Wutong1luo!"
    

