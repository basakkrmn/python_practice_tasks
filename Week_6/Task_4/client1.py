import socketio

sio = socketio.Client()
USERNAME = "Client1"
ROOM = None

@sio.event
def connect():
    print("Connected as", USERNAME)

@sio.event
def room_joined(data):
    print("SERVER:", data)

@sio.event
def new_room_message(data):
    print("MESSAGE:", data)

sio.connect("http://localhost:5003")

ROOM = input("Join which room? (roomA / roomB): ")


sio.emit("join_room", {"room": ROOM})

while True:
    msg = input(f"{USERNAME}: ")
    sio.emit("room_message", {"room": ROOM, "message": msg})
