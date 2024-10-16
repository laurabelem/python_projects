from tkinter import *
from tkinter import ttk

colour1 = "#0a0a0a"  # black
colour2 = "#fffcfc"  # white
colour3 = "#1f1a4f"  # blue
colour4 = "#c9c9c9"  # grey
colour5 = "#f0b14d"  # orange

window = Tk()
window.title("Simple Calculator")
window.geometry("240x320")


frame_display = Frame(window, width=240, height=60, bg=colour3)
frame_display.grid(row=0, column=0)

frame_body = Frame(window, width=240, height=290, bg=colour2)
frame_body.grid(row=1, column=0)

b_1 = Button(frame_body, text="C", width=11, height=2, bg=colour4,
             font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_body, text="%", width=5, height=2, bg=colour4,
             font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)

b_3 = Button(frame_body, text="/", width=5, height=2, bg=colour5,
             font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=0)

b_4 = Button(frame_body, text="7", width=5, height=2, bg=colour4,
             font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(frame_body, text="8", width=5, height=2, bg=colour4,
             font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=52)

b_6 = Button(frame_body, text="9", width=5, height=2, bg=colour4,
             font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=52)

b_7 = Button(frame_body, text="*", width=5, height=2, bg=colour5,
             font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=180, y=52)

b_8 = Button(frame_body, text="4", width=5, height=2, bg=colour4,
             font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)

b_9 = Button(frame_body, text="5", width=5, height=2, bg=colour4,
             font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=104)

b_10 = Button(frame_body, text="6", width=5, height=2, bg=colour4,
              font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=104)

b_11 = Button(frame_body, text="-", width=5, height=2, bg=colour5,
              font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=180, y=104)

b_12 = Button(frame_body, text="1", width=5, height=2, bg=colour4,
              font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13 = Button(frame_body, text="2", width=5, height=2, bg=colour4,
              font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=156)

b_14 = Button(frame_body, text="3", width=5, height=2, bg=colour4,
              font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=156)

b_15 = Button(frame_body, text="+", width=5, height=2, bg=colour5,
              font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=180, y=156)

b_16 = Button(frame_body, text="0", width=11, height=2, bg=colour4,
              font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)

b_17 = Button(frame_body, text=".", width=5, height=2, bg=colour4,
              font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x=120, y=208)

b_18 = Button(frame_body, text="=", width=5, height=2, bg=colour5,
              font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_18.place(x=180, y=208)
window.mainloop()
