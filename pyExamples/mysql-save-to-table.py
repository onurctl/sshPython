import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='sakila',
                                         user='root',
                                         password='root')

    mySql_insert_query = """INSERT INTO data (intf, ipaddr, status, proto) 
                           VALUES 
                           ('Fast', '123', 'up', 'up') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "kayıt başarılı bir şekilde gerçekleşti")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL bağlantısı sonlandırıldı")

# output u list e atıp oradan da tek tek elemanalrı dict1 = list[0], dict2 = list[1] alıp db sütunlarına
# veya json olarak al oradan bu şekilde alıp dict e sonra aktar db ye
