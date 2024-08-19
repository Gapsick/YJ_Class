import pygame
import sys

# 초기화
pygame.init()

# 화면 크기
screen = pygame.display.set_mode((800, 600))

# FPS 설정
clock = pygame.time.Clock()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (165, 42, 42)

# 벽돌 위치 설정
brick_positions = [(50 + i * 70, 50 + j * 30, 55, 20) for i in range(10) for j in range(5)]

# 스피드 설정
speed_x = 5
speed_y = 5

# 원 반지름
radius = 10

# 원 위치
x = 400
y = 300

# 벽돌 그리기
def draw_bricks(bricks):
    for brick in bricks:
        pygame.draw.rect(screen, BROWN, brick)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면을 흰색으로 설정
    screen.fill(WHITE)

    # 벽돌 그리기
    draw_bricks(brick_positions)

    # 공 그리기
    pygame.draw.circle(screen, BLACK, (x, y), radius)

    # 공 이동
    x += speed_x
    y += speed_y

    # 공 튕기기
    if x - radius <= 0 or x + radius >= screen.get_width():
        speed_x = -speed_x
    if y - radius <= 0:
        speed_y = -speed_y
    if y + radius >= screen.get_height():
        print("Game Over")
        running = False

    # 벽돌 부수기
    for brick in brick_positions:
        brick_x, brick_y, brick_w, brick_h = brick
        if brick_x <= x <= brick_x + brick_w and brick_y <= y <= brick_y + brick_h:
            brick_positions.remove(brick)
            speed_y = -speed_y
            break

    # 화면 업데이트
    pygame.display.flip()

    # FPS 설정
    clock.tick(30)

pygame.quit()
sys.exit()
