from customtkinter import *
from PIL import Image, ImageTk
from tkfontawesome import icon_to_image
import emoji
import re

# Initialize main window
root = CTk()
root.title("AI Bingo")
root.geometry('600x400')
root.minsize(500, 350)
set_appearance_mode("dark")

# Configure grid for main window
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Load icons
send_icon_image = icon_to_image("paper-plane", fill="#EA6E08", scale_to_width=24)
quit_icon_image = icon_to_image("xmark", fill="#EA6E08", scale_to_width=24)
rules_icon_image = icon_to_image("book", fill="#EA6E08", scale_to_width=24)
back_icon_image = icon_to_image("arrow-left", fill="#EA6E08", scale_to_width=24)
reset_icon_image = icon_to_image("rotate-right", fill="#EA6E08", scale_to_width=24)

# Track drawn numbers
drawn_numbers = []

# Tasks dictionary with emojis (expanded to 15 tasks)
tasks = {
    '1': {'task': 'Autocorrect spelling', 'emoji': ':writing_hand:'},
    '2': {'task': 'Guess the drawing', 'emoji': ':artist_palette:'},
    '3': {'task': 'Guess the animal sound', 'emoji': ':paw_prints:'},
    '4': {'task': 'Spot a smile in a photo', 'emoji': ':smiling_face:'},
    '5': {'task': 'Pictures of faces', 'emoji': ':smiling_face:'},
    '6': {'task': 'Pick a bedtime story', 'emoji': ':books:'},
    '7': {'task': 'Identify a song', 'emoji': ':musical_note:'},
    '8': {'task': 'Detect objects in a picture', 'emoji': ':camera:'},
    '9': {'task': 'Translate a phrase', 'emoji': ':speech_balloon:'},
    '10': {'task': 'Guess the emoji', 'emoji': ':grinning_face:'},
    '11': {'task': 'Recognize a flower type', 'emoji': ':flower_playing_cards:'},
    '12': {'task': 'Identify a car model', 'emoji': ':car:'},
    '13': {'task': 'Answer a math question', 'emoji': ':abacus:'},
    '14': {'task': 'Spot a landmark', 'emoji': ':world_map:'},
    '15': {'task': 'Describe a weather scene', 'emoji': ':cloud:'}
}

# Function to convert non-BMP emojis to surrogate pairs for Tkinter
_nonbmp = re.compile(r'[\U00010000-\U0010FFFF]')
def with_surrogates(text):
    def _surrogatepair(match):
        char = match.group()
        assert ord(char) > 0xffff
        encoded = char.encode('utf-16-le')
        return (
            chr(int.from_bytes(encoded[:2], 'little')) +
            chr(int.from_bytes(encoded[2:], 'little'))
        )
    return _nonbmp.sub(_surrogatepair, text)

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
lbl = CTkLabel(main_frame, text='Ready to play?', font=("Arial", 24), text_color="#FCDDA4")
lbl.grid(row=0, column=0, columnspan=3, pady=(20, 10), sticky='n')

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
                      font=("Arial", 18))
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
                font=("Arial", 18))
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
                     font=("Arial", 18))
quit_btn.grid(row=1, column=2, padx=10, pady=10, sticky='w')

# Create rules frame
rules_frame = CTkFrame(root, fg_color="transparent")

# Configure grid for rules frame
rules_frame.grid_rowconfigure(0, weight=1)
rules_frame.grid_rowconfigure(1, weight=1)
rules_frame.grid_columnconfigure(0, weight=1)

# Rules frame widgets
rules_label = CTkLabel(rules_frame, text="AI Bingo Rules\n\n1. Click 'Play' to go to the bingo page.\n2. Select a number from 1 to 15 on the right side.\n3. View drawn numbers, tasks, and emojis on the left.\n4. Numbers in the pile on the right are shaded when drawn.\n5. Match emojis to your bingo card!\n6. Have fun and explore AI challenges!",
                       font=("Arial", 16), text_color="#FCDDA4", justify="center")
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
bingo_frame.grid_columnconfigure(0, weight=1)  # Left side
bingo_frame.grid_columnconfigure(1, weight=1)  # Right side

# Bingo frame header (Back, Rules, Reset buttons)
header_frame = CTkFrame(bingo_frame, fg_color="transparent")
header_frame.grid(row=0, column=0, columnspan=2, sticky='ew')
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

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
                           font=("Arial", 20))
back_bingo_btn.grid(row=0, column=0, padx=5, pady=5, sticky='w')

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
                            font=("Arial", 20))
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
                      font=("Arial", 20))
reset_btn.grid(row=0, column=2, padx=5, pady=5, sticky='e')

# Left side: Drawn numbers and tasks
left_frame = CTkFrame(bingo_frame, fg_color="#2B2B2B")
left_frame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
left_frame.grid_columnconfigure(0, weight=1)
left_frame.grid_rowconfigure(1, weight=1)

drawn_label = CTkLabel(left_frame, text="Drawn Numbers", font=("Arial", 28), text_color="#FCDDA4")
drawn_label.grid(row=0, column=0, pady=(5, 5), sticky='n')
drawn_text = CTkTextbox(left_frame, font=("Arial", 28), text_color="#AEAEAE", state='disabled')
drawn_text.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

# Right side: Number pile (5x3 grid for 15 numbers)
right_frame = CTkFrame(bingo_frame, fg_color="#2B2B2B")
right_frame.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')
for i in range(3):
    right_frame.grid_columnconfigure(i, weight=1)
for i in range(5):
    right_frame.grid_rowconfigure(i, weight=1)

number_buttons = {}
for i in range(1, 16):
    row = (i-1) // 3
    col = (i-1) % 3
    num = str(i)
    btn = CTkButton(right_frame,
                    text=num,
                    command=lambda n=num: draw_number(n),
                    fg_color='orange',
                    hover_color="#EAAC79",
                    border_color='white',
                    border_width=2,
                    width=120,
                    height=120,
                    font=("Arial", 32))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
    number_buttons[num] = btn

# Function to draw a number
def draw_number(number):
    if number not in drawn_numbers:
        drawn_numbers.append(number)
        update_bingo_page()

# Function to update bingo page
def update_bingo_page():
    # Update drawn numbers text
    drawn_text.configure(state='normal')
    drawn_text.delete("1.0", "end")
    for num in drawn_numbers:
        task = tasks.get(num, {'task': 'Unknown task', 'emoji': ''})
        emoji_text = emoji.emojize(task['emoji'])
        emoji_text = with_surrogates(emoji_text)
        drawn_text.insert("end", f"Number {num}: {task['task']} {emoji_text}\n")
    drawn_text.configure(state='disabled')
    # Update number buttons
    for num, btn in number_buttons.items():
        if num in drawn_numbers:
            btn.configure(fg_color="#8B5A2B", hover_color="#8B5A2B", state='disabled')
        else:
            btn.configure(fg_color='orange', hover_color="#EAAC79", state='normal')

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
    lbl.configure(text="Ready to play?")

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
