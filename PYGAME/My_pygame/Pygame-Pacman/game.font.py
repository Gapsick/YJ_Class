import pygame

WHITE = (255, 255, 255)
font = pygame.font.Font(None, 36)
score = 0

if True:
    score += 100

Score_text = font.render(f"Score: {score}", True, WHITE)