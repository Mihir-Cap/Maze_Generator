# Maze Generator

This is a Python program that generates a random maze using a recursive backtracking algorithm. The maze is displayed using the Pygame library and can be generated with custom width and height.

## Prerequisites
- Python 3.x
- Pygame library

## Getting Started
1. Install Pygame by running the following command:
   ```
   pip install pygame
   ```

2. Copy and paste the provided code into a Python file (e.g., `maze_generator.py`).

3. Run the program using the following command:
   ```
   python maze_generator.py
   ```

## Usage
1. Upon running the program, a graphical user interface (GUI) window will appear.

2. Enter the desired width and height for the maze in the input fields.

3. Click the "Generate Maze" button to start the maze generation process.

4. A Pygame window will open, displaying the generated maze.

5. The maze generation process may take some time depending on the size of the maze. The speed of generation can be adjusted by modifying the `clock.tick(10)` line in the code, where a lower value increases the speed.

6. Once the maze is generated, you can close the Pygame window to exit the program.

## How It Works
The program utilizes the recursive backtracking algorithm to generate the maze. The maze is represented as a grid of cells, where each cell has four walls (top, right, bottom, and left). Initially, all walls are present, and no cells are visited.

The algorithm starts at a random cell and marks it as visited. It then randomly chooses an unvisited neighboring cell and removes the wall between them. This process continues recursively until all cells are visited.

The graphical representation of the maze is created using Pygame. The maze is drawn as a series of lines based on the walls of each cell. The Pygame window is continuously updated to display the maze generation process.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
- The maze generation algorithm is based on the recursive backtracking algorithm.
- Pygame is used for the graphical representation of the maze.
