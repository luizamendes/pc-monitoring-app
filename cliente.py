import pickle
import pygame
import socket
import plota_dados

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

s.connect((host, 8881))

largura_tela = 1600
altura_tela = 800
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Informações de CPU")
pygame.display.init()

s1 = pygame.Surface((largura_tela/2, altura_tela * 0.28))
s2 = pygame.Surface((largura_tela/2, altura_tela * 0.38))
s3 = pygame.Surface((largura_tela/2, altura_tela * 0.17))
s4 = pygame.Surface((largura_tela/2, altura_tela * 0.17))
s5 = pygame.Surface((largura_tela/2, altura_tela * 0.4))
s6 = pygame.Surface((largura_tela/2, altura_tela * 0.32))
s7 = pygame.Surface((largura_tela/2, altura_tela * 0.15))
s8 = pygame.Surface((largura_tela/2, altura_tela * 0.15))

pygame.font.init()
font_menor = pygame.font.Font(None, 20)
font_maior = pygame.font.Font(None, 22)

clock = pygame.time.Clock()

cont = 60

terminou = False

while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            s.send("$".encode())
            terminou = True

    if cont == 60:
        s.send("?".encode())
        msg = s.recv(4096)
        try:
            dic = pickle.loads(msg)

            plota_dados.mostra_info_cpu(dic["cpu"], s1)
            plota_dados.mostra_uso_cpu(dic["nucleos"], s2)
            plota_dados.mostra_uso_memoria(dic["memoria"], s3)
            plota_dados.mostra_uso_disco(dic["disco"], s4)
            plota_dados.mostra_info_arquivos(dic["arquivos"], s5)
            plota_dados.mostra_info_processos(dic["processos"], s6)
            plota_dados.mostra_info_redes(dic["redes"], s7)
            plota_dados.mostra_creditos(s8)
        except EOFError:
            pass

        tela.blit(s1, (0, 0))
        tela.blit(s2, (0, tela.get_height() * 0.28))
        tela.blit(s3, (0, tela.get_height() * 0.66))
        tela.blit(s4, (0, tela.get_height() * 0.83))
        tela.blit(s5, (800, 0))
        tela.blit(s6, (800, tela.get_height() * 0.4))
        tela.blit(s7, (800, tela.get_height() * 0.72))
        tela.blit(s8, (800, tela.get_height() * 0.85))

        cont = 0

    pygame.display.update()

    clock.tick(60)
    cont = cont + 1

pygame.display.quit()
