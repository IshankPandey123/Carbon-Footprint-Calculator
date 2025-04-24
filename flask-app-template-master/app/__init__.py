# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__,static_url_path='/static')

# csrf = CSRFProtect(app)
# app.config.update(
#     SESSION_KEY_SECURE=False,
#     SECRET_KEY='NONBINARY'
# )

#Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('configuration.ProductionConfig')
app.config.from_object('app.configuration.ProductionConfig')
#app.config.from_object('configuration.TestingConfig')

bs = Bootstrap(app) #flask-bootstrap
from app import views
