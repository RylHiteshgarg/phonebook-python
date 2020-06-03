
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Phone Book")
root.geometry("900x600")

tframe = Frame(root)
tframe.pack(side = TOP)

v0 = StringVar()
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
v7 = StringVar()
v8 = StringVar()
id_no = StringVar()
s0 = StringVar()


def save_in_file():
    global mlist

    global a0, a1, a2, a3, a4

    a0 = id_no.get()
    a1 = v5.get()
    a2 = v6.get()
    a3 = v7.get()
    a4 = v8.get()

    mlist = [a0,a1,a2,a3,a4]
    with open("db.txt", 'w') as f:
        for i in mlist:
            f.write(i + '|')
        f.write('\n')


def save_in_file2():
    global nlist
    nlist = []
    m = v0.get()
    a = v1.get()
    b = v2.get()
    c = v3.get()
    d = v4.get()

    nlist = [m, a, b, c, d]

    with open("db.txt", 'a+') as f:
        for i in nlist:
            f.write(i + '|')
        f.write('\n')


def add_number():

    global window2
    window2 = Toplevel(root)
    window2.geometry("900x600")
    window2.title("Add Contact")
    root.withdraw()
    btn4 = Button(window2, text="Back to the main menu", font=("arial", 8, "bold"), width=20, command=add_back)
    btn4.pack(side = LEFT)

    ttframe = Frame(window2)
    ttframe.pack(side = TOP)
    bbframe = Frame(window2)
    bbframe.pack(side = TOP)

    lbl = Label(ttframe, text="Contact ID", fg="black", font=("arial", 12, "bold"))
    lbl.grid(row=0, column=0, sticky=E)
    entry = Entry(ttframe, bd=7, textvariable=v0)
    entry.grid(row=0, column=1, sticky=W)

    lbl2 = Label(ttframe, text="First Name", fg="black", font=("arial", 12, "bold"))
    lbl2.grid(row = 1,column = 0,sticky = E)
    entry1 = Entry(ttframe, bd=7,textvariable = v1)
    entry1.grid(row = 1,column = 1,sticky = W)

    lbl3 = Label(ttframe, text="Last Name", fg="black", font=("arial", 12, "bold"))
    lbl3.grid(row = 2,column = 0,sticky = E)
    entry2 = Entry(ttframe, bd=7,textvariable = v2)
    entry2.grid(row = 2,column = 1,sticky = W)

    lbl4 = Label(ttframe, text="Phone Number", fg="black", font=("arial", 12, "bold"))
    lbl4.grid(row = 3,column = 0,sticky = E)
    entry3 = Entry(ttframe, bd=7,width = 25,textvariable = v3)
    entry3.grid(row = 3,column = 1)

    lbl5 = Label(ttframe, text="Address", fg="black", font=("arial", 12, "bold"))
    lbl5.grid(row = 4,column = 0,sticky = E)
    entry4 = Entry(ttframe, bd=7,width = 25,textvariable = v4)
    entry4.grid(row = 4,column = 1)

    btns = Button(bbframe,text = "Save info",fg = 'red',font = ("arial",12,"bold"),command = save_in_file2)
    btns.pack(side = LEFT)


def add_back():

    window2.withdraw()
    root.deiconify()


def edit_number():

    global window3
    window3 = Toplevel(root)
    window3.geometry("900x600")
    window3.title("Edit Contact")
    tttframe = Frame(window3)
    tttframe.pack(side = TOP)
    root.withdraw()
    btn5 = Button(window3, text="Back to the main menu", font=("arial", 8, "bold"), width=20, command=edit_back)
    btn5.pack(side = LEFT)

    lbl01 = Label(tttframe, text="Enter the contact ID you wish to edit",fg="black", font=("arial", 12, "bold"))
    lbl01.grid(row=0, column=0, sticky=E)
    entry01 = Entry(tttframe, bd=7, textvariable = id_no)
    entry01.grid(row=0, column=1, sticky=W)

    def edit_check():

            global a0, a1, a2, a3, a4,x,v5,v6,v7,v8
            with open("db.txt", 'r') as f:

                y = f.readlines()

                x = y[0].split("|")

                a0 = x[0]
                a1 = x[1]
                a2 = x[2]
                a3 = x[3]
                a4 = x[4]

                if id_no.get() == a0 or id_no.get() == nlist[0]:

                    lbl10 = Label(tttframe, text="First Name", fg="black", font=("arial", 12, "bold"))
                    lbl10.grid(row=2, column=0, sticky=E)
                    entry10 = Entry(tttframe, bd=7, text=a1,textvariable = v5)
                    entry10.grid(row=2, column=1, sticky=W)

                    lbl11 = Label(tttframe, text="Last Name", fg="black", font=("arial", 12, "bold"))
                    lbl11.grid(row=3, column=0, sticky=E)
                    entry11 = Entry(tttframe, bd=7, text=a2,textvariable = v6)
                    entry11.grid(row=3, column=1, sticky=W)

                    lbl13 = Label(tttframe, text="Phone Number", fg="black", font=("arial", 12, "bold"))
                    lbl13.grid(row=4, column=0, sticky=E)
                    entry13 = Entry(tttframe, bd=7, text=a3,textvariable = v7)
                    entry13.grid(row=4, column=1, sticky=W)

                    lbl14 = Label(tttframe, text="Address", fg="black", font=("arial", 12, "bold"))
                    lbl14.grid(row=5, column=0, sticky=E)
                    entry14 = Entry(tttframe, bd=7, text=a4,textvariable = v8)
                    entry14.grid(row=5, column=1, sticky=W)

    btns = Button(tttframe,text = "Click here to save your edit", command=save_in_file)
    btns.grid(row = 5,column = 8)

    btncheck = Button(window3, text="Click here to edit your contact", command=edit_check)
    btncheck.pack(side=TOP)

    def display():

        global a0, a1, a2, a3, a4,x

        with open("db.txt", 'r') as f:
            z = f.readlines()
            x = z[0].split("|")
            a0 = x[0]
            a1 = x[1]
            a2 = x[2]
            a3 = x[3]
            a4 = x[4]



        window3.withdraw()
        window99 = Toplevel(root)
        window99.geometry("900x600")
        window99.title("Display Saved Contacts")
        frame99 = Frame(window99)
        frame99.pack()

        lbl03 = Label(frame99, text="Contact ID", fg="black", font=("arial", 12, "bold"))
        lbl03.grid(row=2, column=0, sticky=E)
        lbl04 = Label(frame99, bd=7, text=a0)
        lbl04.grid(row=2, column=1, sticky=W)

        lbl03 = Label(frame99, text="First Name", fg="black", font=("arial", 12, "bold"))
        lbl03.grid(row=3, column=0, sticky=E)
        lbl04 = Label(frame99, bd=7, text=a1)
        lbl04.grid(row=3, column=1, sticky=W)

        lbl05 = Label(frame99, text="Last Name", fg="black", font=("arial", 12, "bold"))
        lbl05.grid(row=4, column=0, sticky=E)
        lbl06 = Label(frame99, bd=7, text=a2)
        lbl06.grid(row=4, column=1, sticky=W)

        lbl07 = Label(frame99, text="Phone Number", fg="black", font=("arial", 12, "bold"))
        lbl07.grid(row=5, column=0, sticky=E)
        lbl08 = Label(frame99, bd=7, text=a3)
        lbl08.grid(row=5, column=1, sticky=W)

        lbl09 = Label(frame99, text="Address", fg="black", font=("arial", 12, "bold"))
        lbl09.grid(row=6, column=0, sticky=E)
        lbl10 = Label(frame99, bd=7, text=a4)
        lbl10.grid(row=6, column=1, sticky=W)

        buttonq = Button(frame99,text = "Quit",fg = 'red',command = root.destroy)
        buttonq.grid(row = 8,column = 4)

        def edit_back2():

            window99.withdraw()
            window3.deiconify()
        buttonback = Button(frame99,text = "Back",fg = 'red',command = edit_back2)
        buttonback.grid(row = 8,column = 2)

    display = Button(window3, text="Click here to display saved contacts", command=display)
    display.pack()


def edit_back():

    window3.withdraw()
    root.deiconify()


def delete_number():

    global window4
    window4 = Toplevel(root)
    window4.geometry("900x600")
    window4.title("Delete Contact")
    root.withdraw()
    btn6 = Button(window4, text="Back to the main menu", font=("arial", 8, "bold"), width=20, command=delete_back)
    btn6.pack(side=LEFT)

    def deleted():

        with open("db.txt", 'w') as f:
            f.writelines("")

        messagebox.showinfo("Info", "Contacts Deleted!!")

    btnd = Button(window4, text="Click here to delete all the contacts", font=("arial", 8, "bold"),
                  command = deleted)

    btnd.pack(side=LEFT)


def delete_back():

    window4.withdraw()
    root.deiconify()


def search_number():

    global window5
    window5 = Toplevel(root)
    framez = Frame(window5)
    framez.pack(side = RIGHT)
    window5.geometry("900x600")
    window5.title("Search Contact")
    root.withdraw()
    btn66 = Button(window5, text="Back to the main menu", font=("arial", 8, "bold"), width=20, command=search_back)
    btn66.pack(side=LEFT)

    def searched():

        if s0.get() == a0 or s0.get() == nlist[0]:

            messagebox.showinfo("Info", "Contact Found")

        else:

            messagebox.showinfo("Info","Contact Not Found")

    btn98 = Button(window5, text="search for contact", font=("arial", 8, "bold"), command=searched)
    btn98.pack(side=LEFT)
    lbl77 = Label(framez, text="Enter the id of contact first", font=("arial", 8, "bold"))
    lbl77.pack(side=LEFT)

    entry68 = Entry(framez,textvariable = s0, font=("arial", 8, "bold"))
    entry68.pack(side=LEFT)


def search_back():

    window5.withdraw()
    root.deiconify()


lbl0 = Label(tframe,text = "Phone Book App",font = ("arial",20,"bold"),fg = "steel blue")
lbl0.pack(side = TOP)

lframe = Frame(root)
lframe.pack(side = LEFT)

bframe = Frame(root)
bframe.pack(side = BOTTOM)

lbl1 = Label(lframe,text = "Choose one of those options",font = ("arial",15,"bold"),fg = "red")
lbl1.grid(row = 0,column = 0)


btn1 = Button(lframe,text = "Add Contact",font = ("arial",12,"bold"),width = 12,command = add_number)
btn1.grid(row = 10,column = 4)

btn2 = Button(lframe,text = "Edit Contact",font = ("arial",12,"bold"),width = 12,command = edit_number)
btn2.grid(row = 10,column = 6)

btn3 = Button(lframe,text = "Delete Contact",font = ("arial",12,"bold"),width = 12,command = delete_number)
btn3.grid(row = 10,column = 8)

btn33 = Button(lframe,text = "Search Contact",font = ("arial",12,"bold"),width = 12,command = search_number)
btn33.grid(row = 10,column = 10)

btn7 = Button(bframe,text = "Quit",font = ("arial",15,"bold"),width = 18,fg = "red",command = root.destroy)
btn7.pack(side = LEFT)

root.mainloop()