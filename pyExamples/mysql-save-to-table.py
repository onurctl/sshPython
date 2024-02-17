import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='',
                                         user='',
                                         password='')

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
