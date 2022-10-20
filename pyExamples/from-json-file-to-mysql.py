import mysql.connector
from mysql.connector import Error

import ast
with open('data.txt', 'r') as file:
    list = ast.literal_eval(f'[{file.read()}]')
ios1 = list[0]
ios2 = list[1]

#bunu thread ile yap

try:
        connection = mysql.connector.connect(host='localhost',
                                         database='sakila',
                                         user='root',
                                         password='root')

        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO data (intf, ipaddr, status, proto) 
                                VALUES (%s, %s, %s, %s) """

        record = (ios2['intf'], ios2['ipaddr'],ios2['status'],ios2['proto'])
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("kayıt başarıyla gerçekleşti")
        cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL bağlantısı sonlandırıldı")




"""

import threading 
from netmiko import ConnectHandler
import time
import logging

from datetime import datetime

start_time = datetime.now()


#sorunsuz çalışıyor, diğer router a authentication hatası verdi çünkü onun ssh ayarlarını kaydetmemiştik

ios1 = {
   
    'device_type': 'cisco_ios',
    'ip':   '192.168.50.2',
    'username': 'admin',
    'password': 'cisco',
    'port' : 22,    
}

#  'port' : 22,                                    opsiyonel
# 'secret': 'C1sco12345',          opsiyonel

ios2 = {
   
    'device_type': 'cisco_ios',
    'ip':   '192.168.50.3',
    'username': 'admin2',
    'password': 'cisco2',
    'port' : 22,    #port 22 ekleyince düzeldi kimlik doğrulama hatası, secret ları da ekle gerekirse
}

def baglan(device_data):
    net_connect = ConnectHandler(**device_data)
    output = net_connect.send_command('show ip int brief')
    print(net_connect.host)
    #print("*" * len(net_connect.host)) -- host adının uzunluğu kadar *** koyuyor
    print(output)

#parametre probleminin çözümü:
if __name__ == "__main__":
    threads = []
    all_devices = [ios1,ios2]
    for device in all_devices:
        # Spawn threads and append to threads list
        th = threading.Thread(target=baglan, args=(device,))
        threads.append(th)
    
    # iterate through threads list and start each thread to perform its task
    for thread in threads:
        thread.start()

    #Once all threads have done the work, join the output of all threads to return the final output.
    for thread in threads:
        thread.join()

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

"""
