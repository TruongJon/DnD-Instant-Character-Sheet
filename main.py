#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from array import array
import pymysql
import flask
import operations

try:
    connection = pymysql.connect(
    host = 'cs3200.cbnhan2y2mpk.us-east-2.rds.amazonaws.com',
    user = 'admin', password = 'cs3200dnd', 
    db = 'dnd_database', charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)
except:
    raise ValueError('Incorrect username and password pairing')

operations.parseInput(connection)
