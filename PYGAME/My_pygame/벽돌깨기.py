import pygame

# 초기화
pygame.init()

# 화면 크기
screen = pygame.display.set_mode((800, 600))

# FPS설정
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

# 벽돌 그리기
def Brick1():
    return pygame.draw.rect(screen, BROWN, brick_pos())

# 벽돌 참
brick_visible = True

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 화면을 흰색으로 설정
    screen.fill(WHITE)
    
    # 벽돌 그리기
    if brick_visible:
        try:
            Brick1()
        except Exception as e:
            print(f"An error occurred: {e}")
    
    # 공 그리기
    pygame.draw.circle(screen, BLACK, (x, y), radius)
    
    # 공 이동
    y -= speed
    
    # 공 튕기기
    if y + radius >= screen.get_height() or y - radius <= 0:
        speed = -speed
    
    # 벽돌 부셔버리기
    if brick_pos()[0] <= x <= brick_pos()[0] + brick_pos()[2] and \
        brick_pos()[1] <= y <= brick_pos()[1] + brick_pos()[3]:
        brick_visible = False
        speed = -speed
    
    
    # 화면 업데이트
    pygame.display.flip()
    
    # FPS 설정
    clock.tick(30)

pygame.quit