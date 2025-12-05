# Python Practice Tasks – Week 6

This repository contains a collection of 6 projects designed to demonstrate the capabilities of the [python-socketio](https://python-socketio.readthedocs.io/en/latest/index.html) library. The projects range from a basic server-client connection to advanced features like rooms, namespaces, and asynchronous handling with `aiohttp`.

## Prerequisites & Installation

Before running these projects, ensure you have Python installed. You will need to install `python-socketio` and the necessary server/async libraries.

For Standard Projects (1-5):
    pip install python-socketio[client]
    pip install eventlet  # Recommended for standard server WSGI support

For the Async Project (6):
    pip install aiohttp
    pip install python-socketio[asyncio_client]

---

## Project 1: Basic Socket.IO Server & Client

**Goal:** Establish a basic connection between a server and a client.

### Server (`server.py`)
- Listens on port **5000**.
- Logs "Client connected" and "Client disconnected" events.
- Sends a `welcome` event to the client upon connection with the message: `"Welcome to the Socket.IO server!"`.

### Client (`client.py`)
- Connects to the server at `http://localhost:5000`.
- Listens for the `welcome` event and prints the received message.

**Expected Output:**
> **Server:** Logs connection ID and status.  
> **Client:** Prints: `Welcome to the Socket.IO server!`

---

## Project 2: Sending Custom Events & Data

**Goal:** Exchange JSON data between client and server.

### Client
- Sends a `login` event with the following JSON data:
    { "username": "Ali", "level": 5 }

### Server
- Listens for the `login` event.
- Extracts the data and responds with a `login_response` event containing:  
  `"Hello Ali! Your level is 5."`

**Expected Output:**
> **Client:** Prints the custom response received from the server.

---

## Project 3: Implement Real-Time Chat (Broadcasting)

**Goal:** Broadcast messages to all connected clients.

### Server
- Listens for a `chat_message` event.
- When received (e.g., `"chat_message": "Hello"`), it broadcasts a `new_message` event to **all** connected clients (including the sender).
- Broadcast data: `"Ali says: Hello"` (assuming username logic or raw text).

### Verification
- Create two separate client scripts.
- Run both clients simultaneously.

**Expected Output:**
> **Both Clients:** See messages sent by each other instantly.

---

## Project 4: Working with Rooms

**Goal:** Isolate communication using Rooms.

### Setup
- Define two rooms: `roomA` and `roomB`.

### Workflow
1. **Join:** Client emits `join_room` with `{"room": "roomA"}`. The server adds the client to that specific room.
2. **Message:** Client sends `room_message`.
3. **Broadcast:** Server broadcasts this message **only** to clients inside that specific room.

**Expected Output:**
> Clients in `roomA` communicate only with other `roomA` members. Clients in `roomB` do not see these messages.

---

## Project 5: Namespaces & Event Separation

**Goal:** Use Namespaces to separate application logic (e.g., Chat vs. System Status).

### Namespaces
1. **`/chat`**: Handles chat-related events (`chat_message`).
2. **`/status`**: Handles system events.
   - Event: `health_check`
   - Response: `"ok"`

### Client
- Connects to both `/chat` and `/status` namespaces.
- Logs events received from both channels separately.

**Expected Output:**
> Chat messages appear strictly on the `/chat` channel, while system checks appear on `/status`.

---

## Project 6: Asynchronous Socket.IO Server (aiohttp)

**Goal:** Build a non-blocking, asynchronous server and client using `asyncio` and `aiohttp`.

### Async Server (`aiohttp`)
- Uses `socketio.AsyncServer`.
- Defines asynchronous event handlers:
    @sio.event
    async def get_time(sid):
        return {"server_time": time.time()}

### Async Client
- Uses `python-socketio[asyncio]`.
- Asynchronously connects to the server.
- Sends a `get_time` event every **1 second**.
- Prints the server response.

**Expected Output:**
> **Client:** Prints the updated server time every second.  
> **Server:** Handles the load asynchronously without blocking.

---
## How to Run

- Each project is independent.

- Open the Python file for each project and run it in your preferred environment (PyCharm, VS Code, etc.).

- Follow on-screen prompts for input where applicable.
## Documentation

For full documentation on the library used in these projects, visit:
[https://python-socketio.readthedocs.io/en/latest/index.html](https://python-socketio.readthedocs.io/en/latest/index.html)