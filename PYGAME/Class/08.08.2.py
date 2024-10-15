# import pygame

# pygame.init()

# # 3개의 Rect 객체를 생성
# # (x, y, width, height)
# rects = [
#     pygame.Rect(20, 20, 40, 40),  # 첫 번째 Rect: (20, 20) 위치, 40x40 크기
#     pygame.Rect(100, 100, 50, 50),  # 두 번째 Rect: (100, 100) 위치, 50x50 크기
#     pygame.Rect(200, 200, 60, 60)  # 세 번째 Rect: (200, 200) 위치, 60x60 크기
# ]

# rects[1].x = 700

# # 충돌 감지를 수행할 대상 Rect 객체 생성: 파란색 사각형
# moving_rect = pygame.Rect(120, 130, 100, 100)  # (120, 130) 위치, 100x100 크기

# # moving_rect가 rects 리스트의 어떤 Rect와 충돌하는지 확인
# # collidelist 메서드는 충돌한 Rect의 인덱스를 반환. 충돌이 없으면 -1을 반환한다
# index = moving_rect.collidelist(rects)

# if index != -1:
#     # 충돌이 발생한 경우, 충돌한 Rect의 인덱스를 출력
#     print(f"moving_rect가 rects[{index}]와 충돌했습니다.")
# else:
#     # 충돌이 발생하지 않은 경우, 해당 메시지를 출력
#     print("충돌이 없습니다.")

import pygame

pygame.init()

# 여러 개의 Rect 객체를 생성
# (x, y, width, height)
obstacles = [
    pygame.Rect(350, 150, 100, 100),  # 첫 번째 장애물: (150, 100) 위치, 100x100 크기
    pygame.Rect(300, 300, 150, 50),   # 두 번째 장애물: (300, 300) 위치, 150x50 크기
    pygame.Rect(500, 200, 50, 150),   # 세 번째 장애물: (500, 200) 위치, 50x150 크기
    pygame.Rect(400, 400, 200, 50)    # 네 번째 장애물: (400, 400) 위치, 200x50 크기
]

# 충돌 감지를 수행할 대상 Rect 객체 생성: 파란색
moving_rect = pygame.Rect(420, 220, 100, 100)  # (420, 220) 위치, 100x100 크기

# moving_rect가 obstacles 리스트의 어떤 Rect와 충돌하는지 확인
# collidelistall 메서드는 충돌한 모든 Rect의 인덱스를 리스트로 반환.
# 충돌이 없으면 빈 리스트를 반환한다
collision_indices = moving_rect.collidelistall(obstacles)

if collision_indices:
    # 충돌이 발생한 경우, 충돌한 모든 Rect의 인덱스를 출력
    print(f"moving_rect가 obstacles[{collision_indices}]와 충돌했습니다.")
else:
    # 충돌이 발생하지 않은 경우, 해당 메시지를 출력
    print("충돌이 없습니다.")
    
    

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
colors = [(255, 0, 0), (0, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)] # 빨간색, 검정색, 노란색, 녹색, 파란색

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    for index, rect in enumerate(obstacles, 0):
        pygame.draw.rect(screen, colors[index],rect)
        
    pygame.draw.rect(screen, (0, 0, 255),moving_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()