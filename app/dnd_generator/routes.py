from flask import render_template, jsonify
from app import app
from app.dnd_generator.Npc import Npc
from app.dnd_generator.Tavern import Tavern


@app.route('/npc')
def return_npc():
  return render_template('npc.html')

@app.route('/npc_json')
def return_npc_json():
  testNPC = Npc()
  npc = testNPC.describe()
  return jsonify(npc)

@app.route('/tavern')
def return_tavern():
  tavern = Tavern().describe()
  return render_template('tavern.html', tavernObj=tavern)

@app.route('/tavern_json')
def return_tavern_json():
  jsonTavern = Tavern()
  tavern = jsonTavern.describe()
  return jsonify(tavern)  