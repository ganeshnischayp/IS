import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import sys
from scapy.all import *

# if len(sys.argv) != 4:
#     print("Usage %s target startport endport " % (sys.argv[0]))
#     sys.exit(0)

target = str(sys.argv[1])
print(target)
start = int(sys.argv[2])
end = int(sys.argv[3])
# print("Scanning "+target+" for open TCP ports\n")

# if start == end:
#     end += 1

# for x in range(start,end):
#     packet = IP(dst=target)/TCP(dport=x,flags='S')
#     response = sr1(packet,timeout=0.5,verbose=0)
#     if response.haslayer(TCP) and response.getlayer(TCP).flag==0x14:
#         print("Port "+str(x)+" port is open")
#     sr(IP(dst=target)/TCP(dport=response.sport,flag='R'),timeout=0.5,verbose=0)

print("scan is complete")