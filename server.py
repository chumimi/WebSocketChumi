import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('Client connected', sid)

@sio.event
def disconnect(sid):
    print('Client disconnected', sid)

@sio.event
def chat_message(sid, data):
    print('Message from {}: {}'.format(sid, data))
    sio.emit('chat_message', data)

if __name__ == '__main__':
    import eventlet
    eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)
