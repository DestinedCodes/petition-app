""" This module contains the PetitionPage class """
# pylint: disable=import-error
from customtkinter import (
    CTkEntry,
    CTkTextbox,
    CTkButton,
    CTkLabel,
    CTkFrame,
    CTkFont,
)
from CTkListbox import CTkListbox
from .services import save_data_to_file, load_data_from_file


class VotingPage:
    """ The class for the Voting Page """
    def __init__(self, main_frame, petition):
        self.petitions_data = load_data_from_file()
        self.petition = petition

        # Destroy the existing widgets in the main frame
        for widget in main_frame.winfo_children():
            widget.destroy()

        # Create the voting page label
        voting_page_label = CTkLabel(
            main_frame,
            text="Vote for/against Petition",
            font=CTkFont(size=30, weight="bold"),
            text_color="black",
        )
        voting_page_label.pack(pady=20)

        # Create the voting frame
        voting_frame = CTkFrame(
            main_frame,
            fg_color="#A5D8FF",
            border_width=2,
            border_color="black"
        )
        voting_frame.pack()

        # Create the title label
        title_label = CTkLabel(
            voting_frame,
            text="Title:",
            font=CTkFont(size=20, weight="normal"),
            text_color="black",
            justify="left",
            anchor="w",
            width=330,
        )
        title_label.pack(padx=10, pady=10)

        # Create the title entry
        title_entry = CTkEntry(
            voting_frame,
            width=330,
            fg_color="#B2F2BB",
            text_color="black",
            border_color="black",
        )
        title_entry.delete(0, "end")
        title_entry.insert(0, petition["title"])
        title_entry.configure(state="disabled")
        title_entry.pack(pady=(0, 10))

        # Create the description label
        description_label = CTkLabel(
            voting_frame,
            text="Description:",
            font=CTkFont(size=20, weight="normal"),
            text_color="black",
            justify="left",
            anchor="w",
            width=330,
        )
        description_label.pack(padx=10, pady=0)

        # Create the description text box
        description_entry = CTkTextbox(
            voting_frame,
            width=330,
            height=100,
            fg_color="#B2F2BB",
            text_color="black",
            border_width=2,
            border_color="black",
        )
        description_entry.delete("1.0", "end")
        description_entry.insert("1.0", petition["description"])
        description_entry.configure(state="disabled")
        description_entry.pack(pady=(0, 10))

        # Create the voters name label
        voters_name_label = CTkLabel(
            voting_frame,
            text="Voters Name:",
            font=CTkFont(size=20, weight="normal"),
            text_color="black",
            justify="left",
            anchor="w",
            width=330,
        )
        voters_name_label.pack(padx=10, pady=0)

        # Create the voters name entry
        self.voters_name_entry = CTkEntry(
            voting_frame,
            width=330,
            fg_color="#B2F2BB",
            text_color="black",
            border_color="black",
        )
        self.voters_name_entry.pack(pady=(0, 10))

        # Create the vote for button
        vote_for_button = CTkButton(
            voting_frame,
            text="Vote for",
            font=CTkFont(size=20, weight="normal"),
            text_color="black",
            fg_color="#B2F2BB",
            border_width=2,
            border_color="black",
            command=self.vote_for,
        )

        vote_for_button.pack(padx=10, pady=10, side="left",
                             fill="x", expand=True)

        # Create the vote against button
        vote_against_button = CTkButton(
            voting_frame,
            text="Vote against",
            font=CTkFont(size=20, weight="normal"),
            text_color="black",
            fg_color="#B2F2BB",
            border_width=2,
            border_color="black",
            command=self.votes_against,
        )
        vote_against_button.pack(
            padx=10, pady=10, side="right", fill="x", expand=True)

        # Create a scrollable frame to display the votes
        votes_frame = CTkFrame(
            main_frame, width=400, height=300, fg_color="#FFEC3C"
        )
        votes_frame.pack(fill="both", expand=True)

        # Create the votes label
        votes_label = CTkLabel(
            votes_frame,
            text="Votes:",
            font=CTkFont(size=20, weight="normal"),
            text_color="black",
            justify="left",
            anchor="w",
            width=330,
        )
        votes_label.pack(padx=10, pady=10)

        # Create the votes list
        self.votes_list = CTkListbox(
            votes_frame,
            width=310,
            height=200,
            fg_color="#A5D8FF",
            text_color="black",
            border_width=0,
        )
        self.votes_list.pack(padx=10, pady=(0, 10))
        self.update_votes_list()

        # Create the back to dashboard button
        back_to_dashboard_button = CTkButton(
            main_frame,
            text="Back to Dashboard",
            font=CTkFont(size=20, weight="normal"),
            text_color="black",
            fg_color="#B2F2BB",
            border_width=2,
            border_color="black",
            command=self.back_to_dashboard,
        )
        back_to_dashboard_button.pack(padx=10, pady=10)

    def update_votes_list(self):
        """ Updates the votes list """
        if self.votes_list.size() > 0:
            self.votes_list.delete(0, "end")
        for vote in self.petition["voters"]:
            self.votes_list.insert("end", vote)

    def vote_for(self):
        """ Adds a vote for the petition """
        name = self.voters_name_entry.get()

        self.petition["voters"].append(name)
        self.petition["votes_for"] += 1
        self.petitions_data[self.petition["id"]] = self.petition
        save_data_to_file(self.petitions_data)
        self.update_votes_list()
        self.voters_name_entry.delete(0, "end")

    def votes_against(self):
        """ Adds a vote against the petition """
        name = self.voters_name_entry.get()

        self.petition["voters"].append(name)
        self.petition["votes_against"] += 1
        self.petitions_data[self.petition["id"]] = self.petition
        save_data_to_file(self.petitions_data)
        self.update_votes_list()
        self.voters_name_entry.delete(0, "end")

    def back_to_dashboard(self):
        """ Goes back to the dashboard page """
        pass
