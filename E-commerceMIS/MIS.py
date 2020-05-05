import signInFunction
import pymysql
import sys
from PyQt5 import QtWidgets


db = pymysql.connect("localhost", "root", "130e340", "e-commerce")
cursor = db.cursor()

signInFunction.SignIn.db = db
signInFunction.SignIn.dbcursor = cursor
signInFunction.showSignInUI()

