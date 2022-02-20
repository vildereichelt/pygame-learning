import pygame
pygame.init()
screen = pygame.display.set_mode([500,500])
running = True
blue = 0
position = 0
position_up_down = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                position = position - 1
            if event.key == pygame.K_RIGHT:
                position = position + 1
            if event.key == pygame.K_UP:
                    position = position - 50
            if event.key == pygame.K_DOWN:
                    position = position + 50
        if event.type == pygame.QUIT:
            running = False
    print(position)
    # running = False
    screen.fill((255, 100, 0))
    ttt = pygame.Rect(0, position, 255, 255)
    pygame.draw.rect(screen, (190, 165, blue), ttt)
    if blue < 255:
        blue = blue + 1
    #else:
        #blue = 0
    pygame.display.flip()
pygame.quit()
