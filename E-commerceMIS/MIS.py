from signInFunction import showSignInUI
import pymysql
import sys
from PyQt5 import QtWidgets


db = pymysql.connect("******", "******", "******", "******")
cursor = db.cursor()

showSignInUI(db, cursor)

