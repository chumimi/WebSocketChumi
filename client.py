import socketio

sio = socketio.Client()
sio.connect('http://localhost:5000')

@sio.event
def connect():
    print('Connected to server')

@sio.event
def disconnect():
    print('Disconnected from server')

@sio.event
def chat_message(data):
    print('\nMessage from server:', data)

while True:
    message = input("Enter your message: ")
    sio.emit('chat_message', message)
