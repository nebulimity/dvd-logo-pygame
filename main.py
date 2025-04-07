import pygame
import sys
import config

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_RESOLUTION[0], config.WINDOW_RESOLUTION[1]), pygame.RESIZABLE)
    pygame.display.set_caption("dvd logo pygame")
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def tint_image(image, tint_color):
    tinted_image = image.copy()
    tinted_image.fill(tint_color, special_flags=pygame.BLEND_MULT)
    return tinted_image

def main():
    screen = init_game()
    clock = pygame.time.Clock()
    
    dvd_logo = pygame.image.load("assets/dvd_logo.png").convert_alpha()
    logo_rect = dvd_logo.get_rect()
    window_size = screen.get_size()
    
    pos_x, pos_y = window_size[0] // 2, window_size[1] // 2
    vel_x, vel_y = 3, 2
    
    RAINBOW_COLORS = [
        (190, 0, 255),
        (0, 254, 255),
        (255, 131, 0),
        (0, 38, 255),
        (255, 250, 1),
        (255, 38, 0),
        (255, 0, 139)
    ]
    color_index = 0

    running = True
    while running:
        clock.tick(config.FPS)
        running = handle_events()

        pos_x += vel_x
        pos_y += vel_y

        bounce = False

        if pos_x <= 0 or pos_x + logo_rect.width >= window_size[0]:
            vel_x *= -1
            bounce = True

        if pos_y <= 0 or pos_y + logo_rect.height >= window_size[1]:
            vel_y *= -1
            bounce = True

        if bounce:
            color_index = (color_index + 1) % len(RAINBOW_COLORS)
        current_color = RAINBOW_COLORS[color_index]

        tinted_logo = tint_image(dvd_logo, current_color)

        screen.fill((0, 0, 0))
        screen.blit(tinted_logo, (pos_x, pos_y))
        
        window_size = screen.get_size()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()