__name__ = "RoboPos"
"""Created by Dustin Brashear, Jan 2014"""
"""Designed to generate simulated robots and
   distribute them based on simulated attributes"""

import math as m

def check(a, b):
    a.sort()
    return a in b

robot_attr = ['herder', 'goalie', 'launcher', 'catcher']
robot_attr.sort()
robots = [[attr] for attr in robot_attr]
sums = 69
for i in range(3):      #generates all unique attribute lists of size 2
    temp_check = robot_attr[i + 1:]
    for j in range(len(temp_check)):
        temp = [robot_attr[i]]
        temp.append(temp_check[j])
        robots.append(temp)

for i in range(2):      #generates all unique attribute lists of size 3
    temp_check = robot_attr[i + 1:]
    for j in range(len(temp_check)):
        temp_check_b = temp_check[j + 1:]
        for k in range(len(temp_check_b)):
            temp = [robot_attr[i]]
            temp.append(temp_check[j])
            temp.append(temp_check_b[k])
            if not check(temp, robots):
                robots.append(temp)
                
l = []
for e in robot_attr:
    l.append(e)
robots.append(l)

zones = {'Home' : 0, 'Middle' : 0, 'Goal' : 0}

home = []
middle = []
goal = []

for robot in robots: #assigns robots to zones based on certain criteria
    if 'herder' in robot or 'goalie' in robot:
        home.append(robot)
    if ('launcher' in robot and 'catcher' in robot) or 'herder' in robot:
        middle.append(robot)
    if 'launcher' in robot and 'herder' in robot:
        goal.append(robot)
zones['Home'] = home
zones['Middle'] = middle
zones['Goal'] = goal

for key in zones:
    print key
    for value in zones[key]:
        print value, '\n'
