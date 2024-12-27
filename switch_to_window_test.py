import win32gui
import win32com.client

def focus_window(hwnd):
    """
    Bring a window with the given handle to the foreground.
    """
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')  # Simulate pressing the ALT key (workaround for permission issues)
    win32gui.SetForegroundWindow(hwnd)

# Example usage
# Replace with the handle of the window you want to focus
target_window_handle = 922186  # Example window handle
while True:
    try:
        focus_window(target_window_handle)
        print(f"Successfully focused on window with handle: {target_window_handle}")
    except Exception as e:
        print(f"Failed to focus window: {e}")