import socketio

sio = socketio.Client()

USERNAME = "Ali"

@sio.event
def connect():
    print("Connected as", USERNAME)

@sio.event
def new_message(data):
    print("Received:", data)

sio.connect("http://localhost:5002")

while True:
    msg = input("Ali: ")
    sio.emit("chat_message", {"username": USERNAME, "message": msg})
