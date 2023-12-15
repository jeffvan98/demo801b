from os import environ
from flask_bootstrap import Bootstrap4
from flask import Flask
from main.views import main_bp

prefix = environ.get("REPORT_READER_PREFIX", "")

app = Flask(__name__)
bootstrap = Bootstrap4(app)

app.register_blueprint(main_bp, url_prefix=prefix)