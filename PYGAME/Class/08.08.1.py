import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# 사각형 정의
rect1 = pygame.Rect(screen.get_width()/2 - 40 , 0, 80, 40)
# rect2 = pygame.Rect(screen.get_width()/2 - 150 , screen.get_height()/2 - 100, 300, 200)
rect2 = pygame.Rect(0, 0, 300, 200)
rect2.center = screen.get_rect().center

# 객체 이동 속도
speed = 300 # 300 pixel / second

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000 # dt 프로그램 실행 멈춤    
    
    keys = pygame.key.get_pressed()
    
    # 왼쪽 방향키가 눌러졌을 때
    if keys[pygame.K_LEFT]:
        rect1.x = rect1.x - speed * dt      

    # 오른쪽 방향키가 눌러졌을 때
    if keys[pygame.K_RIGHT]:
        rect1.x += speed * dt 
        
    # 아래쪽 방향키가 눌러졌을 때
    if keys[pygame.K_DOWN]:
        rect1.y += speed * dt
    
    # 위쪽 방향키가 눌러졌을 때
    if keys[pygame.K_UP]:
        rect1.y -= speed * dt
    
    # 화면 경계 처리
    rect1.x = max(0, min(rect1.x, screen.get_width() - rect1.width))
    rect1.y = max(0, min(rect1.y, screen.get_height() - rect1.height))
    
    if rect1.colliderect(rect2):
        print("충돌 발생")
    
    
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), rect2)
    pygame.draw.rect(screen, (0, 0, 255), rect1) # Rect 객체 이용
    
    
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
    
pygame.quit()


