from flask import render_template
from app import app
from app.dnd_generator.Npc import Npc

@app.route('/npc')
def home():
  testNPC = Npc()
  return f"Render NPC page, {testNPC.first_name}"
  