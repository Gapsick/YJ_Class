import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

BLACK = (0, 0, 0)

brick_x = 59
brick_y = 100

# 벽돌 위치
def brick_position():
    brick_position = [(brick_x + i * 5, 20, 50, 20)for i in range(5)]
    return brick_position

# 벽돌 생성
for pos in brick_position():
    brick = pygame.draw.rect(screen, BLACK, pos)




running = True
# 게임 시작
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    
    # 벽돌 생성
    for pos in brick_position():
        pygame.draw.rect(screen, BLACK, pos)

    pygame.display.flip()

pygame.quit()