import pygame
from os.path import join


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.sprite_sheet = pygame.image.load(join("Assets", "Images", "player-Sheet.png")).convert_alpha()
        self.frame_rect = (0, 0, 32, 32)
        self.image = self.sprite_sheet.subsurface(self.frame_rect).copy()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))


# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Racing Mania")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

# game loop
running = True
while running:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw
    display_surface.fill((20, 126, 20))

    all_sprites.draw(display_surface)

    pygame.display.update()