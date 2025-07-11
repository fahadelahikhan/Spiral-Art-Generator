import turtle


def setup_canvas():
    """Set up the drawing canvas with basic configuration"""
    canvas = turtle.Screen()
    canvas.bgcolor("black")  # Dark background makes colors pop
    canvas.title("Spiral Art Generator")
    canvas.setup(width=800, height=600)
    return canvas


def create_pen():
    """Create and configure the drawing pen"""
    pen = turtle.Turtle()
    pen.shape("circle")
    pen.speed(0)  # Fastest speed
    pen.width(2)  # Slightly thicker lines
    return pen


def draw_colorful_spiral(pen, num_lines, line_length, turn_degrees):
    """
    Draw a colorful spiral pattern

    Parameters:
    pen: The turtle object for drawing
    num_lines: How many lines to draw
    line_length: Length of each line
    turn_degrees: Angle to turn after each line
    """
    # List of vibrant colors for the spiral
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

    for i in range(num_lines):
        # Change color for each line
        pen.color(colors[i % len(colors)])

        # Draw the line
        pen.forward(line_length)
        pen.right(turn_degrees)

        # Gradually increase line length for spiral effect
        line_length += 2


def draw_simple_spiral(pen, num_lines, line_length, turn_degrees):
    """
    Draw a simple single-color spiral

    Parameters:
    pen: The turtle object for drawing
    num_lines: How many lines to draw
    line_length: Length of each line
    turn_degrees: Angle to turn after each line
    """
    pen.color("white")

    for i in range(num_lines):
        pen.forward(line_length)
        pen.right(turn_degrees)


def main():
    """Main function to run the spiral art generator"""
    print("Welcome to the Spiral Art Generator!")
    print("Watch as beautiful spiral patterns are created...")

    # Set up the drawing environment
    canvas = setup_canvas()
    pen = create_pen()

    # Hide the turtle cursor for cleaner look
    pen.hideturtle()

    # Move to center of screen
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()

    # Drawing parameters - feel free to experiment with these!
    number_of_lines = 100
    starting_length = 5
    turning_angle = 91  # Try different angles like 89, 90, 91, 120, 144

    # Draw the spiral
    draw_colorful_spiral(pen, number_of_lines, starting_length, turning_angle)

    # Show completion message
    pen.penup()
    pen.goto(-200, -250)
    pen.color("white")
    pen.write("Click anywhere to close!", font=("Arial", 16, "normal"))

    # Keep the window open until clicked
    canvas.exitonclick()


# Run the program
if __name__ == "__main__":
    main()