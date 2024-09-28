import tkinter as tk
import customtkinter as ctk
import time
from plyer import notification
from PIL import Image
import json
import widgets

tasks = []


def send_notification(_title,_message,_app_icon = None,_timeout = 10):
    notification.notify(
        title = _title,
        message = _message,
        app_icon = _app_icon,
        timeout = _timeout
    )








app = ctk.CTk()
app.geometry("800x500")
app.title("Prask")
app.minsize(800,500)
app.maxsize(800,500)


tasklist = widgets.ScrollableCheckboxFrame(app,title="Tasks",values=tasks)

title = ctk.CTkEntry(app, placeholder_text="Title")
objetive = ctk.CTkEntry(app, placeholder_text="Objetive")
thour = widgets.FloatSpinbox(app,width=150,step_size=1,max_size=24)
thourtext = ctk.CTkLabel(app,text="Hour:")
tmin = widgets.FloatSpinbox(app,width=150,step_size=1,max_size=60)
tmintext = ctk.CTkLabel(app,text="Minutes:")
tsec = widgets.FloatSpinbox(app,width=150,step_size=1,max_size=60)
tsectext = ctk.CTkLabel(app,text="Seconds:")

tasklist.grid(row=0,column=5,padx=100,pady=10)

thourtext.grid(row=0,column=2,padx=10,pady=10)
tmintext.grid(row=1,column=2,padx=10,pady=10)
tsectext.grid(row=2,column=2,padx=10,pady=10)


thour.grid(row=0,column=3,padx=10,pady=10)
tmin.grid(row=1,column=3,padx=10,pady=10)
tsec.grid(row=2,column=3,padx=10,pady=10)
title.grid(row=0,column=4,padx=10,pady=10)
objetive.grid(row=1,column=4,padx=10,pady=10)

def add_task():
    global tasklist
    
    tasks.append({
        'time': f"{int(thour.get())}:{int(tmin.get())}:{int(tsec.get())}",
        'title': title.get(),
        'objetive': objetive.get()
    })
    

    tasklist.destroy()
    
    tasklist = widgets.ScrollableCheckboxFrame(app, title="Tasks", values=tasks)
    tasklist.grid(row=0,column=5,padx=100,pady=10)

button = ctk.CTkButton(app, text="Add Task", command=add_task)
button.grid(row=2,column=4,padx=10,pady=10)

def check_tasks():
    actualtime = time.strftime("%H:%M:%S",time.localtime())

    for i in tasks:
        task_time = tasks[i]['time']

        if actualtime == task_time:
            send_notification(tasks[i]['title'],tasks[i]['objetive'])
    app.after(1000, check_tasks)

check_tasks()

app.mainloop()
