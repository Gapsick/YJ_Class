import random
import pygame

pygame.init()

# 게임 변수 설정
screen_width = 800
screen_height = 600

# 장애물
obs_width = 100
obs_height = 50
num_of_obs = 20

# 아이템
item_width = 20
item_height = 20
num_of_item = 10

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# 장애물 생성
obs_list = []
for _ in range(num_of_obs):
    while True:
        # 사각형을 랜덤한 위치에 생성
        rect1_x = random.randint(0, screen_width - obs_width) # 0 ~ 540 X
        rect1_y = random.randint(0, screen_height - obs_height ) # 0 ~ 430 Y
        rect = pygame.Rect(rect1_x, rect1_y, obs_width, obs_height)
        
        # 생성된 사각형이 기존 사각형의 충돌이 일어나지 않을 경우
        if rect.collidelist(obs_list) == -1:
           # 생성된 사각형을 리스트에 추가
           obs_list.append(rect)
           break

# 아이템 생성
item_list = []
for _ in range(num_of_item):
    while True:
        item_x = random.randint(0, screen_width - item_width)
        item_y = random.randint(0, screen_height - item_height)
        item = pygame.Rect(item_x, item_y, item_width, item_height)
        
        # item이 기존 item과 충돌하지 않고 and 장애물(Obstacle)과도 충돌하지 않을 경우 
        if item.collidelist(item_list) == -1 and\
                                            item.collidelist(obs_list) == -1:
            item_list.append(item)
            break


while running:
    # << -- 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # -- >> 

    # <<-- 화면 그리기
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    # 장애물 그리기
    for rect in obs_list:
        pygame.draw.rect(screen, (255, 0, 0), rect) # Rect 객체 이용
    
    # 아이템 그리기
    for rect in item_list:
        pygame.draw.rect(screen, (0, 0, 255), rect) # Rect 객체 이용
    
    pygame.display.flip()
    # -->>
    
    # FPS 설정
    clock.tick(60)

pygame.quit()


