import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import sys 
from scapy.all import *

# destination = input("Enter url: ")
destination = "www.nitk.ac.in"

# destination_port = int(input("Enter port to check: "))
# destination_port = 1024
# if destination_port > 65535:
#     print("Enter port less than 65535. ")
#     destination_port = int(input("Enter port to check: "))


# start = int(input("lower range: "))
start = 0
end = 26
# end = int(input("upper range: "))

source_port = RandShort()
conf.verb = 0

ping = sr1(IP(dst = destination)/ICMP(),timeout=5)

print("Checking %s is alive...."%(destination))

if(str(type(ping))=="<class 'NoneType'>"):
    print("%s is dead"%(destination))
    sys.exit(0)
print("Host is Working")

def synchronize(destination_port):
    result_ping=""
    SYN=IP(dst=destination)/TCP(sport=source_port,dport=destination_port,flags="S")
    print("Sending SYN to ",destination,"with contents")
    SYN.getlayer(TCP).display()
    scan_response = sr1(SYN,timeout=10)
    result_ping=""

    if(str(type(scan_response))=="<class 'NoneType'>"):
        print("No packets recieved from ",destination)
        result_ping="Filtered / dropped"

    elif(scan_response.haslayer(TCP)):
        print("Packet recieved from ",destination," with contents:")
        scan_response.getlayer(TCP).display()

        if(scan_response.getlayer(TCP).flags == 0x12):
            result_ping="Port "+str(destination_port)+" is open"
            RST=IP(dst=destination)/TCP(sport=source_port,dport=destination_port,flags="R")
            print("Reseting Connection with ",destination,"with contents:")
            RST.getlayer(TCP).display()
            send(RST)
            

        elif (scan_response.getlayer(TCP).flags == 0x14):
            result_ping="Port "+str(destination_port)+" is Closed"
    
    return result_ping

def tcp(destination_port):
    SYN=IP(dst=destination)/TCP(sport=source_port,dport=destination_port,flags="S")
    print(" Sending SYN message to ",destination)
    print("TCP header contents")
    SYN.getlayer(TCP).display()
    tcp_response = sr1(SYN,timeout=10)
    result_ping=""
    conf.verb = 0 

    if(str(type(tcp_response))=="<class 'NoneType'>"):
        print("No packet recieved from ",destination)
        result_ping="SYN packet was filtered/dropped"

    elif(tcp_response.haslayer(TCP)):

        print("Packet Recieved!!")
        print("Content of packet recieved from  ",destination)
        tcp_response.getlayer(TCP).display()
        if(tcp_response.getlayer(TCP).flags == 0x12):
            
            result_ping="Port "+str(destination_port)+" is Open"
            print("Sending ACK  packet to ",destination,"with content:")
            A=IP(dst=destination)/TCP(sport=source_port,dport=destination_port,flags="A")
            A.getlayer(TCP).display()
            send_ack = sr(A,timeout=10)
            print("Reseting the connection to ",destination,"with content")
            R=IP(dst=destination)/TCP(sport=source_port,dport=destination_port,flags="R")
            R.getlayer(TCP).display()
            send(R)
            

        elif (tcp_response.getlayer(TCP).flags == 0x14):
            result_ping="Port "+str(destination_port)+" is closed"

    return result_ping

if sys.argv[1] == "syn":
    for i in range(start,end):
        result_ping=synchronize(i)

    # result_ping=synchronize(destination_port)
        print("---------------")
        print(result_ping)
        print("---------------")

elif sys.argv[1] == "tcp":
    for i in range(start,end):
        result_ping=synchronize(i)

    # result_ping=synchronize(destination_port)
        print("---------------")
        print(result_ping)
        print("---------------")

