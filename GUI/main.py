import sys
import pyautogui as pag
import time
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def open_notepad_and_write(number):
    pag.hotkey('win', 'r')
    time.sleep(1)
    pag.typewrite('notepad')
    pag.press('enter')
    time.sleep(2)

    pag.typewrite(str(number))
    time.sleep(1)

    pag.hotkey('alt', 'f4')
    time.sleep(1)
    pag.press('n')

def display_result(argument):
    root = ttk.Window(themename="cosmo")
    root.title(f"Result for Mode {argument}")

    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    # 背景色を変更
    root.configure(background="#e0e0f8")

    ttk.Label(root, text=f"Argument: {argument}", font=("Helvetica", 16, "bold"), background="#e0e0f8").pack(pady=20)
    ttk.Label(root, text=f"Task completed: {argument} written in Notepad.", font=("Helvetica", 14), background="#e0e0f8").pack(pady=10)
    
    # ボタンのスタイルを設定
    style = ttk.Style()
    style.configure('TButton', font=("Helvetica", 14), width=20)
    
    ttk.Button(root, text="Close", bootstyle=PRIMARY, command=root.destroy, style='TButton').pack(pady=20)

    # 結果画面を最前面に表示
    root.attributes('-topmost', True)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        open_notepad_and_write(arg)
        display_result(arg)
    else:
        print("No argument provided.")
