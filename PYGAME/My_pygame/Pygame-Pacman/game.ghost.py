import pygame
import os
from board import boards

# Pygame 초기화
pygame.init()

# 환경 변수
WIDTH = 900
HEIGHT = 950

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
# Score
font = pygame.font.Font(None, 36)
score = 0


level = boards
clock = pygame.time.Clock()

# 윈도우 크기 설정
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# 이미지 파일 경로 설정
ghost_path_1 = os.path.join('assets', 'ghost_images', 'blue.png')
ghost_path_2 = os.path.join('assets', 'ghost_images', 'orange.png')
ghost_path_3 = os.path.join('assets', 'ghost_images', 'pink.png')
ghost_path_4 = os.path.join('assets', 'ghost_images', 'red.png')
ghost_path_5 = os.path.join('assets', 'ghost_images', 'dead.png')
ghost_path_6 = os.path.join('assets', 'ghost_images', 'powerup.png')


# 이미지 로드
list_ghost_img = []

ghost_blue = pygame.image.load(ghost_path_1)
ghost_blue = pygame.transform.scale(ghost_blue, (35, 35))
list_ghost_img.append(ghost_blue)

ghost_orange = pygame.image.load(ghost_path_2)
ghost_orange = pygame.transform.scale(ghost_orange, (35, 35))
list_ghost_img.append(ghost_orange)

ghost_pink = pygame.image.load(ghost_path_3)
ghost_pink = pygame.transform.scale(ghost_pink, (35, 35))
list_ghost_img.append(ghost_pink)

ghost_red = pygame.image.load(ghost_path_4)
ghost_red = pygame.transform.scale(ghost_red, (35, 35))
list_ghost_img.append(ghost_red)

ghost_dead = pygame.image.load(ghost_path_5)
ghost_dead = pygame.transform.scale(ghost_dead, (35, 35))
list_ghost_img.append(ghost_dead)

ghost_powerup = pygame.image.load(ghost_path_6)
ghost_powerup = pygame.transform.scale(ghost_powerup, (35, 35))
list_ghost_img.append(ghost_powerup)


# 초기 이미지와 Rect 설정
list_ghost_rect = []

ghost_blue_rect = ghost_blue.get_rect(topleft=(380, 400))
list_ghost_rect.append(ghost_blue_rect)

ghost_orange_rect = ghost_orange.get_rect(topleft=(480, 400))
list_ghost_rect.append(ghost_orange_rect)

ghost_pink_rect = ghost_pink.get_rect(topleft=(380, 450))
list_ghost_rect.append(ghost_pink_rect)

ghost_red_rect = ghost_red.get_rect(topleft=(480, 450))
list_ghost_rect.append(ghost_red_rect)

ghost_dead_rect = ghost_red.get_rect(topleft=(0, 0))
list_ghost_rect.append(ghost_dead_rect)

ghost_powerup_rect = ghost_red.get_rect(topleft=(0, 0))
list_ghost_rect.append(ghost_powerup_rect)


# board
def draw_board(lvl):
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)
    
    board_rects = []  # Rect 객체를 저장할 리스트

    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            center_x = j * num2 + (0.5 * num2)
            center_y = i * num1 + (0.5 * num1)
            
            if lvl[i][j] == 3:  # 수직선 (| 형태)
                line_width = 3
                pygame.draw.line(screen, BLUE, (center_x, i * num1), (center_x, i * num1 + num1), line_width)
                rect = pygame.Rect(center_x - line_width / 2, i * num1, line_width, num1)
                board_rects.append(rect)
            
            elif lvl[i][j] == 4:  # 수평선 (- 형태)
                line_width = 3
                pygame.draw.line(screen, BLUE, (j * num2, center_y), (j * num2 + num2, center_y), line_width)
                rect = pygame.Rect(j * num2, center_y - line_width / 2, num2, line_width)
                board_rects.append(rect)
            
            elif lvl[i][j] == 5:  # 왼쪽과 아래 방향 라인
                line_width = 3
                pygame.draw.line(screen, BLUE, (center_x, center_y), (j * num2, center_y), line_width)  # 왼쪽으로
                pygame.draw.line(screen, BLUE, (center_x, center_y), (center_x, i * num1 + num1), line_width)  # 아래로
                rect1 = pygame.Rect(j * num2, center_y - line_width / 2, 0.5 * num2, line_width)
                rect2 = pygame.Rect(center_x - line_width / 2, center_y, line_width, 0.5 * num1)
                board_rects.append(rect1)
                board_rects.append(rect2)
            
            elif lvl[i][j] == 6:  # 오른쪽과 아래 방향 라인
                line_width = 3
                pygame.draw.line(screen, BLUE, (center_x, center_y), (j * num2 + num2, center_y), line_width)  # 오른쪽으로
                pygame.draw.line(screen, BLUE, (center_x, center_y), (center_x, i * num1 + num1), line_width)  # 아래로
                rect1 = pygame.Rect(center_x, center_y - line_width / 2, 0.5 * num2, line_width)
                rect2 = pygame.Rect(center_x - line_width / 2, center_y, line_width, 0.5 * num1)
                board_rects.append(rect1)
                board_rects.append(rect2)
            
            elif lvl[i][j] == 7:  # 오른쪽과 위 방향 라인
                line_width = 3
                pygame.draw.line(screen, BLUE, (center_x, center_y), (j * num2 + num2, center_y), line_width)  # 오른쪽으로
                pygame.draw.line(screen, BLUE, (center_x, center_y), (center_x, i * num1), line_width)  # 위로
                rect1 = pygame.Rect(center_x, center_y - line_width / 2, 0.5 * num2, line_width)
                rect2 = pygame.Rect(center_x - line_width / 2, i * num1, line_width, 0.5 * num1)
                board_rects.append(rect1)
                board_rects.append(rect2)
            
            elif lvl[i][j] == 8:  # 왼쪽과 위 방향 라인
                line_width = 3
                pygame.draw.line(screen, BLUE, (center_x, center_y), (j * num2, center_y), line_width)  # 왼쪽으로
                pygame.draw.line(screen, BLUE, (center_x, center_y), (center_x, i * num1), line_width)  # 위로
                rect1 = pygame.Rect(j * num2, center_y - line_width / 2, 0.5 * num2, line_width)
                rect2 = pygame.Rect(center_x - line_width / 2, i * num1, line_width, 0.5 * num1)
                board_rects.append(rect1)
                board_rects.append(rect2)

            elif lvl[i][j] == 9:  # 수평선 (두꺼운)
                line_width = 3
                pygame.draw.line(screen, WHITE, (j * num2, center_y), (j * num2 + num2, center_y), line_width)
                # rect = pygame.Rect(j * num2, center_y - line_width / 2, num2, line_width)
                # board_rects.append(rect)

    return board_rects


def generate_items(lvl):
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)
    
    item_rects = []
    item_types = []  # 아이템의 종류 (작은 점, 큰 점 등)을 저장

    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            center_x = j * num2 + (0.5 * num2)
            center_y = i * num1 + (0.5 * num1)
            
            if lvl[i][j] == 1:  # 작은 점
                rect = pygame.Rect(center_x - 4, center_y - 4, 8, 8)
                item_rects.append(rect)
                item_types.append(1)  # 작은 점 표시
            
            elif lvl[i][j] == 2:  # 큰 점
                rect = pygame.Rect(center_x - 10, center_y - 10, 20, 20)
                item_rects.append(rect)
                item_types.append(2)  # 큰 점 표시

    return item_rects, item_types


# 맵과 아이템 초기화
board_rects = draw_board(level)
item_rects, item_types = generate_items(level)

# 윈도우 루프
running = True
while running:
    
    # 델타 타임 계산 (초 단위 경과 시간)
    dt = clock.tick(60) / 1000.0  # 60 FPS로 제한
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False







    # 화면을 검정으로 채우기
    screen.fill(BLACK)
    
    # Ghost 그리기
    for index in range(4):
        screen.blit(list_ghost_img[index], list_ghost_rect[index])
    
    # 보드 그리기
    draw_board(level)
    
    # 남아있는 아이템 그리기
    for index, rect in enumerate(item_rects):
        if item_types[index] == 1:
            pygame.draw.circle(screen, WHITE, rect.center, 4)
        elif item_types[index] == 2:
            pygame.draw.circle(screen, WHITE, rect.center, 10)
    
    # 화면 업데이트
    pygame.display.flip()

pygame.quit()
