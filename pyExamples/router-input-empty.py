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


#input()

#router degisimi için baştaki kodu bir metot içine al ve metotun so nsatırında da komut metodu çalışsın, komut metodunda "deg" denilirse tekrar router seçim metodu çalışsın if ile kontrol

#conf t dediğimde mod değişiyor bu nedenle hata var bence çünkü enterladığımda boş komutu orada sorun #çıkmıyor, mod değişiminde farklı bir şey oluyor
# output istenmiyorsa komut yazdıktan sonra output isterseniz bu komutta komut için şunu girin vs dense çok angarya olur

#çıkmadan komut yazıyoruz sürekli çok iyi ama output vermeyen conf t gibi komutlarda sorun çıkmaması
#için ya onlar için while içine if ekleyip bunlarda output vermemesini sağlarız ya da başka bir yol
# ya da basiti if output is not empty deriz else için de tekrar komut girin ve kontrol

"""çalışan kod: 
while komut!='x':
	komut = input('Komut girin: ')
	output = device.send_command(komut)
	print(output)"""
# boş değil de direkt null dönüyor sanırım bo şdeğil null kontrolünü dene
#kod hatalı girilirse de sorun olmadan hata verdirip devam eder output veriyor zaten ona da
#halen eksik tabii komple bir program için şu an conf t demiyim config dhcp de miyim bilmiyorum
# O ANKİ STATUS U ALMAM LAZIM # CONFIG VS NE OLDUĞUNU!!!!!!!!!!!!