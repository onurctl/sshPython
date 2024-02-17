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
   
    #send one command to one router 

    def inputOneCommand():
    
        runRouterInfo = inputs.Inputs()
        runRouterInfo.routerInfo('one command') 
    
        platform = runRouterInfo.getPlatform()
        host = runRouterInfo.getHost()
        username = runRouterInfo.getUsername()
        password = runRouterInfo.getPassword()
        command = runRouterInfo.getCommand()
       
        """
        if keyChoise == "withKey":
            device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
        elif keyChoise == "withoutKey":
            device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
         """
        
        device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)

        outputOption = input('\nTextfsm (1) | Json (2) | Write on database (3) | Default (4)\nChoose output option: ')  
    
        outPutOpt = outputs.Outputs()
        
        outPutOpt.setOutputOption(outputOption)
        outPutOpt.setOutputTextfsm(device.send_command(command, use_textfsm=True))
        outPutOpt.setOutputDefault(device.send_command(command))
        
        outPutOpt.oneCommandOutput()
        
    # run the method depends on what comes from the input choise 

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

        config_commands = [ 'conf t', 'service dhcp', 'ip dhcp excluded-address 192.168.-.- 192.168.-.-', 'ip dhcp pool myPool', 'network 192.168.. 255.255.255.0', 'lease 2', 'default-router 192.168..' ]

        output = net_connect.send_config_set(config_commands)   
        print (output)

        output =net_connect.send_command('show ip int brief')
        print (output)

    def changeRouterIP():
    
        runRouterInfo = inputs.Inputs()
        runRouterInfo.routerInfo('change router IP') 

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

        config_commands = [ 'int f0/0', 'ip address 192.168.. 255.255.255.0', 'no sh']
        output = net_connect.send_config_set(config_commands)
        print (output)

        output = net_connect.send_command('show ip int brief')
        print (output)

    def pingFromRouterToOthers():

        """ 
        platform = 'cisco_ios'
        host = input('Host adı veya IP girin: ')
        username = input('Kullanıcı Adı girin: ') 
        password = input('Şifre girin: ') 
        """

        runRouterInfo = inputs.Inputs()
        runRouterInfo.routerInfo('ping from router') 

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
