import pygame
import random

# Criar a SCREEN do Jogo
WIDTH = 1200
HEIGHT = 800
pygame.init()
pygame.display.set_caption("Snake Game V1")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Cores do Jogo
GAME_BGND_COLOR = (0, 0, 0)
ENDGAME_BGND_COLOR = (255, 0, 0)
SCORE_TEXT_COLOR = (255, 255, 255)
GAMEOVER_TEXT_COLOR = (0, 0, 0)
SNAKE_COLOR = (255, 255, 0)
FRUIT_COLOR = (0, 255, 0)

# Parâmetros do Jogo
FPS = 60
SIZE = 20

# Parâmetros da cobrinha
snake_speed = 10

# Gerar Frutas
def generate_fruit():
    x = round(random.randrange(0, WIDTH - SIZE) / SIZE) * SIZE
    y = round(random.randrange(0, HEIGHT - SIZE) / SIZE) * SIZE
    return x, y

# Desenhar Frutas
def draw_fruit(color, size, fruit_x, fruit_y):
    pygame.draw.rect(SCREEN, color, [fruit_x, fruit_y, size, size])

# Desenhar a cobrinha
def draw_snake(pixels):
    for pixel in  pixels:
        pygame.draw.rect(SCREEN, SNAKE_COLOR, [pixel[0], pixel[1], SIZE, SIZE])

# Desenhar o placar
def draw_score(points):
    score_font = pygame.font.SysFont('Arial', 35)
    score_text = score_font.render(f'Pontos: {points}', True, SCORE_TEXT_COLOR)
    SCREEN.blit(score_text, [1, 1])

# Desenhar o Game Over
def draw_game_over(points):
    score_font = pygame.font.SysFont('Arial', 80)
    score_text = score_font.render(f'Pontos: {points}', True, GAMEOVER_TEXT_COLOR)
    SCREEN.blit(score_text, [WIDTH / 2, HEIGHT / 2])

def snake_move(key):
    if key == pygame.K_DOWN:
        move_x = 0
        move_y = SIZE
    elif key == pygame.K_UP:
        move_x = 0
        move_y = -SIZE
    elif key == pygame.K_RIGHT:
        move_x = SIZE
        move_y = 0
    elif key == pygame.K_LEFT:
        move_x = -SIZE
        move_y = 0
    
    return move_x, move_y

# Jogo
def game():
    running = True
    fruit_x, fruit_y = generate_fruit()
    pixels = []
    snake_x = WIDTH / 2
    snake_y = HEIGHT / 2
    move_x = 0
    move_y = 0
    snake_size = 1
    
    while running:
        SCREEN.fill(GAME_BGND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                move_x, move_y = snake_move(event.key)

        draw_fruit(FRUIT_COLOR, SIZE, fruit_x, fruit_y)

        # atualizar posição da cobrinha
        if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
            running = False
        snake_x += move_x
        snake_y += move_y

        # Desenhar a cobrinha
        pixels.append([snake_x, snake_y])
        if len(pixels) > snake_size:
            del pixels[0]
        draw_snake(pixels)

        # Verificar se a cobrinha bateu em si mesma
        for pixel in pixels[:-1]:
            if pixel == [snake_x, snake_y]:
                running = False

        # Desenhar placar
        draw_score(snake_size - 1)

        # Atualizar a tela
        pygame.display.update()

        # Desenhar uma nova fruta se a cobra pegar a atual
        if snake_x == fruit_x and snake_y == fruit_y:
            snake_size += 1
            fruit_x, fruit_y = generate_fruit()

        clock.tick(snake_speed)        

# Executar o Jogo
game()