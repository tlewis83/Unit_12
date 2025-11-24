import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    def __init__(self, fleet: 'AlienFleet', x:float, y:float):
        super().__init__()
        
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        angle = float(270)
        self.image = pygame.transform.rotate(self.image, angle)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))

        self.rect = self.image.get_rect()
        self.rect.midright = self.boundaries.midright
        self.rect.x = x
        self.rect.y = y
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        temp_speed = self.settings.fleet_speed

        if self.check_edges():
            self.settings.fleet_direction *= -1
            self.x += self.settings.fleet_drop_speed

        self.y += temp_speed * self.settings.fleet_direction
        self.rect.y = self.y
        self.rect.x = self.x

    def check_edges(self):
        return (self.rect.top >= self.boundaries.bottom or self.rect.bottom <= self.boundaries.top)

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)