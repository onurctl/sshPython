import threading
from netmiko import ConnectHandler 

def calistir(*ios):
     for i in range(2): 
        net_connect =ConnectHandler(*ios)
        net_connect.enable()
        output =net_connect.send_command('show ip int brief')
        print(output)

#t1 = threading.Thread(target=calistir, args = ("thread-1", ))
#t2 = threading.Thread(target=calistir, args = ("thread-2", ))
"""
ios1 = { 
    'device_type': 'cisco_ios',
    'ip':   '192.168.50.2',
    'username': 'admin',
    'password': 'cisco',}
ios2 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.50.3',
    'username': 'admin2',
    'password': 'cisco3',
}
"""
ios1 =('cisco_ios',  '192.168.50.2', 'admin', 'cisco')
ios2 =('cisco_ios',  '192.168.50.3', 'admin2', 'cisco2')

#bu map, bunun yerine dict olarak yollamaya çalış bu sorun çıkarıyor!!!!!!!!!!!!!

t1 = threading.Thread(target=calistir, args=(ios1,))
t2 = threading.Thread(target=calistir, args=(ios2,))

t1.start()
t2.start()

""" Tuple parameters are not supported in Python3, but you can pass it as a variable and unpack it after defining the function.

def transform_mesh(translate_xyz):
    translate_x, translate_y, translate_z = translate_xyz  
"""

#You're passing a sequence of arguments, for which you use one asterisk. The double-asterisk syntax is for #passing a mapping, for instance to do something like this:
