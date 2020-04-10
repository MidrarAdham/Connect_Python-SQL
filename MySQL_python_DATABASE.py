#Enter Credentials:
import MySQLdb
host = "localhost"
user = "root"
password = "1111"


#Connect to MySQL:
mydb = MySQLdb.connect(host,user,password)
#Initilize cursor:
mycursor = mydb.cursor()
#Create DATABASE: 
#Remember ALL CAPS

mycursor.execute("CREATE DATABASE LOAD_PROFILES")

#Confirm database is created
    #The following command will bring all databases:
mycursor.execute("SHOW DATABASES")
    #To print databases, let python go through all databases and print them
for db in mycursor:
    print(db)
    