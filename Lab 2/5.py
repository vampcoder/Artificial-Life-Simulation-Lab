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
colors = [black, green, blue, red, yellow]
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
    def __init__(self, name, position, size, color = (255, 255, 255),velocity = euclid.Vector2(0, 0) , width = 0):
        self.position = position
        self.name = name
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

    def agentfunc(self, agents, velocity, time):
        near, mindist = -1,10000000000000000
        for i in range(len(agents)):
            if not self.name == agents[i].name:
                diff = agents[i].position-self.position
                if diff.magnitude() < mindist:
                    mindist = diff.magnitude()
                    near = i
        agent = agents[near].position
        if random.randint(0, 100) < 30:
            x, y = generatePoints()
            agent = euclid.Vector2(x, y)

        diff = agent - self.position
        mag = diff.magnitude()
        position = self.position
        if (not mag == 0):
            position = self.position + velocity * time * (diff) / diff.magnitude()
        if self.collisionChecking(position, agents):
            self.move(position)


    def collisionChecking(self, position, agents):
        for i in range(len(agents)):
            if not self.position == agents[i].position:
                diff = agents[i].position - position
                if int(diff.magnitude()) <= 2 * agents[i].size:
                    # print agents[i].position, agents[current].position
                    return False
        return True


def generatePoints():
    return random.randint(0, 499), random.randint(0, 499)

def dist(x1, y1, x2, y2):
    return  ((x1-x2)**2 + (y1-y2)**2)**(0.5)


class environment:
    def __init__(self, velocity):
        size = 10
        no_of_bots = 10
        bots = []
        j = 0
        while len(bots) < no_of_bots:
            #print len(bots)
            flag = False
            while not flag:
                k = 0
                x, y = generatePoints()
                for i in range(len(bots)):
                    k += 1
                    if not dist(bots[i][0], bots[i][1], x, y) >= 2*size:
                        break

                if k == len(bots):
                    bots.append((x, y))
                    flag = True

        agents =[]
        for i in range(no_of_bots):
            agents.append(Mycircle(i, euclid.Vector2(bots[i][0], bots[i][1]), size, colors[random.randint(0, len(colors)-1)], velocity, 1))
        dtime_ms = clock.tick(60)
        timediff = dtime_ms / 100.0
        flag1 = True
        while flag1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag1 = False
            for i in range(no_of_bots):
                agents[i].agentfunc(agents, velocity, timediff)

            pygame.display.flip()

def check(pos1, pos2):
    if pos1.x <= pos2.x+1 and pos1.x > pos2.x-1 and pos1.y <= pos2.y+1 and pos1.y > pos2.y-1:
        return True



def main():
    initialize()
    env = environment(0.05)
    pygame.quit()

main()