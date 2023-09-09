# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:27:47 2023

@author: XE
"""

from tkinter import *

class Sezar(Frame):
    LETTERSrus = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window

        Label(window, text="Введите текст: ", relief=GROOVE, width=20).place(x=20, y=30)
        self.Ent1 = Entry(window, width=30)
        self.Ent1.place(x=170, y=30)

        Label(window, text="Введите шаг: ", relief=GROOVE, width=20).place(x=20, y=90)
        self.Ent2 = Entry(window, width=30)
        self.Ent2.place(x=170, y=90)

        Button(window, text="Шифровка", relief=GROOVE, font="bold", command=self.Encrypt).place(x=30, y=150)
        Button(window, text="Расшифровка", relief=GROOVE, font="bold", command=self.Decrypt).place(x=200, y=150)

        self.RESULT = Entry(window, width=30)
        self.RESULT.place(x=170, y=200)
     
    def Encrypt(self):
        key = int(self.Ent2.get())
        length = len(self.LETTERSrus)

        translation = ''

        for char in self.Ent1.get():
            if char.lower() in self.LETTERSrus:
                sayı = self.LETTERSrus.find(char.lower())
                sayı = (sayı + key) % length
                translation += self.LETTERSrus[sayı]
            else:
                translation += char

        self.RESULT.delete(0, END)
        self.RESULT.insert(0, translation)

    def Decrypt(self):
        key = int(self.Ent2.get())
        length = len(self.LETTERSrus)

        translation = ''

        for char in self.Ent1.get():
            if char.lower() in self.LETTERSrus:
                sayı = self.LETTERSrus.find(char.lower())
                sayı = (sayı - key) % length
                translation += self.LETTERSrus[sayı]
            else:
                translation += char

        self.RESULT.delete(0, END)
        self.RESULT.insert(0, translation)

if __name__ == "__main__":
    root = Tk()
    root.title("Шифр Цезаря")
    root.geometry("400x300+50+50")
    Sezar(root).pack(side="top", fill="both")
    root.mainloop()