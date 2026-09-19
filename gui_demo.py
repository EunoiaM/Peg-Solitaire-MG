import tkinter as tk

def create_gui():
    """Creates a basic GUI to fulfill Sprint #0 requirements."""
    # Main window setup
    root = tk.Tk()
    root.title("Solitaire Setup")
    root.geometry("300x250")
    root.resizable(False, False)

    # 1. TEXT & 2. LINES (Using the Canvas widget)
    canvas = tk.Canvas(root, width=300, height=80)
    canvas.pack()
    
    # Requirement: Text
    canvas.create_text(150, 30, text="Solitaire Game Settings", font=("Arial", 14, "bold"))
    
    # Requirement: Lines
    canvas.create_line(30, 60, 270, 60, fill="black", width=2)
    canvas.create_line(30, 65, 270, 65, fill="gray", width=1) # Double line effect

    # 3. RADIO BUTTONS
    tk.Label(root, text="Select Draw Rule:", font=("Arial", 10)).pack(pady=(10, 0))
    draw_var = tk.IntVar(value=1)
    
    rb1 = tk.Radiobutton(root, text="Draw 1 Card", variable=draw_var, value=1)
    rb1.pack()
    
    rb3 = tk.Radiobutton(root, text="Draw 3 Cards", variable=draw_var, value=3)
    rb3.pack()

    # 4. CHECK BOX
    hints_var = tk.BooleanVar(value=True)
    cb = tk.Checkbutton(root, text="Enable Visual Hints", variable=hints_var)
    cb.pack(pady=(15, 0))

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    create_gui()
