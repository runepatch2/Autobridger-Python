import minescript # A mod that lets you create python scripts for minecraft
import time

# These functions are called by another file called hotkeys.py 
# with the help of the keyboard module

def sprint():
    minescript.player_press_sprint(True)
    minescript.player_press_forward(True)

# Can click up to 40 times per second
def autoclick_start():
    minescript.player_press_attack(True)
    time.sleep(0.025)
    minescript.player_press_attack(False)

def speed_bridge():
    # Get player orientation and position info
    x, y, z = minescript.player_position()
    dec_x = abs(x - int(x))
    dec_z = abs(z - int(z))
    yaw = minescript.player_orientation()[0] % 360
    
    # Used to determine what direction the player is facing
    # South is 0/360 degrees, west is 90 degrees, north is 180, and east is 270
    direction_deltas = {
    's': abs(yaw),
    'w': abs(yaw - 90),
    'n': abs(yaw - 180),
    'e': abs(yaw - 270)
    }
    directions = []

    for direction in direction_deltas:
        directions.append(direction_deltas.get(direction))

    directions.sort()

    facing = ([key for key, value in direction_deltas.items() if value == directions[0]])
    # Accounts for weird case where the player would be facing south-south east, but was still considered east
    if yaw > 315:
        facing[0] = 's'
    
    # Do something different depending on which direction the player is facing
    # The player is set to walk if they are far from the edge of a block.
    # Once they get near the edge of a block the player sneaks.
    match facing[0]:
     case 's':
            minescript.player_set_orientation(0, 78.6)
            if (dec_z > 0.65):
                minescript.player_press_sneak(True)
            else:
                minescript.player_press_sneak(False)
     case 'w':
            minescript.player_set_orientation(90, 78.6)
            if (dec_x > 0.35):
                minescript.player_press_sneak(False)
            else:
                minescript.player_press_sneak(True)
     case 'n':
         minescript.player_set_orientation(180, 78.6)
         if (dec_z < 0.35):
            minescript.player_press_sneak(True)
         else:
            minescript.player_press_sneak(False)
     case 'e':
         minescript.player_set_orientation(270, 78.6)
         if (dec_x < 0.65):
            minescript.player_press_sneak(False)
         else:
            minescript.player_press_sneak(True)

    # Automatically place block when facing the side of a block
    try:
        if minescript.player_get_targeted_block()[2] != 'up':
            minescript.player_press_use(True)
            time.sleep(0.1)
            minescript.player_press_use(False)
    except TypeError: # Used to handle the exception where the player isn't targeting a block
        pass