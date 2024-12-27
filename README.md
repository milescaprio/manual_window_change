A little script to change windows using a game controller manual gearbox. Windows-only, ~20 minute setup. 
Install x360ce to emulate a game controller with your steering wheel & transmission (I'm using a Logitech G920)
Add any button bind to each of the gears using *record* and any axis bind to the clutch.
Make sure the controller is running and "add game" the executable which is running this script. You can use task manager and "open file path" to view it... typically it will be a variant of python.exe
Change the gear buttons list in `manual_window_change.py` to the buttons actuated by each gear when you run `measurement_test.py`, and the clutch_axis to the axis moved when you press the clutch.
Run the script and you can change windows with your shifter. Simply move the shifter dry when you want to bind the window to that gear, and hold in the clutch and move the shifter to change windows. =)
