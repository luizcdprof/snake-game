import pygame
import random

# Criar a SCREEN do Jogo
LARGURA = 1200
ALTURA = 800
pygame.init()
pygame.display.set_caption("Snake Game V1")
SCREEN = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()

# Cores do Jogo
BGND = (0, 0, 0)
TEXTO = (255, 255, 255)
SNAKE_COLOR = (255, 255, 0)
FRUTA = (0, 255, 0)

# Parâmetros do Jogo
FPS = 60
SIZE = 20

# Parâmetros da cobrinha
snake_speed = 5

# Gerar Frutas
def gerar_fruta():
    x = round(random.randrange(0, LARGURA - SIZE) / SIZE) * SIZE
    y = round(random.randrange(0, ALTURA - SIZE) / SIZE) * SIZE
    return x, y

# Desenhar Frutas
def desenhar_fruta(cor, tamanho, fruta_x, fruta_y):
    pygame.draw.rect(SCREEN, cor, [fruta_x, fruta_y, tamanho, tamanho])

# Desenhar a cobrinha
def draw_snake(pixels):
    for pixel in  pixels:
        pygame.draw.rect(SCREEN, SNAKE_COLOR, [pixel[0], pixel[1], SIZE, SIZE])

# Jogo
def jogo():
    running = True
    fruta_x, fruta_y = gerar_fruta()
    pixels = []
    snake_x = LARGURA / 2
    snake_y = ALTURA / 2
    snake_size = 1
    
    while running:
        SCREEN.fill(BGND)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False

        desenhar_fruta(FRUTA, SIZE, fruta_x, fruta_y)
        
        snake_x += SIZE
        pixels.append([snake_x, snake_y])

        if len(pixels) > snake_size:
            del pixels[0]

        draw_snake(pixels)

        pygame.display.update()
        relogio.tick(snake_speed)

# Executar o Jogo
jogo()