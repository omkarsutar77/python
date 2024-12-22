import turtle

def draw_star():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Star Drawing")

    # Set up the turtle
    star_turtle = turtle.Turtle()
    star_turtle.color("yellow")
    star_turtle.speed(5)
    star_turtle.pensize(2)

    # Draw the star
    for _ in range(5):
        star_turtle.forward(100)  # Length of star arm
        star_turtle.right(144)   # Angle to create a star

    # Keep the window open
    screen.mainloop()

# Call the function
draw_star()
