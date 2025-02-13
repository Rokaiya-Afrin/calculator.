from tkinter import Tk, Entry, Button, StringVar
import math
class Calculator:
    def __init__(self, master):
        master.title('Calculator')
        master.geometry('357x490+0+0')
        master.config(bg='gray')
        master.resizable(True, True)
        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=20, bg='#ccddff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)
        Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.show(')')).place(x=90,
                                                                                                              y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.show('%')).place(x=180,
                                                                                                              y=50)
        Button(width=11, height=4, text='√', relief='flat', bg='white', command=self.sqrt).place(x=0, y=125)
        Button(width=11, height=4, text='x²', relief='flat', bg='white', command=self.square).place(x=90, y=125)
        Button(width=11, height=4, text='x³', relief='flat', bg='white', command=self.cube).place(x=180, y=125)
        Button(width=11, height=4, text='⌫', relief='flat', bg='white', command=self.delete).place(x=270, y=200)
        Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.show(1)).place(x=0, y=200)
        Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.show(2)).place(x=90, y=200)
        Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.show(3)).place(x=180,
                                                                                                            y=200)
        Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.show(4)).place(x=0, y=275)
        Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.show(5)).place(x=90, y=275)
        Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.show(6)).place(x=180,
                                                                                                            y=275)
        Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.show(7)).place(x=0, y=350)
        Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.show(8)).place(x=90, y=350)
        Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.show(9)).place(x=180,
                                                                                                            y=350)
        Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.show(0)).place(x=90, y=425)
        Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.show('.')).place(x=180,
                                                                                                              y=425)
        Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.show('+')).place(x=270,
                                                                                                              y=350)
        Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.show('-')).place(x=270,
                                                                                                              y=275)
        Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda: self.show('/')).place(x=270,
                                                                                                              y=50)
        Button(width=11, height=4, text='*', relief='flat', bg='white', command=lambda: self.show('*')).place(x=270,
                                                                                                              y=125)
        Button(width=11, height=4, text='=', relief='flat', bg='lightblue', command=self.solve).place(x=270, y=425)
        Button(width=11, height=4, text='C', relief='flat', bg='white', command=self.clear).place(x=0, y=425)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

    def sqrt(self):
        try:
            result = math.sqrt(eval(self.entry_value))
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

    def square(self):
        try:
            result = eval(self.entry_value) ** 2
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

    def cube(self):
        try:
            result = eval(self.entry_value) ** 3
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

    def delete(self):
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)
root = Tk()
calculator = Calculator(root)
root.mainloop()
