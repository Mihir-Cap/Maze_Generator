import tkinter as tk
import tkinter.messagebox as messagebox
import pygame
from pygame.locals import *
import threading
import random

# Maze size
MAZE_SIZE = 20
PADDING = 30  # Adjust the padding value to increase/decrease the space around the maze

# Maze cell class
class MazeCell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}

# Maze class
class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[MazeCell(x, y) for y in range(height)] for x in range(width)]
        self.current_cell = self.maze[0][0]

    def generate_maze(self, x=0, y=0):
        directions = ["top", "right", "bottom", "left"]
        random.shuffle(directions)

        for direction in directions:
            new_x = x
            new_y = y
            if direction == "top" and y > 0:
                new_y = y - 1
            elif direction == "right" and x < self.width - 1:
                new_x = x + 1
            elif direction == "bottom" and y < self.height - 1:
                new_y = y + 1
            elif direction == "left" and x > 0:
                new_x = x - 1

            if self.maze[new_x][new_y].visited:
                continue

            self.maze[x][y].walls[direction] = False
            if direction == "top":
                self.maze[new_x][new_y].walls["bottom"] = False
            elif direction == "right":
                self.maze[new_x][new_y].walls["left"] = False
            elif direction == "bottom":
                self.maze[new_x][new_y].walls["top"] = False
            elif direction == "left":
                self.maze[new_x][new_y].walls["right"] = False

            self.maze[new_x][new_y].visited = True
            self.generate_maze(new_x, new_y)

# Maze generation function
def generate_maze_thread():
    width = int(width_entry.get())
    height = int(height_entry.get())

    if width <= 0 or height <= 0:
        messagebox.showerror("Invalid Input", "Width and height must be positive integers.")
        return

    maze = Maze(width, height)
    maze.generate_maze()

    pygame.init()
    window_width = width * MAZE_SIZE + 2 * PADDING
    window_height = height * MAZE_SIZE + 2 * PADDING
    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True

        screen.fill((255, 255, 255))  # White background

        # Calculate the offset to center the maze
        offset_x = (window_width - width * MAZE_SIZE) // 2
        offset_y = (window_height - height * MAZE_SIZE) // 2

        for x in range(width):
            for y in range(height):
                cell = maze.maze[x][y]
                if cell.walls["top"]:
                    pygame.draw.line(screen, (0, 0, 0),
                                     (offset_x + x * MAZE_SIZE, offset_y + y * MAZE_SIZE),
                                     (offset_x + (x + 1) * MAZE_SIZE, offset_y + y * MAZE_SIZE))
                if cell.walls["right"]:
                    pygame.draw.line(screen, (0, 0, 0),
                                     (offset_x + (x + 1) * MAZE_SIZE, offset_y + y * MAZE_SIZE),
                                     (offset_x + (x + 1) * MAZE_SIZE, offset_y + (y + 1) * MAZE_SIZE))
                if cell.walls["bottom"]:
                    pygame.draw.line(screen, (0, 0, 0),
                                     (offset_x + x * MAZE_SIZE, offset_y + (y + 1) * MAZE_SIZE),
                                     (offset_x + (x + 1) * MAZE_SIZE, offset_y + (y + 1) * MAZE_SIZE))
                if cell.walls["left"]:
                    pygame.draw.line(screen, (0, 0, 0),
                                     (offset_x + x * MAZE_SIZE, offset_y + y * MAZE_SIZE),
                                     (offset_x + x * MAZE_SIZE, offset_y + (y + 1) * MAZE_SIZE))

        pygame.display.flip()
        clock.tick(10)  # Adjust the speed of maze generation by changing the tick rate

    pygame.quit()

# Create the Tkinter window
window = tk.Tk()
window.title("Maze Generator")

# Create the input fields and labels
width_label = tk.Label(window, text="Width:")
width_label.pack()
width_entry = tk.Entry(window)
width_entry.pack()

height_label = tk.Label(window, text="Height:")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

# Generate maze button
generate_button = tk.Button(window, text="Generate Maze", command=lambda: threading.Thread(target=generate_maze_thread).start())
generate_button.pack()

window.mainloop()
