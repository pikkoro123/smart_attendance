#import pymysql
#import pymysql.cursors
#db = pymysql.connect(host='127.0.0.1',user='',passwd='')
#cursor = db.cursor()
#query = ("SHOW DATABASES")
#cursor.execute(query)
#for r in cursor:
#print r
import pymysql.cursors  
 
# Connect to the database.
connection = pymysql.connect(host='127.0.0.1',
                             user='root',                                                        
                             db='facedata',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")
 
try:
  
 
    with connection.cursor() as cursor:
       
        # SQL 
        sql = "SELECT * FROM registered"
         
        # Execute query.
        cursor.execute(sql)
         
        print ("cursor.description: ", cursor.description)
 
        print()
 
        for row in cursor:
            print(row)
             
finally:
    # Close connection.
    connection.close()