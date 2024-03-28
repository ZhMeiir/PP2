import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((700, 526 ))
pygame.display.set_caption("Clock")
done = False
clock = pygame.time.Clock()

im_cl = pygame.image.load(r"C:\Users\meiir\OneDrive\Изображения\clock.png")
secs = pygame.image.load(r"C:\Users\meiir\OneDrive\Изображения\mins.png")
mins = pygame.image.load(r"C:\Users\meiir\OneDrive\Изображения\secs.png")

clock_r = im_cl.get_rect(center = (350, 263))
secs_r = secs.get_rect(center = (350, 263))
mins_r = mins.get_rect(center = (350, 263))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    now = datetime.now().time()

    angle_s = now.second * 6 #because 360 degrees (60 * 6 = 360)
    angle_m = (now.minute * 60 + now.second) / 3600.0 * 360 #total num os seconds

    rotated_secs = pygame.transform.rotate(secs, -angle_s)
    rotated_mins = pygame.transform.rotate(mins, -angle_m)

    secs_r = rotated_secs.get_rect(center = clock_r.center)
    mins_r = rotated_mins.get_rect(center = clock_r.center)

    screen.blit(im_cl, clock_r)
    screen.blit(rotated_secs, secs_r)
    screen.blit(rotated_mins, mins_r)
    pygame.display.flip()
    clock.tick(60)

