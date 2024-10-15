# 구성요소

# 1. 무한루프 - 계속 프로그램이 돌고 있는 것
# 2. Event Listener - Event를 듣고 있는중, 각 상황에 맞는 Handler를 호출 해 실행
# 3. Event Handler - 함수 (특정 Event가 날라왔을때)

# event가 발생하면 queue라는 자료구조에 저장
# get : queue에 저장된 event를 가지고 오는 것
# 해당 event에 맞는 handler를 들고 오는 것



import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Event Listener and Handler Example")
running = True

while running:
    for event in pygame.event.get():
        print(event)
    
    
pygame.quit()