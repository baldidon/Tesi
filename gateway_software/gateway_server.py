import socket
import sys
import subprocess

#codice per "assegnare ogni volta socket diverso al server. Quando viene lanciato il programma, oltre al nome del va scritto

if len(sys.argv) == 3:
    # Get "IP address of Server" and also the "port number" 
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Run like : python3 server.py <arg1:server ip:this system IP 192.168.43.158> <arg2:server port:4444 >")
    exit(1)



# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the po
server_address = (ip,port)
s.bind(server_address)
print("Do Ctrl+c to exit the program !!")

while True:
    print("####### Server in attesa di datagrammi #######")
    data, address = s.recvfrom(4096)
    print("\n\n pacchetto ricevuto!: ", data.decode("utf-8", "ignore"), "\n\n")
    string = data.decode("utf-8", "ignore")
    x = string.find("<5678>")

    if x !=-1: #find restituisce la pos del primo carattere, in questo caso la pos di "<". se non trova la sequenza data in input restituisce -1
        #print("ok") #only for debug 
        y = string[0:x]; #l'"header" da scartare prima di ogni messaggio!
        string.replace(y,"")
        string.split(" ")
        data=string.split()[1]

        #per dare il comando
        cmd =  f'mosquitto_pub -h mqtt.thingspeak.com -p 1883 -u dragino -P VBYIAGAZXRGBPFXM -i dragino -t channels/5678/publish/SI70N5CLF8S4929A -m "{data}&status=MQTTPUBLISH"'
        results = subprocess.run(cmd, shell=True, universal_newlines=True, check=True)
        print(results.stdout)
