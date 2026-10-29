from scapy.all import Ether, IP, TCP, Raw, wrpcap

packet = (
    Ether()
    / IP(src="192.0.2.10", dst="192.0.2.20")
    / TCP(sport=12345, dport=8080)
    / Raw(load=b"CODTECH-IDS-TEST")
)

wrpcap("test_capture.pcap", [packet])

print("Created test_capture.pcap")