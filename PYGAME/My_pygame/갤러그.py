import pygame
import random

pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Galaga Game")

# 폰트 설정
font = pygame.font.Font(None, 36)

# 이미지 로드
my_ship = pygame.image.load("My_pygame/내 우주선.png")
enemy_ship = pygame.image.load("My_pygame/상대 우주선.png")
my_missile = pygame.image.load("My_pygame/내 미사일.png")
enemy_missile = pygame.image.load("My_pygame/상대 미사일.png")

# 적 미사일 발사 이벤트 타입
ENEMY_MISSILE_EVENT = pygame.USEREVENT + 1
# 적 미사일 발사 타이머 설정 (5초마다 발사)
pygame.time.set_timer(ENEMY_MISSILE_EVENT, 3000)  # 3000 밀리초 == 3초

# 현재 스테이지 변수
stage = 1

# 내 우주선
my_ship_rect = my_ship.get_rect()
my_ship_rect.topleft = (375, 500)

# 적 우주선 리스트
list_enemy_ship = []

# 적 생성 함수
def create_enemy_ships(num_ships):
    list_enemy_ship.clear()
    for i in range(num_ships):
        enemy_ship_rect = enemy_ship.get_rect()
        enemy_ship_rect.topleft = (random.randint(0, screen_width - enemy_ship_rect.width),\
                                   random.randint(50, 150))
        list_enemy_ship.append({"rect": enemy_ship_rect, "missiles": []})

# 첫 스테이지 적 생성
create_enemy_ships(stage * 3)

# 내 미사일 생성 함수
def create_my_missile():
    my_missile_rect = my_missile.get_rect()
    my_missile_rect.midtop = my_ship_rect.midtop
    return my_missile_rect

# 내 미사일 리스트
my_missile_list = []

# 적 미사일 생성 함수
def create_enemy_missile(enemy_rect):
    enemy_missile_rect = enemy_missile.get_rect()
    enemy_missile_rect.midbottom = enemy_rect.midbottom
    return enemy_missile_rect


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
                my_missile_list.append(create_my_missile())
        
        elif event.type == ENEMY_MISSILE_EVENT:
            for enemy in list_enemy_ship:
                enemy["missiles"].append(create_enemy_missile(enemy["rect"]))

                
    ### 키 입력
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
    
    # 적 우주선, 미사일
    for enemy in list_enemy_ship:
        screen.blit(enemy_ship, enemy["rect"])
        for missile in enemy["missiles"]:
            missile.y += delta_speed
            screen.blit(enemy_missile, missile)
    
    # 내 미사일 이동 및 출력
    for my_missile_rect in my_missile_list:
        my_missile_rect.y -= delta_speed
        screen.blit(my_missile, my_missile_rect)
    
    # 내 미사일이 적을 맞췄을 때 적 격추
    for my_missile_rect in my_missile_list:
        collision_index = my_missile_rect.collidelist([enemy["rect"] for enemy in list_enemy_ship])
        if collision_index != -1:
            del my_missile_list[my_missile_list.index(my_missile_rect)]
            del list_enemy_ship[collision_index]
            break
    
    # 적 미사일이 내 우주선을 맞췄을 때 게임 오버
    for enemy in list_enemy_ship:
        for missile in enemy["missiles"]:
            if missile.colliderect(my_ship_rect):
                running = False
                print("미사일에 맞으셨습니다. 게임 끝")
    
   # 내 우주선이 상대 우주선에 충돌할 때 게임 오버
    if any(my_ship_rect.colliderect(enemy["rect"]) for enemy in list_enemy_ship):
        running = False
        print("적에게 부딪혔습니다. 게임 끝")
    
    # 적을 모두 격추했을 때 다음 스테이지로 이동
    if not list_enemy_ship:
        stage += 1
        print(f"Stage {stage}에 도달했습니다!")
        create_enemy_ships(stage * 5)
    
    
    
    # 우주선 경계 처리    
    my_ship_rect.x = max(0, min(my_ship_rect.x, screen.get_width() - my_ship_rect.width))
    my_ship_rect.y = max(0, min(my_ship_rect.y, screen.get_height() - my_ship_rect.height))
    
    
    # 내 미사일 관리
    for i in range(len(my_missile_list) - 1, -1, -1):
        # 내 미사일이 화면을 벗어날시
        if my_missile_list[i].y < 0:
            del my_missile_list[i]
    
    # 상대 미사일
    for enemy in list_enemy_ship:
        for missile in enemy["missiles"]:
            if missile.y > 600:
                enemy["missiles"].remove(missile)
    
    # Stage 텍스트 생성
    Stage_text = font.render(f"Stage: {stage}", True, WHITE)
    
    # Stage 텍스트 화면에 출력
    screen.blit(Stage_text, (10, 10))
    
    # 화면 업데이트
    pygame.display.flip()

pygame.quit()