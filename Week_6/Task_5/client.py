import socketio

chat_sio = socketio.Client()
status_sio = socketio.Client()

@chat_sio.event(namespace="/chat")
def connect():
    print("Connected to /chat")

@chat_sio.on("new_chat_message", namespace="/chat")
def receive_chat(data):
    print("[CHAT] Message:", data)


@status_sio.event(namespace="/status")
def connect():
    print("Connected to /status")

@status_sio.on("health_response", namespace="/status")
def health_ok(data):
    print("[STATUS] Server health:", data)

chat_sio.connect("http://localhost:5004", namespaces=["/chat"])
status_sio.connect("http://localhost:5004", namespaces=["/status"])

print("\nBoth namespaces connected.\n")

while True:
    msg = input("Send chat message (or type 'check'): ")

    if msg == "check":
        status_sio.emit("health_check", "ping", namespace="/status")
    else:
        chat_sio.emit("chat_message", msg, namespace="/chat")
