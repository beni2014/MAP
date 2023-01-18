from tkinter import *

expression = " "
num=" "
def press(num):
    try:
        global expression
        expression = expression + str(num)
        equation.set(expression)

    except:
        equation.set("Avem o eroare")
        expression = ""
def equalpress():
    try:
        global expression
        total=str(eval (expression))
        equation.set(total)
        
    except:
        equation.set(total)
def delete():
    global expression
    expression= expression[:-1]
    equation.set(expression)
def clear ():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="#000000")
    gui.title("Calculator")
    gui.geometry("470x250")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4,ipadx=70)

button1 = Button(gui, text=" 1 ", fg="black", bg="red", command=lambda: press(num=1),height=1,width=7)
button1.grid(row=2,column=0)
button2 = Button(gui, text=" 2 ", fg="black", bg="red", command=lambda: press(num=2),height=1,width=7)
button2.grid(row=2,column=1)
button3 = Button(gui, text=" 3 ", fg="black", bg="red", command=lambda: press(num=3),height=1,width=7)
button3.grid(row=2,column=2)

button4 = Button(gui, text=" 4 ", fg="black", bg="red", command=lambda: press(num=4),height=1,width=7)
button4.grid(row=3,column=0)
button5 = Button(gui, text=" 5 ", fg="black", bg="red", command=lambda: press(num=5),height=1,width=7)
button5.grid(row=3,column=1)
button6 = Button(gui, text=" 6 ", fg="black", bg="red", command=lambda: press(num=6),height=1,width=7)
button6.grid(row=3,column=2)

button7 = Button(gui, text=" 7 ", fg="black", bg="red", command=lambda: press(num=7),height=1,width=7)
button7.grid(row=4,column=0)
button8 = Button(gui, text=" 8 ", fg="black", bg="red", command=lambda: press(num=8),height=1,width=7)
button8.grid(row=4,column=1)
button9 = Button(gui, text=" 9 ", fg="black", bg="red", command=lambda: press(num=9),height=1,width=7)
button9.grid(row=4,column=2)

button0 = Button(gui, text=" 0 ", fg="black", bg="red", command=lambda: press(num=0),height=1,width=7)
button0.grid(row=5,column=1)

plus = Button(gui, text=" + ", fg="black", bg="red", command=lambda: press(num="+"),height=1,width=7)
plus.grid(row=2,column=3)
minu = Button(gui, text=" - ", fg="black",bg="red",command=lambda: press(num="-"),height=1,width=7)
minu.grid(row=3,column=3)
inmu = Button(gui, text=" * ", fg="black",bg="red",command=lambda: press(num="*"),height=1,width=7)
inmu.grid(row=4,column=3)
div = Button(gui, text=" / ", fg="black",bg="red",command=lambda: press(num="/"),height=1,width=7)
div.grid(row=5,column=3)
equal=Button(gui,text=" = ", fg="black", bg="red", command=equalpress,height=1,width=7)
equal.grid(row=6,column=3)
c=Button(gui, text=" C ", fg="black", bg="red", command=clear,height=1,width=7)
c.grid(row=5,column=0)
dele=Button(gui,text=" D ", fg="black", bg="red", command=delete,height=1,width=7)
dele.grid(row=5,column=2)
gui.mainloop()