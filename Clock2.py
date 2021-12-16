import tkinter as tk
import time


def see_date():
    current_time2 = time.strftime("%m/%d/%Y")
    clock2.config(text=current_time2, bg="#101b33", fg="white")
    clock2.after(500,times)


def times():
    current_time1 = time.strftime("%X %p")
    clock1.config(text=current_time1, bg="#101b33", fg="white")
    clock1.after(200,times)


win = tk.Tk()
win.title("Clock")
win.geometry("345x320+1170+470")
win.resizable(0,0)


canvas_width = 424
canvas_height = 390
can1 = tk.Canvas(win, width= canvas_width, height= canvas_height, bg="#101b33", relief="groove", bd=10)
can1.create_text(canvas_width, canvas_height, fill="#13264e")
can1.pack()

clock2 = tk.Label(can1,font="times 20 bold" ,bg="white")
clock2.grid(row=4, column=2, pady=20, padx=20)
# times()


clock1 = tk.Label(can1,font="times 25 bold" ,bg="white")
clock1.grid(row=2, column=2, pady=30, padx=80)
times()

btn_date = tk.Button(can1, text="View Date", font="arial 10 bold", bg="#101b33", fg="white", bd=2, command= see_date)
btn_date.grid(row=6, column=2, pady=8)

digi = tk.Label(can1,text="Digital Clock", font="times 24 bold", bg="#101b33", fg="white")
digi.grid(row=1, column=2)


note1 = tk.Label(can1, text= "  Hours  |  Minutes  |  Seconds ", font="times 15 bold", bg="#101b33", fg="white")
note1.grid(row=3, column=2)

note2 = tk.Label(can1, text= "  Month | Day | Year ", font="times 15 bold", bg="#101b33", fg="white")
note2.grid(row=5, column=2)

win.mainloop()
