from scapy.all import *

packets = sniff(iface="Ethernet", filter="icmp", count=8)
packets.show()
print(packets[2][1].src)
print(packets[4][1].dst)
