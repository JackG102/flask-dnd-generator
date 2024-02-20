from flask import Blueprint

bp = Blueprint(
  'dndgenerator', 
  __name__, 
  template_folder='templates/dnd_generator',
  static_folder="static",
  static_url_path='/dnd_generator_static_files'
  )

from app.dnd_generator import routes