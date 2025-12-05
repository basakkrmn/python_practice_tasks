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

@sio.event
def disconnect(sid):
    print("Client disconnected:", sid)

@sio.event
def chat_message(sid, data):
    username = data.get("username", "Unknown")
    message = data.get("message", "")

    broadcast_text = f"{username} says: {message}"

    print("Broadcasting:", broadcast_text)
    sio.emit("new_message", broadcast_text)

if __name__ == "__main__":
    print("Chat server running on http://0.0.0.0:5002")
    try:
        eventlet.wsgi.server(eventlet.listen(("0.0.0.0", 5002)), app)
    except KeyboardInterrupt:
        print("\nServer shutting down gracefully...")
