import psycopg2

con = psycopg2.connect(
    database="prsr_db",
    user="postgres",
    password="practicA4",
    host="127.0.0.1",
    port="5432"
)
print("Database opened successfully")
cur = con.cursor()
cur.execute('''DROP TABLE IF EXISTS MAINNEWS''')
cur.execute('''DROP TABLE IF EXISTS HOURNEWS''')
cur.execute('''DROP TABLE IF EXISTS TOPNEWS''')
cur.execute('''DROP TABLE IF EXISTS OTHNEWS''')
cur.execute('''CREATE TABLE MAINNEWS
      (NAME TEXT NOT NULL,
      FILE TEXT);''')
print("Table MAINNEWS created succcessfully")
cur.execute('''CREATE TABLE HOURNEWS
      (NAME TEXT NOT NULL,
      FILE TEXT);''')
print("Table HOURNEWS created succcessfully")
cur.execute('''CREATE TABLE TOPNEWS
      (NAME TEXT NOT NULL,
      FILE TEXT);''')
print("Table TOPNEWS created succcessfully")
cur.execute('''CREATE TABLE OTHNEWS
      (NAME TEXT NOT NULL,
      FILE TEXT,
      KATEGORY TEXT,
      COMMENTS TEXT);''')
print("Table OTHNEWS created succcessfully")

