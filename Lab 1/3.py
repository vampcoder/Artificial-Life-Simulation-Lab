import os, sys, math, pygame, pygame.mixer, euclid, time
from pygame.locals import *
import random
from math import sin, cos, pi

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
        rx, ry = int(self.position.x), int(self.position.y)
        pygame.draw.circle(screen, white, (rx, ry), self.size, self.width)
        self.position = position
        self.changeColor(self.color)
        self.display()

    def change_velocity(self, velocity):
        self.velocity = velocity

class environment:
    def __init__(self, pos1, pos2, pos3, velocity):
        size = 3
        self.agent1 = Mycircle(pos1, size, green, velocity, 3)
        self.agent2 = Mycircle(pos2, size, blue, velocity, 3)
        self.agent3 = Mycircle(pos3, size, red, velocity, 3)
        time = 0
        flag = True
        dtime_ms = clock.tick(60)
        timediff = dtime_ms / 100.0
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False

            current = AgentFunction(self.agent1.position, velocity, timediff, self.agent2.position)
            if current.x == -1 and current.y == -1:
                flag = False
            else:
                self.agent1.move(current)

            current = AgentFunction(self.agent2.position, velocity, timediff, self.agent3.position)
            if current.x == -1 and current.y == -1:
                flag = False
            else:
                self.agent2.move(current)
            pygame.display.flip()

            current = AgentFunction(self.agent3.position, velocity, timediff, self.agent1.position)
            if current.x == -1 and current.y == -1:
                flag = False
            else:
                self.agent3.move(current)
            pygame.display.flip()

        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False

def check(pos1, pos2):
    if pos1.x <= pos2.x+1 and pos1.x > pos2.x-1 and pos1.y <= pos2.y+1 and pos1.y > pos2.y-1:
        return True

def AgentFunction(currentPosition, velocity, time, finalPosition):
        diff = finalPosition - currentPosition
        position = currentPosition + velocity * time * (finalPosition - currentPosition) / diff.magnitude()
        if check(position, finalPosition):
            return euclid.Vector2(-1, -1)
        else:
            return position

def main():
    initialize()
    center = euclid.Vector2(150, 150)
    radius = 70
    pos1 = euclid.Vector2(center.x + radius*cos(0), center.y + radius*sin(0))
    pos2 = euclid.Vector2(center.x + radius * cos(2*pi/3), center.y + radius * sin(2*pi/3))
    pos3 = euclid.Vector2(center.x + radius * cos(4*pi/3), center.y + radius * sin(4*pi/3))
    env = environment(pos1, pos2, pos3, 0.01)
    pygame.quit()

main()