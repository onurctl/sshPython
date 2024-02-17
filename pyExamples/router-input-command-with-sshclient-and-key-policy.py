import paramiko
ip = "192.168.."
kullanici = ""
sifre = ""
komut = input('Komut girin: ')
port = 22

# birden çok komut girilmesi için bir deneme:

#durum = True
#giris = "empty"

ssh = paramiko.SSHClient()
#ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect('mysite.com')
ssh.connect(ip,port,kullanici,sifre)

#key_filename="openssh" >> not found in known_hosts

stdin,stdout,stderr = ssh.exec_command(komut)
sonuc = stdout.read()
print(sonuc.decode("utf-8"))
	  
ssh.close()

# yan yana tek satırda girilebiliyor tüm komutlar

"""
 while giris!='exit':
 
 	if giris=='x':
		durum=False
 	else:

timeout ve key'i .connect içinden çıkarınca çalışıyor
muhtemelen yukarıda auto add policy olduğundan key kullanımı gerekmiyor?
"""

# set_missing_host_key_policy >> eğer bilinen bir key yoksa bunu ekliyoruz
