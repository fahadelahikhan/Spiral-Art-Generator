# Spiral Art Generator

A Python application that creates beautiful mathematical spiral patterns with customizable parameters using the Turtle graphics library.

## Description

The Spiral Art Generator is an interactive tool that allows users to create various types of spiral patterns. It leverages mathematical principles to generate visually appealing designs, from simple spirals to complex Fibonacci and parametric patterns. The application provides both pre-defined patterns and random art generation capabilities.

## Features

- **Multiple Spiral Types**:
  - Basic Spiral: Simple expanding spiral with customizable growth factor and angle
  - Geometric Spiral: Based on regular polygon shapes
  - Fibonacci Spiral: Based on the Fibonacci sequence
  - Multi-Spiral: Multiple spirals emanating from different starting points
  - Parametric Spiral: Including Archimedes, logarithmic, and hyperbolic variants
  - Rose Spiral: Creates flower-like patterns with adjustable petal count

- **Customization Options**:
  - Adjust number of iterations
  - Modify growth factors
  - Change angles and starting positions
  - Control number of petals/sides

- **Color Effects**:
  - Rainbow color progression
  - Customizable color palettes

- **Interactive Menu**:
  - User-friendly command-line interface
  - Options to select and customize patterns

## Requirements

- Python 3.x
- Turtle graphics library (included in standard Python installation)
- Math library (included in standard Python installation)
- Random library (included in standard Python installation)
- Typing module (included in standard Python installation)

## Installation

No special installation is required beyond having Python installed on your system.

1. Ensure you have Python 3.x installed
2. Download the `Spiral Art Generator.py` file
3. Run the script using Python

```bash
python "Spiral Art Generator.py"
```

## Usage

1. Run the script to launch the application
2. A random spiral pattern will be generated initially
3. Use the interactive menu to select a specific pattern type:
   ```
   🎨 Enhanced Spiral Art Generator 🎨
   =====================================
   1. Basic Spiral
   2. Geometric Spiral
   3. Fibonacci Spiral
   4. Multi-Spiral
   5. Parametric Spiral
   6. Rose Spiral
   7. Random Art
   8. Exit
   ```
4. Follow the prompts to customize your selected pattern
5. Click anywhere on the drawing window to exit when finished

## Pattern Types Explained

### Basic Spiral
A simple spiral that expands outward with each iteration. The growth factor determines how quickly the spiral expands, while the angle determines how tightly it coils.

### Geometric Spiral
Creates a spiral based on regular polygon shapes. The number of sides determines the base polygon (e.g., 3 for triangle, 4 for square).

### Fibonacci Spiral
Based on the famous Fibonacci sequence (1, 1, 2, 3, 5, 8, 13, ...), where each number is the sum of the two preceding ones. This creates a spiral that closely approximates the golden spiral found in nature.

### Multi-Spiral
Generates multiple spirals emanating from different starting points arranged in a circle, creating complex and symmetric patterns.

### Parametric Spiral
Offers three mathematical variants:
- **Archimedes Spiral**: The distance from the center increases linearly with the angle
- **Logarithmic Spiral**: The distance increases exponentially, creating a self-similar curve
- **Hyperbolic Spiral**: The distance is inversely proportional to the angle

### Rose Spiral
Creates flower-like patterns where the number of petals can be adjusted. Based on the mathematical rose curve.

## Examples

When running the application, you can:

- Generate a basic spiral: Select option 1
- Create a geometric spiral with 8 sides: Select option 2, then enter 8 when prompted
- Generate a rose pattern with 5 petals: Select option 6, then enter 5 when prompted
- Let the program surprise you: Select option 7 for random art

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fahad Elahi Khan

---

Enjoy creating beautiful spiral art with this generator! Feel free to modify the code to create your own unique patterns.