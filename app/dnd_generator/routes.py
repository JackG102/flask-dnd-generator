from flask import render_template, jsonify
from app import app
from app.dnd_generator.Npc import Npc

@app.route('/npc')
def home():
  testNPC = Npc()
  npc = testNPC.describe()
  return jsonify(npc)
  