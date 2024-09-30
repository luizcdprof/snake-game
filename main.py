import pygame
import random

# Criar a Tela do Jogo
LARGURA = 1200
ALTURA = 800
pygame.init()
pygame.display.set_caption("Snake Game V1")
TELA = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()

# Cores do Jogo
BGND = (0, 0, 0)
TEXTO = (255, 255, 255)
SNAKE = (255, 255, 0)
FRUTA = (0, 255, 0)

# Parâmetros do Jogo
FPS = 60
TAMANHO = 20

# Gerar Frutas
def gerar_fruta():
    x = round(random.randrange(0, LARGURA - TAMANHO) / TAMANHO) * TAMANHO
    y = round(random.randrange(0, ALTURA - TAMANHO) / TAMANHO) * TAMANHO
    return x, y

# Desenhar Frutas
def desenhar_fruta(cor, tamanho, fruta_x, fruta_y):
    pygame.draw.rect(TELA, cor, [fruta_x, fruta_y, tamanho, tamanho])

# Jogo
def jogo():
    running = True    
    fruta_x, fruta_y = gerar_fruta()
    
    while running:
        TELA.fill(BGND)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False

        desenhar_fruta(FRUTA, TAMANHO, fruta_x, fruta_y)

        pygame.display.update()
        relogio.tick(FPS)

# Executar o Jogo
jogo()