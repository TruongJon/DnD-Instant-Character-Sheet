#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def savingThrow(char_class, connection):
    cur = connection.cursor()
    cur.execute("SELECT * from proficiency WHERE type = 'Saving Throw' and parent = {};".format(char_class))
    
    output = 'Saving Throw Proficiencies: '
    for row in cur.fetchall():
        output += row["desc"] + ", "
    cur.close()
    output.rstrip(output[-2])
    return output[0:-2]

def proficiencies(p_type, char_class, char_subclass, char_race, char_subrace, char_background, connection):
    cur = connection.cursor()
    cur.execute("SELECT * from proficiency WHERE type = '{}' and (parent = {} or parent = {} or parent = {} or parent = {} or parent = {});"
    .format(p_type, char_class, char_race, char_subrace, char_subclass, char_background))
    
    output = p_type + " Proficiencies: "
    for row in cur.fetchall():
        output += row["desc"] + ", "
    cur.close()
    return output[0:-2]

def racialFeatures(char_level, char_race, char_subrace, connection):
    cur = connection.cursor()
    cur.execute("SELECT * from feature WHERE parent = {} or parent = {};"
    .format(char_race, char_subrace))
    
    output = "Racial Features: \n"
    for row in cur.fetchall():
        if (char_level >= row["f_level"]):
            output += row["f_name"] + ": " + row["f_description"] + '\n'
    cur.close()
    return output

def classFeatures(char_level, char_class, char_subclass, connection):
    cur = connection.cursor()
    cur.execute("SELECT * from feature WHERE parent = {} or parent = {};"
    .format(char_class, char_subclass))
    
    output = "Class Features: "
    for row in cur.fetchall():
        if (char_level >= row["f_level"]):
            output += row["f_description"] + ", "
    cur.close()
    output.rstrip(output[-1])
    return output

def background(char_background, connection):
    cur = connection.cursor()
    cur.execute("SELECT * from feature WHERE parent = {};"
    .format(char_background))
    
    output = "Background Feature: "
    for row in cur.fetchall():
        output += row["f_description"]
    cur.close()
    return output