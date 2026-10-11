import pygame
import sys
import socket
import json

###### Joystick Init #######
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick detected.")
    sys.exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Initialized Joystick: {joystick.get_name()}")

###### Socket Init #######
print("Initializing sockets...")
SERVERS = [
    ("172.16.196.158", 5005),  # Raspberry Pi 1
    ("172.16.153.172", 5005),
    ("172.16.184.51", 5005), 
    ("172.16.132.128", 5005),
    ("172.16.254.155", 5005), 
    ("172.16.251.74", 5005),
    
    ("172.16.192.212", 5005)
    # Add more servers if needed
]

sockets = []
for host, port in SERVERS:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sockets.append(sock)
        print(f"Connected to {host}:{port}")
    except Exception as e:
        print(f"Failed to connect to {host}:{port} - {e}")

if not sockets:
    print("No servers connected. Exiting.")
    sys.exit()

print("Socket initialization complete.")
print("Listening for joystick events...")

###### Main loop ######
running = True
state = {"stick1": [], "stick2": [], "triggers": []}
socket_id = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.JOYAXISMOTION:
            axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
            state["stick1"] = axes[0:2]
            state["stick2"] = axes[2:4]
            state["triggers"] = axes[4:6]
            try:
                json_state = json.dumps(state) + "\n"
                sockets[socket_id].sendall(json_state.encode('utf-8'))
            except Exception as e:
                print(f"Connection lost to {sockets[socket_id].getpeername()} - {e}")
                break

        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 5:
                socket_id = (socket_id + 1) % len(sockets)
                print(f"Switched to server {socket_id}: {sockets[socket_id].getpeername()}")

pygame.quit()