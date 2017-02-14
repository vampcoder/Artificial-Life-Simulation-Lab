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
    screen_size = screen_width, screen_height = 500, 500
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

    def move(self, position):
        rx, ry = int(self.position.x), int(self.position.y)
        pygame.draw.circle(screen, white, (rx, ry), self.size, self.width)
        self.position = position
        self.changeColor(self.color)
        self.display()

    def change_velocity(self, velocity):
        self.velocity = velocity

def getRandomChoice():
    x = random.randint(0, 100)
    if x < 20:
        return 1
    else:
        return 2

class environment:
    def __init__(self, velocity):
        size = 3
        pos = [euclid.Vector2(10, 10), euclid.Vector2(200, 10), euclid.Vector2(200, 200), euclid.Vector2(10, 200)]
        dtime_ms = clock.tick(60)
        timediff = dtime_ms / 500.0
        center = euclid.Vector2(350, 150)
        initialAngle = 0
        radius = 70
        angularVelocity = 0.001
        initialPosition = center + euclid.Vector2(math.cos(initialAngle), math.sin(initialAngle))
        self.agent3 = Mycircle(euclid.Vector2(250, 450), size, blue, width=3)
        self.agent2 = Mycircle(initialPosition, size, red, width=3)
        i = 0
        self.agent1 = Mycircle(pos[0], size, green, velocity, 3)
        i = 0
        flag1 = True
        time2 = 0
        while flag1:
            self.agent1.move(pos[i%4])
            time1 = 0

            flag = True

            while flag and flag1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        flag1 = False
                finalPosition = pos[(i + 1)%4]

                current = AgentFunction1(pos[i%4], velocity, time1, finalPosition)
                if current.x == -1 and current.y == -1:
                    flag = False
                else:
                    self.agent1.move(current)
                finalPosition = pos[(i + 2) % 4]
                current = AgentFunction2(radius, center, initialAngle, time2, angularVelocity)
                self.agent2.move(current)

                current = self.agent3.position
                if getRandomChoice() == 1:
                    current = AgentFunction3(current, velocity, timediff, self.agent1.position)
                else:
                    current = AgentFunction3(current, velocity, timediff, self.agent2.position)
                if current == euclid.Vector2(-1, -1):
                    pass
                else:
                    self.agent3.move(current)

                time1 += timediff
                time2 += timediff

                pygame.display.flip()

            i += 1

def check(pos1, pos2):
    if pos1.x <= pos2.x+1 and pos1.x > pos2.x-1 and pos1.y <= pos2.y+1 and pos1.y > pos2.y-1:
        return True

def AgentFunction1(startPosition, velocity, time, finalPosition):
        diff = finalPosition - startPosition
        position = startPosition + velocity * time * (finalPosition - startPosition) / diff.magnitude()
        diff = position-finalPosition
        if check(position, finalPosition):
            return euclid.Vector2(-1, -1)
        else:
            return position

def AgentFunction2(radius, center, initialAngle, time, angularVelocity):
    Angle = initialAngle + angularVelocity * time
    position = center + radius * euclid.Vector2(math.cos(Angle), math.sin(Angle))
    return position

def AgentFunction3(currentPosition, velocity, time, finalPosition):
    diff = finalPosition - currentPosition
    position = currentPosition + velocity * time * (finalPosition - currentPosition) / diff.magnitude()
    diff = finalPosition-position

    if diff.magnitude() < 5:
        return euclid.Vector2(-1, -1)
    else:
        return position


def main():
    initialize()
    env = environment(0.1)
    pygame.quit()

main()