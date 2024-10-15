import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# 사각형 정의
rect1 = pygame.Rect(360, 260, 80, 40)

# 객체 이동 속도
speed = 100 # 100 pixel / 1 sec
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == pygame.KEYDOWN: # 키보드가 눌러졌다.
            if event.key == pygame.K_LEFT: # 어떤 key가 눌러졌습니까
                rect1.x -= speed
            if event.key == pygame.K_RIGHT: # 어떤 key가 눌러졌습니까
                rect1.x += speed
        

    dt = clock.tick(60) / 1000

    # <-, -> Key를 누를 때 사각형을 좌우로 이동.
    # keys = pygame.key.get_pressed()
    
    # if keys[pygame.K_LEFT]:
    #     rect1.x -= speed
    # if keys[pygame.K_RIGHT]:
    #     rect1.x += speed
    
    # 화면 나가지마
    if rect1.x < 0:
        rect1.x = 0

    if rect1.x + rect1.width > screen.get_width():
        rect1.x = screen.get_width() - rect1.width    
    
    # rect1.y += speed * dt
    
    
    # if rect1.bottom > screen.get_height():
    #     rect1.y = screen.get_height() - rect1.height
    #     speed = -speed
        
    # if rect1.y < 0:
    #     rect1.y = 0
    #     speed = -speed

    # if rect1.x + rect1.width > screen.get_width():
    #     rect1.x = screen.get_width() - rect1.width
    #     speed = -speed 
    
    # if rect1.x < 0:
    #     rect1.x = 0
    #     speed = -speed
    
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 255), rect1) # Rect 객체 이용
    
    
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
    
pygame.quit()


