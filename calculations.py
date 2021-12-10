#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def hitpoints(ch_class, ch_level, constitution):
    #D6
    if(ch_class == "Sorcerer" or ch_class == "Wizard"):
        if (ch_level == 1):
            return abilityscore(constitution) + 6 + constitution
        else:
            return abilityscore(constitution) + ((4 + constitution) * ch_level)
    #D8
    elif(ch_class == "Bard" or ch_class == "Cleric" or ch_class == "Druid" or ch_class == "Monk" or ch_class == "Rogue" or ch_class == "Warlock"):
        if (ch_level == 1):
            return abilityscore(constitution) + 8 + constitution
        return abilityscore(constitution) + ((5 + constitution) * ch_level)
    #D10
    elif(ch_class == "Fighter" or ch_class == "Paladin" or ch_class == "Ranger"):
        if (ch_level == 1):
            return abilityscore(constitution) + 10 + constitution
        return abilityscore(constitution) + ((6 + constitution) * ch_level)
    #D12
    elif (ch_class == "Barbarian"):
        if (ch_level == 1):
            return abilityscore(constitution) + 12 + constitution
        else:
            return abilityscore(constitution) + ((7 + constitution) * ch_level)
    else:
        return 0

def abilityscore(stat):
    ret = -5
    for x in range(stat):
        if (x % 2) == 0:
            ret += 1
    return ret