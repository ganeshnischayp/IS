#!/usr/bin/env python
 
import time
import queue
import threading
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
 
# ip = "www.nitk.ac.in"
ip = "192.168.43.75"
closed = 0
 
class Scanner(threading.Thread):
    """ Scanner Thread class """
    def __init__(self, queue, lock):
        super(Scanner, self).__init__()
        self.queue = queue
        self.lock = lock
 
    def run(self):
        global closed
        src_port = RandShort()
        port = self.queue.get()
        p = IP(dst=ip)/TCP(sport=src_port, dport=port, flags='S')
        resp = sr1(p, timeout=2)
        if str(type(resp)) == "<type 'NoneType'>":
            with lock:
                closed += 1
        elif resp.haslayer(TCP):
            if resp.getlayer(TCP).flags == 0x12:
                send_rst = sr(IP(dst=ip)/TCP(sport=src_port, dport=port, flags='AR'), timeout=1)
                with lock:
                    print( "[*] %d open ", port)
            elif resp.getlayer(TCP).flags == 0x14:
                with lock:
                    closed += 1
        self.queue.task_done()
 
def is_up(ip):
    p = IP(dst=ip)/ICMP()
    resp = sr1(p, timeout=10)
    if resp == None:
        return False
    elif resp.haslayer(ICMP):
        return True
 
if __name__ == '__main__':
    conf.verb = 0
    start_time = time.time()
    ports = range(1, 1024)
    lock = threading.Lock()
    queue = queue.Queue()
    if is_up(ip):
        print ("Host %s is up, start scanning" , ip)
        for port in ports:
            queue.put(port)
            scan = Scanner(queue, lock)
            scan.start()
        queue.join()
        duration = time.time()-start_time
        print( ip, " Scan Completed in ",duration)
        print( closed," closed ports in ",len(ports)," total port scanned")
    else:
        print ("Host ",ip," is Down")