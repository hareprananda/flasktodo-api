import mysql.connector

dbUser = 'root'
dbPassword = ''
dbName = ''
dbHost = '127.0.0.1'

my = mysql.connector.connect(
    host=dbHost,
    user=dbUser,
    password=dbPassword
)

myCursor = my.cursor()

myCursor.execute("CREATE DATABASE our_users")
myCursor.execute('SHOW DATABASES')
for db in myCursor:
    print(db)