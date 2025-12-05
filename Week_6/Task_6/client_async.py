import asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("Connected to server.")

@sio.event
async def disconnect():
    print("Disconnected from server.")

async def main():
    await sio.connect("http://localhost:5005")

    while True:
        response = await sio.call("get_time")
        print("Server Time:", response["server_time"])
        await asyncio.sleep(1)

asyncio.run(main())
