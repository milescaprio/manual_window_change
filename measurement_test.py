import pygame

# Initialize pygame and joystick module
pygame.init()
pygame.joystick.init()

# Check for controllers
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No controllers detected!")
else:
    joystick = pygame.joystick.Joystick(0)  # Assuming the x360ce controller is the first
    joystick.init()
    print(f"Controller: {joystick.get_name()}")

    # Main loop to read inputs
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.JOYAXISMOTION:
                print(f"Axis {event.axis} moved to {event.value:.2f}")
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")
            elif event.type == pygame.JOYBUTTONUP:
                print(f"Button {event.button} released")

pygame.quit()