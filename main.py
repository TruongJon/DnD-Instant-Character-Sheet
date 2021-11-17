#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

import pymysql
from array import array

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#%% Simple selector (MySQL database)
# import mysql.connector needs to be installed pip install mysql-connector
import pymysql
import flask

username = input("MySQL Username: ");
password = input("Password: ")

try:
    cnx = pymysql.connect(host = 'localhost', user = username, password = password, 
    db = 'dnd_database', charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)
except:
    raise ValueError('Incorrect username and password pairing')