import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Definições de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (33, 117, 68)
YELLOW = (255, 255, 255)
GREEN = (0, 153, 51)

# Configurações da janela
WIDTH, HEIGHT = 800, 520
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo Educativo de Matemática")

# Fontes
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 24)
instruction_font = pygame.font.Font(None, 36)

# Função para mostrar texto na tela
def draw_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    rect.midtop = (x, y)
    screen.blit(surface, rect)

# Função para gerar questões
def generate_question():
    num1 = random.randint(10, 50)
    num2 = random.randint(1, 10)
    operator = random.choice(["+", "-", "*", "/"])
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2
    else:
        answer = num1 // num2  # divisão inteira
    question_text = f"{num1} {operator} {num2} = ?"
    return question_text, answer

# Função para tela de fim de jogo
def game_over(score):
    screen.fill(BLUE)
    draw_text("Fim de jogo!", font, YELLOW, WIDTH/2, HEIGHT/4)
    draw_text(f"Você fez {score} pontos.", small_font, YELLOW, WIDTH/2, HEIGHT/2)
    draw_text("Pressione ESC para sair.", small_font, YELLOW, WIDTH/2, HEIGHT * 3/4)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Tela inicial com instruções
def show_instructions():
    screen.fill(BLUE)
    draw_text("Bem-vindo ao Jogo Educativo de Matemática!", instruction_font, YELLOW, WIDTH/2, HEIGHT/4)
    draw_text("Resolva as questões matemáticas digitando as respostas.", instruction_font, YELLOW, WIDTH/2, HEIGHT/2)
    draw_text("Pressione qualquer tecla para começar.", small_font, YELLOW, WIDTH/2, HEIGHT * 3/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

# Loop do jogo
def main():
    score = 0
    clock = pygame.time.Clock()
    question, answer = generate_question()
    input_text = ""
    running = True
    show_instructions()
    while running:
        screen.fill(BLUE)
        draw_text("Resolva a seguinte questão:", instruction_font, YELLOW, WIDTH/2, HEIGHT/4)
        draw_text(question, instruction_font, YELLOW, WIDTH/2, HEIGHT/2)
        draw_text(input_text, instruction_font, YELLOW, WIDTH/2, HEIGHT * 3/4)
        pygame.display.flip()

        # Eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        if int(input_text) == answer:
                            score += 10
                            question, answer = generate_question()
                            input_text = ""
                        else:
                            game_over(score)
                    except ValueError:
                        pass
                elif event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    input_text += event.unicode

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
