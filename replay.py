from scapy.all import rdpcap, sendp

packets = rdpcap("telaverge.pcap")

for packet in packets:
    sendp(packet, iface="en0")  
