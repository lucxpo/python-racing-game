import pygame
from os.path import join

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 720
TILE_SIZE = 32
SCROLL_SPEED = 100

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.sprite_sheet = pygame.image.load(join("Assets", "Images", "player-Sheet.png")).convert_alpha()
        self.frame_rect = (0, 0, TILE_SIZE, TILE_SIZE)
        self.image = self.sprite_sheet.subsurface(self.frame_rect).copy()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.math.Vector2()
        self.speed = 300

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        self.rect.x += self.direction.x * self.speed * dt
        if self.rect.left <= collision_pos[0]:
            self.rect.left = collision_pos[0]
        if self.rect.right >= collision_pos[1]:
            self.rect.right = collision_pos[1]

class Road(pygame.sprite.Sprite):
    counter = 0

    def __init__(self, groups, cols=7, y=0):
        super().__init__(groups)
        type(self).counter += 1

        sheet = pygame.image.load(join("Assets", "Images", "street-Sheet.png")).convert_alpha()

        rows = (WINDOW_HEIGHT // TILE_SIZE) + 1

        road_height = rows * TILE_SIZE
        road_width = cols * TILE_SIZE

        self.image = pygame.Surface((road_width, road_height), pygame.SRCALPHA)
        self.rect = self.image.get_frect(midtop = (WINDOW_WIDTH / 2, y))

        for row in range(rows):
            for col in range(cols):
                if col == 0:
                    frame_x = 0
                elif col == cols - 1:
                    frame_x = TILE_SIZE * 2
                else:
                    frame_x = TILE_SIZE

                x = col * TILE_SIZE
                y = row * TILE_SIZE
                
                frame_rect = (frame_x, 0, TILE_SIZE, TILE_SIZE)
                road_part = sheet.subsurface(frame_rect).copy()
                self.image.blit(road_part, (x, y))

    def update(self, dt):
        self.rect.y += SCROLL_SPEED * dt
        if self.rect.y >= WINDOW_HEIGHT:
            self.rect.y -= self.image.get_height() * type(self).counter

class Background(pygame.sprite.Sprite):
    counter = 0

    def __init__(self, groups, x=0):
        super().__init__(groups)
        type(self).counter += 1

        surf = pygame.transform.scale_by(pygame.image.load(join("Assets", "Backgrounds", "pixelart_starfield.png")).convert(), 2)

        rows = (WINDOW_HEIGHT // surf.get_height()) + 1
        cols = (WINDOW_WIDTH // surf.get_width()) + 1

        bg_height = rows * surf.get_height()
        bg_width = cols * surf.get_width()

        self.image = pygame.Surface((bg_width, bg_height), pygame.SRCALPHA)
        self.rect = self.image.get_frect(topleft = (x, 0))

        for row in range(rows):
            for col in range(cols):
                x = col * surf.get_width()
                y = row * surf.get_height()
                
                self.image.blit(surf, (x, y))

    def update(self, dt):
        self.rect.x += 10 * dt
        if self.rect.x >= WINDOW_WIDTH:
            self.rect.x -= self.image.get_width() * type(self).counter


# general setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Racing Mania")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
background = Background(all_sprites)
Background(all_sprites, x=background.rect.right)
road = Road(all_sprites)
Road(all_sprites, y=road.rect.bottom)
collision_pos = (road.rect.left, road.rect.right)
player = Player(all_sprites)

# game loop
running = True
while running:
    dt = clock.tick(60) / 1000

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update
    all_sprites.update(dt)

    # draw
    display_surface.fill("black")

    all_sprites.draw(display_surface)

    pygame.display.update()