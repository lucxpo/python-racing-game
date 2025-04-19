import pygame
from os.path import join

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 720
TILE_SIZE = 32

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.sprite_sheet = pygame.image.load(join("Assets", "Images", "player-Sheet.png")).convert_alpha()
        self.frame_rect = (0, 0, TILE_SIZE, TILE_SIZE)
        self.image = self.sprite_sheet.subsurface(self.frame_rect).copy()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))


class RoadPart(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, part, pos, groups):
        super().__init__(groups)
        self.frame_rect = (TILE_SIZE * (part-1), 0, TILE_SIZE, TILE_SIZE)
        self.image = sprite_sheet.subsurface(self.frame_rect).copy()
        self.rect = self.image.get_frect(center = pos)


def build_road(size=9):
    y = 0
    while y <= WINDOW_HEIGHT:
        x = (WINDOW_WIDTH / 2) - (int(size / 2) * TILE_SIZE)
        for i in range(size):
            if i == 0:
                part = 1
            elif i == size - 1:
                part = 3
            else:
                part = 2
            RoadPart(road_surf, part, (x, y), all_sprites)
            x += TILE_SIZE
        y += TILE_SIZE
    
    l = (WINDOW_WIDTH / 2) - (int(size / 2) * TILE_SIZE) - (TILE_SIZE / 2)
    r = (WINDOW_WIDTH / 2) + (int(size / 2) * TILE_SIZE) + (TILE_SIZE / 2)
    return (l, r)

# general setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Racing Mania")
clock = pygame.time.Clock()

road_surf = pygame.image.load(join("Assets", "Images", "street-Sheet.png")).convert_alpha()

all_sprites = pygame.sprite.Group()
collision_pos = build_road()
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