import tkinter
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import random
from array import *
def main_algo():
    def find_paths(matrix: list, i: int, j: int, dest: tuple, N: int, nth_move: int, visited: list): 
        if (i, j) == dest:
            raw_paths.append([array("i",[_ for _ in _]) for _ in visited])
            return 
        nth_move+=1
        visited[i][j] = nth_move
        if i + 1 < N and not visited[i + 1][j] and matrix[i+1][j] != 0:
            find_paths(matrix, i + 1, j, dest, N, nth_move, visited)
        if i - 1 >= 0 and not visited[i - 1][j] and matrix[i-1][j] != 0:
            find_paths(matrix, i - 1, j, dest, N, nth_move, visited)
        if j + 1 < N and not visited[i][j + 1] and matrix[i][j+1] != 0:
            find_paths(matrix, i, j + 1, dest, N, nth_move, visited)
        if j - 1 >= 0 and not visited[i][j - 1] and matrix[i][j-1] != 0:
            find_paths(matrix, i, j - 1, dest, N, nth_move, visited)
        visited[i][j] = 0
        nth_move -=1
        return 

    def get_final_paths(paths: list):
        def numberize_moves(paths: list):
            final_paths = []
            for path in paths:
                previous_move = path[0]
                temp_path = []
                for move in path:
                    if move == previous_move and temp_path:
                        temp_path[-1] = f"{move}({int(temp_path[-1][-2])+1})"
                    else:
                        temp_path.append(f"{move}(1)")
                    previous_move = move
                final_paths.append(temp_path)
            return final_paths
        
        shortest_paths = numberize_moves([path for path in paths if len(path) == min([len(path) for path in paths])])
        shortest_paths = [path for path in shortest_paths if len(path) == min([len(moves) for moves in shortest_paths])]
        shortest_paths = [[f"\n{' '*11}{move}" if not move_count%4 and move_count else move for move_count, move in enumerate(path)] for path in shortest_paths]
        final_shortest_paths = [f"      {str(i+1)}]  {' > '.join(shortest_paths[i])}" for i in range (len(shortest_paths))]
        all_paths = [path for path in numberize_moves(paths)]
        all_paths = [[f"\n{' '*12}{move}" if not move_count%4 and move_count else move for move_count, move in enumerate(path)] for path in all_paths]
        final_all_paths = [f"       {str(i+1)}]  {' > '.join(all_paths[i])}" for i in range (len(all_paths))]
        return "\n\n".join(final_all_paths) ,  "\n"+"\n\n".join(final_shortest_paths)  

    def get_paths_indexes(paths: list):
        def get_index_of_move(path: list, element_to_find: int):
            for row_num , row in enumerate(path):
                for index, element in enumerate(row):
                    if element == element_to_find:
                        return (row_num, index)

        move_count = 0
        all_moves_indexes = []
        for path in paths:
            temp_moves_indexes = []
            for row in path:
                for element in row:
                    if element:
                        move_count+=1
            for i in range(1, move_count+1):
                temp_moves_indexes.append(get_index_of_move(path, i))
            move_count = 0
            all_moves_indexes.append(temp_moves_indexes[1:]+[dest])
        return all_moves_indexes

    def translate_pathsIndexes_into_Moves(paths_indexes: list):
        def translate_index_into_move (curr_index: tuple, next_move: tuple):
            if next_move[0] < curr_index[0]:
                return "UP"
            elif next_move[0] > curr_index[0]:
                return "DOWN"
            elif next_move[1] > curr_index[1]:
                return "RIGHT"
            else:
                return "LEFT"

        all_paths_asMoves = [] 
        for moves_index in paths_indexes:
            temp_moves = []
            curr_index = src
            for move in moves_index:
                temp_moves.append(translate_index_into_move(curr_index, move))
                curr_index = move
            all_paths_asMoves.append(temp_moves)
        return all_paths_asMoves
        

    raw_paths = []

    matrix = [array("i",[random.choice((0,1,1,0,0,1)) for _ in range (10)]) for _ in range (10)]
    src = (random.choice([_ for _ in range(10)]), random.choice([_ for _ in range(10)]))
    matrix[src[0]][src[1]] = 1
    dest = (random.choice([num for num in range(10) if num != src[0]]), random.choice([num for num in range(10) if num != src[1]] ))
    matrix[dest[0]][dest[1]] = 1
    i, j = src
    x, y = dest
    N = len(matrix)
    visited = [array("i",[0 for _ in range(N)]) for _ in range(N)]

    if (j-1 < 0 or matrix[i][j-1] == 0) and (j+1 >= N or matrix[i][j+1] == 0 ) and (i-1 < 0 or matrix[i-1][j] == 0) and (i+1 >= N or matrix[i+1][j] == 0 ):
        return matrix, "\n\n\n"+" "*31+"No path towards the bear.", "\n\n\n"+" "*30+"No path towards the bear.", src, dest
    elif (y-1 < 0 or matrix[x][y-1] == 0 ) and (y+1 >= N or matrix[x][y+1] == 0) and (x-1 < 0 or matrix[x-1][y] == 0) and (x+1 >= N or matrix[x+1][y] == 0 ):
        return matrix, "\n\n\n"+" "*31+"No path towards the bear.", "\n\n\n"+" "*30+"No path towards the bear.", src, dest
    else:
        find_paths(matrix, i, j, dest, N, 0, visited)
        if raw_paths:
            all_paths_indexes = get_paths_indexes(raw_paths)
            all_paths_asMoves = translate_pathsIndexes_into_Moves(all_paths_indexes)
            all_paths, shortest_paths = get_final_paths(all_paths_asMoves)
            return matrix, " "*32+f"{len(raw_paths)} Total Unique Paths\n\n"+ all_paths, shortest_paths, src, dest
        else:
            return matrix, "\n\n\n"+" "*31+"No path towards the bear.", "\n\n\n"+" "*30+"No path towards the bear.", src, dest
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

window = Tk()
window["bg"] = "#567"
window.title("HUNT THE PRELIM BEAR")
window.geometry("1170x670+150+48")
window.resizable(False, False)

def create_grid():
    num = 48
    for _ in range(9):
        gui_matrix.create_line(num, 0, num, 480)
        gui_matrix.create_line(0, num, 480, num)
        num +=48

def exit_button():
    window.destroy()

def show_frame(frame):
    frame.tkraise()

def generate_4genButton():
    global gui_all_paths, gui_shortest_path, gui_matrix    
    gui_matrix.destroy()
    gui_matrix.__init__()
    gui_matrix = tkinter.Canvas(frame2, bg="burlywood1", highlightthickness=0, width=480, height=480)
    gui_matrix.place(x=80, y=90)
    create_grid()
    gen_button["state"] = "disabled"
    matrix, all_paths, shortest_paths, src, dest = main_algo()
    gen_button["state"] = "normal"
    
    num2 = 24
    for row_num, row in enumerate(matrix):
        num1 = 24
        for col_num, element in enumerate(row):
            if (row_num, col_num) == src: gui_matrix.create_image(num1, num2, image=juan)
            elif (row_num, col_num) == dest: gui_matrix.create_image(num1, num2, image=bear)
            elif element: pass
            else: gui_matrix.create_image(num1, num2, image=random.choice(obstacles))
            num1+=48
        num2+=48

    gui_all_paths.configure(state="normal")
    gui_shortest_path.configure(state="normal")    
    gui_shortest_path.delete('1.0', END)
    gui_all_paths.delete('1.0', END)
    gui_all_paths.insert(tkinter.END, all_paths)
    gui_shortest_path.insert(tkinter.END, shortest_paths)
    gui_all_paths.configure(state="disabled")
    gui_shortest_path.configure(state="disabled")


window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame1 = tk.Frame(window, highlightbackground="red", highlightthickness=0)
frame2 = tk.Frame(window)

background = PhotoImage(file="1.png")
label1 = Label(frame1, image=background)
label1.place(bordermode=OUTSIDE, anchor=NW)

all_label = tkinter.Label(text="ALL PATHS AVAILABLE", bg="green")
all_label.place(x=930, y=250)

title = tkinter.Label(text="HUNT THE PRELIM BEAR", width=55, height=4, bg="red")
title.place(x=660, y=10)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nsew")

frame1_btn = tk.Button(frame1, text="START", font=('Arial', 20), command=lambda: show_frame(frame2),
                       activebackground="tan1", fg="white", borderwidth=3, relief="raised", padx=5, pady=10,
                       bg="red", width=10)
frame1_btn.pack(pady=100, side=BOTTOM)

gui_matrix = tkinter.Canvas(frame2, bg="burlywood1", highlightthickness=0, width=480, height=480)
gui_matrix.place(x=80, y=90)

background2 = Image.open("2.png")
resized_image= background2.resize((1170,670), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
label2 = Label(frame2, image=new_image, borderwidth=0)
label2.place(bordermode=OUTSIDE, anchor=NW)

#all paths widget
gui_all_paths = tkinter.Text(frame2, height=7, width=51, font=('Segoe UI Semibold', 11), fg="#db2a02", bd=4, bg="burlywood1")
gui_all_paths.configure(state="disabled")
gui_all_paths.place(x=710, y=113)

shortest_label = tkinter.Label(text="SHORTEST PATH AVAILABLE", bg="green")
shortest_label.place(x=660, y=250)
#shortest paths widget
gui_shortest_path = tkinter.Text(frame2, height=7, width=48, bd=4, bg="burlywood1", font=('Segoe UI Semibold', 11), fg="#db2a02")
gui_shortest_path.configure(state="disabled")
gui_shortest_path.place(x=720, y=418)

#bear
img1 = Image.open("bear.png").resize((50,50))
bear = ImageTk.PhotoImage(img1)
#juan
img2 = Image.open("Juan.png").resize((50,45))
juan = ImageTk.PhotoImage(img2)

#obstables
img3 = Image.open("mountains.png").resize((40,25))
mountains = ImageTk.PhotoImage(img3)
img4 = Image.open("tiger.png").resize((43,30))
tiger = ImageTk.PhotoImage(img4)
img5 = Image.open("hyena.png").resize((48,35))
hyena = ImageTk.PhotoImage(img5)
img6 = Image.open("puddle.png").resize((40,20))
puddle = ImageTk.PhotoImage(img6)
obstacles = (mountains, tiger, hyena, puddle)

#buttons
restart_button = tkinter.Button(frame2, text="✖", command=exit_button,  font=('Arial', 15), bg="#db2a02",
                            activebackground="burlywood1", width=5, fg="burlywood1", bd=5, relief="groove")
restart_button.place(x=840, y=610)

gen_button = tkinter.Button(frame2, text="▶",  font=('Arial', 15), bg="#db2a02",
                            activebackground="burlywood1", width=5, fg="burlywood1", bd=5, relief="groove", command=generate_4genButton)
gen_button.place(x=930, y=610)


create_grid()

show_frame(frame1)

window.mainloop()