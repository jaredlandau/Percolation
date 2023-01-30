## *************************
## Percolation Theory v0.1
##   Two dimensional graph-based model of percolation theory,
##   created to analyse the effect of various p-values on emergent cluster behaviour.
##
## Authors: Jeremy Rabinowicz
##          Jared Landau
## 15/11/2022
## *************************

import random
import numpy as np
import cv2
from pathlib import Path


class DisjointSet:
    def __init__(self, n):
        self.disjoint_set = [-1] * n

    def find(self, item):
        if self.disjoint_set[item] < 0:
            return item
        else:
            root = self.find(self.disjoint_set[item])
            self.disjoint_set[item] = root
            return root

    def union(self, item1, item2):
        root1 = self.find(item1)
        root2 = self.find(item2)
        if root1 == root2:
            return False

        height1 = -self.disjoint_set[root1]
        height2 = -self.disjoint_set[root2]

        if height1 > height2:
            self.disjoint_set[root2] = root1
        elif height1 < height2:
            self.disjoint_set[root1] = root2
        else:
            self.disjoint_set[root1] = root2
            self.disjoint_set[root2] -= 1

        return True


def generate_percolation(size_x, size_y, p):
    disjoint_set = DisjointSet(size_x * size_y)
    for y in range(size_y):
        for x in range(size_x):
            # Check the left case and connect with a probability p
            if x % size_x != 0:
                if random.random() <= p:
                    disjoint_set.union(y * size_x + (x - 1), y * size_x + x)
            # Check the upper case and connect with probability p
            if y != 0:
                if random.random() <= p:
                    disjoint_set.union((y - 1) * size_x + x, y * size_x + x)

    return disjoint_set


def print_percolation_grid(size_x, size_y, disjoint_set):
    grid = np.zeros((size_y, size_x, 3))

    def define_cell(x, y, percolation_set, pic_grid):
        val = percolation_set.find(y * size_x + x)
        if val == y * size_x + x:
            if list(grid[y, x]) != [0, 0, 0]:
                return grid[y,x]
            else:
                colour = generate_rgb()
                pic_grid[y, x] = colour
                return colour
        else:
            new_x = val % size_x
            new_y = val // size_x
            returned_colour = define_cell(new_x, new_y, percolation_set, pic_grid)
            pic_grid[y, x] = returned_colour

    for x in range(size_x):
        for y in range(size_y):
            if list(grid[y, x]) == [0, 0, 0]:
                define_cell(x, y, disjoint_set, grid)

    return grid


def generate_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def generate_network_image(x,y,p,i):
    Path("networks/n" + str(x) + "/").mkdir(parents=True, exist_ok=True)
    filename = str("networks/n" + str(x) + "/perc" + "_n" + str(x) + "_p" + str(f'{p:.4f}') + "_i" + str(i) + ".png")
    cv2.imwrite(filename, print_percolation_grid(x, y, generate_percolation(x, y, p)))
    print("Image has been saved under " + filename)


def generate_multiple_networks(numOfNetworks):
    i = 0
    n = int(input("n value: "))
    p = round(float(input("median p value: ")),4)
    step = round(float(input("step value: ")),4)

    p -= (step * (numOfNetworks - 1) * 0.5)

    while(i < numOfNetworks):
        print("Generating graph for p = " + str(p))
        generate_network_image(n,n,p,i)
        i += 1
        p = np.round(p + step,4)

    print("Done!")


if __name__ == '__main__':
    userInput = input("Generate a batch of graphs? (y/n)\n").lower()
    if(userInput == "y"):
        generateBatch = True
    else:
        generateBatch = False
    
    running = True
    i = 0
    while(running):
        if(generateBatch):
            numOfNetworks = int(input("How many networks do you want to generate?\n"))
            generate_multiple_networks(numOfNetworks)
            running = False
            break
        else:
            n = int(input("n value: "))
            p = float(input("p value: "))

            generate_network_image(n,n,p,i)

            userChoice = input("Generate a new graph? (y/n)\n").lower()
            if(userChoice == "n"):
                print("Exiting...")
                running = False
                break
            else:
                print("Restarting...")
                i += 1
                continue