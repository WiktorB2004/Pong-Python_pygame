# module imports
import pygame
import os
# pygame initializations
pygame.init()
pygame.font.init()
# Window variables
WIDTH, HEIGHT = 800, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')
BG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'background-black.png')), (WIDTH, HEIGHT))
BORDER = pygame.Rect(WIDTH//2 - 2, 0, 4, HEIGHT)

# Color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Classes
class Paddle():
    pass

class Ball():
    pass

# Main game loop
def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    
    def redraw_window(window):
        window.blit(BG, (0, 0))
        pygame.draw.rect(WIN, WHITE, BORDER)
        pygame.display.update()
    
    while run:
        clock.tick(FPS)
        redraw_window(WIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

# Main menu
def main_menu():
    run = True
    start_font = pygame.font.SysFont('comicsans', 24)
    start_label = start_font.render('Press mouse button to start!!!', 1, WHITE)
    while run:
        WIN.blit(BG, (0, 0))
        WIN.blit(start_label, (WIDTH//2 - start_label.get_width()//2, HEIGHT//2 - start_label.get_height()//2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

if __name__ == '__main__':
    main_menu()