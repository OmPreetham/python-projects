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
reps = 0
work_reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_canvas, text="00:00")
    checkmark.config(text="")
    timer_label.config(text="TIMER", fg="GREEN")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global work_reps
    reps += 1
    if reps in [1, 3, 5, 7]:
        count_down(WORK_MIN * 60)
        timer_label.config(text="WORK", fg="GREEN")
        work_reps += 1
    elif reps in (2, 4, 6):
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="SHORT BREAK", fg="PINK")
        checkmark.config(text=f"{'✔' * work_reps}")
    elif reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="LONG BREAK", fg="RED")
        checkmark.config(text=f"{'✔' * work_reps}")
    else:
        reset_timer()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_canvas, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_canvas = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(text="", fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()
