import pygame

# 사용자 정의 이벤트 생성
# SPAWN_ENEMY는 pygame.USEREVENT에 1을 더하여 고유한 이벤트로 정의
SPAWN_ENEMY = pygame.USEREVENT + 1

# 타이머 설정 : 2초마다 SPAWN_ENEMY 이벤트가 발생하도록 설정
pygame.time.set_timer(SPAWN_ENEMY, 2000)  # 2000밀리초(2초)마다 이벤트 발생

# 게임 루프 내 이벤트 처리
for event in pygame.event.get():
    # 발생한 이벤트가 SPAWN_ENEMY인 경우 처리
    if event.type == SPAWN_ENEMY:
        # 주기적으로 수행할 작업
        print("Spawn new enemy!")  # 콘솔에 "Spawn new enemy!" 출력