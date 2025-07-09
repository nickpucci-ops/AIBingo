from customtkinter import *

root = CTk()
root.title('AI Bingo')
root.geometry('350x200')

# menu = CTkOptionMenu(root)
# item = CTkOptionMenu(menu)
# item.add_command(label='New')
# menu.add_cascade(label='File', menu=item)
# root.config(menu=menu)


lbl = CTkLabel(root, text = 'Ready to play?')
lbl.grid()

txt = CTkEntry(root, width=10)
txt.grid(column=1, row = 0)

def clicked():
    lottoball = txt.get()
    tasks = {
        '1': 'Autocorrect spelling',
        '2': 'Guess the drawing',
        '3': 'Guess the animal sound',
        '4': 'Spot a smile in a photo',
        '5': 'Pictures of faces', 
        '6': 'Pick a bedtime story'
    }
    task = tasks[lottoball]
    res = "Lotto Ball " + lottoball + "\n Task: \n"
    lbl.configure(text = res + task)

btn = CTkButton(master=root, text = 'Play', fg_color = 'orange', command = clicked)
btn.place(relx=0.5, rely=0.5, anchor='center')


root.mainloop()
