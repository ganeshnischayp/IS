#!/usr/bin/python3

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip = input("Enter ip address / website url \n")
src_port=RandShort()
dst_port=53
conf.verb=0

#print(str(type(tcp_connect_scan_resp)))
print("Checking whether  dstination host is alive....")
ping = sr1(IP(dst = dst_ip)/ICMP(),timeout=5)
if(str(type(ping))=="<class 'NoneType'>"):
    print("host is dead, cannot conduct port scaninng")
    print("Exiting...")
    sys.exit(1)

print("Destination Host is alive!!")

def TCP_CONNECT(dst_port):
    SYN=IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S")
    print(" Sending SYN message to ",dst_ip)
    print("TCP header contents")
    SYN.getlayer(TCP).display()
    tcp_connect_scan_resp = sr1(SYN,timeout=10)
    scan_result=""
    conf.verb = 0 

    if(str(type(tcp_connect_scan_resp))=="<class 'NoneType'>"):
        print("No packet recieved from ",dst_ip)
        scan_result="SYN packet was filtered/dropped"

    elif(tcp_connect_scan_resp.haslayer(TCP)):

        print("Packet Recieved!!")
        print("Content of packet recieved from  ",dst_ip)
        tcp_connect_scan_resp.getlayer(TCP).display()
        if(tcp_connect_scan_resp.getlayer(TCP).flags == 0x12):
            
            scan_result="Port "+str(dst_port)+" is Open"
            print("Sending ACK  packet to ",dst_ip,"with content:")
            A=IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="A")
            A.getlayer(TCP).display()
            send_ack = sr(A,timeout=10)
            print("Reseting the connection to ",dst_ip,"with content")
            R=IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="R")
            R.getlayer(TCP).display()
            send(R)
            

        elif (tcp_connect_scan_resp.getlayer(TCP).flags == 0x14):
            scan_result="Port "+str(dst_port)+" is closed"

    return scan_result
scan_result=TCP_CONNECT(dst_port)
print("---------------")
print(scan_result)
print("---------------")
