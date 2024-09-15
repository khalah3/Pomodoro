from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def timer_reset():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00" )
    label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    if reps % 8 ==0:
        countdown(LONG_BREAK_MIN*60)
        label.config(text='Break',fg=RED)
    if reps % 2 ==0:
        countdown(SHORT_BREAK_MIN*60)
        label.config(text='Break', fg=PINK)
    else:
        countdown(WORK_MIN*60)
        label.config(text='Work', fg=GREEN)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(Count):

    count_min = math.floor(Count/60)
    count_sec = Count % 60
    if count_sec==0:
        count_sec="00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if Count>0:
        global timer
        timer = window.after(4,countdown,Count-1)
    else:
        start_timer()
        mark = ""
        work_sessions=math.floor(reps / 2)
        for _ in range(work_sessions):
            mark+='✔'
        check_marks.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodora")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00", fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)



label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,50), highlightthickness=0)
label.grid(row=0,column=1)

button1 = Button(text="Start", highlightthickness=0, command=start_timer)
button2 = Button(text="Reset", highlightthickness=0, command=timer_reset)

button1.grid(row=2, column=0)
button2.grid(row=2, column=2)

check_marks=Label(bg=YELLOW,fg=GREEN)
check_marks.grid(row=2, column=1)



window.mainloop()