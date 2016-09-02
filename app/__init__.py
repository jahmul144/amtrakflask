from flask import Flask
from flask import request

app = Flask(__name__)

from app.templates import views


