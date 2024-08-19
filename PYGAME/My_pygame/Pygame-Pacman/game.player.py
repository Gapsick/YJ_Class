import pygame
import os

# Pygame 초기화
pygame.init()

# 환경변수
screen_width = 900
screen_height = 950
clock = pygame.time.Clock()

# 윈도우 크기 설정
screen = pygame.display.set_mode((screen_height, screen_width))

# 이미지 파일 경로 설정
image_path_1 = os.path.join('assets', 'player_images', '1.png')
image_path_2 = os.path.join('assets', 'player_images', '2.png')
image_path_3 = os.path.join('assets', 'player_images', '3.png')
image_path_4 = os.path.join('assets', 'player_images', '4.png')

# 이미지 로드
image1 = pygame.image.load(image_path_1)
image2 = pygame.image.load(image_path_2)
image3 = pygame.image.load(image_path_3)
image4 = pygame.image.load(image_path_4)

# 초기 이미지와 Rect 설정
current_image = image1
image_rect = current_image.get_rect(topleft=(100, 100))

# 이미지 스피드
image_speed = 300

# 윈도우 루프
running = True
while running:
    
    # 델타 타임 계산 (초 단위 경과 시간)
    dt = clock.tick(60) / 1000.0  # 60 FPS로 제한
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
     # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  # 왼쪽 화살표 키로 플레이어 이동
        current_image = image1
        image_rect.x -= image_speed * dt  # 델타 타임을 사용하여 프레임 독립적 이동
    if keys[pygame.K_RIGHT]:  # 오른쪽 화살표 키로 플레이어 이동
        current_image = image2
        image_rect.x += image_speed * dt  # 델타 타임을 사용하여 프레임 독립적 이동
    if keys[pygame.K_UP]:  # 왼쪽 화살표 키로 플레이어 이동
        current_image = image3
        image_rect.y -= image_speed * dt  # 델타 타임을 사용하여 프레임 독립적 이동
    if keys[pygame.K_DOWN]:  # 왼쪽 화살표 키로 플레이어 이동
        current_image = image4
        image_rect.y += image_speed * dt  # 델타 타임을 사용하여 프레임 독립적 이동
    
   
    # 화면을 하얀색으로 채우기
    screen.fill((255, 255, 255))
    
    
    
    # 이미지 그리기
    screen.blit(current_image, image_rect)

    # 화면 업데이트
    pygame.display.flip()

pygame.quit()
