import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess

def run_bat_and_exit(mode):
    bat_file = f'run_mode{mode}.bat'
    subprocess.Popen([bat_file], shell=True)
    root.destroy()

# GUIの設定
root = ttk.Window(themename="flatly")  # テーマを選択
root.title("Mode Selection")

# ウィンドウのサイズを設定
root.geometry("400x300")

# ウィンドウを中央に配置
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# 背景色を変更
root.configure(background="#f0f0f5")

# タイトルラベル
ttk.Label(root, text="Choose a Mode", font=("Helvetica", 18, "bold"), background="#f0f0f5").pack(pady=20)

# ボタンのスタイルを設定
style = ttk.Style()

# 赤いボタン
style.configure('Red.TButton', font=("Helvetica", 14), width=20, background="#FF6347", foreground="white")

# オレンジのボタン
style.configure('Orange.TButton', font=("Helvetica", 14), width=20, background="#FFA500", foreground="white")

# 青いボタン
style.configure('Blue.TButton', font=("Helvetica", 14), width=20, background="#1E90FF", foreground="white")

# 緑のボタン
style.configure('Green.TButton', font=("Helvetica", 14), width=20, background="#32CD32", foreground="white")

# モード1ボタン（赤）
mode1_button = ttk.Button(root, text="Mode 1", command=lambda: run_bat_and_exit(1), style='Red.TButton')
mode1_button.pack(pady=5)

# モード2ボタン（オレンジ）
mode2_button = ttk.Button(root, text="Mode 2", command=lambda: run_bat_and_exit(2), style='Orange.TButton')
mode2_button.pack(pady=5)

# モード3ボタン（青）
mode3_button = ttk.Button(root, text="Mode 3", command=lambda: run_bat_and_exit(3), style='Blue.TButton')
mode3_button.pack(pady=5)

# モード4ボタン（緑）
mode4_button = ttk.Button(root, text="Mode 4", command=lambda: run_bat_and_exit(4), style='Green.TButton')
mode4_button.pack(pady=5)

# メインループ開始
root.mainloop()
