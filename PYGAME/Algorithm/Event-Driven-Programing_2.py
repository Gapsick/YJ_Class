import pygame

# 파이게임 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Event Listener and Handler Example")
running = True

# 이벤트 핸들링: 함수 사용
def handle_keydown(event):
    if event.key == pygame.K_SPACE:
        print("Spacebar pressed - handled by function.")

while running:
    # 이벤트 큐에서 이벤트를 가져옴
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # 이벤트 핸들링 : 직접 입력
            if event.key == pygame.K_ESCAPE:
                print("Escape key pressed - handled by algorithm.")
                running = False
            else:
                handle_keydown(event)

# 파이게임 종료
pygame.quit()