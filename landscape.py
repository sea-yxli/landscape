import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
import random 

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
count = 0

# main clouds
cloud_x = 0
cloud_y = 50
cloud_speed = random.randint(1, 3)
cloud1_x = 200
cloud1_y = 20
cloud1_speed = random.randint(3, 5)
cloud2_x = 500
cloud2_y = 30
cloud2_speed = random.randint(5, 7)

# layered clouds
cloud3_x = -20
cloud3_y = 100
cloud4_x = 180
cloud4_y = 70
cloud5_x = 550
cloud5_y = 25

# day and night
sun_x = 200
sun_y = 480
moon_x = 200
moon_y = 480
white_cloud = "#FFFFFF"
gray_cloud = "#f5f6f6"
grayer_cloud = "#e1dfdf"
grayest_cloud = "#3d3d3d"

clock = pygame.time.Clock()

# main loop
running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            print(mouse_x, mouse_y)

    # update cloud positions
    cloud_x += cloud_speed
    cloud3_x += cloud_speed
    cloud1_x += cloud1_speed
    cloud4_x += cloud1_speed
    cloud2_x += cloud2_speed
    cloud5_x += cloud2_speed

    # sun
    if count < 200:
      sun_y += -2
      sky_r = 155	
      sky_g = 173
      sky_b = 218
      screen.fill((sky_r, sky_g, sky_b))
      white_cloud = "#FFFFFF"
      gray_cloud = "#f5f6f6"
      grayer_cloud = "#e1dfdf"

    if count > 200 and count < 600:
      sun_y += 0
      
    if count > 600 and count < 800:
      sky_r -= (129 - 40) / 150
      sky_g -= (159 - 60) / 150
      sky_b -= (226 - 107) / 150
      sun_y += 2
      screen.fill((sky_r, sky_g, sky_b))

    if count > 800 and count < 1000:
      moon_y += -2
      sky_r += (129 - 40) / 150
      sky_g += (159 - 60) / 150
      sky_b += (226 - 107) / 150
      screen.fill((sky_r, sky_g, sky_b))
  
    if count > 1000 and count < 1400:
      moon_y += 0
      white_cloud = grayest_cloud
      gray_cloud = grayest_cloud
      grayer_cloud = grayest_cloud

    if count > 1400 and count < 1600:
      moon_y += 2

    if count > 1600:
      count = 0

    # looping clouds back to the left
    if cloud1_x > WIDTH and cloud4_x > WIDTH:
      cloud1_x = -200
      cloud4_x = -220
      cloud1_speed = random.randint(3, 4)
    if cloud2_x > WIDTH and cloud5_x > WIDTH:
      cloud2_x = -200
      cloud5_x = -300
      cloud2_speed = random.randint(5, 6)
    if cloud_x > WIDTH and cloud3_x > WIDTH:
      cloud_x = -200
      cloud3_x = -225
      cloud_speed = random.randint(1, 2)

    screen.fill((sky_r, sky_g, sky_b))
  
  #landscape
    pygame.draw.polygon(screen, ("#b3bcc4"), ((378, 167), (189, 112), (93, 146), (0, 184), (2, 317), (152, 282)))

  #sun and moon 
    pygame.draw.ellipse(screen, ("#fff900"), (sun_x, sun_y, 150, 150))
    pygame.draw.ellipse(screen, ("#f2f3f2"), (moon_x, moon_y, 75, 75))


  #mountains and clouds
    pygame.draw.ellipse(screen, (white_cloud), (cloud_x, cloud_y, 125, 100))
    pygame.draw.ellipse(screen, (gray_cloud), (cloud1_x, cloud1_y, 125, 75))
    pygame.draw.ellipse(screen, (white_cloud), (cloud2_x, cloud2_y, 120, 60))
    pygame.draw.ellipse(screen, (gray_cloud), (cloud3_x, cloud3_y, 100, 75))
    pygame.draw.ellipse(screen, (grayer_cloud), (cloud4_x, cloud4_y, 100, 50))
    pygame.draw.ellipse(screen, (gray_cloud), (cloud5_x, cloud5_y, 125, 50))
    pygame.draw.rect(screen, ("#437857"), (1, 317, 536, 162))

  #other mountains
    pygame.draw.polygon(screen, ("#788487"), ((2, 317), (69, 94), (169, 319)))
    pygame.draw.polygon(screen, ("#51595b"), ((126, 320), (325, 176), (531, 140), (534, 316)))
    pygame.draw.polygon(screen, ("#484F50"), ((122, 320), (242, 166), (307, 201), (340, 320)))

    # update display and limit framerate
    pygame.display.flip()
    clock.tick(30)
    count += 1

# quit pygame
pygame.quit()
