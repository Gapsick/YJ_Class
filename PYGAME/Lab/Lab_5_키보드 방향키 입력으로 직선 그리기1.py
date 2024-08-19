# 800, 600 픽셀 크기의 파이게임 윈도우에서 시작점을 화면의 중앙으로 설정
# 키보드의 방향키를 이용하여 해당 방향으로 직선을 연장하여 그린다
# 각 방향키를 누를 때마다 직선을 10 픽셀씩 해당 방향으로 연장되며, 직선의 색상은 초기에 무작위로 설정

# 구현 요구 사항
# 시작점을 화면의 중앙(400, 300)으로 설정
# 방향키 입력에 따라 시작점에서 시작하여 직선을 해당 방향으로 10픽셀씩 연장하라
# 각 직선의 끝점은 새로운 시작점이 된다
# 직선의 색상은 프로그램 시작 시 무작위로 결정되며, 이후에는 동일한 색상을 유지한다

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

# 무작위 색상 생성
rand_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

# 시작점 (화면 중앙)
start_width, start_height = screen.get_width() / 2, screen.get_height() / 2

# 화면 색상
screen.fill((255, 255, 255))

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.draw.line(screen, rand_color, (start_width, start_height), (start_width, start_height - 10))
                start_height -= 10
            elif event.key == pygame.K_DOWN:
                pygame.draw.line(screen, rand_color, (start_width, start_height), (start_width, start_height + 10))
                start_height += 10
            elif event.key == pygame.K_LEFT:
                pygame.draw.line(screen, rand_color, (start_width, start_height), (start_width - 10, start_height))
                start_width -= 10
            elif event.key == pygame.K_RIGHT:
                pygame.draw.line(screen, rand_color, (start_width, start_height), (start_width + 10, start_height))
                start_width += 10
    
    pygame.display.flip()

pygame.quit()