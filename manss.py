import os
import curses
import random
import time

def matrix_effect(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.curs_set(0)
    stdscr.nodelay(1)

    height, width = stdscr.getmaxyx()
    start_time = time.time()

    while time.time() - start_time < 5:
        stdscr.clear()
        for _ in range(100):
            y = random.randint(0, height - 1)
            x = random.randint(0, width - 1)
            char = random.choice(['1', '0'])
            try:
                stdscr.addstr(y, x, char, curses.color_pair(1))
            except curses.error:
                pass

        stdscr.refresh()
        time.sleep(0.05)

def show_banner():
    print("""
    ███╗   ███╗ █████╗ ███╗   ██╗
    ████╗ ████║██╔══██╗████╗  ██║
    ██╔████╔██║███████║██╔██╗ ██║
    ██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
        NMAP VE OSINT TOOL
    """)

def main_menu():
    while True:
        print("\n\033[92m\033[1m=== ANA MENÜ ===\033[0m\n")
        print("1. NMAP TARAMASI")
        print("2. WEB OSINT TARAMA")
        print("99. ÇIKIŞ\n")
        choice = input("SEÇİMİNİZİ YAPIN: ")

        if choice == "1":
            nmap_menu()
        elif choice == "2":
            web_osint_menu()
        elif choice == "99":
            print("ÇIKIŞ YAPILIYOR...")
            break
        else:
            print("GEÇERSİZ SEÇİM, LÜTFEN TEKRAR DENEYİN.")

def nmap_menu():
    while True:
        print("\n\033[92m\033[1m=== NMAP TARAMASI ===\033[0m")
        print("1. HIZLI TARAMA (-T4 -F)")
        print("2. TÜM PORTLAR (-P 1-65535)")
        print("3. OS VE VERSİYON TARAMA (-A)")
        print("4. SCRIPT TARAMA (--SCRIPT)")
        print("5. DETAYLI SERVİS TARAMASI (-sV)")
        print("6. GÜÇLÜ TARAMA (-sS -sU -T4 -A -v)")
        print("7. DNS ENUM TARAMASI (--script dns-* -T4)")
        print("99. ANA MENÜYE DÖN\n")
        choice = input("SEÇİMİNİZİ YAPIN: ")

        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            target_ip = input("HEDEF IP ADRESİNİ GİRİN: ")
            if choice == "1":
                os.system(f"nmap -T4 -F {target_ip}")
            elif choice == "2":
                os.system(f"nmap -p 1-65535 {target_ip}")
            elif choice == "3":
                os.system(f"nmap -A {target_ip}")
            elif choice == "4":
                os.system(f"nmap --script default {target_ip}")
            elif choice == "5":
                os.system(f"nmap -sV {target_ip}")
            elif choice == "6":
                os.system(f"nmap -sS -sU -T4 -A -v {target_ip}")
            elif choice == "7":
                os.system(f"nmap --script dns-* -T4 {target_ip}")
        elif choice == "99":
            break
        else:
            print("GEÇERSİZ SEÇİM.")

def web_osint_menu():
    while True:
        print("\n\033[92m\033[1m=== WEB OSINT TARAMA ===\033[0m")
        print("1. NIKTO")
        print("2. DIRB")
        print("3. DIRBUSTER")
        print("4. FFUF")
        print("5. DAVTEST")
        print("6. WFUZZ")
        print("7. SQLMAP")
        print("99. ANA MENÜYE DÖN\n")
        choice = input("SEÇİMİNİZİ YAPIN: ")

        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            target_url = input("HEDEF URL'Yİ GİRİN (HTTP:// OR HTTPS:// İLE BAŞLAYARAK): ")
            if choice == "1":
                os.system(f"nikto -h {target_url}")
            elif choice == "2":
                os.system(f"dirb {target_url}")
            elif choice == "3":
                os.system(f"dirbuster {target_url}")
            elif choice == "4":
                os.system(f"ffuf -u {target_url}/FUZZ")
            elif choice == "5":
                os.system(f"davtest -url {target_url}")
            elif choice == "6":
                os.system(f"wfuzz -u {target_url}")
            elif choice == "7":
                os.system(f"sqlmap -u {target_url}")
        elif choice == "99":
            break
        else:
            print("GEÇERSİZ SEÇİM.")

def start_tool():
    curses.wrapper(matrix_effect)
    show_banner()
    main_menu()

if __name__ == "__main__":
    start_tool()
