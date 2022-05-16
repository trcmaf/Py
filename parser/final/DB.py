import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="qwerty", host="localhost", port="5432")
print("Database opened successfully")
cur = con.cursor()
sql1 = '''CREATE TABLE MAINNEWS (id  SERIAL NOT NULL, NAME TEXT NOT NULL, FILE TEXT);'''
sql2 = '''CREATE TABLE HOURNEWS (id  SERIAL NOT NULL, NAME TEXT NOT NULL, FILE TEXT);'''
sql3 = '''CREATE TABLE TOPNEWS (id  SERIAL NOT NULL, NAME TEXT NOT NULL, FILE TEXT);'''
sql4 = '''CREATE TABLE OTHNEWS (id  SERIAL NOT NULL, NAME TEXT NOT NULL, FILE TEXT, KATEGORY TEXT, COMMENTS TEXT);'''
cur.execute('''DROP TABLE IF EXISTS MAINNEWS''')
cur.execute('''DROP TABLE IF EXISTS HOURNEWS''')
cur.execute('''DROP TABLE IF EXISTS TOPNEWS''')
cur.execute('''DROP TABLE IF EXISTS OTHNEWS''')
cur.execute(sql1)
print("Table MAINNEWS created succcessfully")
cur.execute(sql2)
print("Table HOURNEWS created succcessfully")
cur.execute(sql3)
print("Table TOPNEWS created succcessfully")
cur.execute(sql4)
print("Table OTHNEWS created succcessfully")

