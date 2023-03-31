import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
text="✔"
reps=1
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="Timer")
    global reps
    reps=1
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec=WORK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    long_breaks=LONG_BREAK_MIN*60
    if reps%2!=0:
        count_down(WORK_MIN*60)
        label.config(text="Work",fg=GREEN)
    elif reps%8==0:
        count_down(LONG_BREAK_MIN*60)
        label.config(text="Long break",fg=PINK)
    else:
        count_down(SHORT_BREAK_MIN*60)
        label.config(text="short break",fg=RED)
    reps+=1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
# while(true):
#     time.sleep(1)
#     counter-=1
# cannot use it because of mainloop used in tkinteer
def count_down(count):
    count_min=math.floor(count/60)
    count_sec =count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        time.sleep(1)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)



canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

button=Button(text="Start",command=start_timer)
button.grid(column=0,row=2)

button=Button(text="Reset",command=reset_timer)
button.grid(column=2,row=2)
label=Label(text="Timer",font=(FONT_NAME,34,"bold"),fg=GREEN,bg=YELLOW)
label.grid(column=1,row=0)



window.mainloop()