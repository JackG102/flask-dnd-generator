from flask import Blueprint

bp = Blueprint('dndgenerator', __name__)

from app.dnd_generator import routes