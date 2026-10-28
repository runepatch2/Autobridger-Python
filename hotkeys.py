import keyboard
import threading
import time
import funcs
import minescript

mining = False
autoclicking = False
click_thread = None
bridge_thread = None
bridging = False

def clicking_loop():
    while autoclicking:
        funcs.autoclick_start()

def bridging_loop():
    while bridging:
        funcs.speed_bridge()

    
def on_press_f():
    global autoclicking, click_thread

    if not autoclicking:
        autoclicking = True
        click_thread = threading.Thread(target=clicking_loop)
        click_thread.start()

def on_press_g():
    global autoclicking
    autoclicking = False

def on_press_h():
    minescript.player_press_backward(True)
    global bridging, bridge_thread
    if not bridging:
        minescript.echo_json('{"text": "Bridging script started", "color": "green"}')
        bridging = True
        bridge_thread = threading.Thread(target=bridging_loop)
        bridge_thread.start()

def on_press_j():

    global bridging
    if bridging:
        minescript.echo_json('{"text": "Bridging script stopped", "color": "red"}')
    bridging = False
    minescript.player_press_backward(False)
    time.sleep(0.1)
    minescript.player_press_sneak(False)
    minescript.player_press_forward(True)
    time.sleep(0.1)
    minescript.player_press_forward(False)

keyboard.add_hotkey('f', on_press_f)
keyboard.add_hotkey('g', on_press_g)
keyboard.add_hotkey('h', on_press_h)
keyboard.add_hotkey('j', on_press_j)

while True:
    time.sleep(0.1)