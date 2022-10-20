from netmiko import ConnectHandler 
import textfsm

platform = 'cisco_ios'
host = input('Host adı veya IP girin: ')
username = input('Kullanıcı Adı girin: ') 
password = input('Şifre girin: ') 

device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
output = device.send_command('show version', use_textfsm=True)

print(output)
input()

#show running-config >> yapılmış tüm konfigürasyonlar
#show version >> cihaz özellikleri
# show ip int brief >> interface'lerin ip'leri ve aktif olma durumu
# show ip route