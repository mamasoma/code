import ctypes
from tkinter import Tk, Button, Entry, StringVar, Frame
import os

# DLLファイルの正しいパスを指定
dll_path = r"C:\Users\maho\Desktop\Programing\clc\calculator.dll"
calculator = ctypes.CDLL(dll_path)

# C言語の関数を定義
calculator.add.argtypes = [ctypes.c_double, ctypes.c_double]
calculator.add.restype = ctypes.c_double

calculator.subtract.argtypes = [ctypes.c_double, ctypes.c_double]
calculator.subtract.restype = ctypes.c_double

calculator.multiply.argtypes = [ctypes.c_double, ctypes.c_double]
calculator.multiply.restype = ctypes.c_double

calculator.divide.argtypes = [ctypes.c_double, ctypes.c_double]
calculator.divide.restype = ctypes.c_double

# GUIの作成
class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("電卓")
        master.configure(bg="white")  # 背景色

        self.result = StringVar()
        self.entry = Entry(master, textvariable=self.result, width=14, font=('Arial', 20), bd=10, insertwidth=2, justify='right', bg="white", fg="black")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # ボタンの配置
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        button_frame = Frame(self.master, bg="white")
        button_frame.grid(row=1, column=0, columnspan=4)

        for button in buttons:
            command = lambda x=button: self.click(x)
            Button(button_frame, text=button, width=5, height=2, command=command, bg="white", fg="black", font=('Arial', 16), relief="solid", borderwidth=1).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # クリアボタンを追加
        Button(button_frame, text='C', width=5, height=2, command=self.clear, bg="white", fg="black", font=('Arial', 16), relief="solid", borderwidth=1).grid(row=row_val, column=col_val, padx=5, pady=5)

    def click(self, key):
        if key == '=':
            self.calculate()
        elif key in ['+', '-', '*', '/']:
            self.result.set(self.result.get() + ' ' + key + ' ')
        else:
            self.result.set(self.result.get() + key)

    def calculate(self):
        try:
            expression = self.result.get().split()
            if len(expression) == 3:
                a, op, b = expression
                a, b = float(a), float(b)

                if op == '+':
                    result = calculator.add(a, b)
                elif op == '-':
                    result = calculator.subtract(a, b)
                elif op == '*':
                    result = calculator.multiply(a, b)
                elif op == '/':
                    result = calculator.divide(a, b)
                    if result == -1.0 and b == 0:
                        self.result.set("ゼロ除算エラー")
                        return

                self.result.set(result)
        except Exception as e:
            self.result.set("エラー")

    def clear(self):
        self.result.set("")

def main():
    root = Tk()
    calc = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
