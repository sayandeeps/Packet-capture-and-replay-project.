from scapy.all import sniff, wrpcap


target_ip = "3.7.179.253"

def packet_callback(packet):
  
    if packet.haslayer('IP') and (packet['IP'].src == target_ip or packet['IP'].dst == target_ip):

        if packet.haslayer('Raw'):
            payload = packet['Raw'].load
            if b'HTTP' in payload:
                print(packet.summary())

packets = sniff(iface="en0", filter=f"ip host {target_ip}", count=50, prn=packet_callback)

with open("telaverge-about-us.txt", "w") as f:
    for packet in packets:
        f.write(str(packet) + "\n")