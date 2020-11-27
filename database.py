import pymysql
import pymysql.cursors
from config import DB, USER, HOST, PASS, PORT

def conncect():
    return pymysql.connect(HOST, USER, PASS, DB, cursorclass=pymysql.cursors.DictCursor)

def add_user(id_user, lang, nickname=None, refferal=None):
    con = conncect()
    cursor = con.cursor()
    sql = "INSERT INTO users (id_user,username,balance,id_refferal,lang,date_reg) VALUES (%s, %s,%s,%s,%s,NOW())"
    cursor.execute(sql, (id_user, nickname, 0.0, refferal, lang))
    con.commit()
    con.close()


def check_user_in_db(id_user):
    con = conncect()
    cursor = con.cursor()
    sql = "SELECT id FROM users WHERE id_user=%s"
    cursor.execute(sql, (id_user))
    result = cursor.fetchone()
    con.close()
    return result

def get_user( id_user):
    con = conncect()
    cursor = con.cursor()
    sql = "SELECT * FROM users WHERE id_user=%s"
    cursor.execute(sql, (id_user))
    result = cursor.fetchone()
    con.close()
    return result

def count_ref( id_user):
    con = conncect()
    cursor = con.cursor()
    sql = "SELECT COUNT(*) FROM users WHERE id_refferal=%s"
    cursor.execute(sql, (id_user))
    result = cursor.fetchone()
    con.close()
    return result

def add_pays( id_user, ammount):
    con = conncect()
    cursor = con.cursor()
    sql = "SELECT balance FROM users WHERE id_user=%s"
    cursor.execute(sql, (id_user))
    result = cursor.fetchone()
    balance = float(result['balance'])
    balance += ammount
    sql = "Update users set balance = %s where id_user=%s"
    cursor.execute(sql, (balance, id_user))
    con.commit()
    con.close()

def add_category(name):
    con = conncect()
    cursor = con.cursor()
    sql = "INSERT INTO categorus (name) VALUES (%s)"
    cursor.execute(sql,(name))
    con.commit()
    con.close()

def delete_category(name):
    con = conncect()
    cursor = con.cursor()
    sql = "DELETE FROM categorus WHERE name = %s"
    cursor.execute(sql,(name))
    con.commit()
    con.close()

def get_categorus():
    con = conncect()
    cursor = con.cursor()
    sql = "SELECT name FROM categorus"
    cursor.execute(sql)
    result = cursor.fetchall()
    con.close()
    return result

def add_product(name,category,price,link):
    con = conncect()
    cursor = con.cursor()
    sql = "INSERT INTO products (name,category,price,link) VALUES (%s,%s,%s,%s)"
    cursor.execute(sql,(name,category,price,link))
    con.commit()
    con.close()