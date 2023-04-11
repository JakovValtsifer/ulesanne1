import pygame

pygame.init()

ekraani_pind = pygame.display.set_mode((300, 300))
ekraani_pind.fill((0,0,200))

pygame.display.set_caption("lumemees")


body_bottom_circle = pygame.draw.circle(ekraani_pind, (255,255,255), (150, 190), 50)
body_middle_circle = pygame.draw.circle(ekraani_pind, (255,255,255), (150, 120), 40)
body_top_circle = pygame.draw.circle(ekraani_pind, (255,255,255), (150, 60), 30)

left_eye_circle = pygame.draw.circle(ekraani_pind, (0,0,0), (135, 50), 5)
right_eye_circle = pygame.draw.circle(ekraani_pind, (0,0,0), (165, 50), 5)

mouth_points = [(150, 80), (155, 70), (145, 70)]
mouth_triangle = pygame.draw.polygon(ekraani_pind, (255, 0, 0), mouth_points)

pilt=pygame.image.load("pppp.png")
ekraani_pind.blit(pilt,(1,1))




pygame.display.flip()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


pygame.quit()
