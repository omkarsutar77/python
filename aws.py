import turtle

def draw_aws_logo():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("AWS Logo")

    # Set up the turtle
    logo_turtle = turtle.Turtle()
    logo_turtle.speed(1)  # Slow speed
    logo_turtle.width(3)

    # Draw the arc (yellow smile)
    logo_turtle.penup()
    logo_turtle.goto(-100, -50)
    logo_turtle.pendown()
    logo_turtle.color("yellow")
    logo_turtle.setheading(-60)
    logo_turtle.circle(120, 120)  # Draw an arc with radius 120 and 120 degrees

    # Draw the "AWS" text in white
    logo_turtle.penup()
    logo_turtle.goto(-70, 50)
    logo_turtle.color("white")
    logo_turtle.write("AWS", font=("Arial", 36, "bold"))

    # Keep the window open
    screen.mainloop()

# Call the function
draw_aws_logo()
