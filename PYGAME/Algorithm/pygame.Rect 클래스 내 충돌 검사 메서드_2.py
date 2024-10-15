import pygame

pygame.init()

# 3개의 Rect 객체를 생성
# (x, y, width, height)
obstacles = [
    pygame.Rect(350, 150, 100, 100), # 첫 번째 장애물: (20, 20) 위치, 100x100 크기
    pygame.Rect(300, 300, 150, 50), # 두 번째 장애물: (300, 300) 위치, 150x50 크기
    pygame.Rect(500, 200, 50, 150), # 세 번째 장애물: (500, 200) 위치, 50x150 크기
    pygame.Rect(400, 400, 200, 50), # 네 번째 장애물: (400, 400) 위치, 200x50 크기
]

# 충돌 감지를 수행할 대상 Rect 객체 생성: 파락색 사각형
moving_rect = pygame.Rect(420, 220, 100, 100)  # (420, 220) 위치, 100x100 크기

# moving_rect가 rects 리스트의 어떤 Rect와 충돌하는지 확인
# collidelist 메서드는 충돌한 모든 Rect의 인덱스를 반환.
# 충돌이 없으면 빈 리스트를 반환한다
collision_indices = moving_rect.collidelistall(obstacles)

if collision_indices:
    # 충돌이 발생한 경우, 충돌한 Rect의 인덱스를 출력
    print(f"moving_rect가 rects[{collision_indices}]와 충돌했습니다.")
else:
    # 충돌이 발생하지 않은 경우, 해당 메시지를 출력
    print("충돌이 없습니다.")