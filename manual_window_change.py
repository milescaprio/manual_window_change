import pygame
import win32gui
import win32com.client

gear_buttons = [3, 1, 2, 0, 6, 7, 5]
# Gear buttons ID's that the manual maps to the controller maps to
# 1st 2nd 3456R

saved_windows = [None, None, None, None, None, None, None]

clutch_axis = 2
clutch_threshold = 0.6


pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()

joystick = pygame.joystick.Joystick(0)  # Assuming the x360ce controller is the first
joystick.init()
print(f"Controller: {joystick.get_name()}")

def focus_window(hwnd):
    """
    Bring a window with the given handle to the foreground.
    """
    try:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')  # Simulate pressing the ALT key (workaround for permission issues)
        win32gui.SetForegroundWindow(hwnd)
    except Exception as e:
        pass

def get_focused_window_handle():
    hwnd = win32gui.GetForegroundWindow()  # Get handle of the current focused window
    return hwnd

def switch_to_window(gear):
    focus_window(saved_windows[gear])

def set_window_to(gear):
    saved_windows[gear] = get_focused_window_handle()
    
# Main loop to read inputs

#When event detected, categorize the event.
#-   If clutch changed, check its actuation point, if so, change clutch
#-   variable
#-   We care if it's a button pressed
#-   If it's pressed and clutch is on, switch to that window
#-   If it's pressed and clutch is off, set the bind


running = True
clutch = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.JOYAXISMOTION:
            if event.axis == clutch_axis:
                if event.value >= clutch_threshold:
                    clutch = True
                else:
                    clutch = False

        if event.type == pygame.JOYBUTTONDOWN:
            print(event.button)
            if event.button in gear_buttons:
                if clutch:
                    switch_to_window(gear_buttons.index(event.button))
                else:
                    set_window_to(gear_buttons.index(event.button))

pygame.quit()
