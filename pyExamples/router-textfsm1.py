from netmiko import ConnectHandler 
import textfsm

platform = 'cisco_ios'
host = input('Host adı veya IP girin: ')
username = input('Kullanıcı Adı girin: ') 
password = input('Şifre girin: ') 

device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
output = device.send_command('show ip int brief', use_textfsm=True)

"""f = open('fsmout.txt', 'w')
with open('fsmout.txt', 'w') as f:
    for line in metin:
        f.write(line)
        f.write('\n')"""

with open('fsmout.txt', 'w') as outfile:
    outfile.write(' '.join(map(str, output)))

print(output)
input()
