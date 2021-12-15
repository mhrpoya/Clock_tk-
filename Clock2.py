import tkinter as tk
import time


def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time, bg="#ffffff", fg="#252c41")
    clock.after(200,times)


win = tk.Tk()
win.title("Clock")
win.geometry("347x215+600+250")
win.resizable(0,0)
win.config(bg="#394465")
clock = tk.Label(win,font=("times",30,"bold"),bg="white")
clock.grid(row=2,column=2,pady=50,padx=95)
times()

digi = tk.Label(win,text="Digital Clock", font="times 24 bold", bg="white", fg="#252c41")
digi.grid(row=0,column=2)


nota= tk.Label(win, text="Hours | Minutes | Seconds", font="times 13 bold")

nota.grid(row=3,column=2)

win.mainloop()
