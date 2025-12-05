import socketio
from flask import Flask
import eventlet
import eventlet.wsgi

app = Flask(__name__)
sio = socketio.Server()
app = socketio.WSGIApp(sio, app)

@sio.event
def connect(sid, environ):
    print("Client connected:", sid)
    sio.emit("welcome", "Welcome to the Socket.IO server!", room=sid)

@sio.event
def disconnect(sid):
    print("Client disconnected:", sid)

@sio.event
def join_room(sid, data):
    room = data.get("room")
    print(f"{sid} joined room: {room}")

    sio.enter_room(sid, room)
    sio.emit("room_joined", f"You joined {room}", room=sid)

@sio.event
def room_message(sid, data):
    room = data.get("room")
    message = data.get("message", "")

    broadcast_text = f"[{room}] {sid}: {message}"
    print("Room broadcast:", broadcast_text)

    sio.emit("new_room_message", broadcast_text, room=room)

if __name__ == '__main__':
    print("Server is running on http://0.0.0.0:5003")
    try:
        eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5003)), app)
    except KeyboardInterrupt:
        print("\nServer shutting down gracefully...")


