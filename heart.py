import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Turtle Graphics - Heart")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.color("red")
t.hideturtle()

# Function to draw the heart
def draw_heart():
    points = []
    for i in range(0, 360, 2):
        angle = math.radians(i)
        x = 16 * (math.sin(angle) ** 3)
        y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)
        points.append((x * 12, y * 12))

    # Draw the string art effect
    num_points = len(points)
    for i in range(num_points):
        for j in range(i + 1, num_points):
            t.penup()
            t.goto(points[i])
            t.pendown()
            t.goto(points[j])

# Call the function
draw_heart()

# Keep the window open
turtle.done()
