import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

# 화면 가로, 세로 크기 출력
print(screen.get_width(), screen.get_height()) # get_width, get_height : 현재 사이즈를 나타 내는 함수

# 중심점 좌표 계산
centry_x = int(screen.get_width() / 2)
centry_y = int(screen.get_height() / 2)

# 색상 정의 -> 원소가 3개인 Tuple
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 점 그리기
pygame.draw.circle(screen, RED, (centry_x, centry_y), 40) # 중앙 (반지름 40)
pygame.draw.circle(screen, GREEN, (0, 0), 40) # 왼쪽 상단 모서리
pygame.draw.circle(screen, BLUE, (799, 599), 40) # 오른쪽 하단 모서리
pygame.display.flip() # 준비된 값을 실제 화면에 보여주는 것, Flip은 계속 쓰면 안되고 한번에 한번만 딱 해야됨


running = True
while running:
    for event in pygame.event.get(): # get (event 수집)
        if event.type == pygame.QUIT: # QUIT -> X를 누르면 Running을 False로 치환후 종료
            running = False

pygame.quit()