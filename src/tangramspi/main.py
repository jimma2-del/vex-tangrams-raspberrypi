import asyncio

import websockets
import json

from .robot import Robot

with open('id.txt', 'r') as f:
    ID = f.read()

HOSTNAME = input("Enter hostname: ")
PORT = 3000

URI = "ws://{HOSTNAME}:{PORT}"

robot = Robot(id)

async def handle_websocket():
    while True:
        try:
            print("Connecting to server...")

            async with websockets.connect(URI) as ws:
                print("Connected!")

                await ws.send(json.dumps({ 'type': 'id', 'id': ID }))
        
                async for msg in ws:
                    event = json.loads(msg)
                    robot.set_action(event)
                    
        except websockets.exceptions.ConnectionClosed as e:
            print(f"Disconnected from server: {e}. Retrying in 5 seconds...")
            await asyncio.sleep(5)


async def main():
    asyncio.create_task(handle_websocket())
    
asyncio.run(main())