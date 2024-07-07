import tkinter as tk
import subprocess
import os

def run_bat_and_exit(mode):
    # モードに応じたバッチファイルを選択
    if mode == 1:
        bat_file = 'run_mode1.bat'
    if mode == 2:
        bat_file = 'run_mode2.bat'
    if mode == 3:
        bat_file = 'run_mode3.bat'
    else:
        bat_file = 'run_mode4.bat'

    # バッチファイルを実行
    subprocess.Popen([bat_file], shell=True)

    # GUIを閉じる
    root.destroy()

# GUIの設定
root = tk.Tk()
root.title("Mode Selection")

tk.Label(root, text="Choose a Mode").pack()

mode1_button = tk.Button(root, text="Mode 1", command=lambda: run_bat_and_exit(1))
mode1_button.pack()

mode2_button = tk.Button(root, text="Mode 2", command=lambda: run_bat_and_exit(2))
mode2_button.pack()
mode3_button = tk.Button(root, text="Mode 3", command=lambda: run_bat_and_exit(3))
mode3_button.pack()
mode4_button = tk.Button(root, text="Mode 4", command=lambda: run_bat_and_exit(4))
mode4_button.pack()

root.mainloop()
