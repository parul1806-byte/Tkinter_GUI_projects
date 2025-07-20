# import tkinter
from tkinter import *
import time
# creating the main window
window = Tk()
window.geometry("500x500")
window.title("HABBIT_TRACKER")
window.configure(bg="pink")

#input
lable1 = Label(window,text="DAILY_HABBIT_TRACKER",font=("Impact",20),bg="yellow",fg="black",bd=2)
lable1.pack()


frame1 = Frame(window,bg="yellow",height=200,width=430,relief="solid",bd=2)
frame1.place(x=30,y=60)
lable2 =Label(frame1,text="-----HABITS YOU NEED TO FOLLOW---------")
lable2.place(x=70,y=2)


frame2 = Frame(window,bg='yellow',height=80,width=180,relief='solid',bd=2)
frame2.place(x=30,y=280)

# for assigning date
today = time.strftime("%d:%b:%y")

label3 = Label(frame2,text="--------DATE-----",font=("Brush Script MT",13) )
label3.place(x=3,y=1)
label4 = Label(frame2,text=f"{today}",font=("Impact",10),bg="black",fg="cyan",height=2,width=18,anchor="center")
label4.place(x=20,y=33)
frame3 = Frame(window,bg='yellow', height=80,width=180,relief='solid',bd=2)
frame3.place(x=280,y=280)
label5 =Label(frame3,text="-------TIME--------",font=("Brush Script MT",12) )
label5.place(x=3,y=1)
label6 = Label(frame3, font=("Impact",10),bg="black",fg="cyan",height=2,width=18,anchor="center")
label6.place(x=20,y=33)

label7 = Label(window,font=("Impact",10),bg="yellow",fg="black",bd=2)
label7.place(x=180,y=410)
#function for updating time
def update_time():
    current_time = time.strftime("%I:%M:%S:%p")
    label6.configure(text=current_time)
    window.after(1000, update_time)

#creating checkbutton
habit1 = IntVar()
habit2 = IntVar()
habit3 = IntVar()
habit4 = IntVar()
habit5 = IntVar()
habit6 = IntVar()
habit7 = IntVar()
Checkbutton(frame1,text="drink 4l of water daily".capitalize(),font=("Brush Script MT",12), variable = habit1,height=1,width=30,bd=2).place(x=70,y=40)
Checkbutton(frame1,text="Do light exercise or stretching".capitalize(),font=("Brush Script MT",12), variable=habit2, height=1,width=30).place(x=70,y=65)
Checkbutton(frame1,text="journal for 5 mins ".capitalize(),font=("Brush Script MT",12),height=1,variable=habit3,width=30).place(x=70,y=85)
Checkbutton(frame1,text="Eat balanced meals".capitalize(),font=("Brush Script MT",12),height=1,variable=habit4,width=30).place(x=70,y=105)
Checkbutton(frame1,text="Avoid Junk Food".capitalize(),font=("Brush Script MT",12),height=1,variable=habit5,width=30).place(x=70,y=125)
Checkbutton(frame1,text="Limit Screen Time Before Bed".capitalize(),font=("Brush Script MT",12),variable=habit6,height=1,width=30).place(x=70,y=145)
Checkbutton(frame1,text="Sleep 7–8 hours ".capitalize(),font=("Brush Script MT",12),height=1,variable=habit7,width=30).place(x=70,y=165)


# fun for creating save button
def save_data():
    complete = 0
    if habit1.get() == 1: complete +=1
    if habit2.get() == 1: complete +=1
    if habit3.get()== 1: complete +=1
    if habit4.get() == 1: complete +=1
    if habit5.get() == 1: complete +=1
    if habit6.get() == 1: complete +=1
    if habit7.get() == 1: complete +=1

    if complete>0:
        try:
            with open("streak.txt",'r')as f:
                last_date = f.readline().strip()
                last_streak = int(f.readline())

            if last_date == today:
                streak = last_streak
            else:
                 last_time = time.strptime(last_date, "%d:%b:%Y")
                 today_time = time.strptime(today, "%d:%b:%Y")
                 days_between = (time.mktime(today_time) - time.mktime(last_time)) / (60 * 60 * 24)
            if days_between == 1:
                 streak = last_streak + 1
            else:
                  streak = 1
        except:
                streak = 1


        with open("streak.txt", "w") as file:
             file.write(f"{today}\n{streak}")
             label7.configure(text=f"✅ {complete}/7 Habits done!\n🔥Streak: {streak} days", fg="green")
    else:
        label7.configure(text="⚠️Complete at least 1 habit to track!", fg="red")

Button(window, text="Save Today's Progress", command=save_data, bg="green", fg="white", font=("Arial", 11, "bold")).place(x=150, y=380)

# Result message label

#running the main window
update_time()
window.mainloop()