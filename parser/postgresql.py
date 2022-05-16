import psycopg2

connection = psycopg2.connect(user = "postgres", password = "qwerty", host = "localhost", port = "5432", database = "postgres")
cursor = connection.cursor()

print("Информация о сервере PostgreSQL")
print(connection.get_dsn_parameters(), "\n")

sql = '''CREATE TABLE employee(id  SERIAL NOT NULL, name varchar(20) not null, state varchar(20) not null)'''
#sql = '''CREATE TABLE news(id  SERIAL NOT NULL, news_name varchar(100) not null, news_text varchar(1000) not null)'''
cursor.execute(sql)

# list that contain records to be inserted into table
data = [('Babita', 'Bihar'), ('Anushka', 'Hyderabad'), ('Anamika', 'Banglore'), ('Sanaya', 'Pune'), ('Radha', 'Chandigarh')]
# inserting record into employee table
for d in data:
    cursor.execute("INSERT into employee(name, state) VALUES (%s, %s)", d)
#for d in data:
    #cursor.execute("INSERT into news(news_name, news_text) VALUES (%s, %s)", d)

sql2 = '''select * from employee;'''
#sql2 = '''select * from news;'''
cursor.execute(sql2)
print(cursor.fetchall())

connection.commit()
connection.close()