from netmiko import ConnectHandler 
import sys

def komutGiris():
	komut='abc'
	while komut!='x':
		komut = input('Komut girin: ')
		if komut=='deg':
			routerSecim()
		elif komut=='cik'
			sys.exit()
		else:
			output = device.send_command(komut)
		if (output != None):		
			print(output)		
		else:
			print("...")
def routerSecim():
	global device
	platform = 'cisco_ios'
	host = input('Host adı veya IP girin: ')
	username = input('Kullanıcı Adı girin: ') 
	password = input('Şifre girin: ') 
	device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
	komutGiris()

routerSecim()

""" çalışan kod: 
while komut!='x':
	komut = input('Komut girin: ')
	output = device.send_command(komut)
	print(output)
"""
