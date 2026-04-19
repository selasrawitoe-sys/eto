import requests
import os
import time
import socket
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style, init

init(autoreset=True)

# --- إعدادات الـ VIP الخاصة بك ---
BOT_TOKEN = "8406859700:AAFKj0GpFWDq_Uzk7N43TUIGO_l3GI_VNc0"
CHAT_ID = "7804053419"
PASSWORD = "777"  # كلمة سر الدخول

def send_vip_msg(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    try: requests.post(url, data=payload)
    except: pass

def vip_loading(text):
    print(Fore.MAGENTA + f" [Wait] {text}", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(Fore.GREEN + " [Done]")

def vip_logo():
    os.system('clear')
    # شعار VIP ضخم ومنسق
    print(Fore.MAGENTA + Style.BRIGHT + r"""
    ░██████╗░████████╗░█████╗░  ░█████╗░███████╗
    ░██╔═══╝░╚══██╔══╝██╔══██╗  ██╔══██╗╚════██║
    ░█████╗░░░░░██║░░░██║░░██║  ╚██████║░░░░██╔╝
    ░██╔══╝░░░░░██║░░░██║░░██║  ░╚═══██║░░░██╔╝░
    ░██████╗░░░░██║░░░╚█████╔╝  ░█████╔╝░░██╔╝░░
    ░╚═════╝░░░░╚═╝░░░░╚════╝░  ░╚════╝░░░╚═╝░░░
    """)
    print(Fore.WHITE + "    --- " + Fore.MAGENTA + "V I P   M O D E   A C T I V A T E D" + Fore.WHITE + " ---")
    print(Fore.CYAN + "    [+] DEV: ETO_07 | [+] RANK: HERCULES ASATIR")
    print(Fore.MAGENTA + "    " + "═"*41 + "\n")

def track_ip_vip():
    vip_logo()
    ip = input(f"{Fore.MAGENTA}[?]{Fore.WHITE} Enter Target IP: ")
    vip_loading("Bypassing Proxies & Locating")
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        if data['status'] == 'success':
            msg = (f"<b>💎 VIP REPORT: IP TRACKED</b>\n"
                   f"━━━━━━━━━━━━━━━━━━\n"
                   f"<b>🌐 IP:</b> <code>{data['query']}</code>\n"
                   f"<b>📍 Country:</b> {data['country']} ({data['countryCode']})\n"
                   f"<b>🏙️ City:</b> {data['city']}\n"
                   f"<b>🏢 ISP:</b> {data['isp']}\n"
                   f"<b>🗺️ Google Maps:</b> \nhttps://www.google.com/maps?q={data['lat']},{data['lon']}")
            send_vip_msg(msg)
            print(Fore.GREEN + "[+] Data Captured! Check your VIP Telegram Bot.")
        else: print(Fore.RED + "[-] IP Not Found.")
    except: print(Fore.RED + "[-] Connection Lost.")
    input("\n[Press Enter]")

def track_phone_vip():
    vip_logo()
    num = input(f"{Fore.MAGENTA}[?]{Fore.WHITE} Enter Phone (+212...): ")
    vip_loading("Extracting Database Info")
    try:
        parsed = phonenumbers.parse(num)
        if phonenumbers.is_valid_number(parsed):
            country = geocoder.description_for_number(parsed, "en")
            provider = carrier.name_for_number(parsed, "en")
            tz = timezone.time_zones_for_number(parsed)
            
            msg = (f"<b>💎 VIP REPORT: PHONE INFO</b>\n"
                   f"━━━━━━━━━━━━━━━━━━\n"
                   f"<b>📱 Number:</b> {num}\n"
                   f"<b>🌍 Country:</b> {country}\n"
                   f"<b>📶 Carrier:</b> {provider}\n"
                   f"<b>⏰ Timezone:</b> {tz}\n"
                   f"<b>💬 WhatsApp:</b> wa.me/{num.replace('+', '')}")
            send_vip_msg(msg)
            print(Fore.GREEN + "[+] Success! Telegram updated.")
        else: print(Fore.RED + "[-] Invalid Phone Number.")
    except: print(Fore.RED + "[-] Analysis Failed.")
    input("\n[Press Enter]")

def scan_host_vip():
    vip_logo()
    site = input(f"{Fore.MAGENTA}[?]{Fore.WHITE} Enter Host (site.com): ")
    vip_loading("Reverse DNS Lookup")
    try:
        ip_addr = socket.gethostbyname(site)
        data = requests.get(f"http://ip-api.com/json/{ip_addr}").json()
        msg = (f"<b>💎 VIP REPORT: HOST SCAN</b>\n"
               f"━━━━━━━━━━━━━━━━━━\n"
               f"<b>🌐 Domain:</b> {site}\n"
               f"<b>🔑 Server IP:</b> {ip_addr}\n"
               f"<b>📍 Host Location:</b> {data['country']}\n"
               f"<b>🚀 ISP:</b> {data['isp']}")
        send_vip_msg(msg)
        print(Fore.GREEN + f"[+] Server IP {ip_addr} Tracked and Sent.")
    except: print(Fore.RED + "[-] Host Unreachable.")
    input("\n[Press Enter]")

def main():
    vip_logo()
    # نظام الدخول بالباسورد
    p = input(f"{Fore.MAGENTA}[#]{Fore.WHITE} Admin Password: ")
    if p != PASSWORD:
        print(Fore.RED + "!! ACCESS DENIED !!")
        exit()
    
    while True:
        vip_logo()
        print(f"[{Fore.MAGENTA}1{Fore.WHITE}] Track Target IP")
        print(f"[{Fore.MAGENTA}2{Fore.WHITE}] Phone Database Scan")
        print(f"[{Fore.MAGENTA}3{Fore.WHITE}] Website Server Lookup")
        print(f"[{Fore.MAGENTA}0{Fore.WHITE}] Terminate Session")
        
        c = input(f"\n{Fore.MAGENTA}ETO_07_VIP > {Fore.WHITE}")
        if c == '1': track_ip_vip()
        elif c == '2': track_phone_vip()
        elif c == '3': scan_host_vip()
        elif c == '0': break

if __name__ == "__main__":
    main()

