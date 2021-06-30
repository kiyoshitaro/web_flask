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
import os
import logging

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'static/uploads'
app.config['OUTPUT_PATH'] = 'static/outputs'

app.config['UPLOAD_FOLDER'] = "static/uploads"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# def create_app(config_class=Config):
# ...
# if not app.debug and not app.testing:
#     ...

#     if app.config['LOG_TO_STDOUT']:
#         stream_handler = logging.StreamHandler()
#         stream_handler.setLevel(logging.INFO)
#         app.logger.addHandler(stream_handler)
#     else:
#         if not os.path.exists('logs'):
#             os.mkdir('logs')
#         file_handler = RotatingFileHandler('logs/myblog.log',
#                                            maxBytes=10240, backupCount=10)
#         file_handler.setFormatter(logging.Formatter(
#             '%(asctime)s %(levelname)s: %(message)s '
#             '[in %(pathname)s:%(lineno)d]'))
#         file_handler.setLevel(logging.INFO)
#         app.logger.addHandler(file_handler)

#     app.logger.setLevel(logging.INFO)
#     app.logger.info('Myblog startup')

# return app
