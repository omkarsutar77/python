import turtle

def draw_colored_rings():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Colorful Rings")

    # Set up the turtle
    ring_turtle = turtle.Turtle()
    ring_turtle.speed(0)  # Maximum speed
    ring_turtle.width(2)

    # List of colors for the rings
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

    # Draw rings
    radius = 150  # Initial radius
    for color in colors:
        ring_turtle.penup()  # Lift the pen to move without drawing
        ring_turtle.goto(0, -radius)  # Move to the starting position of the ring
        ring_turtle.pendown()  # Put the pen down to start drawing
        ring_turtle.color(color)  # Set the color for the ring
        ring_turtle.circle(radius)  # Draw a circle
        radius -= 20  # Decrease the radius for the next ring

    # Keep the window open
    screen.mainloop()

# Call the function
draw_colored_rings()
