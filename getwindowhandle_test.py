import win32gui

# Function to get the handle of the current focused window
def get_focused_window_handle():
    hwnd = win32gui.GetForegroundWindow()  # Get handle of the current focused window
    return hwnd

while True:
    # Example usage
    current_window_handle = get_focused_window_handle()
    print(f"The handle of the currently focused window is: {current_window_handle}")