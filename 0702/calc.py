import tkinter as tk
import ctypes

# C言語のライブラリを読み込む
libcalc = ctypes.CDLL('./libcalc.dll')  # Windowsの場合

# C言語の関数の戻り値の型を設定
libcalc.calculate.restype = ctypes.c_double
# C言語の関数の引数の型を設定
libcalc.calculate.argtypes = [ctypes.c_char_p]

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        self.result_label = tk.Label(root, textvariable=self.result_var, font=("Arial", 18), width=15, borderwidth=5, relief="ridge")
        self.result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # ボタンの配置
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0)  # Cボタンを追加
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, font=("Arial", 18), width=3, height=1, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
        
    def on_button_click(self, text):
        if text == "=":
            result = self.calculate_expression(self.result_var.get())
            self.result_var.set(result)
        elif text == "C":
            self.result_var.set("0")
        elif self.result_var.get() == "0":
            self.result_var.set(text)
        else:
            self.result_var.set(self.result_var.get() + text)
    
    def calculate_expression(self, expr):
        # C言語の関数を呼び出す
        result = libcalc.calculate(expr.encode('utf-8'))
        return str(result)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
