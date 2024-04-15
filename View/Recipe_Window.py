from Model.Recipe import Recipe
# import customtkinter as tk
import customtkinter as ctk
import io, requests, threading
from tkinter import messagebox
from PIL import ImageTk
from Model.Recipe_API import Recipe_API
from Model.Recipe_Service import Recipe_Service



class Recipe_Window:
    def __init__(self, recipe: Recipe):
        # Create the main application window
        app = ctk.CTk()
        app.title("My CustomTkinter App")
        app.geometry("400x300")  # Set the size of the window

        # Create a label widget
        label = ctk.CTkLabel(app, text=recipe.get_title(), font=("Arial", 16))
        label.pack(pady=20)  # Add padding around the label

        # Create a label widget
        label = ctk.CTkLabel(app, text=recipe.get_ingredients(), font=("Arial", 13))
        label.pack(pady=20)  # Add padding around the label

        # Create a label widget
        label = ctk.CTkLabel(app, text=recipe.get_instructions(), font=("Arial", 13))
        label.pack(pady=20)  # Add padding around the label



        # Create a button widget
        # button = tk.CTkButton(app, text="Click Me!", command=lambda: print("Button clicked"))
        # button.pack()

        # Run the application's event loop
        app.mainloop()


class Recipe_Window2:
    def __init__(self, recipe):
        app = ctk.CTk()
        app.title("My CustomTkinter App")
        app.geometry("700x700")

        # Setup UI or label to show loading state
        self.status_label = ctk.CTkLabel(app, text="Loading, please wait...")
        self.status_label.pack(pady=20, padx=10)

        # Start a thread to load data and setup UI
        threading.Thread(target=self.setup_ui, args=(app, recipe)).start()

        app.mainloop()

    def setup_ui(self, app, recipe):
        # Assume this might take time, so it's run in a thread
        # Simulating a delay in fetching data (e.g., from an API)
        import time
        time.sleep(2)  # simulate delay

        # Now update the UI, make sure to run UI updates in the main thread
        app.after(0, self.update_ui, app, recipe)

    def update_ui(self, app, recipe):
        # Clear the status label
        self.status_label.pack_forget()

        # Create labels now that data is loaded
        label = ctk.CTkLabel(app, text=recipe.get_title(), font=("Arial", 16))
        label.pack(pady=20, padx=10)
        label.configure(wraplength=app.winfo_width() - 20)

        # Create a label widget
        label = ctk.CTkLabel(app, text=recipe.get_ingredients(), font=("Arial", 13))
        label.pack(pady=20)  # Add padding around the label
        label.configure(wraplength=app.winfo_width() - 20)


        # Create a label widget
        label = ctk.CTkLabel(app, text=recipe.get_instructions(), font=("Arial", 13))
        label.pack(pady=20)  # Add padding around the label
        label.configure(wraplength=app.winfo_width() - 20)


        # More labels can be added here


