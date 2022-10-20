#ana class'ta constructor nesne oluşturmadan çalışmadı ama child class'ta nesnesiz çalıştı?

#gns3

#constructor nesne oluşturulduğu an çalışır o halde bu şekilde çalışmasını beklemek saçma, çalışacağı sınıftan nesne oluşmalı

#inputs un bundan kalitim almasina gerek yok karşılıklı circular hatası veriyor constructor ı main den çalıştırınca ve bir de zaten input main den bir şey almayacak o nedenle gerek yok kalıtıma

import ast

class Inputs():

    #choose one task before the connection -----------------------------------------------------------------
     
    #BU CONSTRUCTOR DIYE MI IKIZ KEZ CALISIYOR????

    def getTask(self):
        self.__whatToDo = input("Input one command (for only one router) - 1\n"     

        #private için "__" protected için "_" kullanılır

                            +"Simple thread using dicts from text file | json | database - 2\n"
                            #DB DEN VERI CEKEREK THREAD DE YAPMAYA CALIS VEYA KESINLKLE JSON'DAN DA API DEN CEKEREK YAPILIYORDUR UZAK DB YE BAGLANIP
                            
                            +"Send multiple commands (Set router's IP) - 3\n"            
                            +"DHCP Configuration - 4\n"
                            +"Using PuTTY Key Generator - 5\n"
                            +"Ping from Router to PC - 6\n"
                            +"Exit - 0\n\n"

                            +"Enter the number of work you want to run: ")
        return self.__whatToDo
    
    """def getWhatToDo(self):
      return self.__whatToDo"""

    #connection infos ----------------------------------------------------------------

    def routerInfo(self, choise):

        if choise == 'default infos':
          self.__platform = 'cisco_ios'
          self.__host = input('Hostname or IP: ')
          self.__username = input('Username: ') 
          self.__password = input('Password: ') 
        
        #başka bir metot bunun 4 değişkeni de kullanacak ama sadece hedef ip değişkeni farklı eklenecek bir de, command ise yok
        #bunun için tekrarlı kod yazmaktan bizi kurtaracak bir OOP yapısı olmalı araştır
        #yoksa overload mı edeceğiz mecbur?

        if choise == 'one command':
          self.__command = input ('Command: ')
        elif choise == 'ping from router':
            self.__target = input('Target: ')
        elif choise == 'change router IP':
            self.__newIP = input ('New IP: ')

    def getNewIP(self):
      return self.__newIP

    def getTarget(self):
      return self.__target

    #

    def getPlatform(self):
      return self.__platform
    
    def getHost(self):
      return self.__host
    
    def getUsername(self):
      return self.__username
    
    def getPassword(self):
      return self.__password
    
    def getCommand(self):
      return self.__command

    # bunun router sayısı kadar getter i olsun ASLINDA OLMASI GEREKEN ARRAYLIST GIBI BIR SEYE ATMAK 500 ROUTER OLABILIR CUNKU

    #getting router infos for threading ---------------------------------------------------------------
    
    def getDataForThreading(self, chooseNumber):

        if chooseNumber=='1':
          with open('dict-list.txt', 'r') as file:
            list = ast.literal_eval(f'[{file.read()}]')
            
            ios1 = list[0]
            ios2 = list[1]

            #print(ios2) bunları yazdırdık dosyadan çekmesinde bir sorun yok sorun sonrasında

            dicts = []
            dicts.append(list[0])
            dicts.append(list[1])

            #print(dicts)
            #ikisini bir list içine koyup yolla ve indeksle al
          
            return dicts