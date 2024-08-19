import pygame
import random

pygame.init()

# 화면 설정
screen_width = 800
screen_height = 1200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Galaga Game")

# 폰트 설정
font = pygame.font.Font(None, 36)

# 이미지 로드
my_ship = pygame.image.load("My_pygame/내 우주선.png")
enemy_ship = pygame.image.load("My_pygame/상대 우주선.png")
my_missile = pygame.image.load("My_pygame/내 미사일.png")
enemy_missile = pygame.image.load("My_pygame/상대 미사일.png")

# 현재 스테이지 변수
stage = 1

# 내 우주선
my_ship_rect = my_ship.get_rect()
my_ship_rect.topleft = (screen_width / 2 - my_ship_rect.x / 2, screen_height - 100)

# 적 우주선 리스트
list_enemy_ship = []

# 적 생성 함수
def create_enemy_ships(num):
    for _ in range(num):
        while True:
            list_num = [50, 100, 150]
            enemy_ship_rect = enemy_ship.get_rect()
            enemy_ship_rect.x = random.randint(0, my_ship_rect.width)
            rect = pygame.Rect(random.randint(0, screen_width - enemy_ship_rect.width), list_num[random.randint(0, 2)], 50, 50)
            if rect.collidelist(list_enemy_ship) == -1:
                list_enemy_ship.append(rect)
                break
    return list_enemy_ship

# 내 미사일
list_my_missile = []
def create_my_missile():
    my_missile_rect = my_missile.get_rect()
    my_missile_rect.midtop = my_ship_rect.midtop
    return my_missile_rect

# 적 미사일
list_enemy_missile = []
def create_enemy_missile():
    for num in range(5):
        enemy_rect = list_enemy_ship[num]
        enemy_missile_rect = enemy_rect.get_rect
        enemy_missile_rect.y = enemy_rect.midtop
        list_enemy_missile.append(enemy_missile_rect)

# 첫 스테이지 적 생성
create_enemy_ships(stage * 2)

# 배경설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 이동속도 설정
speed = 300
delta_speed = 0

# FPS 설정
clock = pygame.time.Clock()
fps = 60


# 게임 시작
running = True
while running:
    
    delta_speed = speed * (clock.tick(fps) / 1000.0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: # 키보드가 눌러졌다.
            if event.key == pygame.K_LCTRL: # 어떤 key가 눌러졌습니까
                list_my_missile.append(create_my_missile())

    # 키 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        my_ship_rect.x -= delta_speed
    if keys[pygame.K_RIGHT]:
        my_ship_rect.x += delta_speed    
    if keys[pygame.K_UP]:
        my_ship_rect.y -= delta_speed
    if keys[pygame.K_DOWN]:
        my_ship_rect.y += delta_speed
    
    # 화면 채우기
    screen.fill(BLACK)
    
    # 내 우주선
    screen.blit(my_ship, my_ship_rect)
    
    # 적 우주선
    for rect in list_enemy_ship:
        screen.blit(enemy_ship, rect)
    
    # 내 미사일
    for rect in list_my_missile:
        screen.blit(my_missile, rect)
        
    # 적 미사일
    for rect in list_enemy_missile:
        screen.blit(enemy_missile, rect)
    
    # 내 미사일 보내기
    for rect in list_my_missile:
        rect.y -= delta_speed
    
    # 미사일 적 처치
    for missile in list_my_missile:
        print(missile)
        kill_enemy = missile.collidelist(list_enemy_ship)
        if kill_enemy != -1:
            list_enemy_ship.remove(list_enemy_ship[kill_enemy])
    
    # 적과 부딪치면 죽음
    if my_ship_rect.collidelist(list_enemy_ship) != -1:
        print("적 맞아 죽음")
        running = False
    
    # 미사일로 죽음
    
    
    
    
    
    # 다음 스테이지
    if not list_enemy_ship:
        stage += 1
        create_enemy_ships(stage * 3)
    
    # 우주선 경계 처리    
    my_ship_rect.x = max(0, min(my_ship_rect.x, screen.get_width() - my_ship_rect.width))
    my_ship_rect.y = max(0, min(my_ship_rect.y, screen.get_height() - my_ship_rect.height))

    # 내 미사일 삭제
    for rect in list_my_missile:
        if rect.y < 0:
            list_my_missile.remove(rect)
    
    # 적이 죽으면 그 적의 미사일도 삭제
    for my_missile_rect in list_my_missile:
        index = my_missile_rect.collidelist(list_enemy_ship)
        if index != -1:
            list_enemy_ship.remove[index]
            
    
    
    
    # Stage 텍스트 생성
    Stage_text = font.render(f"Stage: {stage}", True, WHITE)
    
    # Stage 텍스트 화면에 출력
    screen.blit(Stage_text, (10, 10))
    
    # 화면 업데이트
    pygame.display.flip()

pygame.quit()