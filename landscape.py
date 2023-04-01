import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
import random 

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
frame_count = 0

# stars
star_x_positions = []
star_y_positions = []
star_sizes = []

# clouds
cloud1_x = 0
cloud1_y = 50
cloud1_speed = random.randint(1, 7)
cloud2_x = 200
cloud2_y = 20
cloud2_speed = random.randint(1, 7)
cloud3_x = 500
cloud3_y = 30
cloud3_speed = random.randint(1, 7)

# layered clouds
cloud4_x = -20
cloud4_y = 100
cloud5_x = 180
cloud5_y = 70
cloud6_x = 550
cloud6_y = 25


# sun and moon
sun_x = 200
sun_y = 480
moon_x = 200
moon_y = 480

# cloud colours
white_cloud = "#FFFFFF"
gray_cloud = "#f5f6f6"
grayer_cloud = "#e1dfdf"
grayest_cloud = "#3d3d3d"

# elephant
legs_x = -130
head_x = -60
eye_x = -35

body_x1 = -151
body_x2 = -151
body_x3 = -119
body_x4 = -61
body_x5 = -61

ears_x1 = -60
ears_x2 = -75
ears_x3 = -86
ears_x4 = -86
ears_x5 = -75
ears_x6 = -60

trunk_x1 = -30
trunk_x2 = -10
trunk_x3 = -9
trunk_x4 = -24
trunk_x5 = -30


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
    cloud1_x += cloud1_speed
    cloud4_x += cloud1_speed
    cloud2_x += cloud2_speed
    cloud5_x += cloud2_speed
    cloud3_x += cloud3_speed
    cloud6_x += cloud3_speed

    # update elephant positions
    legs_x += 1
    eye_x += 1
    head_x += 1

    body_x1 += 1
    body_x2 += 1
    body_x3 += 1
    body_x4 += 1
    body_x5 += 1
  
    ears_x1 += 1
    ears_x2 += 1
    ears_x3 += 1
    ears_x4 += 1
    ears_x5 += 1
    ears_x6 += 1
  
    trunk_x1 += 1
    trunk_x2 += 1
    trunk_x3 += 1
    trunk_x4 += 1
    trunk_x5 += 1
  
    # sunrise
    if frame_count < 200:
      sun_y += -2
      sky_r = 155   
      sky_g = 173
      sky_b = 218
      screen.fill((sky_r, sky_g, sky_b))
      white_cloud = "#FFFFFF"
      gray_cloud = "#f5f6f6"
      grayer_cloud = "#e1dfdf"
      legs_x = -130
      body_x1 = -151
      body_x2 = -151
      body_x3 = -119
      body_x4 = -61
      body_x5 = -61
      ears_x1 = -60
      ears_x2 = -75
      ears_x3 = -86
      ears_x4 = -86
      ears_x5 = -75
      ears_x6 = -60
      head_x = -60
      eye_x = -35
      trunk_x1 = -30
      trunk_x2 = -10
      trunk_x3 = -9
      trunk_x4 = -24
      trunk_x5 = -30

    # midday
  
    if frame_count > 200 and frame_count < 600:
      sun_y += 0

    # sunset
  
    if frame_count > 600 and frame_count < 800:
      sky_r -= (129 - 40) / 150
      sky_g -= (159 - 60) / 150
      sky_b -= (226 - 107) / 150
      sun_y += 2
      screen.fill((sky_r, sky_g, sky_b))

    # moon goes up
    if frame_count > 800 and frame_count < 1000:
      moon_y += -2
      screen.fill((sky_r, sky_g, sky_b))
      
    # midnight
    if frame_count > 1000 and frame_count < 1400:
      moon_y += 0
      white_cloud = grayest_cloud
      gray_cloud = grayest_cloud
      grayer_cloud = grayest_cloud
      screen.fill((sky_r, sky_g, sky_b))

    # moon goes down
  
    if frame_count > 1400 and frame_count < 1600:
      moon_y += 2
      screen.fill((sky_r, sky_g, sky_b))
      sky_r += (129 - 40) / 150
      sky_g += (159 - 60) / 150
      sky_b += (226 - 107) / 150

    if frame_count > 1600:
      frame_count = 0

      screen.fill((sky_r, sky_g, sky_b))

    # resetting clouds back to the left
    if cloud2_x > WIDTH and cloud5_x > WIDTH:
      cloud2_x = -200
      cloud5_x = -220
      cloud2_speed = random.randint(3, 4)
    if cloud3_x > WIDTH and cloud6_x > WIDTH:
      cloud3_x = -200
      cloud6_x = -300
      cloud3_speed = random.randint(5, 6)
    if cloud1_x > WIDTH and cloud4_x > WIDTH:
      cloud1_x = -200
      cloud4_x = -225
      cloud1_speed = random.randint(1, 2)

    screen.fill((sky_r, sky_g, sky_b))

  # mountains behind the sun
    pygame.draw.polygon(screen, ("#b3bcc4"), ((378, 167), (189, 112), (93, 146), (0, 184), (2, 317), (152, 282), (545, 245), (640, 280), (640, 480)))
    pygame.draw.polygon(screen, "#dde5f4", ((1, 142), (60, 160), (1, 184)))

  # draw sun and moon 
    pygame.draw.ellipse(screen, ("#fff900"), (sun_x, sun_y, 150, 150))
    pygame.draw.ellipse(screen, ("#f2f3f2"), (moon_x, moon_y, 75, 75))
  
    if frame_count > 1000:
      for i in range(20):
        star_x = random.randint(0, 640)
        star_y = random.randint(0, 120)
        star_size = random.randint(1, 5)
        star_x_positions.append(star_x)
        star_y_positions.append(star_y)
        star_sizes.append(star_size)
        
      for i in range(20):
        star_x = star_x_positions[i]
        star_y = star_y_positions[i]
        star_size = star_sizes[i]
        pygame.draw.circle(screen, ("#f7fccc"), (star_x, star_y), star_size)
  
  # draw background mountains and clouds
    pygame.draw.ellipse(screen, (white_cloud), (cloud1_x, cloud1_y, 125, 100))
    pygame.draw.ellipse(screen, (gray_cloud), (cloud2_x, cloud3_y, 125, 75))
    pygame.draw.ellipse(screen, (white_cloud), (cloud3_x, cloud3_y, 120, 60))
    pygame.draw.ellipse(screen, (gray_cloud), (cloud4_x, cloud4_y, 100, 75))
    pygame.draw.ellipse(screen, (grayer_cloud), (cloud5_x, cloud5_y, 100, 50))
    pygame.draw.ellipse(screen, (gray_cloud), (cloud6_x, cloud6_y, 125, 50))

  # draw ground
    pygame.draw.rect(screen, ("#437857"), (0, 317, 650, 180))

  # draw close-by mountains
    pygame.draw.polygon(screen, ("#788487"), ((2, 317), (69, 94), (169, 319)))
    pygame.draw.polygon(screen, ("#51595b"), ((126, 320), (325, 176), (531, 140), (640, 316)))
    pygame.draw.polygon(screen, ("#484F50"), ((122, 320), (242, 166), (307, 201), (340, 320)))
    pygame.draw.polygon(screen, ("#dde5f4"), ((556, 183), (613, 271), (639, 281), (639, 145)))
  
    # trees
    for x in range(10, 640, 100):
      pygame.draw.rect(screen, ("#5C4033"), (x + 10, 300, 10, 40))
      pygame.draw.polygon(screen, ("#013220"), ((x - 10, 300), (x + 15, 180), (x + 40, 300)))
      pygame.draw.polygon(screen, ("#013220"), ((x - 7, 250), (x + 13, 140), (x + 33, 250)))

    # elephant    
      pygame.draw.polygon(screen, ("#243640"), ((body_x1, 460), (body_x2, 361), (body_x3, 325), (body_x4, 325), (body_x5, 460)))
      pygame.draw.rect(screen, ("#437857"), (legs_x + 5, 400, 40, 80))
      pygame.draw.polygon(screen, ("#edc5d3"), ((ears_x1, 325), (ears_x2, 325), (ears_x3, 340), (ears_x4, 377), (ears_x5, 388), (ears_x6, 388)))
      pygame.draw.rect(screen, ("#243640"), (head_x, 325, 30, 63))
      pygame.draw.polygon(screen, ("#243640"), ((trunk_x1, 326), (trunk_x2, 338), (trunk_x3, 413), (trunk_x4, 414), (trunk_x5, 387)))
      pygame.draw.circle(screen, ("#000000"), (eye_x, 353), 5)

    
    # update display and limit framerate
    pygame.display.flip()
    clock.tick(30)
    frame_count += 1

# quit pygame
pygame.quit()
