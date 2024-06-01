Cの環境構築
https://www.javadrive.jp/cstart/install/index6.html

注意：
どちらもビット数を合わせる必要がある

PythonとCどちらも64ビットで行った。
確認方法
Python
import platform
print(platform.architecture())

C
MSYS２をインストール
MSYS２のターミナルでfileコマンドインストール
pacman -Syu
pacman -S file
ビット数確認
file path\to\calculator.dll

Cの64bitのdll作成方法
gcc -shared -o calculator.dll calculator.c -m64
![Uploading image.png…]()
