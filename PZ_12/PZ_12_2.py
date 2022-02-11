from tkinter import*

def sr(event):
    a = int(num1.get())
    b = int(num2.get())
    c = int(num3.get())
    if (a != 0) and (a + b == 0):
        stroka['text'] = 'Есть пара противоположных чисел'
    elif (a != 0) and (a + c == 0):
        stroka['text'] = 'Есть пара противоположных чисел'
    elif (b != 0) and (b + c == 0):
        stroka['text'] = 'Есть пара противоположных чисел'
    else:
        stroka['text'] = 'Нет пары противоположных чисел'

root = Tk()
root.title('Поиск пары проивоположных чисел')
root.geometry('350x150+40+80')

Label(text = 'Введите первое число: ').grid(row = 1, column = 0)
num1 = Entry()
num1.grid(row = 1, column = 1)

Label(text = 'Введите второе число: ').grid(row = 2, column = 0)
num2 = Entry()
num2.grid(row = 2, column = 1)

Label(text = 'Введите третье число: ').grid(row = 3, column = 0)
num3 = Entry()
num3.grid(row = 3, column = 1)

knopka = Button(text = 'Результат')
knopka.grid(row = 4, column = 1)

stroka = Label()
stroka.grid(row = 5, column = 1)

knopka.bind('<Button-1>', sr)

root.mainloop()