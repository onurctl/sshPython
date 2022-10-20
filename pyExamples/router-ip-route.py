import netmiko
from netmiko import ConnectHandler
ios = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.50.2',
    'username': 'admin',
    'password': 'cisco',
}
net_connect =ConnectHandler(**ios)
net_connect.enable()

config_commands = [ 'conf t', 'ip route 192.168.98.0 255.255.255.0 192.168.100.4 ', 'end', 'show ip route']
output = net_connect.send_config_set(config_commands)
print (output)
