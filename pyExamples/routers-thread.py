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
    'ip':   '192.168..',
    'username': '',
    'password': '',}
ios2 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168..',
    'username': '2',
    'password': '3',
}
"""

ios1 =('cisco_ios',  '192.168..', '', '')
ios2 =('cisco_ios',  '192.168..', '2', '2')

#map yerine dict olarak yolla

t1 = threading.Thread(target=calistir, args=(ios1,))
t2 = threading.Thread(target=calistir, args=(ios2,))

t1.start()
t2.start()

"""
def transform_mesh(translate_xyz):
    translate_x, translate_y, translate_z = translate_xyz  
"""
