import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

# 사각형을 X 축으로 이동

speed = 50   # 사각형의 X 축 이동 속도 :
x = 0       # 사각형의 현재 X 축 좌표 값

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 1/60 시간 만큼 프로그램을 stop 
    dt = clock.tick(60) / 1000 # clock.tick(fps number) -> 1 sec / fps number -> delta time
    

    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    # 사각형을 x, 120 지점에서 그린다. (가로 : 50, 세로: 100)
    pygame.draw.rect(screen, (255, 0, 0), (x, 120, 50, 100)) # Rect 객체 이용
        
    # 사각형의 x 좌표을 5 pixel 우측으로 이동
    x += dt * speed
    
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
    # 1/60 시간 만큼 프로그램을 stop 
    # clock.tick(60) # clock.tick(fps number) -> 1 sec / fps number -> delta time

pygame.quit()


