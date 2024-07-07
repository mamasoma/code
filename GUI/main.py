import sys
import pyautogui as pag
import time
import tkinter as tk

def open_notepad_and_write(number):
    # メモ帳を開く
    pag.hotkey('win', 'r')
    time.sleep(1)
    pag.typewrite('notepad')
    pag.press('enter')
    time.sleep(2)  # メモ帳が開くまで待機

    # 数値を入力
    pag.typewrite(str(number))
    time.sleep(1)

    # メモ帳を保存せずに閉じる
    pag.hotkey('alt', 'f4')
    time.sleep(1)
    pag.press('n')

def display_result(argument):
    root = tk.Tk()
    root.title(f"Result for Mode {argument}")

    tk.Label(root, text=f"Argument: {argument}").pack()
    tk.Label(root, text=f"Task completed: {argument} written in Notepad.").pack()

    tk.Button(root, text="Close", command=root.destroy).pack()
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        open_notepad_and_write(arg)
        display_result(arg)
    else:
        print("No argument provided.")
