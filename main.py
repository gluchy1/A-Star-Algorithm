import sys
import numpy as np
import heapq
import tkinter
import turtle

class astaralgorithm(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.build_window()
        self.running = False

    def build_window(self):

        self.master.title("A Star Pathfinding Algorithm visualisation using Tkinter")
        menu_bar = tkinter.Menu(self.master)
        file_menu = tkinter.Menu(menu_bar, tearoff=0)

        def run_animation():
            if self.running:
                return
            try:
                self.running = True
                screen = self.theTurtle.getscreen()
                screen.clear()
                screen.tracer(0)
                screen.setworldcoordinates(0, 800, 1300, 0)
                self.screen = screen
                maze = np.loadtxt(self.filename.get(), delimiter=',')
                start = (0, 0)
                goal = (maze.shape[0] - 1, maze.shape[1] - 1)
                path, visited_nodes = self.a_star(maze, start, goal)
                self.visualize(maze, visited_nodes, path)
                self.running = False
            except Exception as ex:
                tkinter.messagebox.showwarning("Alert", str(ex))
                tb = sys.exc_info()[2]
                self.running = False
                raise ex

        def stop_animation():
            self.running = False

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
        self.filename.set("array.txt")

        select_label = tkinter.Label(side_bar, text="Select File")
        select_label.pack()

        file_entry_box = tkinter.Entry(side_bar, textvariable=self.filename)
        file_entry_box.pack()

        start_button = tkinter.Button(side_bar, text="Start", command=run_animation)
        start_button.pack()

        stop_button = tkinter.Button(side_bar, text="Stop", command=stop_animation)
        stop_button.pack()

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

        heapq.heappush(oheap, (fscore[start], start))

        while oheap:
            current = heapq.heappop(oheap)[1]

            if current == goal:
                data = []
                while current in came_from:
                    data.append(current)
                    current = came_from[current]
                return data, visited_nodes

            close_set.add(current)
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j
                tentative_g_score = gscore[current] + self.heuristic(current, neighbor)
                if 0 <= neighbor[0] < array.shape[0]:
                    if 0 <= neighbor[1] < array.shape[1]:
                        if array[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        continue
                else:
                    continue

                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue

                if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(oheap, (fscore[neighbor], neighbor))
                    visited_nodes.append(neighbor)

        return False, visited_nodes

    def visualize(self, maze, visited_nodes, path):
        canvas_width = 800
        canvas_height = 800
        cell_size = min(canvas_width // maze.shape[1], canvas_height // maze.shape[0])

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
                self.theTurtle.fillcolor("white" if maze[row, col] == 0 else "black")
                self.theTurtle.begin_fill()
                for _ in range(4):
                    self.theTurtle.forward(cell_size)
                    self.theTurtle.right(90)
                self.theTurtle.end_fill()
                self.theTurtle.penup()

        for node in visited_nodes:
            row, col = node
            self.theTurtle.goto(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)
            self.theTurtle.dot(cell_size / 4, 'blue')

        if path:
            for node in path:
                row, col = node
                self.theTurtle.goto(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)
                self.theTurtle.dot(cell_size / 4, 'red')
        self.theTurtle.goto(0, 0)
        self.theTurtle.dot(cell_size / 2, 'green')
        self.theTurtle.goto((maze.shape[1] - 1) * cell_size, (maze.shape[0] - 1) * cell_size)
        self.theTurtle.dot(cell_size / 2, 'purple')
        turtle_screen.update()

def main():
    root = tkinter.Tk()
    animApp = astaralgorithm(root)
    animApp.mainloop()
if __name__ == "__main__":
    main()
    print("A-Star-Algorithm initiated")
