import socketio
from flask import Flask
import eventlet
import eventlet.wsgi

app = Flask(__name__)

sio = socketio.Server()
app = socketio.WSGIApp(sio, app)

@sio.on("connect", namespace="/chat")
def chat_connect(sid, environ):
    print("[/chat] Client connected:", sid)

@sio.on("disconnect", namespace="/chat")
def chat_disconnect(sid):
    print("[/chat] Client disconnected:", sid)

@sio.on("chat_message", namespace="/chat")
def handle_chat_message(sid, data):
    print("[/chat] Message:", data)
    sio.emit("new_chat_message", data, namespace="/chat")

@sio.on("connect", namespace="/status")
def status_connect(sid, environ):
    print("[/status] Client connected:", sid)

@sio.on("disconnect", namespace="/status")
def status_disconnect(sid):
    print("[/status] Client disconnected:", sid)

@sio.on("health_check", namespace="/status")
def health_check(sid, data):
    print("[/status] Health check received:", data)
    sio.emit("health_response", "ok", room=sid, namespace="/status")

if __name__ == "__main__":
    print("Server running on http://0.0.0.0:5004")
    try:
        eventlet.wsgi.server(eventlet.listen(("0.0.0.0", 5004)), app)
    except KeyboardInterrupt:
        print("\nServer shutting down gracefully...")
