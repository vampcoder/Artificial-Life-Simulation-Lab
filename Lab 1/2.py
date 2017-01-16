import os, sys, math, pygame, pygame.mixer, euclid, time
from pygame.locals import *
import random

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
yellow = 255, 255, 0
timediff = 1
colors = [white, green, blue, red, yellow]
screen = None
screen_size = None
clock = pygame.time.Clock()
center_circle = None
image = None
rect = None


def initialize():
    global center_circle, Road1, Road2, screen, screen_size
    screen_size = screen_width, screen_height = 300, 300
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Assignment 1")
    screen.fill(white)

class Mycircle:
    def __init__(self, position, size, color = (255, 255, 255),velocity = euclid.Vector2(0, 0) , width = 0):
        self.position = position
        self.size = size
        self.color = color
        self.width = width
        self.velocity = velocity
        self.display()

    def display(self):
        rx, ry = int(self.position.x), int(self.position.y)
        pygame.draw.circle(screen, self.color, (rx, ry), self.size, self.width)

    def changeColor(self, color):
        self.color = color

    def move(self ,position):
        self.changeColor(white)
        self.display()
        self.position = position
        self.changeColor(green)
        self.display()

    def change_velocity(self, velocity):
        self.velocity = velocity

class environment:
    def __init__(self, center, radius, angularVelocity, initialAngle):
        C = Mycircle(center, 4, black)
        size = 3
        initialPosition = center + euclid.Vector2(math.cos(initialAngle), math.sin(initialAngle))
        self.agent = Mycircle(initialPosition, size, green, width = 3)
        time = 0
        flag = True
        dtime_ms = clock.tick(60)
        timediff = dtime_ms / 10000.0
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
            current = AgentFunction(radius, center, initialAngle, time, angularVelocity)
            self.agent.move(current)
            time -= timediff
            pygame.display.flip()


def check(pos1, pos2):
    if pos1.x <= pos2.x+1 and pos1.x > pos2.x-1 and pos1.y <= pos2.y+1 and pos1.y > pos2.y-1:
        return True

def AgentFunction(radius, center, initialAngle, time, angularVelocity):
        Angle = initialAngle + angularVelocity*time
        position = center + radius * euclid.Vector2(math.cos(Angle), math.sin(Angle))
        return position

def main():
    initialize()
    env = environment(euclid.Vector2(150, 150), 100, .01 ,0)
    pygame.quit()

main()