from customtkinter import *
from PIL import Image
import random
from tkfontawesome import icon_to_image

# Initialize main window
root = CTk()
root.title("STEAM Day Digital Booth: AI Bingo")
root.geometry('600x400')
root.minsize(500, 350)
set_appearance_mode("dark")

# Configure grid for main window
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Load icons from tkfontawesome
send_icon_image = icon_to_image("paper-plane", fill="#EA6E08", scale_to_width=24)
quit_icon_image = icon_to_image("xmark", fill="#EA6E08", scale_to_width=24)
rules_icon_image = icon_to_image("book", fill="#EA6E08", scale_to_width=24)
back_icon_image = icon_to_image("arrow-left", fill="#EA6E08", scale_to_width=24)
reset_icon_image = icon_to_image("rotate-right", fill="#EA6E08", scale_to_width=24)
dice_icon_image = icon_to_image("dice", fill="#EA6E08", scale_to_width=24)
undo_icon_image = icon_to_image("undo", fill="#EA6E08", scale_to_width=24)

# Track drawn numbers
drawn_numbers = []

# Tasks dictionary with emoji image paths (25 tasks)
tasks = {
    '1': {'task': 'Recommend a song on Spotify ', 'emoji': 'emojis/Musical_Notes_3D.png'},
    '2': {'task': 'Identify a type of flower ', 'emoji': 'emojis/Tulip_3D.png'},
    '3': {'task': 'Use a map app to find the fastest route ', 'emoji': 'emojis/World_Map_3D.png'},
    '4': {'task': 'Predict if the weather will be snow ', 'emoji': 'emojis/cloud_with_snow_3d.png'},
    '5': {'task': 'Use autocomplete in your Google search ', 'emoji': 'emojis/Magnifying_Glass_Tilted_Left_3D.png'},
    '6': {'task': 'Writing assignment graded by a computer ', 'emoji': 'emojis/Memo_3D.png'},
    '7': {'task': 'Send a voice-to-text message ', 'emoji': 'emojis/Microphone_3D.png'},
    '8': {'task': 'Recommend a product on Amazons shopping website ', 'emoji': 'emojis/Shopping_Cart_3D.png'},
    '9': {'task': 'Have a news app suggest a news article ', 'emoji': 'emojis/Newspaper_3D.png'},
    '10': {'task': 'Identify a hand-drawn number ', 'emoji': 'emojis/Writing_Hand_3D_default.png'},
    '11': {'task': 'Use your face to unlock a device ', 'emoji': 'emojis/grinning_Face_with_smiling_eyes_3D.png'},
    '12': {'task': 'Suggest a new game to play on Roblox ', 'emoji': 'emojis/Video_Game_3D.png'},
    '13': {'task': 'Identify any type of drawings ', 'emoji': 'emojis/Artist_Palette_3D.png'},
    '14': {'task': 'Play a motion-sensitive video game ', 'emoji': 'emojis/man_dancing_3d_default.png'},
    '15': {'task': 'Identify a type of bird species ', 'emoji': 'emojis/parrot_3D.png'},
    '16': {'task': 'Have your words autocorrected in a text ', 'emoji': 'emojis/Keyboard_3D.png'},
    '17': {'task': 'Get a YouTube video recommendation ', 'emoji': 'emojis/Video_Camera_3D.png'},
    '18': {'task': 'Write an AI version of a Harry Potter story ', 'emoji': 'emojis/Books_3D.png'},
    '19': {'task': 'Use an app to identify some fruit ', 'emoji': 'emojis/Red_Apple_3D.png'},
    '20': {'task': 'Create an AI classical music song ', 'emoji': 'emojis/musical_score_3d.png'},
    '21': {'task': 'Identify a planet or asteroid in a picture ', 'emoji': 'emojis/Ringed_Planet_3D.png'},
    '22': {'task': 'Predict which football team will win a game ', 'emoji': 'emojis/American_Football_3D.png'},
    '23': {'task': 'Identify a type of bug ', 'emoji': 'emojis/bug_3D.png'},
    '24': {'task': 'Create an unbeatable chess bot ', 'emoji': 'emojis/Chess_Pawn_3D.png'},
    '25': {'task': 'Predict if an email is important or junk/spam ', 'emoji': 'emojis/E-mail_3D.png'}
}

# Cache for emoji images to avoid reloading
emoji_cache = {}

# Function to load and resize emoji image as CTkImage
def load_emoji_image(path, size=(28, 28)):
    if path not in emoji_cache:
        img = Image.open(path).resize(size, Image.LANCZOS)
        emoji_cache[path] = CTkImage(light_image=img, dark_image=img, size=size)
    return emoji_cache[path]

# Function to roll a random number
def roll_number():
    available_numbers = [str(i) for i in range(1, 26) if str(i) not in drawn_numbers]
    if available_numbers:
        number = random.choice(available_numbers)
        draw_number(number)

# Function to undo the last drawn number
def undo_action():
    if drawn_numbers:
        drawn_numbers.pop()
        update_bingo_page()

# Create main frame for start page
main_frame = CTkFrame(root, fg_color="transparent")
main_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')

# Configure grid for main frame
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)

# Main frame widgets
lbl1 = CTkLabel(main_frame, text='Welcome to the STEAM Day Digital Booth!', font=("Broadway", 24), text_color="#FCDDA4")
lbl2 = CTkLabel(main_frame, text='Created by Nick Pucci and Jake Lee', font=("Broadway", 18), text_color="#FCDDA4")
lbl3 = CTkLabel(main_frame, text='AI Bingo', font=("Britannic Bold", 48), text_color="#FFB01E")
lbl1.grid(row=0, column=0, columnspan=3, pady=(20, 10), sticky='n')
lbl2.grid(row=0, column=0, columnspan=3, pady=(50, 30), sticky='n')
lbl3.grid(row=0, column=0, columnspan=3, pady=(100,50), sticky='n')

def clicked():
    show_frame(bingo_frame)

# Rules button
rules_btn = CTkButton(master=main_frame,
                      text='Rules',
                      image=rules_icon_image,
                      command=lambda: show_frame(rules_frame),
                      fg_color='orange',
                      hover_color="#EAAC79",
                      border_color='white',
                      border_width=2,
                      width=150,
                      height=50,
                      font=("Britannic Bold", 18))
rules_btn.grid(row=1, column=0, padx=10, pady=10, sticky='e')

# Play button
btn = CTkButton(master=main_frame,
                text='Play',
                image=send_icon_image,
                command=clicked,
                fg_color='orange',
                hover_color="#EAAC79",
                border_color='white',
                border_width=2,
                width=150,
                height=50,
                font=("Britannic Bold", 18))
btn.grid(row=1, column=1, padx=10, pady=10)

# Quit button
quit_btn = CTkButton(master=main_frame,
                     text='Quit',
                     image=quit_icon_image,
                     command=root.destroy,
                     fg_color='orange',
                     hover_color="#EAAC79",
                     border_color='white',
                     border_width=2,
                     width=150,
                     height=50,
                     font=("Britannic Bold", 18))
quit_btn.grid(row=1, column=2, padx=10, pady=10, sticky='w')

# Create rules frame
rules_frame = CTkFrame(root, fg_color="transparent")

# Configure grid for rules frame
rules_frame.grid_rowconfigure(0, weight=1)
rules_frame.grid_rowconfigure(1, weight=1)
rules_frame.grid_columnconfigure(0, weight=1)

# Rules frame widgets
rules_label = CTkLabel(rules_frame, text="AI Bingo Rules\n\n1. Click 'Play' to go to the bingo page.\n2. Select a number from 1 to 25 on the right side or click 'Roll' to draw a random number.\n3. View drawn numbers and tasks with emojis in the center.\n4. Numbers in the pile on the right are shaded when drawn.\n5. Match tasks to your bingo card!\n6. Have fun and explore AI challenges!",
                       font=("Tw Cen MT", 16), text_color="#FCDDA4", justify="center")
rules_label.grid(row=0, column=0, padx=20, pady=(20, 10))

back_btn = CTkButton(rules_frame,
                     text='Back',
                     image=back_icon_image,
                     command=lambda: show_frame(main_frame if not drawn_numbers else bingo_frame),
                     fg_color='orange',
                     hover_color="#EAAC79",
                     border_color='white',
                     border_width=2)
back_btn.grid(row=1, column=0, pady=10)

# Create bingo frame
bingo_frame = CTkFrame(root, fg_color="transparent")
bingo_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')

# Configure grid for bingo frame
bingo_frame.grid_rowconfigure(0, weight=0)  # Header
bingo_frame.grid_rowconfigure(1, weight=1)  # Content
bingo_frame.grid_columnconfigure(0, weight=3)  # Drawn numbers section
bingo_frame.grid_columnconfigure(1, weight=0)  # Number pile section

# Bingo frame header (Back, Rules, Reset, Roll buttons)
header_frame = CTkFrame(bingo_frame, fg_color="transparent")
header_frame.grid(row=0, column=0, columnspan=2, sticky='ew')
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)
header_frame.grid_columnconfigure(3, weight=1)

back_bingo_btn = CTkButton(header_frame,
                           text='Back',
                           image=back_icon_image,
                           command=lambda: confirm_action("Are you sure? Your progress will be lost.", reset_and_back),
                           fg_color='orange',
                           hover_color="#EAAC79",
                           border_color='white',
                           border_width=2,
                           width=150,
                           height=50,
                           font=("Britannic Bold", 20))
back_bingo_btn.grid(row=0, column=0, padx=5, pady=5)

rules_bingo_btn = CTkButton(header_frame,
                            text='Rules',
                            image=rules_icon_image,
                            command=lambda: show_frame(rules_frame),
                            fg_color='orange',
                            hover_color="#EAAC79",
                            border_color='white',
                            border_width=2,
                            width=150,
                            height=50,
                            font=("Britannic Bold", 20))
rules_bingo_btn.grid(row=0, column=1, padx=5, pady=5)

reset_btn = CTkButton(header_frame,
                      text='Reset',
                      image=reset_icon_image,
                      command=lambda: confirm_action("Are you sure? Your progress will be lost.", reset_progress),
                      fg_color='orange',
                      hover_color="#EAAC79",
                      border_color='white',
                      border_width=2,
                      width=150,
                      height=50,
                      font=("Britannic Bold", 20))
reset_btn.grid(row=0, column=2, padx=5, pady=5)

undo_btn = CTkButton(header_frame,
                     text='Undo',
                     image=undo_icon_image,
                     command=undo_action,
                     fg_color='orange',
                     hover_color="#EAAC79",
                     border_color='white',
                     border_width=2,
                     width=150,
                     height=50,
                     font=("Britannic Bold", 20))
undo_btn.grid(row=0, column=3, padx=5, pady=5)

roll_btn = CTkButton(header_frame,
                     text='Roll',
                     image=dice_icon_image,
                     command=roll_number,
                     fg_color='orange',
                     hover_color="#EAAC79",
                     border_color='white',
                     border_width=2,
                     width=150,
                     height=50,
                     font=("Britannic Bold", 20))
roll_btn.grid(row=0, column=4, padx=5, pady=5)

# Drawn numbers section
left_frame = CTkFrame(bingo_frame, fg_color="#FCAC2A", border_color='white')
left_frame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
left_frame.grid_columnconfigure(0, weight=1)
left_frame.grid_rowconfigure(1, weight=1)

drawn_label = CTkLabel(left_frame, text="Drawn Numbers", font=("Britannic Bold", 28), text_color="#FFFFFF")
drawn_label.grid(row=0, column=0, pady=(5, 5), sticky='n')

drawn_content_frame = CTkScrollableFrame(left_frame, fg_color="#FDE9D1")
drawn_content_frame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
drawn_content_frame.grid_columnconfigure(0, weight=1)

# Right side: Number pile (5x5 grid for 25 numbers)
right_frame = CTkFrame(bingo_frame, fg_color="#2B2B2B", width=480)
right_frame.grid(row=1, column=1, padx=5, pady=5, sticky='nse')
for i in range(5):
    right_frame.grid_columnconfigure(i, weight=1)
for i in range(5):
    right_frame.grid_rowconfigure(i, weight=1)

number_buttons = {}
for i in range(1, 26):
    row = (i-1) // 5
    col = (i-1) % 5
    num = str(i)
    btn = CTkButton(right_frame,
                    text=num,
                    command=lambda n=num: draw_number(n),
                    fg_color="#FF6200",
                    hover_color="#ED865E",
                    border_color='white',
                    border_width=2,
                    width=90,
                    height=90,
                    font=("Britannic Bold", 24))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
    number_buttons[num] = btn

# Function to draw a number
def draw_number(number):
    if number not in drawn_numbers:
        drawn_numbers.append(number)
        update_bingo_page()

# Function to update bingo page
def update_bingo_page():
    # Clear existing labels in drawn_content_frame
    for widget in drawn_content_frame.winfo_children():
        widget.destroy()
    
    # Add new labels with emojis and tasks
    for i, num in enumerate(drawn_numbers):
        task = tasks.get(num, {'task': 'Unknown task', 'emoji': ''})
        text = f" {num}: {task['task']}"
        if task['emoji']:
            emoji_img = load_emoji_image(task['emoji'], size=(28, 28))
            label = CTkLabel(drawn_content_frame, text=text, image=emoji_img, compound="right", font=("Tw Cen MT", 28), text_color="#333333", anchor="w")
        else:
            label = CTkLabel(drawn_content_frame, text=text, font=("Tw Cen MT", 28), text_color="#333333", anchor="w")
        label.grid(row=i, column=0, pady=0, sticky='w')
    
    # Update number buttons
    for num, btn in number_buttons.items():
        if num in drawn_numbers:
            btn.configure(fg_color="#895136", hover_color="#895136", state='disabled')
        else:
            btn.configure(fg_color='#FF6200', hover_color="#ED865E", state='normal')

# Function to show confirmation dialog
def confirm_action(message, callback):
    dialog = CTkToplevel(root)
    dialog.title("Confirm")
    dialog.geometry("300x150")
    dialog.transient(root)
    dialog.grab_set()
    
    # Center the dialog on the screen
    dialog.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    dialog_width = 300
    dialog_height = 150
    x = (screen_width - dialog_width) // 2
    y = (screen_height - dialog_height) // 2
    dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")
    
    CTkLabel(dialog, text=message, font=("Arial", 14), text_color="#FCDDA4").pack(pady=20)
    
    frame = CTkFrame(dialog, fg_color="transparent")
    frame.pack(pady=10)
    
    CTkButton(frame, text="Yes", image=send_icon_image, command=lambda: [callback(), dialog.destroy()],
              fg_color='orange', hover_color="#EAAC79", border_color='white', border_width=2).pack(side='left', padx=10)
    CTkButton(frame, text="No", image=quit_icon_image, command=dialog.destroy,
              fg_color='orange', hover_color="#EAAC79", border_color='white', border_width=2).pack(side='right', padx=10)

# Function to reset progress
def reset_progress():
    drawn_numbers.clear()
    update_bingo_page()

# Function to reset and go back
def reset_and_back():
    reset_progress()
    show_frame(main_frame)
    # lbl.configure(text="Welcome to the STEAM Day Digital Booth!")

# Function to switch frames
def show_frame(frame):
    main_frame.grid_remove()
    rules_frame.grid_remove()
    bingo_frame.grid_remove()
    frame.grid(row=0, column=0, columnspan=2, sticky='nsew')

# Show main frame initially
show_frame(main_frame)

# Start the application
root.mainloop()
