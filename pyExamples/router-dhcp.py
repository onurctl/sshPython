import netmiko
from netmiko import ConnectHandler

ios = {
    'device_type': 'cisco_ios',
    'ip':   '192.168..',
    'username': '',
    'password': '',
}

net_connect =ConnectHandler(**ios)
net_connect.enable()
output =net_connect.send_command('show ip int brief')
print(output)

config_commands = [ 'conf t', 'service dhcp', 'ip dhcp excluded-address 192.168.. 192.168..', 'ip dhcp pool myPool', 'network 192.168.. 255.255..', 'lease 2', 'default-router 192.168..' ]

output = net_connect.send_config_set(config_commands)
print (output)

output =net_connect.send_command('show ip int brief')
print (output)

""" 'domain-name mysite.com', 'lease 0 0 30', 'ip dhcp excluded-address 192.168.. 192.168..' """
