from tkinter import *

root = Tk()
root.title("Sample quiz!")
my_label = Label(root, text="Try this test")
frame1 = LabelFrame(root, text="What is 10 * 10?", padx=40, pady=20)
frame1.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
frame2 = LabelFrame(root, text="What is squareroot of 625?", padx=40, pady=20)
frame2.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
frame3 = LabelFrame(root, text="What is 24 squared?", padx=40, pady=20)
frame3.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
frame4 = LabelFrame(root, text="What is the cuberoot ot 8?", padx=40, pady=20)
frame4.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
frame5 = LabelFrame(root, text="What is 10 + 10?", padx=40, pady=20)
frame5.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
frame6 = LabelFrame(root, text="What is 10 / 10?", padx=40, pady=20)
frame6.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
frame7 = LabelFrame(root, text="What is 4 * 7?", padx=40, pady=20)
frame7.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
frame8 = LabelFrame(root, text="What is 6 * 5?", padx=40, pady=20)
frame8.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
frame9 = LabelFrame(root, text="What is 22 + 23", padx=40, pady=20)
frame9.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
frame0 = LabelFrame(root, text="What is 100 / 20?", padx=40, pady=20)
frame0.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

tup1 = (10, 20, 100, 27)
tup2 = (2, 25, 26, 29)
tup3 = (224, 676, 573, 576)
tup4 = (1, 2, 3, 4)
tup5 = (10, 20, 100, 25)
tup6 = (10, 30, 25, 1)
tup7 = (15, 25, 31, 28)
tup8 = (10, 40, 26, 30)
tup9 = (45, 42, 47, 50)
tup0 = (50, 22, 5, 32)
global store
store = IntVar()

def radio_buttons(tup, frame):
    #store.set(tup[0])
    for num in tup:
        Radiobutton(frame, text=num, variable=store, value=num).pack(anchor=W)

list_frame = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame0]
list_tup = [tup1, tup2, tup3, tup4, tup5, tup6, tup7, tup8, tup9, tup0]
global frame
global answer
frame = list_frame[0]
radio_buttons(tup1, frame)

def calculate_score():
    j = 0
    list_answer = [100, 25, 576, 2, 20, 1, 28, 30, 45, 5]
    for i in range(len(list_frame)):
        if list_frame[i].winfo_ismapped() and store.get() == list_answer[i]:
            j += 1
    return j

def forward(question_num):
    global next_button
    #global back_button
    global status_bar
    global frame
    global answer
    global j
    if question_num <= len(list_tup):
        frame.grid_forget()
        frame = list_frame[question_num - 1]
        radio_buttons(list_tup[question_num - 1], frame)
        next_button = Button(root, text="NEXT", command=lambda: forward(question_num + 1))
        status_bar = Label(root, text="Question " + str(question_num) + " of " + str(len(list_tup)), anchor=W, relief=SUNKEN, bd=1)
        #back_button = Button(root, text="BACK", command=lambda: back(question_num - 1))
        status_bar.grid(row=2, column=0)
        next_button.grid(row=2, column=2, padx=10, pady=10)
        answer = store.get()
        
    if question_num == len(list_tup) + 1:
        j = calculate_score()
        frame.grid_forget()
        label1 = Label(root, text="You have " + str(j) + " points")
        label1.grid(row=1, column=1)
        next_button = Button(root, text="NEXT", state=DISABLED)
        status_bar = Label(root, text="Questions done", anchor=W, relief=SUNKEN, bd=1)
    #back_button.grid(row=2, column=0, padx=10, pady=10)
        status_bar.grid(row=2, column=0)
        next_button.grid(row=2, column=2, padx=10, pady=10)
"""def back(question_num):
    global next_button
    global back_button
    global frame
    frame = list_frame[question_num - 1]
    radio_buttons(list_tup[question_num - 1], frame)
    next_button = Button(root, text="NEXT", command=lambda: forward(question_num - 1))
    back_button = Button(root, text="BACK", command=lambda: back(question_num + 1))

    if question_num == 1:
        back_button = Button(root, text="BACK", state=DISABLED)

    back_button.grid(row=2, column=0, padx=10, pady=10)
    next_button.grid(row=2, column=2, padx=10, pady=10)
"""
next_button = Button(root, text="NEXT", command=lambda: forward(2))
exit_button = Button(root, text="QUIT", command=root.quit)
status_bar = Label(root, text="Question 1 of " + str(len(list_tup)), anchor=W, relief=SUNKEN, bd=1)
#back_button = Button(root, text="BACK", command=back, state=DISABLED)

my_label.grid(row=0, column=0)
#back_button.grid(row=2, column=0, padx=10, pady=10)
status_bar.grid(row=2, column=0)
exit_button.grid(row=2, column=1, padx=10, pady=10)
next_button.grid(row=2, column=2, padx=10, pady=10)


root.mainloop(
