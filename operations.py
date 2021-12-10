#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymysql import STRING
import calculations
import sys
import math
import pnf

def registerUser(connection):
  # Prompts for desired username and updates the database for the new user
  username = input('Please enter a username. \n')
  currentUser = ''
  cur = connection.cursor()
  cur.execute("INSERT INTO user(name) VALUES ('{}');".format(username))
  cur.close()

  # Stores the most recent user_id for that username.
  # (This was done because there might be duplicate usernames)
  cur2 = connection.cursor()
  cur2.execute("SELECT user_id FROM user WHERE name = '{}' ORDER BY user_id DESC LIMIT 1;"
  .format(username))
  row = cur2.fetchone()
  key = row["user_id"]
  cur2.close()

  # Prints out username and user_id for reference.
  print("Your username is {} and your user_id is {}.".format(username, key))
  currentUser = key
  return currentUser

def loginUser(connection):
  # Username and user_id both needed to login.
  username = input('Welcome back! Please enter your username. \n')
  key = input('Please enter your user_id. \n')
  currentUser = ''

  # Compares username and user_id to pairings in the user table.
  try:
    cur = connection.cursor()
    cur.execute("SELECT name FROM user where user_id = {};".format(key))
    row = cur.fetchone()
    if (row["name"] == username):
      currentUser = key
      print("Login successful.")
      cur.close()
      return currentUser
    else:
      print("Username and user_id do not match. Please try again. \n")
  except Exception as e:
    return

def createCharacter(currentUser, connection):
  # Checks if the command is called before the user has registered or logged in.
  if (currentUser == ''):
    print('Please login or register.')
    return

  currentCharacter = input('Enter a name for your character: \n')
  char_race = input('Select a race: \n Dwarf / Elf / Halfling / Human / Dragonborn'
  ' / Gnome / Half-Elf / Half-Orc / Tiefling \n') 
  if (char_race == "Dwarf"):
    race_val = 1001
    char_subrace = input('Select a subrace: \n Hill Dwarf / Mountain Dwarf \n')
    if (char_subrace == "Hill Dwarf"):
      subrace_val = 2000
    else:
      subrace_val = 2001
  elif (char_race == "Elf" ):
    race_val = 1002
    char_subrace = input('Select a subrace: \n High Elf / Wood Elf \n')
    if (char_subrace == "High Elf"):
      subrace_val = 2002
    else:
      subrace_val = 2003
  elif (char_race == "Halfing"):
    race_val = 1003
    char_subrace = input('Select a subrace: \n Lightfoot / Stout \n')
    if (char_subrace == "Lightfoot"):
      subrace_val = 2004
    else:
      subrace_val = 2005
  elif (char_race == "Human"):
    race_val = 1000
    subrace_val = 2017
  elif (char_race == "Dragonborn"):
    race_val = 1004
    char_subrace = input('Select an ancestry: \n Black / Blue / Brass / Bronze / Copper / '
    'Gold / Green / Red / Silver / White \n')
    if (char_subrace == "Black"):
      subrace_val = 2006
    elif (char_subrace == "Blue"):
      subrace_val = 2007
    elif (char_subrace == "Brass"):
      subrace_val = 2008
    elif (char_subrace == "Bronze"):
      subrace_val = 2009
    elif (char_subrace == "Copper"):
      subrace_val = 2010
    elif (char_subrace == "Gold"):
      subrace_val = 2011
    elif (char_subrace == "Green"):
      subrace_val = 2012
    elif (char_subrace == "Red"):
      subrace_val = 2013
    elif (char_subrace == "Silver"):
      subrace_val = 2014
    elif (char_subrace == "White"):
      subrace_val = 2015
  elif (char_race == "Gnome"):
    race_val = 1000
    subrace_val = 2016
  elif (char_race == "Half-Elf"):
    race_val = 1006
    subrace_val = 2018
  elif (char_race == "Half-Orc"):
    race_val = 1007
    subrace_val = 2019
  elif (char_race == "Tiefling"):
    race_val = 1008
    subrace_val = 2020
  else:
    print("Invalid race. Please try again")
    return
    
  char_class = input('Select a class: \n Barbarian / Bard / Cleric / Druid / Fighter / Monk'
  '\n Paladin / Ranger / Rogue / Sorcerer / Warlock / Wizard \n')
  char_level = int(input('Starting level of your character \n Lv. '))
  
  # If level is high enough, assign subclass
  if (char_class == 'Barbarian'):
    class_val = 4000
    if (char_level >= 3):
      subclass_val = 5001
    else:
      subclass_val = 5013
  elif (char_class == 'Bard' and char_level >= 3):
    class_val = 4001
    if (char_level >= 3):
      subclass_val = 5002
    else:
      subclass_val = 5014
  elif (char_class == 'Cleric'):
    class_val = 4002
    subclass_val = 5003
  elif (char_class == 'Druid'):
    class_val = 4003
    if (char_level >= 2):
      subclass_val = 5004
    else:
      subclass_val = 5014
  elif (char_class == 'Fighter' and char_level >= 3):
    class_val = 4004
    if (char_level >= 3):
      subclass_val = 5005
    else:
      subclass_val = 5015
  elif (char_class == 'Monk'):
    class_val = 4005
    if (char_level >= 3):
      subclass_val = 5006
    else:
      subclass_val = 5016
  elif (char_class == 'Paladin' and char_level >= 3):
    class_val = 4006
    if (char_level >= 3):
      subclass_val = 5007
    else:
      subclass_val = 5017
  elif (char_class == 'Ranger'):
    class_val = 4007
    if (char_level >= 3):
      subclass_val = 5008
    else:
      subclass_val = 5018
  elif (char_class == 'Rogue'):
    class_val = 4008
    if (char_level >= 3):
      subclass_val = 5009
    else:
      subclass_val = 5019
  elif (char_class == 'Sorcerer'):
    class_val = 4009
    subclass_val = 5011
  elif (char_class == 'Warlock'):
    class_val = 4010
    subclass_val = 5012
  elif (char_class == 'Wizard'):
    class_val = 4011
    subclass_val = 5000
  else:
    print("Invalid class. Please try again.")

  background = input("Choose a background: \n"
  "Acolyte / Criminal / Folk Hero / Noble / Sage / Soldier \n")
  if (background == 'Acolyte'):
    background_val = 3000
  elif (background == 'Criminal'):
    background_val = 3001
  elif (background == 'Folk Hero'):
    background_val = 3002
  elif (background == 'Noble'):
    background_val = 3003
  elif (background == 'Sage'):
    background_val = 3004
  else:
    background_val = 3005

  char_strength = int(input('Enter rolled strength for your character. \n'))
  char_dexterity = int(input('Enter rolled dexterity for your character. \n'))
  char_constitution = int(input('Enter rolled constitution for your character. \n'))
  char_charisma = int(input('Enter rolled charisma for your character. \n'))
  char_intelligence = int(input('Enter rolled intelligence for your character. \n'))
  char_wisdom = int(input('Enter rolled wisdom for your character. \n'))

  if (char_level == 1):
    proficiency = 2
  else:
    proficiency = 2 + math.floor((char_level - 1) / 4) 

  # INSERT ALL VALUES INTO CHARACTER TABLE
  cur = connection.cursor()
  cur.execute("INSERT INTO dnd_character (ch_name, ch_level, strength, dexterity,"
  " constitution, charisma, intelligence, wisdom, proficiency_bonus,"
  " user, class, subclass, race, subrace, background)"
  "VALUES ('{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}', '{}', '{}', '{}', '{}');"
  .format(currentCharacter, char_level, char_strength, char_dexterity,
  char_constitution, char_charisma, char_intelligence, char_wisdom, proficiency,
  currentUser, class_val, subclass_val, race_val, subrace_val, background_val))
  cur.close()
  return currentCharacter

def loadCharacter(currentUser, connection):
  # Checks if the command is called before the user has registered or logged in.
  if (currentUser == ''):
    print('Please login or register.')
    return

  # LIST ALL CHARACTERS TO CHOOSE FROM
  cur = connection.cursor()
  cur.execute("SELECT ch_name, ch_level FROM dnd_character WHERE user = {}"
  .format(currentUser))
  for row in cur.fetchall():
    print(row["ch_name"] + " [Lv. " + str(row["ch_level"]) + "]")
  cur.close()
  currentCharacter = input('Select a character to load: \n')

  #LIST ALL MODIFIABLE ATTRIBUTES OF SELECTED CHARACTER
  cur2 = connection.cursor()
  cur2.execute("SELECT * FROM dnd_character WHERE user = {} and ch_name = '{}'"
  .format(currentUser, currentCharacter))
  for row in cur2.fetchall():
    print(row["ch_name"] + " Lv. " + str(row["ch_level"])
    + "\n Strength: " + str(row["strength"]) + "\n Dexterity: " + str(row["dexterity"])
    + "\n Constitution: " + str(row["constitution"]) + "\n Charisma: " + str(row["charisma"])
    + "\n Intelligence: " + str(row["intelligence"]) + "\n Wisdom: " + str(row["wisdom"]))
  cur2.close()
  print("Character successfully loaded.")
  return currentCharacter


def modifyCharacter(currentUser, currentCharacter, connection):
  # Checks if the command is called before the user has registered or logged in.
  if (currentUser == ''):
    print('Please login or register.')
    return

  # Checks if the command is called before the user has loaded a character
  if (currentCharacter == ''):
    print('No character has been selected.')
    return

  print("Parameters: name, strength, dexterity, constitution, charisma, intelligence, wisdom. \n"
  "Please enter \'quit\' when you are finished modifying.")
  while True:
    n = input('Ready to modify... \n')
    if (n == 'quit'):
      break
    elif (n == 'name'):
      change = input("Enter a new name. \n")
      cur = connection.cursor()
      cur.execute("UPDATE dnd_character SET ch_name = '{}' WHERE ch_name = '{}' and user = {}"
      .format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'level'):
      change = input("Enter a new level. \n")
      cur = connection.cursor()
      cur.execute("UPDATE dnd_character SET ch_level = {} WHERE ch_name = '{}' and user = {}"
      .format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'strength'):
      change = input("Enter a value for STR. \n")
      cur = connection.cursor()
      cur.execute("UPDATE dnd_character SET strength = {} WHERE ch_name = '{}' and user = {}"
      .format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'dexterity'):
      change = input("Enter a new value for DEX. \n")
      cur = connection.cursor()
      cur.execute("UPDATE dnd_character SET dexterity = {} WHERE ch_name = '{}' and user = {}"
      .format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'constitution'):
      change = input("Enter a new value for CON. \n")
      cur = connection.cursor()
      cur.execute("UPDATE dnd_character SET constitution = {} WHERE ch_name = '{}' and user = {}"
      .format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'charisma'):
      change = input("Enter a new value for CHA. \n")
      cur = connection.cursor()
      cur.execute("UPDATE dnd_character SET charisma = {} WHERE ch_name = '{}' and user = {}"
      .format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'intelligence'):
      change = input("Enter a new value for INT. \n")
      cur = connection.cursor()
      cur.execute("UPDATE dnd_character SET intelligence = {} WHERE ch_name = '{}' and user = {}"
      .format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'wisdom'):
      change = input("Enter a new value for WIS. \n")
      cur = connection.cursor()
      cur.execute("UPDATE dnd_character SET wisdom = {} WHERE ch_name = '{}' and user = {}"
      .format(change, currentCharacter, currentUser))
      cur.close()
    else:
      print("Unrecognizable command. Please try again. \n")

def exportCharacter(currentUser, currentCharacter, connection):
  # Checks if the command is called before the user has registered or logged in.
  if (currentUser == ''):
    print('Please login or register.')
    return

  # Checks if the command is called before the user has loaded a character
  if (currentCharacter == ''):
    print('No character has been selected.')
    return

  cur = connection.cursor()
  cur.execute("SELECT * FROM dnd_character WHERE user = {} and ch_name = '{}'"
  .format(currentUser, currentCharacter))
  row = cur.fetchone()
  cur.close()

  cur2 = connection.cursor()
  cur2.execute("CALL fn_identify({}, {}, {}, {}, {});"
  .format(row["class"], row["subclass"], row["race"], row["subrace"], row["background"]))
  row2 = cur2.fetchone()
  get_class = row2["name"]
  row2 = cur2.fetchone()
  get_subclass = row2["name"]
  row2 = cur2.fetchone()
  get_race = row2["name"]
  row2 = cur2.fetchone()
  get_subrace = row2["name"]
  row2 = cur2.fetchone()
  get_background = row2["name"]
  cur2.close()

  output = ''
  output += row["ch_name"] + " Lv. " + str(row["ch_level"]) + '\n'
  output += "Class: " + get_class + ", Subclass: " + get_subclass + '\n'
  output += "Race: " + get_race + ", Subrace: " + get_subrace + '\n'
  output += "Background: " + get_background + ", Hitpoints: " + str(calculations.hitpoints(get_class, row["ch_level"], row["constitution"])) + '\n'
  output += "Strength: " + str(row["strength"]) + " [" + str(calculations.abilityscore(row["strength"])) + "]" + '\n'
  output += "Dexterity: " + str(row["dexterity"]) + " [" + str(calculations.abilityscore(row["dexterity"])) + "]" + '\n'
  output += "Constitution: " + str(row["constitution"]) + " [" + str(calculations.abilityscore(row["constitution"])) + "]" + '\n'
  output += "Charisma: " + str(row["charisma"]) + " [" + str(calculations.abilityscore(row["charisma"])) + "]" + '\n'
  output += "Intelligence: " + str(row["intelligence"]) + " [" + str(calculations.abilityscore(row["intelligence"])) + "]" + '\n'
  output += "Wisdom: " + str(row["wisdom"]) + " [" + str(calculations.abilityscore(row["wisdom"])) + "]" + '\n'
  output += "Proficiencies Bonus: " + str(row["proficiency_bonus"]) + '\n'
  output += pnf.savingThrow(row["class"], connection) + '\n'
  output += pnf.proficiencies("Skill", row["class"], row["subclass"], row["race"], row["subrace"], row["background"], connection) + '\n'
  output += pnf.proficiencies("Weapon", row["class"], row["subclass"], row["race"], row["subrace"], row["background"], connection) + '\n'
  output += pnf.proficiencies("Armor", row["class"], row["subclass"], row["race"], row["subrace"], row["background"], connection) + '\n'
  output += pnf.proficiencies("Tool", row["class"], row["subclass"], row["race"], row["subrace"], row["background"], connection) + '\n'
  output += pnf.proficiencies("Language", row["class"], row["subclass"], row["race"], row["subrace"], row["background"], connection) + '\n'
  output += pnf.racialFeatures(row["ch_level"], row["race"], row["subrace"], connection)
  output += pnf.background(row["background"], connection) + '\n'
  print(output)

  # Exports character sheet as a text file
  with open("CharacterSheet.txt", "w") as text_file:
    print("Session Character Sheet \n{}".format(output), file=text_file)

def deleteCharacter(currentUser, currentCharacter, connection):
  # Checks if the command is called before the user has registered or logged in.
  if (currentUser == ''):
    print('Please login or register.')
    return

  # Checks if the command is called before the user has loaded a character
  if (currentCharacter == ''):
    print('No character has been selected.')
    return
    
  #DELETES CURRENT CHARACTER
  cur = connection.cursor()
  cur.execute("DELETE FROM dnd_character WHERE ch_name = '{}' and user= {}"
  .format(currentCharacter, currentUser)) 
  cur.close()
  print("{} deleted.".format(currentCharacter))

def parseInput(connection):
  currentUser = ''
  currentCharacter = ''
  while True:
    n = input('Ready for input... \n')
    if (n == 'quit'):
      break
    elif (n == 'register'):
      currentUser = registerUser(connection)
    elif (n == 'login'):
      currentUser = loginUser(connection)
    elif (n == 'new character'):
      currentCharacter = createCharacter(currentUser, connection)
    elif (n == 'load character'):
      currentCharacter = loadCharacter(currentUser, connection)
    elif (n == 'modify character'):
      modifyCharacter(currentUser, currentCharacter, connection)
    elif (n == 'export character'):
      exportCharacter(currentUser, currentCharacter, connection)
    elif (n == 'delete character'):
      deleteCharacter(currentUser, currentCharacter, connection)
    else:
      print("Unrecognizable command. Please try again.")