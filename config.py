import pyodbc

class Config:
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://ASHIN/shoopingcart?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    SQLALCHEMY_TRACK_MODIFICATIONS = False







# class Config:
#     SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
