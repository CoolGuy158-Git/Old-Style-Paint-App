import tkinter as tk

root = tk.Tk()
root.title("Paint")
root.geometry("500x400")
root.resizable(False, False)
root.config(bg="grey")
canvas = tk.Canvas(root, width=500, height=370, bg="white")
canvas.place(x=0, y=30)

colors = ["black", "red", "blue", "green"]
current_color_index = 0

def paint1(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    canvas.create_oval(x1, y1, x2, y2, fill=colors[current_color_index], outline=colors[current_color_index])
def toggle_color():
    global current_color_index
    current_color_index = (current_color_index + 1) % len(colors)
    color.config(text=colors[current_color_index])
color = tk.Button(root, width=5, text="Black", bg="tan", fg="black", activebackground="burlywood", activeforeground="white", command=toggle_color)
color.place(x=55, y=0)


canvas.bind("<B1-Motion>", paint1)

def clear_canvas():
    canvas.config(bg="white")
    canvas.delete("all")
def fill():
    canvas.config(bg=colors[current_color_index])

clear_btn = tk.Button(root, text="Clear", command=clear_canvas, bg="red", fg="black", activebackground="pink", activeforeground="white")
clear_btn.place(x=10, y=0)
fill_btn = tk.Button(root, text="Fill", command=fill, bg="tan", fg="black", activebackground="burlywood", activeforeground="white")
fill_btn.place(x=105, y=0)
root.mainloop()