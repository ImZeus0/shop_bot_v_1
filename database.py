import pymysql
import pymysql.cursors
from config import DB,USER,HOST,PASS,PORT

class Database():
    con = pymysql.connect(HOST, USER,PASS, DB,cursorclass=pymysql.cursors.DictCursor)

    def add_user(self,id_user,lang,nickname=None,refferal=None):
        pass


