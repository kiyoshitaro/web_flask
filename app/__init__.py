from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import joblib

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


model = joblib.load(open('models/pipe_clf_checkpoint.joblib', 'rb'))


from app import routes, models
