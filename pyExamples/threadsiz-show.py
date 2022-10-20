from netmiko import ConnectHandler 
import textfsm
from datetime import datetime

start_time = datetime.now()

platform = 'cisco_ios'
host = '192.168.50.2'
username = 'admin'
password = 'cisco' 

device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
output = device.send_command('show ip int brief')

print(output)

host = '192.168.50.3'
username = 'admin2'
password = 'cisco2' 

device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
output = device.send_command('show ip int brief')
print(output)
#input()

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))