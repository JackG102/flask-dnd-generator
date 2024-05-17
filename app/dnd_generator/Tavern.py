import os
import random
from pathlib import Path
from app.dnd_generator.Npc import Npc

"""
A class to generate Taverns.
They have the following attributes:
 - Name
 - Tavern Keeper
 - Tavern NPCS

There are helper methods to:
 - describe the tavern
"""
class Tavern:
  project_location = str(Path(__file__).parent)
  lists_folder_location = project_location + '/lists/'

  def __init__(self):
    self.assign_name()
    self.assign_tavern_keeper()
    self.assign_tavern_npcs()
    self.assign_signature_dish()

  def assign_name(self):
    adjective_list_file = open(os.path.join(os.path.dirname(self.lists_folder_location), 'adjectives.txt'))
    adjective_lines = adjective_list_file.read().splitlines() 
    adjective_name = random.choice(adjective_lines)

    animal_list_file = open(os.path.join(os.path.dirname(self.lists_folder_location), 'animals.txt'))
    animal_lines = animal_list_file.read().splitlines() 
    animal_name = random.choice(animal_lines)

    self.name = f"{adjective_name.capitalize()} {animal_name}"

  def assign_tavern_keeper(self):
    self.tavern_keeper = Npc()
  
  def assign_tavern_npcs(self):
    self.tavern_npcs = Npc.generate_npc(3)

  def assign_signature_dish(self):
    ingredient_list = []
    ingredient_start = 0
    ingredient_list_file = open(os.path.join(os.path.dirname(self.lists_folder_location), 'ingredients.txt'))
    ingredient_lines = ingredient_list_file.read().splitlines() 
    self.signature_dish = ingredient_list
    
    while ingredient_start < 3:
      ingredient_list.append(random.choice(ingredient_lines))
      self.ingredients = ingredient_list
      ingredient_start += 1

  def describe(self):
    return({
        'Name': self.name,
        'Barkeeper': self.tavern_keeper.describe(),
        'Tavern_NPCs': [
          self.tavern_npcs[0].describe(), 
          self.tavern_npcs[1].describe(), 
          self.tavern_npcs[2].describe()
        ],
        'Signature_Dish': self.signature_dish
      })