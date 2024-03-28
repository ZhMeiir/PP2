import pygame

pygame.init()
screen = pygame.display.set_mode((900, 600))
done = False
x = 25
y = 25

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y > 25: y -= 20
        if pressed[pygame.K_DOWN] and y < 575: y += 20
        if pressed[pygame.K_LEFT] and x > 25: x -= 20
        if pressed[pygame.K_RIGHT]and x < 875: x += 20
        
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
        
        pygame.display.flip()
        clock.tick(60)