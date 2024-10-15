import time
import pygame
import random


pygame.init()
screen = pygame.display.set_mode((800, 600))

# 화면 초기화
screen.fill((255, 255, 255)) # 배경을 흰색으로 설정
pygame.display.flip()

# 원 그리기
def rand_color():
    a, b, c = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return a, b, c

def get_rand_pos(x_max = screen.get_width() - 1, y_max = screen.get_height() - 1):
    return random.randint(0, x_max), random.randint(0, y_max)
    
def get_rand_num(max = 30):
    return random.randint(0, max)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    for _ in range(random.randint(5, 20)):
        pygame.draw.circle(screen, rand_color(), get_rand_pos(), get_rand_num(40) )

    pygame.display.flip()
    time.sleep(0.5)
    
pygame.quit()