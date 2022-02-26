# module imports
from email.mime import image
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

# Paddle variables
YELLOW_PADDLE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'yellow_paddle.png')), (100, 20)), 90)
BLUE_PADDLE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'blue_paddle.png')), (100, 20)), 90)
paddle_vel = 5

# Classes
class Paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lives = 3
    
    def move(self, vel):
        self.y += vel
        
class Ball():
    pass

# Main game loop
def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    blue_paddle = Paddle(5, HEIGHT//2 - BLUE_PADDLE.get_height()//2)
    yellow_paddle = Paddle(WIDTH - YELLOW_PADDLE.get_width() - 5, HEIGHT//2 - YELLOW_PADDLE.get_height()//2)
    def redraw_window(window):
        window.blit(BG, (0, 0))
        WIN.blit(BLUE_PADDLE, (blue_paddle.x, blue_paddle.y))
        WIN.blit(YELLOW_PADDLE, (yellow_paddle.x, yellow_paddle.y))
        pygame.draw.rect(WIN, WHITE, BORDER)
        pygame.display.update()
    
    while run:
        clock.tick(FPS)
        redraw_window(WIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                
        pressed_keys = pygame.key.get_pressed()
        # BLUE PADDLE MOVEMENT
        if pressed_keys[pygame.K_w] and blue_paddle.y + paddle_vel > 0: # UP
            blue_paddle.move(-paddle_vel)
        if pressed_keys[pygame.K_s] and blue_paddle.y + BLUE_PADDLE.get_height() + paddle_vel < HEIGHT: # DOWN
            blue_paddle.move(paddle_vel)
        # YELLOW PADDLE MOVEMENT
        if pressed_keys[pygame.K_UP] and yellow_paddle.y + paddle_vel > 0: # UP
            yellow_paddle.move(-paddle_vel)
        if pressed_keys[pygame.K_DOWN] and yellow_paddle.y + YELLOW_PADDLE.get_height() + paddle_vel < HEIGHT: # DOWN
            yellow_paddle.move(paddle_vel)
            

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