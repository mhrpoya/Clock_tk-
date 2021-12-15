import tkinter as tk
import time


def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time, bg="#101b33", fg="white")
    clock.after(200,times)


win = tk.Tk()
win.title("Clock")
win.geometry("347x220+600+250")
win.resizable(0,0)


canvas_width = 347
canvas_height = 220
can1 = tk.Canvas(win, width= canvas_width, height= canvas_height, bg="#13254e", relief="groove", bd=5)
can1.create_text(274, 215, fill="#13264e")
can1.pack()


clock = tk.Label(can1,font="times 30 bold" ,bg="white")
clock.grid(row=2,column=2,pady=50,padx=95)
times()

digi = tk.Label(can1,text="Digital Clock", font="times 24 bold", bg="#101b33", fg="white")
digi.grid(row=1,column=2)


nota= tk.Label(can1, text= "  Hours  |   Minutes  |  Seconds ", font="times 15 bold", bg="#101b33", fg="white")
nota.grid(row=3,column=2)

win.mainloop()
