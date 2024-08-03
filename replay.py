from scapy.all import rdpcap, sendp

# Load the captured packets
packets = rdpcap("telaverge.pcap")

# Replay packets
for packet in packets:
    sendp(packet, iface="en0")  # Send on the specified network interface
