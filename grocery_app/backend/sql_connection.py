
import mysql.connector


__cnx=None
def get_connection():
    global __cnx
    if __cnx is None:
      __cnx = mysql.connector.connect(host="127.0.0.1", user="root", password="123456", db="gs")
  
    return __cnx