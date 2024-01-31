from tkinter import*
window=Tk()

def calculat_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i, 2)

    showlabel.destroy()


result_frame = LabelFrame(window,tet="Result", bg = "gray", font=("Calibri", 12()))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

Showlabel = Label(result_frame,text="Your result will be displayed here", bg = "grey", font=("Calibri", 12), width=55)
Showlabel.place(x=20,y=20)
Showlabel.pack()

