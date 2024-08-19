# 키보드의 모든 키 입력을 감지하고 어떤 키가 눌렸는지 출력
# 마우스 클릭 이벤트를 감지하고 클릭된 위치와 버튼을 출력
# 사용자가 프로그램을 종료할 때까지 이벤트를 계속해서 기록

import pygame

# 파이게임 라이브러리 초기화
pygame.init()

# 800x600 픽셀 크기의 화면을 생성
screen = pygame.display.set_mode((800, 600))

# 게임 루프 실행 여부를 결정하는 변수
running = True

# 게임 루프
while running:
    # 이벤트 큐에서 이벤트를 모두 가져와 순차적으로 정리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 사용자가 윈도우 닫기 버튼을 클릭하면 발생하는 이벤트
            running = False
        elif event.type == pygame.KEYDOWN:
            # 키보드의 키를 누르면 발생하는 이벤트
            # 눌린 키의 이름을 출력
            print(f"Key pressed: {pygame.key.name(event.key)}")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 버튼을 클릭하면 발생하는 이벤트
            # 클릭된 위치와 버튼 번호를 출력
            print(f"Mouse button {event.button} clicked at position {event.pos}")
            
    
    # 화면을 검은색으로 채우기
    screen.fill((0, 0, 0))

    # 화면 업데이트
    pygame.display.flip()

# 파이게임 종료 처리
pygame.quit()