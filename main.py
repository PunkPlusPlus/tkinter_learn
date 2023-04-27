import os
from tkinter import *

from tkinter.ttk import Combobox
import requests
from tkinter.ttk import Checkbutton


def clicked():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    data = response.json()
    title = f'''
    {data['title']}
    ----------------
    '''
    lbl.configure(text=title)

    lbl2 = Label(window, text=data['body'], font=("Arial", 16))
    lbl2.grid(column=0, row=2)
    btn.grid(column=0, row=19)


def clicked2():
    name = os.getlogin()
    lbl.configure(text=name)


# def set_combo():
#     combo = Combobox(window)
#     combo['values'] = (1, 2, 3, 4, 5, "Текст")
#     combo.current(1)  # установите вариант по умолчанию
#     combo.grid(column=0, row=0)

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('720x480')
lbl = Label(window, text="", font=("Arial Bold", 18))
lbl.grid(column=0, row=0)
btn = Button(window, text="Не нажимать!", command=clicked)
btn.grid(column=2, row=0)


window.mainloop()

