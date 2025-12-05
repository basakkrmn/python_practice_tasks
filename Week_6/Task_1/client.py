import socketio

sio = socketio.Client()

@sio.event
def welcome(data):
    print("Server says:", data)

@sio.event
def connect():
    print("Connected to server!")

@sio.event
def disconnect():
    print("Disconnected from server")

sio.connect('http://localhost:5000')
sio.wait()
