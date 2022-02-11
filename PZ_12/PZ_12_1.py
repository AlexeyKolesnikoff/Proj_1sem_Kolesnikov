from tkinter import*
from tkinter import ttk
root = Tk()
root.geometry('1100x550+40+80')

Label(root, text = 'User login info', font = 'Arial 10 bold').place(x = 50, y = 5)
Label(root, text = 'Username:', font = 'Arial 11').place(x = 45, y = 55)
Entry(root, width = 25, bd = 1).place(x = 130, y = 60)

Label(root, text = 'Email:', font = 'Arial 11').place(x = 45, y = 90)
Entry(root, width = 25, bd = 1).place(x = 115, y = 95)

Label(root, text = 'Password:', font = 'Arial 11').place(x = 45, y = 125)
Entry(root, width = 25, bd = 1).place(x = 130, y = 130)

Label(root, text = 'Data diri', font = 'Arial 10 bold').place(x = 50, y = 157)
Label(root, text = 'Alamat:', font = 'Arial 11').place(x = 45, y = 195)
Entry(root, width = 25, bd = 1).place(x = 130, y = 200)

Label(root, text = 'Targgal lahir:', font = 'Arial 11').place(x = 45, y = 230)
Entry(root, width = 25, bd = 1).place(x = 140, y = 235)

Label(root, text = 'Usia:', font = 'Arial 11').place(x = 45, y = 265)
Entry(root, width = 25, bd = 1).place(x = 130, y = 270)

Label(root, text = 'Jenis kelamin:', font = 'Arial 11').place(x = 45, y = 300)
Radiobutton(text = 'Pria', font = 'Arial 11', value = 0).place(x = 160, y = 300)
Radiobutton(text = 'Wanita', font = 'Arial 11', value = 1).place(x = 222, y = 300)

Label(root, text = 'Saya bersedia mengikuti aruran forum', font = 'Arial 11').place(x = 45, y = 370)
Checkbutton(onvalue = 1, offvalue = 0).place(x = 300, y = 370)
Button(root, text = 'Resel', font = 'Arial 11', bd = 1, width = 5).place(x = 49, y = 415)
Button(root, text = 'submit', font = 'Arial 11', bd = 1, width = 5).place(x = 113, y = 415)

root.mainloop()