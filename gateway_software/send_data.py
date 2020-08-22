import os
import datetime
import subprocess

#script che verrà eseguito ogni minuto, temporizzato grazie a crontab

file = open("/home/andrea/lora.txt","r")
#file = open("/home/andrea/prova","r")
string = file.readline()
print(string)
x = string.find("<5678>")
if x !=-1:
    print("bigUp") 
    y = string[0:x]; #l'"header" da scartare prima di ogni messaggio!
    string.replace(y,"")
    string.split(" ")
    data=string.split()[1]

    #per dare il comando
    cmd =  f'mosquitto_pub -h mqtt.thingspeak.com -p 1883 -u dragino -P VBYIAGAZXRGBPFXM -i dragino -t channels/5678/publish/SI70N5CLF8S4929A -m "{data}&status=MQTTPUBLISH"'
    results = subprocess.run(cmd, shell=True, universal_newlines=True, check=True)
    print(results.stdout)
file.close()

#per ottenere un file pulito ogni volta!
file = open("/home/andrea/lora.txt","w")
#file = open("/home/andrea/prova" ,"w")
file.write("")
file.close()