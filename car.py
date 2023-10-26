import pygame
import os
import sys
import numpy as np


CAR = pygame.image.load(os.path.join(os.getcwd(), "./car.png"))

# permet de réduire l'image unifomement plus tard
w = CAR.get_width()
h = CAR.get_height()

x = 200
y = 200
class Car(pygame.sprite.Sprite): #Utilisation de la classe "Sprite" du module "sprite". Car defined by extending Sprite
    def __init__(self):
        super().__init__()
        
        self.image = pygame.transform.scale(CAR, (w * 0.1, h * 0.1))
        self.rect = self.image.get_rect(center=(x, y)) 

        self.position = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0) 
        self.angle = 0
        
        self.brake_deceleration = 20
        self.acceleration = 0
        self.steering = 0
        
    def update(self, dt):
        self.vel.x = self.vel.x + self.acceleration * dt    #(dv = a * dt)
        self.position = self.position + self.vel * dt        #(dx = v * dt)