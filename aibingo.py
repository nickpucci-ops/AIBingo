from tkinter import *

root = Tk()
root.title('AI Bingo')
root.geometry('350x200')


lbl = Label(root, text = 'Ready to play?')
lbl.grid()

txt = Entry(root, width=10)
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

btn = Button(root, text = 'Click me', fg = 'orange', command = clicked)
btn.grid(column = 2, row = 0)


root.mainloop()
