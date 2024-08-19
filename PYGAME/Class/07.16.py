# import pygame

# pygame.init()

# screen = pygame.display.set_mode((640, 480))

# running = True
# while running: # while : event 를 "듣는" 역할을 수행 (Evnet Listener)
#     for event in pygame.event.get(): # Front ~ near까지의 모든 Event들을 순차적으로 list형태로 들고 오는 것
#         if event.type == pygame.QUIT:
#             running = False

# pygame.quit()

# 이벤트를 담기위해 자료구조가 필요한데, Queue 라는 자료구조를 사용한다. pygame안에서 내부적으로 구현되어 있음
# Queue 특징: First in First out (FIFO), 순차적으로 실행
# 버퍼(링)도 Queue의 구조
# event가 많을시 queue의 길이를 길게하면되는데,
# queue에 길이를 길게 할시 메모리가 많이 먹고, service time이 길어질수록 drop이 될수도 있음

### pygame.event.get()이란?
# event들이 queue에 발생한 순서대로 차곡 쌓이는데, pygame.event.get()을 하는 순간 queue에 쌓인 event들을
# 싹다 list형태로 들고 오는 것
# event는 안에있는 어플리케이션을 통해 발생시킴

# event handler란?
# for문을 돌리며 각 특정 event에 맞는 함수나 메서드를 호출 하는 것

# import pygame

# pygame.init()

# screen = pygame.display.set_mode((640, 480))

# running = True
# while running: # while : event 를 "듣는" 역할을 수행 (Evnet Listener)
#     for event in pygame.event.get(): # Front ~ near까지의 모든 Event들을 순차적으로 list형태로 들고 오는 것
#         if event.type == pygame.QUIT:
#             running = False

    
#     # 이벤트 처리가 끝난 후
#     screen.fill((0, 0, 0)) # 이벤트가 발생 할때
    
#     pygame.draw.circle(screen, (0,255,0), (100, 200), 40)
#     pygame.draw.circle(screen, (255,0,0), (300, 500), 40)
    
#     pygame.display.flip() # 읽고 오는데 시간이 걸리기 때문에, 메모리에 그림을 그린후, 한방에 빡 출력
    
# pygame.quit()

# while문 순서 -> 그림을 그리는 순서
# memory에 그림을 그린후 한번에 출력
# get 메소드 호출하면, queue에 쌓인 event들이 list형태로 출력

### Frame Rate
# FPS : Frame per second
# FPS가 높으면 뭐가 문제일까~?
# 스무스하게 움직이겠지만, file의 size가 올라간다.
# Conficting power가 더 필요하다.
# 컴퓨터 성능에 따라 fps가 달라지기 때문에, fps의 설정이 필요하다.

# 공 만들기

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

x = screen.get_width() / 2
y = screen.get_height() / 2
radius = 40
speed = 5
clock = pygame.time.Clock()

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 40)
    
    if x + radius >= screen.get_width() or x - radius <= 0:
        speed = -speed
    
    x += speed
    
    pygame.display.flip()

    clock.tick(60)
    
pygame.quit()


# 1 / FPS(30) = 1 / 30 = 0.016second = 16ms
# Delta time = ms