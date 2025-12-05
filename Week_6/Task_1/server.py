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

if __name__ == '__main__':
    print("Server is running on http://0.0.0.0:5000")
    try:
        eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
    except KeyboardInterrupt:
        print("\nServer shutting down gracefully...")


