from board import boards
import pygame
import math

pygame.init()

WIDTH = 900
HEIGHT = 950

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font(None, 20)
level = boards
color = 'blue'
PI = math.pi

def draw_board(lvl):
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)
    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            if lvl[i][j] == 1:  # 작은 점
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            
            if lvl[i][j] == 2:  # 큰 점
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            
            if lvl[i][j] == 3:  # 수직선 (| 형태)
                pygame.draw.line(screen, 'blue', (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            
            if lvl[i][j] == 4:  # 수평선 (- 형태)
                pygame.draw.line(screen, 'blue', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            
            if lvl[i][j] == 5:  # 왼쪽과 아래 방향 라인
                pygame.draw.line(screen, 'blue', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)),
                                 (j * num2, i * num1 + (0.5 * num1)), 3)  # 왼쪽으로
                pygame.draw.line(screen, 'blue', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)  # 아래로
            
            if lvl[i][j] == 6:  # 오른쪽과 아래 방향 라인
                pygame.draw.line(screen, 'blue', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)  # 오른쪽으로
                pygame.draw.line(screen, 'blue', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)  # 아래로
            
            if lvl[i][j] == 7:  # 오른쪽과 위 방향 라인
                pygame.draw.line(screen, 'blue', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)  # 오른쪽으로
                pygame.draw.line(screen, 'blue', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)),
                                 (j * num2 + (0.5 * num2), i * num1), 3)  # 위로
            
            if lvl[i][j] == 8:  # 왼쪽과 위 방향 라인
                pygame.draw.line(screen, 'blue', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)),
                                 (j * num2, i * num1 + (0.5 * num1)), 3)  # 왼쪽으로
                pygame.draw.line(screen, 'blue', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)),
                                 (j * num2 + (0.5 * num2), i * num1), 3)  # 위로

            if lvl[i][j] == 9:  # 수평선 (두꺼운)
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)


run = True
while run:
    timer.tick(fps)
    screen.fill((0, 0, 0))
    draw_board(level)
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()