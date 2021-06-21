import socket
import time


UDP_IP = "192.168.100.27"
UDP_PORT = 5005
buf = 1024
file_name = "V6 - Change The World.mp3"


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(file_name, (UDP_IP, UDP_PORT))
print "Sending %s ..." % file_name

f = open(file_name, "r")
data = f.read(buf)
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
        data = f.read(buf)
        time.sleep(0.02) # Give receiver a bit time to save

sock.close()
f.close()