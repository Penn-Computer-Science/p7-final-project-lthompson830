import tkinter as tk

# Create window
root = tk.Tk()
root.title("Shape Generator")
# Size of window
root.geometry("500x500")

# Canvas
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

# Function to draw shapes
def draw_shape():
    shape = entry.get().lower()

    # Clear canvas
    canvas.delete("all")

    if "circle" == shape:
        canvas.create_oval(150, 100, 350, 300, fill="blue")

    elif "square" == shape:
        canvas.create_rectangle(150, 100, 350, 300, fill="blue")

    elif "triangle" == shape:
        canvas.create_polygon(
            250, 100,
            150, 300,
            350, 300,
            fill="blue"
        )

#"points" is making a list of the parameters for each of these shapes
# and it's not defined anywhere else because it's only needed here
    elif "star" == shape:
        points = [
            250, 100,
            290, 180,
            380, 180,
            310, 240,
            340, 330,
            250, 280,
            160, 330,
            190, 240,
            120, 180,
            210, 180
        ]
        canvas.create_polygon(points, fill="blue")

    elif "hexagon" == shape:
        points = [
            250, 80,
            350, 140,
            350, 260,
            250, 320,
            150, 260,
            150, 140
        ]
        canvas.create_polygon(points, fill="blue")

    elif "rectangle" == shape:
        canvas.create_rectangle(150, 200, 350, 300, fill="blue")

    elif "oval" == shape:
        canvas.create_oval(150, 200, 350, 300, fill="blue")


# This is for if you enter a shape that isn't implemented
# Of if you enter something that isn't the name of a shape
    else:
        canvas.create_text(
            250, 200,
            text="Shape not recognized",
            font=("Arial", 20),
            fill="black"
        )

# Input box to enter which shape you want
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Button to generate the shape
button = tk.Button(
    root,
    text="Generate Shape",
    command=draw_shape,
    font=("Arial", 12)
)
button.pack()

root.mainloop()