import pygame
import psutil

preto = (0, 0, 0)
branco = (245, 245, 245)
cinza = (100, 100, 100)
laranja = (255, 128, 64)
cinza_escuro = (45, 45, 45)

pygame.font.init()
font_menor = pygame.font.Font(None, 20)
font_maior = pygame.font.Font(None, 22)

clock = pygame.time.Clock()

cont = 60

def mostra_texto(info_cpu, surface, nome, chave, pos_y):
    text = font_menor.render(nome, True, preto)
    surface.blit(text, (20, pos_y))
    if chave == "freq":
        s = f'{round(psutil.cpu_freq().current, 2)}'
    elif chave == "nucleos":
        s = f'({psutil.cpu_count()})'
    elif chave == "nucleos_logicos":
        s = f'({psutil.cpu_count(logical=True)})'
    elif chave == "freq_total":
        s = f'{round(psutil.cpu_freq().max, 2)}'
    else:
        s = f'{info_cpu[chave]}'

    text = font_menor.render(s, True, cinza)
    surface.blit(text, (220, pos_y))

def mostra_info_cpu(info_cpu, superficie):
    superficie.fill(branco)

    texto = "Informações da CPU"
    text = font_maior.render(texto, 1, preto)
    superficie.blit(text, (20, 20))

    mostra_texto(info_cpu, superficie, "Nome: ", "brand", 45)
    mostra_texto(info_cpu, superficie, "Arquitetura: ", "arch", 65)
    mostra_texto(info_cpu, superficie, "Palavra (bits): ", "bits", 85)
    mostra_texto(info_cpu, superficie, "Frequência Atual(MHz): ", "freq", 105)
    mostra_texto(info_cpu, superficie, "Frequência Total(MHz): ", "freq_total", 125)
    mostra_texto(info_cpu, superficie, "Núcleos (físicos): ", "nucleos", 145)
    mostra_texto(info_cpu, superficie, "Núcleos (lógicos): ", "nucleos_logicos", 165)

def mostra_uso_cpu(nucleos, superficie):
    superficie.fill(branco)
    num_cpu = len(nucleos)
    x = 10
    y = 40
    desl = 10
    alt = superficie.get_height() - 2 * y
    larg = (superficie.get_width() - 2 * x - (num_cpu + 1) * desl) / num_cpu
    d = x + desl
    for i in nucleos:
        pygame.draw.rect(superficie, laranja, (d, y, larg, alt))
        pygame.draw.rect(superficie, cinza_escuro, (d, y, larg, (1 - i / 100) * alt))
        d = d + larg + desl
    texto_barra = "Uso da CPU: "
    text = font_maior.render(texto_barra, 1, preto)
    superficie.blit(text, (20, 10))

def mostra_uso_disco(disco, superficie):
    superficie.fill(branco)
    larg = superficie.get_width() - 2 * 20
    pygame.draw.rect(superficie, cinza_escuro, (20, 40, larg, 70))
    larg = larg*disco.percent/100
    pygame.draw.rect(superficie, laranja, (20, 40, larg, 70))
    total = round(disco.total/(1024 * 1024 * 1024), 2)
    texto_barra = f'Uso de Disco (Total: {total} GB):'
    text = font_maior.render(texto_barra, 1, preto)
    superficie.blit(text, (20, 10))

def mostra_uso_memoria(memoria, superficie):
    larg = superficie.get_width() - 2 * 20
    superficie.fill(branco)
    pygame.draw.rect(superficie, cinza_escuro, (20, 40, larg, 70))
    larg = larg * memoria.percent / 100
    pygame.draw.rect(superficie, laranja, (20, 40, larg, 70))
    total = round(memoria.total / (1024 * 1024 * 1024), 2)
    texto_barra = f'Uso de Memória (Total: {total} GB):'
    text = font_maior.render(texto_barra, 1, preto)
    superficie.blit(text, (20, 10))

def mostra_info_arquivos(info, superficie):
    superficie.fill(branco)

    texto_arquivos = "Informações sobre arquivos"
    text = font_maior.render(texto_arquivos, 1, preto)
    superficie.blit(text, (20, 20))

    inicio = 50

    for i in info:
        texto_arquivo = f"Arquivo: {info[i]['path']}"
        text = font_menor.render(texto_arquivo, 1, preto)
        superficie.blit(text, (20, inicio))

        texto_nome = f"Nome: {info[i]['nome']}"
        text = font_menor.render(texto_nome, 1, cinza)
        superficie.blit(text, (20, inicio + 20))

        texto_tamanho = f"Tamanho: {info[i]['tamanho']:.2f} MB"
        text = font_menor.render(texto_tamanho, 1, cinza)
        superficie.blit(text, (20, inicio + 40))

        texto_extensao = f"Extensão: {info[i]['extensão']}"
        text = font_menor.render(texto_extensao, 1, cinza)
        superficie.blit(text, (20, inicio + 60))

        inicio += 90

def mostra_info_processos(info_processos, superficie):
    superficie.fill(branco)

    texto_processos = "Processos ativos que mais estão consumindo memória"
    text = font_maior.render(texto_processos, 1, preto)
    superficie.blit(text, (20, 10))

    inicio = 40

    for i in info_processos:
        texto_nome = f"Nome do processo: {i['nome']}"
        text = font_menor.render(texto_nome, 1, cinza)
        superficie.blit(text, (20, inicio))

        texto_memoria = f"{i['memoria']:.2f}% de memória"
        text = font_menor.render(texto_memoria, 1, cinza)
        superficie.blit(text, (20, inicio + 20))

        texto_pid = f"Pid: {i['pid']}"
        text = font_menor.render(texto_pid, 1, cinza)
        superficie.blit(text, (20, inicio + 40))

        inicio += 70

def mostra_info_redes(info_redes, superficie):
    superficie.fill(branco)

    texto_redes = f"Informações sobre Rede '{info_redes['Ethernet']}'"
    text = font_maior.render(texto_redes, 1, preto)
    superficie.blit(text, (20, 10))

    inicio = 40

    texto_mac = f"Endereço MAC: {info_redes['MAC']}"
    text = font_menor.render(texto_mac, 1, cinza)
    superficie.blit(text, (20, inicio + 20))

    texto_ip = f"IP: {info_redes['IP']}"
    text = font_menor.render(texto_ip, 1, cinza)
    superficie.blit(text, (20, inicio))

    texto_mascara = f"Máscara de rede: {info_redes['Máscara de Rede']}"
    text = font_menor.render(texto_mascara, 1, cinza)
    superficie.blit(text, (20, inicio + 40))

    inicio += 70

def mostra_creditos(superficie):
    superficie.fill(branco)
    texto = "Projeto de Bloco - Python - Luiza Mendes - 2018"
    text = font_maior.render(texto, 1, preto)
    superficie.blit(text, (20, 80))
