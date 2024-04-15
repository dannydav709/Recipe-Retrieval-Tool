import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Multi-Page Recipe App")
        self.geometry("800x600")

        # Dictionary to hold the frames
        self.frames = {}

        for F in (StartPage, RecipesPage, SettingsPage):
            frame = F(parent=self, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, context):
        """Bring a frame to the top for display"""
        frame = self.frames[context]
        frame.tkraise()

class StartPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="This is the Start Page")
        label.pack(pady=10, padx=10)
        button = ctk.CTkButton(self, text="Go to Recipes",
                               command=lambda: controller.show_frame(RecipesPage))
        button.pack()

class RecipesPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="This is the Recipes Page")
        label.pack(pady=10, padx=10)
        button = ctk.CTkButton(self, text="Go to Settings",
                               command=lambda: controller.show_frame(SettingsPage))
        button.pack()

class SettingsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="This is the Settings Page")
        label.pack(pady=10, padx=10)
        button = ctk.CTkButton(self, text="Go to Start Page",
                               command=lambda: controller.show_frame(StartPage))
        button.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
