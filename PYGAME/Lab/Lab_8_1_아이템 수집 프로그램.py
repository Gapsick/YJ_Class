import pygame
import random

pygame.init()


screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
speed = 300
fps = 60

# 장애물 및 아이템 생성
# obstacle
obstacle_list = []
for _ in range(5):
    while True:
        obstacle = pygame.Rect(random.randint(0, 750), random.randint(0, 550), 50, 50)
        check = obstacle.collidelist(obstacle_list)
        if check == -1:
            obstacle_list.append(obstacle)
            break

print(obstacle_list)

# item
item_list = []
for _ in range(3):
    while True:
        item = pygame.Rect(random.randint(0, 790), random.randint(0, 590), 10, 10)
        check1 = item.collidelist(obstacle_list)
        check2 = item.collidelist(item_list)
        if check1 == -1 and check2 == -1:
            item_list.append(item)
            break

print(item_list)

# 플레이어 조작 사각형 생성
while True:
    player = pygame.Rect(random.randint(0, 750), random.randint(0, 550), 50, 50)
    
    check1 = player.collidelist(obstacle_list)
    check2 = player.collidelist(item_list)
    if check1 and check2 == -1:
        break


# 게임 시작
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # dt 설정
    delta_speed = speed * (clock.tick(fps) / 1000.0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 이전 위치
    previous_position = player.topleft
    
    
    
    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= delta_speed
    if keys[pygame.K_RIGHT]:
        player.x += delta_speed    
    if keys[pygame.K_UP]:
        player.y -= delta_speed
    if keys[pygame.K_DOWN]:
        player.y += delta_speed

    
    # 화면 색상
    screen.fill((255, 255, 255))
    
    # 충돌 감지 및 처리
    # 장애물 충돌
    obstacle_crash = player.collidelist(obstacle_list)
    if obstacle_crash != -1:
        player.topleft = previous_position
    
    # 아이템 충돌
    item_index = player.collidelistall(item_list)
    if item_index:
        item_list[item_index]
    

    
    
    
    
    
    # 장애물, 아이템, 플래이어 화면에 출력
    # 장애물
    for obstacle in obstacle_list:
        pygame.draw.rect(screen, (0, 0, 255), obstacle)
      
    # 아이템
    for item in item_list:
        pygame.draw.rect(screen, (255, 255, 0), item)
    
    # 플래이어
    pygame.draw.rect(screen, (255, 0, 0), player)
    
    
    
    
    # 게임 종료
    if not item_list:
        print("모든 아이템을 수집했습니다! 승리!")
        running = False
    
    # 화면 출력
    pygame.display.flip()
    

pygame.quit()