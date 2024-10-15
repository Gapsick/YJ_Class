import pygame
import random
import os
from board import boards

# Pygame 초기화
pygame.init()

# 환경 변수
WIDTH = 900
HEIGHT = 950

# 고스트의 방향을 나타내는 상수
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

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
player_path_1 = os.path.join('assets', 'player_images', '1.png')
player_path_2 = os.path.join('assets', 'player_images', '2.png')
player_path_3 = os.path.join('assets', 'player_images', '3.png')
player_path_4 = os.path.join('assets', 'player_images', '4.png')

# Ghost 이미지 경로
ghost_images = {
    "blue": os.path.join('assets', 'ghost_images', 'blue.png'),
    "orange": os.path.join('assets', 'ghost_images', 'orange.png'),
    "pink": os.path.join('assets', 'ghost_images', 'pink.png'),
    "red": os.path.join('assets', 'ghost_images', 'red.png')
}

# 이미지 로드
player_images = [
    pygame.transform.scale(pygame.image.load(player_path_1), (35, 35)),
    pygame.transform.scale(pygame.image.load(player_path_2), (35, 35)),
    pygame.transform.scale(pygame.image.load(player_path_3), (35, 35)),
    pygame.transform.scale(pygame.image.load(player_path_4), (35, 35))
]

# Ghost 이미지 로드
ghost_images_scaled = {color: pygame.transform.scale(pygame.image.load(path), (35, 35)) for color, path in ghost_images.items()}

# 초기 이미지와 Rect 설정
current_image = player_images[0]
player_rect = current_image.get_rect(topleft=(500, 500))

# 고스트 클래스
class Ghost:
    def __init__(self, rect, img, direction):
        self.rect = rect
        self.img = img
        self.direction = direction

    def move_toward_player(self, target):
        distance_x = target.x - self.rect.x
        distance_y = target.y - self.rect.y

        if abs(distance_x) > abs(distance_y):
            if distance_x > 0:
                self.rect.x += ghost_speed * dt
            else:
                self.rect.x -= ghost_speed * dt
        else:
            if distance_y > 0:
                self.rect.y += ghost_speed * dt
            else:
                self.rect.y -= ghost_speed * dt

    def move(self, board_rects):
        previous_position = self.rect.copy()

        # 고스트의 움직임 로직 (간단하게 플레이어를 추적하는 예시)
        self.move_toward_player(player_rect)

        # 충돌 감지 및 처리
        if self.rect.collidelist(board_rects) != -1:
            self.rect.update(previous_position)  # 벽에 충돌하면 이전 위치로 복구

            # 가능한 모든 방향 시도
            possible_directions = [UP, DOWN, LEFT, RIGHT]
            random.shuffle(possible_directions)  # 무작위 순서로 시도

            for new_direction in possible_directions:
                if new_direction == UP:
                    self.rect.y -= ghost_speed * dt
                elif new_direction == DOWN:
                    self.rect.y += ghost_speed * dt
                elif new_direction == LEFT:
                    self.rect.x -= ghost_speed * dt
                elif new_direction == RIGHT:
                    self.rect.x += ghost_speed * dt

                # 새로운 방향으로 이동 후 충돌이 발생하지 않으면 방향을 업데이트
                if self.rect.collidelist(board_rects) == -1:
                    self.direction = new_direction
                    break
                else:
                    self.rect.update(previous_position)  # 다시 이전 위치로 되돌림

    def draw(self, screen):
        screen.blit(self.img, self.rect)

# Ghost 초기화
ghosts = [
    Ghost(pygame.Rect(380, 400, 35, 35), ghost_images_scaled["blue"], random.choice([UP, DOWN, LEFT, RIGHT])),
    Ghost(pygame.Rect(480, 400, 35, 35), ghost_images_scaled["orange"], random.choice([UP, DOWN, LEFT, RIGHT])),
    Ghost(pygame.Rect(380, 450, 35, 35), ghost_images_scaled["pink"], random.choice([UP, DOWN, LEFT, RIGHT])),
    Ghost(pygame.Rect(480, 450, 35, 35), ghost_images_scaled["red"], random.choice([UP, DOWN, LEFT, RIGHT]))
]

# 이미지 스피드
player_speed = 200
ghost_speed = 100

# 보드 그리기 함수
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

    # 고스트 움직임
    for ghost in ghosts:
        ghost.move(board_rects)
    
    
    # 키 입력 처리
    keys = pygame.key.get_pressed()
    previous_rect = player_rect.copy()

    if keys[pygame.K_LEFT]:
        current_image = player_images[0]
        player_rect.x -= player_speed * dt
    if keys[pygame.K_RIGHT]:
        current_image = player_images[1]
        player_rect.x += player_speed * dt
    if keys[pygame.K_UP]:
        current_image = player_images[2]
        player_rect.y -= player_speed * dt
    if keys[pygame.K_DOWN]:
        current_image = player_images[3]
        player_rect.y += player_speed * dt
        
    # 충돌 검사 및 아이템 삭제
    item_index = player_rect.collidelist(item_rects)
    if item_index != -1:
        del item_rects[item_index]  # 충돌한 아이템 Rect 삭제
        del item_types[item_index]  # 충돌한 아이템 타입 삭제
        score += 10
    
    if player_rect.collidelist(board_rects) != -1:
        player_rect = previous_rect  # 충돌 시 이전 위치로 복구
    
    # 화면을 검정으로 채우기
    screen.fill(BLACK)
    
    # 보드 그리기
    draw_board(level)
    
    # 남아있는 아이템 그리기
    for index, rect in enumerate(item_rects):
        if item_types[index] == 1:
            pygame.draw.circle(screen, WHITE, rect.center, 4)
        elif item_types[index] == 2:
            pygame.draw.circle(screen, WHITE, rect.center, 10)
    
    # 플레이어 이미지 그리기
    screen.blit(current_image, player_rect)
    
    # Ghost 그리기
    for ghost in ghosts:
        ghost.draw(screen)
    
    # Score 그리기
    Score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(Score_text, (10, HEIGHT -30))

    # 화면 업데이트
    pygame.display.flip()

pygame.quit()