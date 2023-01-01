import random
import math
import keyboard
import os
import time

#aw shit here we go
print ("Press 'o' to initialize...")

# create the logs folder if it doesn't already exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# generate the log file name with the current time
log_file_name = f'log_{time.time()}.txt'

# open the log file in write mode
with open(f'logs/{log_file_name}', 'w') as log_file:
    # write the log message to the file
    log_file.write('This is a log message')

class Object:
    def __init__(self, name, x, y, vx, vy, mass):
        self.name = name
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass

    def update(self, forces):
        # update velocity based on forces acting on the object
        self.vx += forces[0] / self.mass
        self.vy += forces[1] / self.mass

        # update position based on velocity
        self.x += self.vx
        self.y += self.vy


class Flatland:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = []
        self.counter = 0 #next avail int


    def spawnObject(self):
        # generate random mass between 1 and 10
        mass = random.randint(1, 10)

        # generate random velocity vector
        vx = random.uniform(-1, 1)
        vy = random.uniform(-1, 1)

        # get the next available number
        number = self.nextNumber()

        # create object with the number as its name @ 0,0 (hopefully with a random vector lol)
        obj = Object(str(number), 0, 0, vx, vy, mass)
        self.objects.append(obj)

    def nextNumber(self):
        # increment the counter and return the current value
        self.counter += 1
        return self.counter

      # def update(self):
    #     for obj in self.objects:
    #         # check if the object is outside the bounds of the simulation
    #         if obj.x < 0 or obj.x > self.width or obj.y < 0 or obj.y > self.height:
    #             # if the object is outside the bounds, remove it from the list of objects
    #             self.objects.remove(obj)
    #             # print a message if the object is destroyed +log
    #             with open(r'C:\Users\Isa\Desktop\logs\{log_file_name}', 'w') as log_file:
    #
    #                 log_file.write(f'Object {obj.name} was destroyed! \n')
    #             print(f'Object {obj.name} was destroyed!')
    #             continue
    #
    #
    #         # calculate the forces acting on the object
    #         forces = self.calculateForces(obj)
    #         obj.update(forces)
    #         # check for collisions with other objects
    #         for other in self.objects:
    #             if other != obj:  # skip the current object
    #                 # calculate the distance between the two objects
    #                 dx = other.x - obj.x
    #                 dy = other.y - obj.y
    #                 r = math.sqrt(dx ** 2 + dy ** 2)
    #
    #                 # set the collision threshold (adjust as needed)
    #                 collision_threshold = 1
    #
    #                 if r < collision_threshold:
    #                     # print+log a message if the objects collide
    #                     log_file.write(f'Object {obj.name} collided with object {other.name}! \n')
    #                     print(f'Object {obj.name} collided with object {other.name}!')
    def update(self):
        # open the log file in append mode
        with open(f'logs/{log_file_name}', 'a') as log_file:
            for obj in self.objects:
                # check if the object is outside the bounds of the simulation
                if obj.x < 0 or obj.x > self.width or obj.y < 0 or obj.y > self.height:
                    # if the object is outside the bounds, remove it from the list of objects
                    self.objects.remove(obj)
                    # write a message to the log file if the object is destroyed
                    log_file.write(f'Object {obj.name} was destroyed! \n')
                    print(f'Object {obj.name} was destroyed!')
                    continue

                # calculate the forces acting on the object
                forces = self.calculateForces(obj)
                obj.update(forces)
                # check for collisions with other objects
                for other in self.objects:
                    if other != obj:  # skip the current object
                        # calculate the distance between the two objects
                        dx = other.x - obj.x
                        dy = other.y - obj.y
                        r = math.sqrt(dx ** 2 + dy ** 2)

                        # set the collision threshold (adjust as needed)
                        collision_threshold = 1

                        if r < collision_threshold:
                            # write a message to the log file if the objects collide
                            log_file.write(f'Object {obj.name} collided with object {other.name}! \n')
                            print(f'Object {obj.name} collided with object {other.name}!')

    def calculateForces(self, obj):
        G = 6.67408e-11  # gravitational constant

        forces = [0, 0]  # forces on the object in the x and y directions

        # calculate the forces due to gravity from other objects
        for other in self.objects:
            if other != obj:  # skip the current object
                    # calculate the distance between the two objects
                dx = other.x - obj.x
                dy = other.y - obj.y
                r = math.sqrt(dx ** 2 + dy ** 2)

                if r == 0:  # handle division by zero
                    continue
                elif r < 1:  # handle objects that are too close together
                    continue
                else:
                        # calculate the force between the two objects
                    f = G * ((obj.mass * other.mass) / r ** 2)
                    forces.append(f)
        return forces

    def render(self):
        output = ''
        for obj in self.objects:
            output += f'Object {obj.name}: x = {obj.x}, y = {obj.y}, vx = {obj.vx}, vy = {obj.vy}, mass = {obj.mass}\n'
        return output
        # generate the log file name with the current time
        log_file_name = f'log_{time.time()}.txt'
        # open the log file in write mode
        # with open(r'C:\Users\Isa\Desktop\logs\{log_file_name}', 'w') as log_file:
            # write the state of the simulation to the file
        log_file.write('Objects in simulation: \n')
        for obj in self.objects:
            log_file.write(f'{obj.name}: x = {obj.x}, y = {obj.y}, vx = {obj.vx}, vy = {obj.vy}, mass = {obj.mass} \n')
        for obj in self.objects:
             print(f'Object {obj.name}: x = {obj.x}, y = {obj.y}, vx = {obj.vx}, vy = {obj.vy}, mass = {obj.mass}')

        # create a Flatland instance with a width and height of 100

flatland_sim = Flatland(100, 100)

while True:
    # spawn a new object in Flatland
    if keyboard.is_pressed('o'):
            flatland_sim.spawnObject()

    # update the state of Flatland
    flatland_sim.update()

    with open(r'C:\Users\Isa\Desktop\logs\log.txt', 'a') as file:
        file.write('Simulation results:\n')
        file.write(flatland_sim.render())

    # render Flatland
    flatland_sim.render()
