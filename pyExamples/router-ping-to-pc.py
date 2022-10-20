from netmiko import ConnectHandler 

platform = 'cisco_ios'
host = input('Host adı veya IP girin: ')
username = input('Kullanıcı Adı girin: ') 
password = input('Şifre girin: ') 
hedef = input('Hedef ip: ') 

device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
output = device.send_command("ping "+hedef)

print(output)
input()