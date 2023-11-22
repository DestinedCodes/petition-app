from customtkinter import (
    CTkEntry,
    CTkTextbox,
    CTkButton,
    CTkLabel,
    CTkFrame,
    CTkFont,
)
from CTkListbox import CTkListbox
from .voting import VotingPage
from services import save_data_to_file, load_data_from_file


class PetitionPage:
    def __init__(self, main_frame):
        self.petitions_data = load_data_from_file()

        self.main_frame = main_frame

        # Create the main label
        self.main_label = CTkLabel(
            main_frame,
            text="Petition Platform",
            font=CTkFont(size=30, weight="bold"),
            text_color="black",
        )
        self.main_label.pack(pady=20)

        # Create the ongoing petitions frame
        self.ongoing_petitions_frame = CTkFrame(
            main_frame,
            fg_color="#A5D8FF",
            border_width=2,
            border_color="black"
        )

        self.ongoing_petitions_frame.pack()

        # Create the ongoing petitions label
        self.ongoing_petitions_label = CTkLabel(
            self.ongoing_petitions_frame,
            text="Ongoing Petitions:",
            font=CTkFont(size=25, weight="normal"),
            text_color="black",
            justify="left",
            anchor="w",
            width=330,
        )
        self.ongoing_petitions_label.pack(padx=10, pady=10)

        # Create the ongoing petitions list
        self.ongoing_petitions = CTkListbox(
            self.ongoing_petitions_frame,
            width=310,
            height=200,
            fg_color="#A5D8FF",
            text_color="black",
            border_width=0,
            command=self.show_petition,
        )
        self.ongoing_petitions.pack(padx=10, pady=(0, 10))
        self.update_ongoing_petitions()

        # Create the Create Petition label
        self.create_petition_label = CTkLabel(
            main_frame,
            text="Create Petition",
            font=CTkFont(size=30, weight="normal"),
            text_color="black",
        )
        self.create_petition_label.pack(padx=10, pady=10)

        # Create the Create Petition frame
        self.create_petition_frame = CTkFrame(
            main_frame,
            fg_color="#A5D8FF",
            border_width=2,
            border_color="black"
        )
        self.create_petition_frame.pack(pady=(0, 10))

        # Create the title label
        self.title_label = CTkLabel(
            self.create_petition_frame,
            text="Title:",
            font=CTkFont(size=20, weight="normal"),
            text_color="black",
            justify="left",
            anchor="w",
            width=330,
        )
        self.title_label.pack(padx=10, pady=10)

        # Create the title entry
        self.title_entry = CTkEntry(
            self.create_petition_frame,
            width=330,
            fg_color="#B2F2BB",
            text_color="black",
            border_color="black",
        )
        self.title_entry.pack(pady=(0, 10))

        # Create the description label
        self.description_label = CTkLabel(
            self.create_petition_frame,
            text="Description:",
            font=CTkFont(size=20, weight="normal"),
            text_color="black",
            justify="left",
            anchor="w",
            width=330,
        )
        self.description_label.pack(padx=10, pady=0)

        # Create the description text box
        self.description_entry = CTkTextbox(
            self.create_petition_frame,
            width=330,
            height=100,
            fg_color="#B2F2BB",
            text_color="black",
            border_width=2,
            border_color="black",
        )
        self.description_entry.pack(pady=(0, 10))

        # Create the Create Petition button
        self.create_petition_button = CTkButton(
            self.create_petition_frame,
            text="Create Petition",
            font=CTkFont(size=20, weight="normal"),
            text_color="black",
            fg_color="#B2F2BB",
            border_width=2,
            border_color="black",
            command=self.create_petition,
        )
        self.create_petition_button.pack(padx=10, pady=10)

        # Create the error label
        self.error_label = CTkLabel(
            main_frame,
            text="",
            font=CTkFont(size=15, weight="normal"),
            text_color="red",
        )

    def create_petition(self):
        title = self.title_entry.get()
        description = self.description_entry.get("1.0", "end-1c")
        if title and description:
            self.error_label.configure(text="")
            petition = {"index": len(self.petitions_data), "title": title,
                        "description": description, "voters": []}
            self.petitions_data.append(petition)
            self.update_ongoing_petitions()
            self.clear_create_petition_fields()
            save_data_to_file(self.petitions_data)
        else:
            self.error_label.configure(text="Please fill in all the fields")

    def update_ongoing_petitions(self):
        if self.ongoing_petitions.size() > 0:
            self.ongoing_petitions.delete(0, "end")
        for petition in self.petitions_data:
            index = petition["index"]
            petition_title = petition["title"]
            votes = len(petition["voters"])
            self.ongoing_petitions.insert(
                "end", f"{index}: {petition_title} - Votes: {votes}")

    def clear_create_petition_fields(self):
        self.title_entry.delete(0, "end")
        self.description_entry.delete("1.0", "end")

    def show_petition(self, selected_petition):
        # Extract the petition title from the selected item
        petition_index = selected_petition.split(":")[0]

        # Find the corresponding petition in the data
        for petition in self.petitions_data:
            if petition["index"] == int(petition_index):
                # Open the voting page for the selected petition
                self.voting = VotingPage(self.main_frame, petition)
                break
