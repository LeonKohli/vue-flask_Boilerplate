import os

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = "postgresql://your_username:your_password@localhost/your_db_name"

SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
