from customtkinter import CTk, CTkScrollableFrame
from .petition import PetitionPage


class PetitionApp:
    def __init__(self):
        # Create the root window
        self.root = CTk(fg_color="#FFEC3C")
        self.root.title("Petition Platform")
        self.root.geometry("400x600")

        # Create the main frame
        self.main_frame = CTkScrollableFrame(self.root, fg_color="#FFEC3C")
        self.main_frame.pack(fill="both", expand=True)

        # Create the dashboard
        self.dashboard = PetitionPage(self.main_frame)

    def run(self):
        # Run the main loop
        self.root.mainloop()
