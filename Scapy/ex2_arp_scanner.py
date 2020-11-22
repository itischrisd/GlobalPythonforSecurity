from scapy.all import *
from scapy.layers.l2 import ARP, Ether

for lsb in range(50):
    ip = "10.21.0.{}".format(lsb)
    arp_req = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
    arp_res = srp1(arp_req, timeout=1, verbose=0)
    if arp_res:
        print("IP: {}, MAC: {}".format(arp_res.psrc, arp_res.hwsrc))
