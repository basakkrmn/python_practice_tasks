import socketio

sio = socketio.Client()

@sio.event
def welcome(data):
    print("Server says:", data)

@sio.event
def login_response(data):
    print("Server says:", data)

@sio.event
def connect():
    print("Connected to server!")
    sio.emit("login", {"username": "Ali", "level": 5})

@sio.event
def disconnect():
    print("Disconnected from server")

sio.connect('http://localhost:5001')
sio.wait()
