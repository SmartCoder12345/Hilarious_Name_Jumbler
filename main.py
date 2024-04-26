"""
Author: #Smart_Coder
--> Hilarious Name Jumbler
"""

import customtkinter as ctk
import random

# Set appearance mode to dark and default color theme to dark-blue
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def check_if_name(first_name: str, last_name: str) -> bool:
    """
    Checks if the name is valid.
    :param first_name: First Name
    :param last_name: Last Name
    :return: True if the name is valid, False otherwise.
    """
    if first_name.strip() == "" or last_name.strip() == "":
        return False
    elif len(first_name) <= 2 or len(last_name) <= 2:
        return False
    else:
        return True

def normalize_button_if_name(entry1: ctk.CTkEntry, entry2: ctk.CTkEntry, add_button: ctk.CTkButton) -> None:
    """
    Normalizes the button state if the name is valid.
    :param entry1: First Name Entry
    :param entry2: Last Name Entry
    :param add_button: Add Name Button
    :return: None
    """
    if check_if_name(entry1.get(), entry2.get()):
        add_button.configure(state="normal")
    else:
        add_button.configure(state="disabled")

def add_name(frame: ctk.CTkScrollableFrame, first_name: ctk.CTkEntry, last_name: ctk.CTkEntry) -> None:
    """
    Adds a name to the frame and clears the entry boxes.
    :param frame: Scrollable Frame object.
    :param first_name: First Name Entry
    :param last_name: Last Name Entry
    :return: None
    """
    name = f"{first_name.get()} {last_name.get()}"

    name_label = ctk.CTkLabel(frame, text=name, font=("Helvetica", 30))
    name_label.pack(pady=10)

    first_name.delete(0, "end")
    last_name.delete(0, "end")

def clear_frame(frame: ctk.CTkScrollableFrame) -> None:
    """
    Clears the frame.
    :param frame: Scrollable Frame object.
    :return: None
    """
    for widget in frame.winfo_children():
        widget.destroy()

def check_if_atleast_two_names(frame: ctk.CTkScrollableFrame) -> bool:
    """
    Checks if there are at least two names in the frame.
    :param frame: Scrollable Frame object.
    :return: True if there are at least two names, False otherwise.
    """
    return len(frame.winfo_children()) >= 2

def jumble_names(first_names: list, last_name: list) -> list:
    """
    Jumbles the names.
    :param first_names: List of first names.
    :param last_name: List of last names.
    :return: None
    """
    jumbled_names = []

    for i in range(len(first_names)):
        random_index = random.randint(0, len(last_name)-1)
        jumbled_name = first_names[i] + " " + last_name[random_index]
        jumbled_names.append(jumbled_name)
        last_name.remove(last_name[random_index])

    return jumbled_names

def show_jumbled_names(frame: ctk.CTkScrollableFrame) -> None:
    """
    Shows the jumbled names.
    :param frame: Scrollable Frame
    :return: None
    """

    names: list = frame.winfo_children()
    first_names = []
    last_names = []

    for name in names:
        name = name.cget("text")
        first_names.append(name.split(" ")[0])
        last_names.append(name.split(" ")[1])

    jumbled_names = jumble_names(first_names, last_names)

    new_root = ctk.CTk()
    new_root.resizable(False, False)
    new_root.title("Jumbled Names")
    new_root.iconbitmap("asset/icon.ico")

    # Create a Scrollable Frame
    my_frame = ctk.CTkScrollableFrame(new_root, orientation="vertical", width=350, height=400)
    my_frame.grid(row=0, column=0, columnspan=2, pady=20)

    for name in jumbled_names:
        name_label = ctk.CTkLabel(my_frame, text=name, font=("Helvetica", 30))
        name_label.pack(pady=10)

    # Run the Tkinter event loop
    new_root.mainloop()


def add_random_name(frame: ctk.CTkScrollableFrame) -> None:
    """
    Adds a random name to the frame.
    :param frame: Scrollable Frame object.
    :return: None
    """

    # List of random first names
    first_names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack",
                   "Katie", "Leo", "Mia", "Nathan", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tina"]

    # List of random last names
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
                  "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name = f"{first_name} {last_name}"

    name_label = ctk.CTkLabel(frame, text=full_name, font=("Helvetica", 30))
    name_label.pack(pady=10)

def main():
    # Setting the Window
    root = ctk.CTk()
    root.title("Hilarious Name Jumbler")
    root.resizable(False, False)
    root.iconbitmap("asset/icon.ico")

    # Create a Scrollable Frame
    my_frame = ctk.CTkScrollableFrame(root, orientation="vertical", width=350)
    my_frame.grid(row=0, column=0, columnspan=2, pady=20)

    # Creating Entry Boxes
    entry1 = ctk.CTkEntry(root, placeholder_text="First Name", height=40, font=("Helvetica", 18))
    entry1.grid(row=1, column=0, padx=25)

    entry2 = ctk.CTkEntry(root, placeholder_text="Last Name", height=40, font=("Helvetica", 18))
    entry2.grid(row=1, column=1, padx=25)

    # Creating Buttons
    add_button = ctk.CTkButton(root, text="Add Name", height=40, state="disabled", command=lambda: add_name(my_frame, entry1, entry2), font=("Helvetica", 20))
    add_button.grid(row=2, column=0, padx=20, pady=20)

    clear_button = ctk.CTkButton(root, text="Clear", fg_color="red", text_color="white", hover_color="orange", command=lambda: clear_frame(my_frame), height=40, state="disabled", font=("Helvetica",
                                                                                                                                                                                        20))
    clear_button.grid(row=2, column=1, padx=20, pady=20)

    random_button = ctk.CTkButton(root, text="Add a Random Name", height=50, width=400, font=("Calibri", 30), command=lambda: add_random_name(my_frame))
    random_button.grid(row=3, column=0, columnspan=2, pady=20)

    jumble_button = ctk.CTkButton(root, text="Jumble Names", height=60, width=400, font=("Calibri", 30), state="disabled", command=lambda: show_jumbled_names(my_frame))
    jumble_button.grid(row=4, column=0, columnspan=2)

    # Binding the Entries and buttons
    entry1.bind("<Key>", lambda eve: root.after(10, lambda: normalize_button_if_name(entry1, entry2, add_button)))
    entry2.bind("<Key>", lambda eve: root.after(10, lambda: normalize_button_if_name(entry1, entry2, add_button)))

    add_button.bind("<Button-1>", lambda eve: clear_button.configure(state="normal"))
    add_button.bind("<Button-1>", lambda eve: add_button.configure(state="disabled"))
    add_button.bind("<Button-1>", lambda eve: jumble_button.configure(state="normal") if check_if_atleast_two_names(my_frame) else jumble_button.configure(state="disabled"))

    random_button.bind("<Button-1>", lambda eve: clear_button.configure(state="normal") if check_if_atleast_two_names(my_frame) else jumble_button.configure(state="disabled"))

    clear_button.bind("<Button-1>", lambda eve: clear_button.configure(state="disabled"))
    clear_button.bind("<Button-1>", lambda eve: jumble_button.configure(state="disabled"))

    random_button.bind("<Button-1>", lambda eve: jumble_button.configure(state="normal") if check_if_atleast_two_names(my_frame) else jumble_button.configure(state="disabled"))
    root.mainloop()

if __name__ == '__main__':
    main()