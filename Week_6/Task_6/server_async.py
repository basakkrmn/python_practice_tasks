import socketio
from aiohttp import web
import time

sio = socketio.AsyncServer(async_mode="aiohttp")
app = web.Application()
sio.attach(app)

@sio.event
async def connect(sid, environ):
    print("Client connected:", sid)

@sio.event
async def disconnect(sid):
    print("Client disconnected:", sid)

@sio.event
async def get_time(sid):
    print("Client requested time:", sid)
    return {"server_time": time.time()}  # async return OK

if __name__ == "__main__":
    web.run_app(app, port=5005)
