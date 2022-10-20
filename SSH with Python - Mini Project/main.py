#proje akış şemasını ve uml sınıf yapısını da çiz ve ekle github'a, linkedin'e

from netmiko import ConnectHandler 
#import textfsm
import inputs
import outputs
#import json
import ast
import sys
#import os
import threading
import myThreads

class Main:
   #bi constructor tanımal buradaki toDo yu baslar baslamaz calistirsin ve diger taraftan gelen veriyi atsin icin? 

    #bir sınıftaki tüm metodları self parametresi ile mi çalıştırmak gerekiyor
    #non static, nor abstract class methods should have a parameter which is typically named self, STATİC VE ABSTRACT OLANLAR HARİÇ

    #metotları da private yap

    #send one command to one router ------------------------------------------------------------------

    def inputOneCommand():
    
        runRouterInfo = inputs.Inputs()
        runRouterInfo.routerInfo('one command') 
    
        platform = runRouterInfo.getPlatform()
        host = runRouterInfo.getHost()
        username = runRouterInfo.getUsername()
        password = runRouterInfo.getPassword()
        command = runRouterInfo.getCommand() #bunları da her yere yazacağımıza bir getRouterInfo metodu bu sınıfta yaz ona cek ondan al
        """
        if keyChoise == "withKey":
            device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
        elif keyChoise == "withoutKey":
            device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)"""
        
        device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)

        outputOption = input('\nTextfsm (1) | Json (2) | Write on database (3) | Default (4)\nChoose output option: ')  
    
        outPutOpt = outputs.Outputs()
        
        outPutOpt.setOutputOption(outputOption)
        outPutOpt.setOutputTextfsm(device.send_command(command, use_textfsm=True))
        outPutOpt.setOutputDefault(device.send_command(command))
        
        outPutOpt.oneCommandOutput()

        #İKİ KEZ ÇALIŞMA SORUNUNU HALLET!!!!!!! constructor oldugundan iki kez çalışıyordu onu değiştirdim

        #progrmadna çık, üst menüye dön vs gibi seçenkler de olmalı, en baştan başlatma mesela ana üst menu main yani tekrar başlatma
        
    # run the method depends on what comes from the input choise ------------------------------------------------------

    def dhcpConf():

        runRouterInfo = inputs.Inputs()
        runRouterInfo.routerInfo('default infos') 

        platform = runRouterInfo.getPlatform()
        host = runRouterInfo.getHost()
        username = runRouterInfo.getUsername()
        password = runRouterInfo.getPassword()

        ios = {}
        ios['device_type']=platform
        ios['host']=host
        ios['username']=username
        ios['password']=password

        net_connect =ConnectHandler(**ios)
        net_connect.enable()
        output =net_connect.send_command('show ip int brief')
        print(output)

        #OUTPUTLARI DA YOLLAMAYI UNUTMA DIGER TARAFA OUTPUT.PY

        config_commands = [ 'conf t', 'service dhcp', 'ip dhcp excluded-address 192.168.100.1 192.168.100.99', 'ip dhcp pool myPool', 'network 192.168.100.0 255.255.255.0', 'lease 2', 'default-router 192.168.100.1' ]
        #bu uzun komutu da input olarak bir textten falan çekmek lazım aslında gömülü olmaz çok amatörce dhcp için

        output = net_connect.send_config_set(config_commands)   
        print (output)

        output =net_connect.send_command('show ip int brief')
        print (output)

    def changeRouterIP():
    
        runRouterInfo = inputs.Inputs()
        runRouterInfo.routerInfo('change router IP') #bunu yazmadığım için object has no attribute hatası veriyordu sürekli, metot çalışmamış
        #command da çıkıyor çünkü bu metot çalıştırılınca command inputu da var, OVERLOAD ETMEK GEREK BAŞKA METODA

        platform = runRouterInfo.getPlatform()
        host = runRouterInfo.getHost()
        username = runRouterInfo.getUsername()
        password = runRouterInfo.getPassword()
        #newIP = runRouterInfo.getNewIP()

        ios = {}
        ios['device_type']=platform
        ios['host']=host
        ios['username']=username
        ios['password']=password

        # output = device.send_command("ping"+' '+hedef)

        net_connect =ConnectHandler(**ios)
        net_connect.enable()
        output =net_connect.send_command('show ip int brief')
        print(output)

        config_commands = [ 'int f0/0', 'ip address 192.168.50.10 255.255.255.0', 'no sh']
        output = net_connect.send_config_set(config_commands)
        print (output)

        output = net_connect.send_command('show ip int brief')
        print (output)

    def pingFromRouterToOthers():

        """ platform = 'cisco_ios'
        host = input('Host adı veya IP girin: ')
        username = input('Kullanıcı Adı girin: ') 
        password = input('Şifre girin: ') """

        runRouterInfo = inputs.Inputs()
        runRouterInfo.routerInfo('ping from router') #bunu yazmadığım için object has no attribute hatası veriyordu sürekli, metot çalışmamış
        #command da çıkıyor çünkü bu metot çalıştırılınca command inputu da var, OVERLOAD ETMEK GEREK BAŞKA METODA

        platform = runRouterInfo.getPlatform()
        host = runRouterInfo.getHost()
        username = runRouterInfo.getUsername()
        password = runRouterInfo.getPassword()
        hedef = runRouterInfo.getTarget()

        device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
        output = device.send_command("ping"+' '+hedef)

        print(output)
        input()

    if __name__ == "__main__":
        #def main(self):
        chooseWhatToDo = inputs.Inputs() #chooseWhatToDo bir nesne, bunun üzerinden getter ile whatToDo değerini alalım
        __toDo = chooseWhatToDo.getTask()
        #__toDo = chooseWhatToDo.getWhatToDo()
        #BU İKİ KEZ CONSTRUCTOR ÇALIŞTIRIYOR SANRIM BİRİNDE NESNE OLUŞUNCA DİĞERİNDE ATAYINCA MI?
        #CONSTRUCTOR YERINE DUZ METOD DENE ORAYI

#HEPSINDE EN BASTA PUTTY KEY ILE MI DEFAULT MU YOKSA AUDO ADD POLICY ILE MI BAGLANTI ISTEDIGINI SORAN BIR SEY OLMALI 
#VE BUNA GORE O TEK SATIRLIK BAGLANTIYA EKLMELER YAPILMALI VEYA AUTO ADD POLICY ICIN BIR SATIR DAHA DEGIESECEK YUKARIDA

        match __toDo:
            case "1":
                inputOneCommand()
            case "2":
                threadObj = myThreads.myThread()
                threadObj.threadRouters()
            case "3":
                changeRouterIP()
            case "4":
                dhcpConf()
            case "5":
                inputOneCommand()
            case "6":
                pingFromRouterToOthers()
            case "0":
                sys.exit()   
            case _:
                print("Doğru bir değer girmediniz.")

            #BU DOĞRU GİRİLMEZSE TEKRAR GİRME SORMASI İÇİN TEKRAR ÇALIŞTIR
            #HER BİR METOTTA ÜST MENÜYE DÖNEMK İÇİN (x) X E BASMA OLSUN MESELA, metotlar da o sırada yazılmalı alt alta 

