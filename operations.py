#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def registerUser(connection):
  # Prompts for desired username and updates the database for the new user
  username = input('Please enter a username \n')
  currentUser = ''
  cur = connection.cursor()
  cur.execute("INSERT INTO user(name) VALUES ({}});".format(username))
  cur.close()

  # Stores the most recent user_id for that username.
  # (This was done because there might be duplicate usernames)
  cur2 = connection.cursor()
  cur2.execute("SELECT user_id FROM user WHERE name = {} ORDER BY id DESC LIMIT 1;".format(username))
  row = cur2.fetchone()
  key = row["user_id"]
  cur2.close()

  # Prints out username and user_id for reference.
  print("Your username is {} and your user_id is {}".format(username, key))
  currentUser = key
  return currentUser

def loginUser(connection):
  # Username and user_id both needed to login.
  username = input('Welcome back! Please enter your username \n')
  key = input('Please enter your user_id \n')
  currentUser = ''

  # Compares username and user_id to pairings in the user table.
  cur = connection.cursor()
  cur.execute("SELECT name FROM user where user_id = {}".format(key))
  row = cur.fetchone()
  if (row["name"] == username):
    currentUser = key
    print("Login successful.")
  else:
    print("Username and user_id do not match. Please log in again \n")
    return
  cur.close()
  return currentUser

def createCharacter(currentUser, connection):
  # Checks if the command is called before the user has registered or logged in.
  if (currentUser == ''):
    print('Please login or register. \n')
    return

  currentCharacter = input('Enter a name for your character: \n')
  char_race = input('Select a race: \n Dwarf / Elf / Halfling / Human / Dragonborn'
  ' / Gnome / Half-Elf / Half-Orc / Tiefling / ') 
  if (char_race == "Dwarf"):
    char_subrace = input('Select a subrace: \n Hill Dwarf / Mountain Dwarf')
  elif (char_race == "Elf" ):
    char_subrace = input('Select a subrace: \n High Elf / Wood Elf / Dark Elf')
  elif (char_race == "Halfing"):
    char_subrace = input('Select a subrace: \n Lightfoot / Stout')
  elif (char_race == "Human"):
    char_subrace = 'None'  
  elif (char_race == "Dragonborn"):
    char_subrace = input('Select an ancestry: \n Black / Blue / Brass / Bronze / Copper'
    'Gold / Green / Red / Silver / White')
  elif (char_race == "Gnome"):
    char_subrace = input('Select a subrace: \n Forest Gnome / Rock Gnome')  
  elif (char_race == "Half-Elf"):
    char_subrace = 'None'
  elif (char_race == "Half-Orc"):
    char_subrace = 'None'
  elif (char_race == "Tiefling"):
    char_subrace = 'None'
  else:
    print("Invalid race. Please try again")
    return
  char_class = input('Select a class: \n Barbarian / Bard / Cleric / Druid / Fighter / Monk'
  '\n Paladin / Ranger / Rogue / Sorcerer / Warlock / Wizard')
  char_sub_class = input('Select a class: \n Barbarian / Bard / Cleric / Druid / Fighter / Monk'
  '\n Paladin / Ranger / Rogue / Sorcerer / Warlock / Wizard')
  print('Write a background for your character (ctrl + d upon finish): ')
  char_background = sys.stdin.read()
  char_level = input('Starting level of your character \n Lv. ')
  print('Add your proficiencies (ctrl + d upon finish): ')
  char_proficiency = sys.stdin.read()

  # INSERT ALL COLLECTED INFORMATION INTO CORRECT TABLES
  cur = connection.cursor()
  cur.execute("")
  cur.close()
  return currentCharacter

def loadCharacter(currentUser, connection):
  # Checks if the command is called before the user has registered or logged in.
  if (currentUser == ''):
    print('Please login or register. \n')
    return

  # LIST ALL CHARACTERS TO CHOOSE FROM
  cur = connection.cursor()
  cur.execute("SELECT ch_name, ch_level FROM character WHERE ch_id = {}".format(currentUser))
  for row in cur.fetchall():
    print(row["ch_name"] + " Lv. " + row["ch_level"] + "\n")
  cur.close()
  currentCharacter = input('Select a character to load: \n')

  #LIST ALL ATTRIBUTES OF SELECTED CHARACTER
  cur2 = connection.cursor()
  cur2.execute("SELECT * FROM character WHERE ch_id = {} and ch_name = {}".format(currentUser, currentCharacter))
  for row in cur2.fetchall():
    print(row["ch_name"] + " Lv. " + row["ch_level"]
    + "\n Strength: " + row["strength"] + "\n Dexterity: " + row["dexterity"]
    + "\n Constitution: " + row["constitution"] + "\n Charisma: " + row["charisma"]
    + "\n Intelligence: " + row["intelligence"] + "\n Wisdom: " + row["wisdom"]
    + "\n Proficiency Bonuses: " + row["proficiency_bonus"])
  cur2.close()
  return currentCharacter

def modifyCharacter(currentUser, currentCharacter, connection):
  # Checks if the command is called before the user has registered or logged in.
  if (currentUser == ''):
    print('Please login or register. \n')
    return

  # Checks if the command is called before the user has loaded a character
  if (currentCharacter == ''):
    print('No character has been selected. \n')
    return

  print("Paramaters: name, strength, dexterity, constitution, charisma, intelligence, wisdom, proficiency \n"
  "Please enter \'return\' when you are finished modifying \n")
  while True:
    n = input('Ready to modify... \n')
    if (n == 'quit'):
      break
    elif (n == 'name'):
      change = input("Enter a new name.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET ch_name = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'name'):
      change = input("Enter a new level.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET ch_level = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'strength'):
      change = input("Enter a value for STRENGTH.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET strength = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'dexterity'):
      change = input("Enter a new value for DEXTERITY.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET dexterity = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'constitution'):
      change = input("Enter a new value for CONSTITUTION.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET constitution = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'charisma'):
      change = input("Enter a new value for CHARISMA.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET charisma = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'intelligence'):
      change = input("Enter a new value for INTELLIGENCE.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET intelligence = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'wisdom'):
      change = input("Enter a new value for WISDOM.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET wisdom = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'proficiency'):
      #Something complicated with reading the proficiency format
      print('Add your proficiencies (ctrl + d upon finish): ')
      change = sys.stdin.read()
      cur = connection.cursor()
      cur.execute("")
      cur.close()
    else:
      print("Unrecognizable command. Please try again.")

def exportCharacter(currentUser, currentCharacter, connection):
  # Checks if the command is called before the user has registered or logged in.
  if (currentUser == ''):
    print('Please login or register. \n')
    return

  # Checks if the command is called before the user has loaded a character
  if (currentCharacter == ''):
    print('No character has been selected. \n')
    return

  cur = connection.cursor()
  cur.execute("SELECT * FROM character WHERE ch_id = {} and ch_name = {}".format(currentUser, currentCharacter))
  for row in cur.fetchall():
    output = row["ch_name"] + " Lv. " + row["ch_level"]
    + "\n Strength: " + row["strength"] + "\n Dexterity: " + row["dexterity"]
    + "\n Constitution: " + row["constitution"] + "\n Charisma: " + row["charisma"]
    + "\n Intelligence: " + row["intelligence"] + "\n Wisdom: " + row["wisdom"]
    + "\n Proficiency Bonuses: " + row["proficiency_bonus"]
  cur.close()

  # Exports character sheet as a text file
  with open("CharacterSheet.txt", "w") as text_file:
    print("Session Character Sheet \n \n {}".format(output), file=text_file)

def deleteCharacter(currentUser, currentCharacter, connection):
  # Checks if the command is called before the user has registered or logged in.
  if (currentUser == ''):
    print('Please login or register. \n')
    return

  # Checks if the command is called before the user has loaded a character
  if (currentCharacter == ''):
    print('No character has been selected. \n')
    return
    
  #DELETES CURRENT CHARACTER
  cur = connection.cursor()
  cur.execute("DELETE FROM characters WHERE ch_name = {} and ch_id = {}".format(currentCharacter, currentUser)) 
  cur.close()

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