import os
import numpy as np
import heapq
import tkinter
import turtle
import array_randomizer

def newarray():
    if not newarray.has_run:
        newarray.has_run = True
        array_randomizer.array_randomizer()
    else:
        raise RuntimeError


class astaralgorithm(tkinter.Frame):

    def __init__(self, master=None, start_point=(0, 0)):
        super().__init__(master)
        self.pack()
        self.build_window()
        self.running = False
        self.start_point = start_point

    def build_window(self):
        self.master.title("A Star Pathfinding Algorithm visualisation using Tkinter")
        menu_bar = tkinter.Menu(self.master)
        file_menu = tkinter.Menu(menu_bar, tearoff=0)

        file_menu.add_command(label="Exit", command=self.master.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        self.master.config(menu=menu_bar)

        canvas = tkinter.Canvas(self, width=1300, height=800)
        canvas.pack(side=tkinter.LEFT)

        self.theTurtle = turtle.RawTurtle(canvas)
        self.theTurtle.ht()

        side_bar = tkinter.Frame(self, padx=5, pady=5, relief=tkinter.RAISED, borderwidth="5pt")
        side_bar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        self.filename = tkinter.StringVar()
        # with_item::("array.txt")[self.filename.set]
        self.filename.set("array.txt")

        select_label = tkinter.Label(side_bar, text="Select File")
        select_label.pack()

        file_entry_box = tkinter.Entry(side_bar, textvariable=self.filename)
        file_entry_box.pack()

        start_button = tkinter.Button(side_bar, text="Start", command=self.run_animation)
        start_button.pack()

    def run_animation(self):
        if self.running:
            return
        try:
            self.running = True
            self.screen = self.setup_screen()
            maze = self.load_maze()
            if maze is None:
                raise Exception("Could not load maze.")
            start, goal = self.calculate_start_goal(maze)
            path, visited_nodes = self.a_star(maze, start, goal)
            self.visualize(maze, visited_nodes, path)
            self.running = False
        except Exception as e:
            print(f"Error occurred: {e}")
            self.running = False

    def setup_screen(self):
        screen = self.theTurtle.getscreen()
        screen.clear()
        screen.tracer(0)
        screen.setworldcoordinates(0, 800, 800, 0)
        return screen

    def load_maze(self):
        filename = self.filename.get()
        if not os.path.isfile(filename):
            print(f"File {filename} does not exist.")
            return None
        if not os.access(filename, os.R_OK):
            print(f"File {filename} is not readable.")
            return None
        try:
            maze = np.loadtxt(filename, delimiter=',')
        except IOError as e:
            print("Unable to open file", e)
            return None
        return maze

    def calculate_start_goal(self, maze):
        start = self.start_point
        goal = (maze.shape[0] - 1, maze.shape[1] - 1)
        return start, goal

    def heuristic(self, a, b):
        return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

    def a_star(self, array, start, goal):
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        close_set = set()
        came_from = {}
        gscore = {start: 0}
        fscore = {start: self.heuristic(start, goal)}
        oheap = []
        visited_nodes = []
        oheap_set = set()

        heapq.heappush(oheap, (fscore[start], start))
        oheap_set.add(start)

        while oheap:
            current = heapq.heappop(oheap)[1]
            oheap_set.remove(current)

            if current == goal:
                data = []
                while current in came_from:
                    data.append(current)
                    current = came_from[current]
                return data[::-1], visited_nodes

            close_set.add(current)
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j
                if 0 <= neighbor[0] < array.shape[0] and 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1:  # Treat 1 as an obstacle
                        continue
                    tentative_g_score = gscore[current] + self.heuristic(current, neighbor)
                else:
                    continue

                if neighbor not in gscore or tentative_g_score < gscore[neighbor]:
                    if array[neighbor[0]][neighbor[1]] == 0:  # Only add the neighbor to the path if it is not an obstacle
                        came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    if neighbor not in oheap_set:
                        heapq.heappush(oheap, (fscore[neighbor], neighbor))
                        oheap_set.add(neighbor)
                        visited_nodes.append(neighbor)

        return False, visited_nodes

    def visualize(self, maze, visited_nodes, path):
        canvas_width = 800
        canvas_height = 800
        cell_size = min(canvas_width // maze.shape[0], canvas_height // maze.shape[1])  # Change here

        turtle_screen = self.theTurtle.getscreen()
        turtle_screen.setworldcoordinates(0, 0, maze.shape[1] * cell_size, maze.shape[0] * cell_size)
        turtle_screen.clear()

        self.theTurtle.penup()
        self.theTurtle.speed(0)

        for row in range(maze.shape[0]):
            for col in range(maze.shape[1]):
                self.theTurtle.goto(col * cell_size, row * cell_size)
                self.theTurtle.pendown()
                self.theTurtle.setheading(0)
                self.theTurtle.fillcolor(
                    "black" if maze[row, col] == 1 else "lightgray")
                self.theTurtle.begin_fill()
                for i in range(4):
                    self.theTurtle.forward(cell_size)
                    self.theTurtle.right(90)
                self.theTurtle.end_fill()
                self.theTurtle.penup()

        for node in visited_nodes:
            row, col = node
            self.theTurtle.goto(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)
            if maze[row, col] == 0:  # If the node is not an obstacle
                self.theTurtle.dot(cell_size / 4, 'blue')
            elif maze[row, col] == 1:  # If the node is an obstacle
                self.theTurtle.dot(cell_size / 4, 'red')  # Change the color as per your requirement

        if path:
            path = path[::-1]
            for node in path:
                row, col = node
                if maze[row, col] == 0:  # check if node = black (1) as obstacle and should not be marked red
                    self.theTurtle.goto(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)
                    self.theTurtle.dot(cell_size / 4, 'red')


        self.theTurtle.goto(cell_size // 2, cell_size // 2)
        self.theTurtle.dot(cell_size / 2, 'green')
        self.theTurtle.write("Start", align="center", font=("Arial", 12, "normal"))

        self.theTurtle.goto((maze.shape[1] - 0.5) * cell_size, (maze.shape[0] - 0.5) * cell_size)
        self.theTurtle.dot(cell_size / 2, 'purple')
        self.theTurtle.write("End", align="center", font=("Arial", 12, "normal"))

        turtle_screen.update()

newarray.has_run = False

def main():
    root = tkinter.Tk()
    animApp = astaralgorithm(root)
    animApp.mainloop()


if __name__ == "__main__":
    main()
    print("A-Star-Algorithm initiated")
