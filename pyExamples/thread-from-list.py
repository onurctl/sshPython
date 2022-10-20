import threading 
from netmiko import ConnectHandler
import time
import logging

import ast
with open('dict-list.txt', 'r') as file:
    list = ast.literal_eval(f'[{file.read()}]')
ios1 = list[0]
ios2 = list[1]

#print(dict1) >> { ...., ..,}, { ...., ..,}, şeklinde text dosyasındaki dict'leri ayrı değişkenlere aktarma
#başarılı oldu tüm kod >>> db'den veri çekerek de yapılmalı

###

def baglan(device_data):
    net_connect = ConnectHandler(**device_data)
    output = net_connect.send_command('show ip int brief')
    print(net_connect.host)
    # print("*" * len(net_connect.host)) -- host adının uzunluğu kadar *** koyuyor
    print(output)

if __name__ == "__main__":
    threads = []
    all_devices = [ios1,ios2]
    for device in all_devices:
        th = threading.Thread(target=baglan, args=(device,))
        threads.append(th)
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

###

""" 
liste text dosyasındaki bilgiler:
{   
    'device_type': 'cisco_ios',
    'ip':  '192.168.50.2',
    'username': 'admin',
    'password': 'cisco',
    'port' : 22,    
},
{   
    'device_type': 'cisco_ios',
    'ip':  '192.168.50.3',
    'username': 'admin2',
    'password': 'cisco2',
    'port' : 22,
},
"""

 