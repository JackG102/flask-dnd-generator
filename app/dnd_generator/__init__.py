from flask import Blueprint

bp = Blueprint('dndgenerator', __name__, template_folder='templates')

from app.dnd_generator import routes