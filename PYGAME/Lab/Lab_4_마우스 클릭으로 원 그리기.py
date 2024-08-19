import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

# 화면
screen.fill((255, 255, 255))

# 랜덤 색
def rand_color():
    color_r, color_g, color_b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return color_r, color_g, color_b



# 랜덤 크기
def rand_size(max = 70):
    return random.randint(0, max)

# 시작
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, rand_color(), event.pos, rand_size())


    pygame.display.flip()

pygame.quit()