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
    def __init__(self, initialPosition, finalPosition, velocity):
        size = 3
        self.agent = Mycircle(initialPosition, size, green, velocity, 3)

        dtime_ms = clock.tick(60)
        timediff = dtime_ms / 100.0
        while True:
            time = 0
            flag = True
            while flag:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        flag = False
                current = AgentFunction(initialPosition, velocity, time, finalPosition)
                if current.x == -1 and current.y == -1:
                    flag = False
                else:
                    self.agent.move(current)
                time += timediff
                pygame.display.flip()
            flag = True
            time = 0
            while flag:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        flag = False
                current = AgentFunction(finalPosition, velocity, time, initialPosition)
                if current.x == -1 and current.y == -1:
                    flag = False
                else:
                    self.agent.move(current)
                time += timediff
                pygame.display.flip()

        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False

def check(pos1, pos2):
    if pos1.x <= pos2.x+1 and pos1.x > pos2.x-1 and pos1.y <= pos2.y+1 and pos1.y > pos2.y-1:
        return True

def AgentFunction(startPosition, velocity, time, finalPosition):
        diff = finalPosition - startPosition
        position = startPosition + velocity * time * (finalPosition - startPosition) / diff.magnitude()
        if check(position, finalPosition):
            return euclid.Vector2(-1, -1)
        else:
            return position

def main():
    initialize()
    env = environment(euclid.Vector2(5, 5), euclid.Vector2(200, 200), 0.01)
    pygame.quit()

main()