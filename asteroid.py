import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

# Class for Asteroid objects
class Asteroid(CircleShape):
	def __init__(self,x,y,radius):
		super().__init__(x,y,radius)

	def draw(self, screen):
		pygame.draw.circle(screen,"white",self.position,self.radius,width=2)
	
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return

		positive_asteroid = Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)
		negative_asteroid = Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)

		angle = random.uniform(20,50)
		positive_asteroid.velocity = self.velocity.rotate(angle) * 1.2
		negative_asteroid.velocity = self.velocity.rotate(-angle) * 1.2

	def update(self, dt):
		self.position += self.velocity * dt