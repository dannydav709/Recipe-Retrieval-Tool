import customtkinter as tk

class Window_Controller:
    def __init__(self):
        # Create the main application window
        app = tk.Tk()
        app.title("My CustomTkinter App")
        app.geometry("400x300")  # Set the size of the window

        # Create a label widget
        label = tk.Label(app, text="Hello, CustomTkinter!", font=("Arial", 16))
        label.pack(pady=20)  # Add padding around the label

        # Create a button widget
        button = tk.Button(app, text="Click Me!", command=lambda: print("Button clicked"))
        button.pack()

        # Run the application's event loop
        app.mainloop()

