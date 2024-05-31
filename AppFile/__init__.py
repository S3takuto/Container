from flask import Flask

app = Flask(__name__)
app.config.from_object('AppFile.config')

from AppFile import views