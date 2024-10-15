import pygame
import os

# Pygame 초기화
pygame.init()

# 환경 변수 설정
WIDTH = 900
HEIGHT = 950
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# 윈도우 설정
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

# 폰트 및 점수 초기화
font = pygame.font.Font(None, 36)
score = 0

# 플레이어와 고스트의 초기 설정
player_speed = 200
player_rect = pygame.Rect(500, 500, 35, 35)  # 플레이어의 위치와 크기 설정

# 고스트 초기 설정 (여기서 고스트들의 위치와 이미지를 설정할 수 있음)
list_ghost_rect = [
    pygame.Rect(380, 400, 35, 35),
    pygame.Rect(480, 400, 35, 35),
    pygame.Rect(380, 450, 35, 35),
    pygame.Rect(480, 450, 35, 35),
]

# 보드 그리기 함수 (여기서 맵과 벽을 그릴 수 있음)
def draw_board():
    # 보드, 벽 등의 요소를 그리고, 필요한 Rect 객체들을 반환
    board_rects = []
    # ... 보드 그리기 로직 ...
    return board_rects

# 아이템 생성 함수
def generate_items():
    item_rects = []
    item_types = []  # 아이템의 종류를 저장
    # ... 아이템 생성 로직 ...
    return item_rects, item_types

# 게임 초기화
board_rects = draw_board()
item_rects, item_types = generate_items()

# 게임 루프
running = True
while running:
    # 델타 타임 계산
    dt = clock.tick(60) / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 플레이어 이동 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed * dt
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed * dt
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed * dt
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed * dt

    # 충돌 검사 및 아이템 처리
    item_index = player_rect.collidelist(item_rects)
    if item_index != -1:
        del item_rects[item_index]
        del item_types[item_index]
        score += 10
    
    if player_rect.collidelist(board_rects) != -1:
        # 벽과 충돌 시 위치 복구
        pass

    # 화면 그리기
    screen.fill(BLACK)
    draw_board()  # 보드 다시 그리기
    
    for index, rect in enumerate(item_rects):
        if item_types[index] == 1:
            pygame.draw.circle(screen, WHITE, rect.center, 4)
        elif item_types[index] == 2:
            pygame.draw.circle(screen, WHITE, rect.center, 10)

    # 플레이어 및 고스트 그리기
    pygame.draw.rect(screen, WHITE, player_rect)  # 플레이어는 단순히 사각형으로 표현
    for ghost_rect in list_ghost_rect:
        pygame.draw.rect(screen, BLUE, ghost_rect)  # 고스트도 단순히 사각형으로 표현
    
    # 점수 표시
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, HEIGHT - 30))
    
    pygame.display.flip()

pygame.quit()
