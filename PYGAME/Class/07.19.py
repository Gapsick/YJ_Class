import pygame

## <<--- 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))

# # <<-- fps 적용을 위한 시간 객체 생성
clock = pygame.time.Clock()
fps = 60
## -->>


x = screen.get_width() / 2
y = screen.get_height() / 2
radius = 40
speed = 10 # FPS 300 pixel/second

## <<--- 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    
    
    dt = clock.tick(fps)/1000.0
    


    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    x += (speed * dt)

    if x + radius >= screen.get_width() or x - radius <= 0:
        speed = -speed

    ## -->>
## -->> 이미지 생성

    pygame.display.flip()

## 게임 종료
pygame.quit()


# delta time 이미지와 이미지의 시간