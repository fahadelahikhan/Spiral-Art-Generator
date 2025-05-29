#!/usr/bin/env python3
"""
Enhanced Spiral Art Generator
Creates beautiful mathematical spiral patterns with customizable parameters
"""

import turtle
import random
import math
from typing import Tuple


class SpiralArtGenerator:
    """A comprehensive spiral art generator with multiple pattern types and effects"""

    def __init__(self, width: int = 1.0, height: int = 1.0):
        """Initialize the art generator with screen dimensions"""
        self.setup_screen(width, height)
        self.setup_artist()
        self.colors = [
            "#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FECA57",
            "#FF9FF3", "#54A0FF", "#5F27CD", "#00D2D3", "#FF9F43",
            "#10AC84", "#EE5A24", "#0652DD", "#9C88FF", "#FFC312"
        ]

    def setup_screen(self, width: int, height: int) -> None:
        """Configure the drawing screen"""
        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.screen.bgcolor("black")
        self.screen.title("Enhanced Spiral Art Generator")
        self.screen.colormode(255)

    def setup_artist(self) -> None:
        """Configure the turtle artist"""
        self.artist = turtle.Turtle()
        self.artist.shape("circle")
        self.artist.speed(0)  # Fastest speed
        self.artist.width(2)
        self.artist.hideturtle()

    def get_rainbow_color(self, step: int, total_steps: int) -> Tuple[int, int, int]:
        """Generate rainbow colors based on step progression"""
        hue = (step / total_steps) * 360
        # Convert HSV to RGB (simplified)
        c = 1
        x = c * (1 - abs((hue / 60) % 2 - 1))
        m = 0

        if 0 <= hue < 60:
            r, g, b = c, x, 0
        elif 60 <= hue < 120:
            r, g, b = x, c, 0
        elif 120 <= hue < 180:
            r, g, b = 0, c, x
        elif 180 <= hue < 240:
            r, g, b = 0, x, c
        elif 240 <= hue < 300:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x

        return int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)

    def draw_basic_spiral(self, iterations: int = 100, initial_length: int = 3,
                          growth_factor: float = 1.05, angle: float = 91) -> None:
        """Draw a basic expanding spiral"""
        self.artist.clear()
        self.artist.penup()
        self.artist.goto(0, 0)
        self.artist.pendown()

        length = initial_length

        for i in range(iterations):
            # Rainbow color progression
            color = self.get_rainbow_color(i, iterations)
            self.artist.pencolor(color)

            self.artist.forward(length)
            self.artist.right(angle)
            length *= growth_factor

    def draw_geometric_spiral(self, sides: int = 6, iterations: int = 360,
                              initial_length: int = 1) -> None:
        """Draw a geometric spiral with regular polygon base"""
        self.artist.clear()
        self.artist.penup()
        self.artist.goto(0, 0)
        self.artist.pendown()

        angle = 360 / sides
        length = initial_length

        for i in range(iterations):
            color = self.get_rainbow_color(i, iterations)
            self.artist.pencolor(color)

            self.artist.forward(length)
            self.artist.right(angle + 1)  # +1 creates the spiral effect
            length += 0.5

    def draw_fibonacci_spiral(self, iterations: int = 15) -> None:
        """Draw a spiral based on Fibonacci sequence"""
        self.artist.clear()
        self.artist.penup()
        self.artist.goto(0, 0)
        self.artist.pendown()

        # Generate Fibonacci sequence
        fib = [1, 1]
        for i in range(2, iterations):
            fib.append(fib[i - 1] + fib[i - 2])

        # Draw the spiral
        for i, size in enumerate(fib):
            color = self.get_rainbow_color(i, len(fib))
            self.artist.pencolor(color)

            # Draw quarter circle
            circumference = 2 * math.pi * size
            arc_length = circumference / 4
            steps = int(arc_length / 2)
            step_angle = 90 / steps if steps > 0 else 90
            step_size = arc_length / steps if steps > 0 else arc_length

            for _ in range(steps):
                self.artist.forward(step_size)
                self.artist.right(step_angle)

    def draw_multi_spiral(self, num_spirals: int = 6, iterations: int = 100) -> None:
        """Draw multiple spirals from different starting points"""
        self.artist.clear()

        for spiral_num in range(num_spirals):
            # Position spirals in a circle
            start_angle = (360 / num_spirals) * spiral_num
            start_x = 100 * math.cos(math.radians(start_angle))
            start_y = 100 * math.sin(math.radians(start_angle))

            self.artist.penup()
            self.artist.goto(start_x, start_y)
            self.artist.pendown()
            self.artist.setheading(start_angle)

            length = 7
            for i in range(iterations):
                color_index = (i + spiral_num * 30) % len(self.colors)
                self.artist.pencolor(self.colors[color_index])

                self.artist.forward(length)
                self.artist.right(91 + spiral_num)
                length += 0.5

    def draw_parametric_spiral(self, spiral_type: str = "archimedes",
                               iterations: int = 500) -> None:
        """Draw parametric spirals (Archimedes, logarithmic, etc.)"""
        self.artist.clear()
        self.artist.penup()
        self.artist.goto(0, 0)
        self.artist.pendown()

        for i in range(iterations):
            t = i * 0.1
            color = self.get_rainbow_color(i, iterations)
            self.artist.pencolor(color)

            if spiral_type == "archimedes":
                # r = a * θ
                r = t * 2
                x = r * math.cos(t)
                y = r * math.sin(t)
            elif spiral_type == "logarithmic":
                # r = a * e^(b*θ)
                r = math.exp(t * 0.1) * 2
                x = r * math.cos(t)
                y = r * math.sin(t)
            elif spiral_type == "hyperbolic":
                # r = a / θ
                if t != 0:
                    r = 50 / t
                    x = r * math.cos(t)
                    y = r * math.sin(t)
                else:
                    continue

            self.artist.goto(x, y)

    def draw_rose_spiral(self, petals: int = 7, iterations: int = 720) -> None:
        """Draw a rose-like spiral pattern"""
        self.artist.clear()
        self.artist.penup()
        self.artist.goto(0, 0)
        self.artist.pendown()

        for i in range(iterations):
            t = math.radians(i)
            color = self.get_rainbow_color(i, iterations)
            self.artist.pencolor(color)

            # Rose equation: r = sin(k*θ) where k determines number of petals
            r = 100 * abs(math.sin(petals * t))
            x = r * math.cos(t)
            y = r * math.sin(t)

            self.artist.goto(x, y)

    def create_random_art(self) -> None:
        """Generate random spiral art with varying parameters"""
        pattern_type = random.randint(1, 6)

        if pattern_type == 1:
            self.draw_basic_spiral(
                iterations=random.randint(50, 150),
                initial_length=random.randint(1, 5),
                growth_factor=random.uniform(1.02, 1.08),
                angle=random.randint(85, 95)
            )
        elif pattern_type == 2:
            self.draw_geometric_spiral(
                sides=random.randint(3, 12),
                iterations=random.randint(200, 400)
            )
        elif pattern_type == 3:
            self.draw_multi_spiral(
                num_spirals=random.randint(3, 8),
                iterations=random.randint(50, 100)
            )
        elif pattern_type == 4:
            spiral_types = ["archimedes", "logarithmic", "hyperbolic"]
            self.draw_parametric_spiral(
                spiral_type=random.choice(spiral_types),
                iterations=random.randint(300, 600)
            )
        elif pattern_type == 5:
            self.draw_rose_spiral(
                petals=random.randint(3, 12),
                iterations=random.randint(360, 1080)
            )
        else:
            self.draw_fibonacci_spiral(iterations=random.randint(10, 18))

    def interactive_menu(self) -> None:
        """Display interactive menu for pattern selection"""
        print("\n🎨 Enhanced Spiral Art Generator 🎨")
        print("=====================================")
        print("1. Basic Spiral")
        print("2. Geometric Spiral")
        print("3. Fibonacci Spiral")
        print("4. Multi-Spiral")
        print("5. Parametric Spiral")
        print("6. Rose Spiral")
        print("7. Random Art")
        print("8. Exit")

        while True:
            try:
                choice = input("\nSelect pattern (1-8): ").strip()

                if choice == '1':
                    self.draw_basic_spiral()
                elif choice == '2':
                    self.draw_geometric_spiral()
                elif choice == '3':
                    self.draw_fibonacci_spiral()
                elif choice == '4':
                    self.draw_multi_spiral()
                elif choice == '5':
                    spiral_type = input("Enter spiral type (archimedes/logarithmic/hyperbolic): ").strip().lower()
                    if spiral_type in ["archimedes", "logarithmic", "hyperbolic"]:
                        self.draw_parametric_spiral(spiral_type)
                    else:
                        print("Invalid spiral type. Using Archimedes spiral.")
                        self.draw_parametric_spiral()
                elif choice == '6':
                    try:
                        petals = int(input("Number of petals (3-12): "))
                        petals = max(3, min(12, petals))
                        self.draw_rose_spiral(petals=petals)
                    except ValueError:
                        self.draw_rose_spiral()
                elif choice == '7':
                    self.create_random_art()
                elif choice == '8':
                    print("Thanks for using Spiral Art Generator! 🎨")
                    break
                else:
                    print("Invalid choice. Please select 1-8.")

            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

    def run(self) -> None:
        """Run the spiral art generator"""
        self.interactive_menu()
        self.screen.exitonclick()


def main():
    """Main function to run the application"""
    generator = SpiralArtGenerator()

    # Start with a random art piece
    generator.create_random_art()

    # Then show the interactive menu
    generator.run()


if __name__ == "__main__":
    main()
