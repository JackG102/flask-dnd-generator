from flask import Flask

app = Flask(__name__)

from app.dnd_generator import bp as dnd_generator_bp
app.register_blueprint(dnd_generator_bp)

from app import routes