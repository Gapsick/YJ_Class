import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

x, y = screen.get_width() / 2, screen.get_height() / 2
radius = 50
speed = 5
running = True
Clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, (255,0,0), (x, y), radius)
    
    x += speed
    
    if x + radius > 800 or x - radius < 0:
        speed = -speed
    
    pygame.display.flip()
    
    Clock.tick(60)

pygame.quit()