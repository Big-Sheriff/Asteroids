import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.PLAYER_SHOOT_COOLDOWN = 0
        self.PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3
        

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def update(self, dt: float) -> None:
        # Update the cooldown timer
        if self.PLAYER_SHOOT_COOLDOWN > 0:
            self.PLAYER_SHOOT_COOLDOWN -= dt
        keys = pygame.key.get_pressed()
        # Handle player input for rotation and movement
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        # Handle shooting
        if keys[pygame.K_SPACE]:
            shot = self.shoot()

    def shoot(self) -> "Shot":
        if self.PLAYER_SHOOT_COOLDOWN > 0:
            return None  # Can't shoot yet, still in cooldown
        # Reset the cooldown timer
        self.PLAYER_SHOOT_COOLDOWN = self.PLAYER_SHOOT_COOLDOWN_SECONDS
        # Create a new shot at the player's position
        shot = Shot(self.position.x, self.position.y)
        # Set the shot's velocity based on the player's rotation and speed
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        return shot
