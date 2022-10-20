#çıktı olarak alınan ve text, json ve/veya veritabanına yazılan veriler

import sys
import json

class Outputs():

    def oneCommandOutput(self):
        if self.__outputOption=='1':
            print(self.__outputWithTextfsm)
            writeOption = input('Do you want the output to write to a text file? (y) for yes | (n) for no: ')
            if writeOption=='y':
                  with open('textOutput.txt', 'w') as outfile:
                    outfile.write(' '.join(map(str, self.__outputWithTextfsm)))
                    outfile.write('\n')
            else: 
                sys.exit()
                #os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
    
            #BUNLARI TRY CATCH ARASINA YAZ DB İŞLEMİ OLMASA DA HATAYI GÖRMEYE YARAR DOĞRU BIR KULLANIM
            #İŞLEMİN YAPILMADIĞINA DAİR MESAJ VERDİRMİŞ OLURUSN IF ELSE TEKRAR KULLANMADAN KONTROL İÇİN

        elif self.__outputOption=='2':
            print(json.dumps(self.__outputWithTextfsm))
            writeOption = input('Do you want the output to write to a json file? (y) for yes | (n) for no')
            if writeOption=='y':
                jsonFile = open("jsonOutput.json", "w")
                jsonFile.write(json.dumps(self.__outputWithTextfsm))
                jsonFile.close()
            else:
                sys.exit()
                #os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)       
      
        elif self.__outputOption=='4':
                print(self.__outputDefault)
        input()

    def setOutputOption(self, outputOption):
        self.__outputOption = outputOption

    def setOutputTextfsm(self, outputWithTextfsm):
        self.__outputWithTextfsm = outputWithTextfsm

    def setOutputDefault(self, outputDefault):
        self.__outputDefault = outputDefault    

#maindeki çıktıları protected değerlere atalım bu onun subclass ı kalıtımla boylece erişir