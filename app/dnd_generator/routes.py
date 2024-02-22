from flask import render_template, jsonify
from app import app
from app.dnd_generator.Npc import Npc

@app.route('/npc')
def return_npc():
  return render_template('npc.html')

@app.route('/npc_json')
def return_npc_json():
  testNPC = Npc()
  npc = testNPC.describe()
  return jsonify(npc)  