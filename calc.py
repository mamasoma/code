# 以下はPythonで電卓を表示するGUIのコードです。
import tkinter as tk
import ctypes

# C言語のライブラリを読み込む
libcalc = ctypes.CDLL('./calc.dll')  # Windowsの場合

# C言語の関数の戻り値の型を設定
libcalc.button_pressed.restype = ctypes.c_char_p
# C言語の関数の引数の型を設定
libcalc.button_pressed.argtypes = [ctypes.c_char_p]

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        self.result_label = tk.Label(root, textvariable=self.result_var, font=("Arial", 18), width=15, borderwidth=5, relief="ridge",anchor=tk.E)
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
        # ボタンがクリックされると、ボタンのテキストをC言語の関数に渡す
        result = self.call_c_function(text)
        self.result_var.set(result)
    
    def call_c_function(self, input_text):
        # C言語の関数を呼び出す
        result = libcalc.button_pressed(input_text.encode('utf-8'))
        return result.decode('utf-8')

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
