from easytello import tello
import keyboard
import time

drone = tello.Tello()
isFlying = False

def flyingToggle():
    global isFlying
    if isFlying:
        print("land")
        drone.land()
        isFlying = False
    else:
        print("take off")
        drone.takeoff()
        isFlying = True

keyboard.on_press_key("enter", lambda _:flyingToggle())


while True:
    if keyboard.is_pressed('w'):
        drone.forward(0.1)
    elif keyboard.is_pressed("space"):
        drone.up(0.1)
    elif keyboard.is_pressed("shift"):
        drone.down(0.1)
    elif keyboard.is_pressed("a"):
        drone.left(0.1)
    elif keyboard.is_pressed("s"):
        drone.back(0.1)
    elif keyboard.is_pressed("d"):
        drone.right(0.1)
