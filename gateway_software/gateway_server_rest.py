#client per caricare dati su thingspeak che sfrutta le apiREST, forse dovrebbe essere 
#più semplice che sfruttare mqtt!
import time
import requests
import urllib
import sys
import socket
import datetime
import json

#codice per "assegnare ogni volta socket diverso al server. 
#Quando viene lanciato il programma, oltre al nome del va scritto
#indirizzo (loopback)
#porta 4444
if len(sys.argv) == 3:
    # Get "IP address of Server" and also the "port number" 
    ip = sys.argv[1]
    port = int(sys.argv[2])
    print(ip)
    print(port)
else:
    print("Run like : python3 server.py <arg1:server ip:this system IP 192.168.43.158> <arg2:server port:4444 >")
    exit(1)



# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (ip,port)
s.bind(server_address)
print("ctrl+c per uscire!!")
get = "https://api.thingspeak.com/update?api_key=SI70N5CLF8S4929A&"

#mostrare anche, oltre al messaggio pacchetto ricevuto, l'orario di ricezione!!
while True:
    print("####### Server in attesa di datagrammi #######")
    data, address = s.recvfrom(4096)
    print("\n\n",datetime.datetime.now(),": pacchetto ricevuto!: ", data.decode('utf-8'), "\n\n")
    string = data.decode('utf-8').strip()
    x = string.find("<5678>")

    if x !=-1: #find restituisce la pos del primo carattere, in questo caso la pos di "<". se non trova la sequenza data in input restituisce -1
        req = ""
        y = string[0:x]; #l'"header" da scartare prima di ogni messaggio!
        string.replace(y,"")
        string.split(" ")
        data=string.split()[1]
        req= get+data #a cui va concatenato il payload del messaggio
        r = requests.post(req) #permette di sfruttare l'api per fare una get
        output = r.json()#restituisce il numero di entry
        print(output)

        if output == 0:
            while output ==0:
                time.sleep(15) #tempo minimo upload da rispettare! vedi accordi di licenza
                r = requests.post(req)
                output = r.json()
                print(r.json())
