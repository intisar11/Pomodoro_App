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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    label.config(text= "Timer", font=(FONT_NAME, 40, "italic"), fg=GREEN, bg= YELLOW)
    check_mark.config(bg= YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", font=(FONT_NAME, 40, "bold"), fg=RED, bg=YELLOW)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", font=(FONT_NAME, 40, "bold"), fg= PINK, bg=YELLOW)

    else:
        count_down(work_sec)
        label.config(text="Work", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg= YELLOW)






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/ 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _  in range(work_session):
            marks += '✅'
        check_mark.config(text=marks)





# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Pomodoro Timer")
window.config(padx= 100, pady= 50, bg=YELLOW)



photo = PhotoImage(file="tomato.png")


canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness= 0)
canvas.create_image(100, 112, image= photo)
timer_text = canvas.create_text(103, 130, text= "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


label = Label(text= "Timer", font=(FONT_NAME, 40, "italic"), fg=GREEN, bg= YELLOW)
label.grid(column= 2, row=1)


check_mark = Label(bg= YELLOW)
check_mark.grid(column= 2, row= 5)

Start_button = Button(text="Start", command= start_timer)
Start_button.grid(column=1, row=4)

reset_button = Button(text="Reset", command= reset_timer)
reset_button.grid(column= 3, row=4)



window.mainloop()