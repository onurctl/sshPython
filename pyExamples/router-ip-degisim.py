import netmiko
from netmiko import ConnectHandler
ios = {
    'device_type': 'cisco_ios',
    'ip':   '192.168..',
    'username': '2',
    'password': '2',
}
net_connect =ConnectHandler(**ios)
net_connect.enable()
output =net_connect.send_command('show ip int brief')
print(output)

config_commands = [ 'int f0/0', 'ip address 192.168.. 255.255.255.0', 'no sh']
output = net_connect.send_config_set(config_commands)
print (output)

output =net_connect.send_command('show ip int brief')
print (output)
