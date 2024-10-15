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
def brick_pos():
    a, b, c, d = 375, 100, 55, 40
    return (a, b, c, d)

# 스피드 설정
speed = 5

# 원 반지름
radius = 10

# 원 위치
x = 400
y = 500

# 패들 설정
paddle_width = 100
paddle_height = 10
paddle_x = 350
paddle_y = 580
paddle_speed = 10

# 벽돌 그리기
def Brick1():
    return pygame.draw.rect(screen, BROWN, brick_pos())

brick_visible = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < 800 - paddle_width:
        paddle_x += paddle_speed

    # 화면을 흰색으로 설정
    screen.fill(WHITE)

    # 벽돌 그리기
    if brick_visible:
        try:
            Brick1()
        except Exception as e:
            print(f"An error occurred: {e}")

    # 패들 그리기
    pygame.draw.rect(screen, BLACK, (paddle_x, paddle_y, paddle_width, paddle_height))

    # 공 그리기
    pygame.draw.circle(screen, BLACK, (x, y), radius)

    # 공 이동
    y -= speed

    # 공 튕기기
    if y - radius <= 0:
        speed = -speed

    if y + radius >= screen.get_height():
        print("Game Over")
        running = False

    # 패들과 공의 충돌 처리
    if paddle_y <= y + radius <= paddle_y + paddle_height and \
            paddle_x <= x <= paddle_x + paddle_width:
        speed = -speed

    # 벽돌 부수기
    if brick_pos()[0] <= x <= brick_pos()[0] + brick_pos()[2] and \
            brick_pos()[1] <= y <= brick_pos()[1] + brick_pos()[3]:
        brick_visible = False
        speed = -speed

    # 화면 업데이트
    pygame.display.flip()

    # FPS 설정
    clock.tick(30)

pygame.quit()
sys.exit()
