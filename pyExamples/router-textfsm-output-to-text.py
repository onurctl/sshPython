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
    #outfile.write('\n') : string'e çevirip tek line yaptık diye tek satır yazıyor 

print(output)
input()

#show running-config >> yapılmış tüm konfigürasyonlar
#show version >> cihaz özellikleri
#show ip int brief >> interface'lerin ip'leri ve aktif olma durumu
#show ip route

#önce string'e çevirmemizi istedi liste şeklinde kabul etmedi, sonra map de kullanmamız gerekti,
#böylece int değerleri de string e çevirdi içindeki o nedenle hata vermişti map yokken
