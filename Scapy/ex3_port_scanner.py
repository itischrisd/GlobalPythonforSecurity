from scapy.all import *
from scapy.layers.inet import TCP, IP

target = input("IP celu: ")

for port in range(0, 100):
    x = (IP(dst=target)/TCP(dport=[port], flags="S"))
    rec, wrong = sr(x, timeout=1, verbose=0)
    if rec:
        data = "{}".format(rec[0]).split(" ")[7][6:]
        print("Port {}, protokół = TCP, Usługa = {}".format(port, data))
