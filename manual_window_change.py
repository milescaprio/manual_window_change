import pygame
import win32gui
import win32com.client

gear_buttons = [11, 12, 13, 14, 15, 16, 17]
# Gear buttons ID's that the manual maps to the controller maps to
# 1st 2nd 3456R

saved_windows = [[None],[None],[None],[None],[None],[None],[None]]

clutch_axis = 3
clutch_threshold = 0 #Default clutch range is -1 to 1
invert_clutch = True

pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()

joystick = pygame.joystick.Joystick(0)  # Assuming the x360ce controller is the first
joystick.init()
print(f"Controller: {joystick.get_name()}")

def remove_all(lst, value):
    while True:
        try: 
            lst.remove(value)
        except ValueError:
            return

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
    focus_window(saved_windows[gear][-1])
    print("Switched to gear", gear, "with window", saved_windows[gear][-1])

def set_window_to(gear):
    handle = get_focused_window_handle()
    saved_windows[gear].append(handle)
    print("Set window handle", handle, "to gear", gear)
    for i, _ in enumerate(saved_windows): #Remove handle from other gears
        if i != gear:
            remove_all(saved_windows[i], handle)
    #print("Saved windows", saved_windows)
    
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
                if (event.value >= clutch_threshold) != invert_clutch:
                    if clutch == False:
                        print("Clutch pressed")
                    clutch = True
                else:
                    if clutch == True:
                        print("Clutch released")
                    clutch = False
            else:
                print("Axis moving is not clutch, it is", event.axis)
                print("Change clutch_axis if this is the clutch")

        if event.type == pygame.JOYBUTTONDOWN:
            print(event.button, "pressed")
            if event.button in gear_buttons:
                if clutch:
                    switch_to_window(gear_buttons.index(event.button))
                else:
                    set_window_to(gear_buttons.index(event.button))

pygame.quit()
