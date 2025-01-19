import pygame
from pynput.keyboard import Key, Controller

keyboard = Controller()

gear_buttons = [11, 12, 13, 14, 15, 16, 17]
# Gear buttons ID's that the manual maps to the controller maps to
# 1st 2nd 3456R


from enum import Enum

class Axis:
    gas_axis = 1
    brake_axis = 2
    clutch_axis = 3


gas_threshold = 0
brake_threshold = 0.9
clutch_threshold = 0 #Default clutch range is -1 to 1

invert_gas = False
invert_brake = False
invert_clutch = False

gear_keys = ["7", "1", "2", "3", "4", "5", "6"]

clutchkey = Key.ctrl
brakekey = Key.shift
gaskey = "w"

pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()

joystick = pygame.joystick.Joystick(0) 
joystick.init()
print(f"Controller: {joystick.get_name()}")

running = True
gas = False
brake = False
clutch = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.JOYAXISMOTION:
            match event.axis:
                case Axis.clutch_axis:
                    if (event.value <= clutch_threshold) != invert_clutch:
                        if clutch == False:
                            print("Clutch pressed")
                            keyboard.press(clutchkey)
                        clutch = True
                    else:
                        if clutch == True:
                            print("Clutch released")
                            keyboard.release(clutchkey)
                        clutch = False
                case Axis.gas_axis:
                    if (event.value <= gas_threshold) != invert_gas:
                        if gas == False:
                            print("Gas pressed")
                            keyboard.press(gaskey)                        
                        gas = True
                    else:
                        if gas == True:
                            print("Gas released")
                            keyboard.release(gaskey)
                        gas = False
                case Axis.brake_axis:
                    if (event.value <= brake_threshold) != invert_brake:
                        if brake == False:
                            print("Brake pressed")
                            keyboard.press(brakekey)
                        brake = True
                    else:
                        if brake == True:
                            print("Brake released")
                            keyboard.release(brakekey)	
                        brake = False
                case _:
                    pass


        if event.type == pygame.JOYBUTTONDOWN:
            print(event.button, "pressed")
            if event.button in gear_buttons:
                keyboard.press(gear_keys[gear_buttons.index(event.button)])
        elif event.type == pygame.JOYBUTTONUP:
            print(event.button, "released")
            if event.button in gear_buttons:
                keyboard.release(gear_keys[gear_buttons.index(event.button)])

pygame.quit()
