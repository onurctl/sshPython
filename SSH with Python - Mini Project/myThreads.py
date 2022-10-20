# --------------

#this class was created because of "function is not defined" error 
#to use "self" without main function

#BUNU MAIN ICINDE BIR CLASS A KOY BUNA GEREK YOK AYRI CLASS ORADA YAZ

import inputs
import threading
from netmiko import ConnectHandler 

class myThread:

    def connectThread(self, device_info, command):
        connect = ConnectHandler(**device_info)
        output = connect.send_command(command)
        print(connect.host)
        print(output+'\n')  

    def simpleThread(self):
        
        chooseSource = input("dict-list.txt (1) | data.json (2) | database (3)\nChoose the source of router informations:")

        if chooseSource=='1':
            getDataFromText = inputs.Inputs()
            dicts = []
            dicts = getDataFromText.getDataForThreading('1')
            ios1 = dicts[0]
            ios2 = dicts[1]

            threads = []
            devices = [ios1,ios2]
            command = input("Command: ")
            for device_info in devices:
                th = threading.Thread(target=self.connectThread, args=(device_info, command))
                threads.append(th)
    
            for thread in threads:
                thread.start()

            for thread in threads:
                thread.join()

    def threadRouters(self):
        self.simpleThread()