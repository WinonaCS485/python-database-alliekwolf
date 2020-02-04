import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='nn4263xb',
                             password='G00d4Gr34t!!!4',
                             db='nn4263xb_University',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select all Students
        sql = "SELECT s.Student_ID, s.First_Name, s.Last_Name, p.Program_Name FROM Students s INNER JOIN Programs p ON s.Major = p.Program_ID"
        
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        for result in cursor:
            print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()
