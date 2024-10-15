import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

# 화면 초기화
screen.fill((255, 255, 255))    # 배경을 흰색으로 설정
pygame.display.flip()

# FPS 설정
clock = pygame.time.Clock()

### 원 그리기
# 랜덤 색
def rand_color():
    rand_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return rand_color

# 랜덤 위치
def rand_pos():
    rand_pos = random.randint(0, screen.get_width() - 1), random.randint(0, screen.get_height() - 1)
    return rand_pos

# 랜덤 크기
def rand_size(max = 70):
    rand_size = random.randint(0, max)
    return rand_size


pygame.display.flip()   # 화면 업데이트

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, rand_color(), rand_pos(), rand_size())
    
    pygame.display.flip()
    
    clock.tick(20)
    
pygame.quit()