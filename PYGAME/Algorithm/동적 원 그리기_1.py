import pygame
import random


pygame.init()
screen = pygame.display.set_mode((800, 600))

# 화면 초기화
screen.fill((255, 255, 255)) # 배경을 흰색으로 설정
pygame.display.flip()

# 원 그리기
num_circles = random.randint(5, 20)
for _ in range(num_circles):
    radius = random.randint(10, 100)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    position = (random.randint(0 + radius, 800 - radius), random.randint(0 + radius, 600 - radius))

    pygame.draw.circle(screen, color, position, radius)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()