import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "Babylone996",
    database = "testdb"
)

mycursor = mydb.cursor()

sqlFormula = "INSERT INTO  Project_logs (car_id, exit_lanes, redirection, accepted) VALUES (%s, %s, %s, %s)"



# how to create a database with the mySQL commands: 
    # mycursor.execute("CREATE DATABSE database_name")
# how to check that the database was indeed created:
    # mycursor.execute("SHOW DATABASES")
#hw to create tables 
    # mycursor.execute("CREATE TABLE Projects_logs (car_id VARCHAR(255), exit_lane INTEGER(10), redirection VARCHAR(255), accepted VARCHAR(255)")
#mycursor.execute("CREATE TABLE Projects_logs (car_id VARCHAR(255), exit_lane INTEGER(10), redirection VARCHAR(255), accepted VARCHAR(255))")

