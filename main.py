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
# Paddle variables
YELLOW_PADDLE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'yellow_paddle.png')), (100, 20)), 90)
BLUE_PADDLE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'blue_paddle.png')), (100, 20)), 90)
paddle_vel = 5
# Ball variables
BALL = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'ball.png')), (25, 25))
# Classes
class Paddle():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.lives = 3
        self.img = img    
    
    def get_width(self):
        return self.img.get_width()
    
    def get_height(self):
        return self.img.get_height()   
        
    def draw(self, win, paddle):
        win.blit(paddle, (self.x, self.y))
        
    def move(self, vel):
        self.y += vel
class Ball():
    MAX_VEL = 5
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(BALL)
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
        
    def draw(self, win):
        win.blit(BALL, (self.x, self.y))
        
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

# Functions

def handle_paddle_movement(pressed_keys, yellow_paddle, blue_paddle):
    # BLUE PADDLE MOVEMENT - LEFT
    if pressed_keys[pygame.K_w] and blue_paddle.y + paddle_vel > 0: # UP
        blue_paddle.move(-paddle_vel)
    if pressed_keys[pygame.K_s] and blue_paddle.y + BLUE_PADDLE.get_height() + paddle_vel < HEIGHT: # DOWN
        blue_paddle.move(paddle_vel)
    # YELLOW PADDLE MOVEMENT - RIGHT
    if pressed_keys[pygame.K_UP] and yellow_paddle.y + paddle_vel > 0: # UP
        yellow_paddle.move(-paddle_vel)
    if pressed_keys[pygame.K_DOWN] and yellow_paddle.y + YELLOW_PADDLE.get_height() + paddle_vel < HEIGHT: # DOWN
        yellow_paddle.move(paddle_vel)
        
def handle_collision(ball, left_paddle, right_paddle):
    if ball.y >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y <= 0:
        ball.y_vel *= -1
        
    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.get_height():
            if ball.x <= left_paddle.x + left_paddle.get_width():
                ball.x_vel *= -1
                
                middle_y = left_paddle.y + left_paddle.get_height() // 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.get_height() // 2) // ball.MAX_VEL
                y_vel = difference_in_y // reduction_factor
                ball.y_vel = -y_vel
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.get_height():
            if ball.x >= right_paddle.x - right_paddle.get_width():
                ball.x_vel *= -1
                
                middle_y = right_paddle.y + right_paddle.get_height() // 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.get_height() // 2) // ball.MAX_VEL
                y_vel = difference_in_y // reduction_factor
                ball.y_vel = -y_vel
    
# Main game loop
def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    blue_paddle = Paddle(5, HEIGHT//2 - BLUE_PADDLE.get_height()//2, BLUE_PADDLE)
    yellow_paddle = Paddle(WIDTH - YELLOW_PADDLE.get_width() - 5, HEIGHT//2 - YELLOW_PADDLE.get_height()//2, YELLOW_PADDLE)
    ball = Ball(WIDTH//2 - BALL.get_width()//2, HEIGHT//2 - BALL.get_height()//2)
    def redraw_window(window):
        window.blit(BG, (0, 0))
        blue_paddle.draw(window, BLUE_PADDLE)
        yellow_paddle.draw(window, YELLOW_PADDLE)
        ball.draw(window)
        pygame.draw.rect(WIN, WHITE, BORDER)
        pygame.display.update()
    
    while run:
        clock.tick(FPS)
        redraw_window(WIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()    
        pressed_keys = pygame.key.get_pressed()
        
        handle_paddle_movement(pressed_keys, yellow_paddle, blue_paddle)
        handle_collision(ball, blue_paddle, yellow_paddle)
        ball.move()

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
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

if __name__ == '__main__':
    main_menu()