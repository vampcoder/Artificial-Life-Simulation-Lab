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

def getRandomChoice1():
    x = random.randint(0, 100)
    if x < 30:
        return 1
    elif x < 60:
        return 2
    else:
        return 3

def getRandomChoice2():
    x = random.randint(0, 100)
    if x < 30:
        return 0
    elif x < 60:
        return 2
    else:
        return 3

def getRandomChoice3():
    x = random.randint(0, 100)
    if x < 30:
        return 0
    elif x < 60:
        return 1
    else:
        return 3

def getRandomChoice4():
    x = random.randint(0, 100)
    if x < 30:
        return 0
    elif x < 60:
        return 1
    else:
        return 2



class environment:
    def __init__(self, velocity):
        size = 3
        pos = [euclid.Vector2(10, 10), euclid.Vector2(400, 10), euclid.Vector2(400, 400), euclid.Vector2(10, 400)]
        dtime_ms = clock.tick(60)
        timediff = dtime_ms / 500.0
        i = 0
        self.agent0 = Mycircle(pos[0], size, green, velocity, 3)
        self.agent1 = Mycircle(pos[1], size, red, velocity, 3)
        self.agent2 = Mycircle(pos[2], size, blue, velocity, 3)
        self.agent3 = Mycircle(pos[3], size, black, velocity, 3)

        flag1 = True
        time2 = 0
        while flag1:
            time1 = 0
            flag = True
            while flag and flag1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        flag1 = False
                choice = getRandomChoice1()
                finalPosition = pos[choice]
                current = self.agent0.position
                current = AgentFunction3(current, velocity, timediff, finalPosition)
                if current.x == -1 and current.y == -1:
                    pass
                else:
                    self.agent0.move(current)
                    pos[0] = current

                choice = getRandomChoice2()
                finalPosition = pos[choice]
                current = self.agent1.position
                current = AgentFunction3(current, velocity, timediff, finalPosition)
                if current.x == -1 and current.y == -1:
                    pass
                else:
                    self.agent1.move(current)
                    pos[1] = current

                choice = getRandomChoice2()
                finalPosition = pos[choice]
                current = self.agent2.position
                current = AgentFunction3(current, velocity, timediff, finalPosition)
                if current.x == -1 and current.y == -1:
                    pass
                else:
                    self.agent2.move(current)
                    pos[2] = current

                choice = getRandomChoice3()
                finalPosition = pos[choice]
                current = self.agent3.position
                current = AgentFunction3(current, velocity, timediff, finalPosition)
                if current.x == -1 and current.y == -1:
                    pass
                else:
                    self.agent3.move(current)
                    pos[3] = current

                time1 += timediff
                time2 += timediff

                pygame.display.flip()

            i += 1

def check(pos1, pos2):
    if pos1.x <= pos2.x+1 and pos1.x > pos2.x-1 and pos1.y <= pos2.y+1 and pos1.y > pos2.y-1:
        return True

def AgentFunction3(currentPosition, velocity, time, finalPosition):
    diff = finalPosition - currentPosition
    mag = diff.magnitude()
    position = currentPosition
    if not mag == 0:
        position = currentPosition + velocity * time * (finalPosition - currentPosition) / diff.magnitude()

    diff = finalPosition-position
    if diff.magnitude() < 1:
        return euclid.Vector2(-1, -1)
    return position

def main():
    initialize()
    env = environment(0.1)
    pygame.quit()

main()