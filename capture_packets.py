from scapy.all import sniff, wrpcap

# Define the IP address you want to filter
target_ip = "3.7.179.253"

def packet_callback(packet):
    # Check if the packet contains an IP layer and matches the target IP address
    if packet.haslayer('IP') and (packet['IP'].src == target_ip or packet['IP'].dst == target_ip):
        # Check if the packet has a Raw layer (which contains the HTTP payload)
        if packet.haslayer('Raw'):
            payload = packet['Raw'].load
            if b'HTTP' in payload:
                print(packet.summary())  # Optional: print packet summary

# Capture packets with a filter for the specific IP address
packets = sniff(iface="en0", filter=f"ip host {target_ip}", count=50, prn=packet_callback)

# Save packets to a pcap file
# wrpcap("telaverge-about-us.pcap", packets)
with open("telaverge-about-us.txt", "w") as f:
    for packet in packets:
        f.write(str(packet) + "\n")