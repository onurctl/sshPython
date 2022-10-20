from netmiko import ConnectHandler 

platform = 'cisco_ios'
host = input('Host adı veya IP girin: ')
username = input('Kullanıcı Adı girin: ') 
password = input('Şifre girin: ') 

device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
output = device.send_command('show running-config')

print(output)
input()

#show ip int brief >> interface'lerin ip'leri ve aktif olma durumu
#show running-config >> yapılmış tüm konfigürasyonlar
#show version >>