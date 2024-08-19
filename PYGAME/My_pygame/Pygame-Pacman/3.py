import pygame
import math
import os
from board import boards

# Pygame 초기화
pygame.init()

# 환경 변수
WIDTH = 900
HEIGHT = 950

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

level = boards
PI = math.pi

clock = pygame.time.Clock()


# 윈도우 크기 설정
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# 이미지 파일 경로 설정
player_path_1 = os.path.join('assets', 'player_images', '1.png')
player_path_2 = os.path.join('assets', 'player_images', '2.png')
player_path_3 = os.path.join('assets', 'player_images', '3.png')
player_path_4 = os.path.join('assets', 'player_images', '4.png')

# 이미지 로드
player1 = pygame.image.load(player_path_1)
player1 = pygame.transform.scale(player1, (35, 35))

player2 = pygame.image.load(player_path_2)
player2 = pygame.transform.scale(player2, (35, 35))

player3 = pygame.image.load(player_path_3)
player3 = pygame.transform.scale(player3, (35, 35))

player4 = pygame.image.load(player_path_4)
player4 = pygame.transform.scale(player4, (35, 35))

# 초기 이미지와 Rect 설정
current_image = player1
player_rect = current_image.get_rect(topleft=(500, 500))

# 이미지 스피드
player_speed = 200

# board
def draw_board(lvl):
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)
    
    item_rects = []
    board_rects = []  # Rect 객체를 저장할 리스트

    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            center_x = j * num2 + (0.5 * num2)
            center_y = i * num1 + (0.5 * num1)
            
            if lvl[i][j] == 1:  # 작은 점
                pygame.draw.circle(screen, WHITE, (center_x, center_y), 4)
                rect = pygame.Rect(center_x - 4, center_y - 4, 8, 8)
                item_rects.append(rect)
            
            elif lvl[i][j] == 2:  # 큰 점
                pygame.draw.circle(screen, WHITE, (center_x, center_y), 10)
                rect = pygame.Rect(center_x - 10, center_y - 10, 20, 20)
                item_rects.append(rect)
            
            elif lvl[i][j] == 3:  # 수직선 (| 형태)
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
                rect = pygame.Rect(j * num2, center_y - line_width / 2, num2, line_width)
                board_rects.append(rect)

    return board_rects, item_rects


board_rects, item_rects = draw_board(level)

# 윈도우 루프
running = True
while running:
    
    # 델타 타임 계산 (초 단위 경과 시간)
    dt = clock.tick(60) / 1000.0  # 60 FPS로 제한
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    previous_rect = player_rect.copy()  # 이전 위치 저장

    if keys[pygame.K_LEFT]:  # 왼쪽 화살표 키로 플레이어 이동
        current_image = player1
        player_rect.x -= player_speed * dt  # 델타 타임을 사용하여 프레임 독립적 이동
    if keys[pygame.K_RIGHT]:  # 오른쪽 화살표 키로 플레이어 이동
        current_image = player2
        player_rect.x += player_speed * dt  # 델타 타임을 사용하여 프레임 독립적 이동
    if keys[pygame.K_UP]:  # 왼쪽 화살표 키로 플레이어 이동
        current_image = player3
        player_rect.y -= player_speed * dt  # 델타 타임을 사용하여 프레임 독립적 이동
    if keys[pygame.K_DOWN]:  # 왼쪽 화살표 키로 플레이어 이동
        current_image = player4
        player_rect.y += player_speed * dt  # 델타 타임을 사용하여 프레임 독립적 이동
        
    # 충돌 검사
    item_index = player_rect.collidelist(item_rects)
    if item_index != -1:
        del item_rects[item_index]
    
    
    if player_rect.collidelist(board_rects) != -1:
        player_rect = previous_rect  # 충돌 시 이전 위치로 복구
    
    # 화면을 검정으로 채우기
    screen.fill(BLACK)
    
    # 맵 그리기 (이제 item_rects와 board_rects가 유지됩니다)
    draw_board(level)
    
    # 아이템 사각형들 다시 그리기
    for item_rect in item_rects:
        pygame.draw.rect(screen, WHITE, item_rect)
    
    # 이미지 그리기
    screen.blit(current_image, player_rect)

    # 화면 업데이트
    pygame.display.flip()

pygame.quit()
