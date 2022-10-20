from netmiko import ConnectHandler 
import textfsm
import json

platform = 'cisco_ios'
host = input('Host adı veya IP girin: ')
username = input('Kullanıcı Adı girin: ') 
password = input('Şifre girin: ') 

device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
output = device.send_command('show ip int brief', use_textfsm=True)

jsonString = json.dumps(output)
"""jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()"""

print(jsonString)
input()