from os import system
from sys import stdout
from time import sleep 
import random

#This function clears the terminal
def clear():
    #I like this reference to the functional programming
    _ = system('clear') 

def draw(x,y):
    clear()
    for i in range(0,len(environment)):
        for j in range(0,len(environment[0][0])):
            if x!=j or y!=i:
                stdout.write(environment[i][0][j])
            else:
                stdout.write("O")
    sleep(0.3)

def get_possible_moves(agent_pos_x, agent_pos_y, environment):
    available_directions = []
    #[1, 2, 3]
    #[4, *, 6]
    #[7, 8, 9]
    #the next two if evaluates if the agent is inside the bounds
    if agent_pos_x > 0 and agent_pos_x < len(environment):
        if agent_pos_y > 0 and agent_pos_y < lowest_right_bound:
            #print(str(agent_pos_x) + " " + str(agent_pos_y))
            if environment[agent_pos_y - 1][0][agent_pos_x - 1] != "X":
                available_directions.append(1)
            if environment[agent_pos_y - 1][0][agent_pos_x] != "X":
                available_directions.append(2)
            if environment[agent_pos_y - 1][0][agent_pos_x + 1] != "X":
                available_directions.append(3)
            if environment[agent_pos_y][0][agent_pos_x - 1] != "X":
                available_directions.append(4)
            if environment[agent_pos_y][0][agent_pos_x + 1] != "X":
                available_directions.append(6)
            if environment[agent_pos_y + 1][0][agent_pos_x - 1] != "X":
                available_directions.append(7)
            if environment[agent_pos_y + 1][0][agent_pos_x] != "X":
                available_directions.append(8)
            if environment[agent_pos_y + 1][0][agent_pos_x + 1] != "X":
                available_directions.append(9)
    print(available_directions)
    return available_directions

def select_direction(available_directions):
    print(available_directions)
    selected = random.choice(available_directions)
    return selected

def update_pos(agent_pos_x, agent_pos_y, new_direction):
    #print(str(agent_pos_x) + "," + str(agent_pos_y))
    if new_direction == 1:
        agent_pos_x -= 1
        agent_pos_y -= 1
    elif new_direction == 2:
        agent_pos_y -= 1
    elif new_direction == 3:
        agent_pos_x += 1
        agent_pos_y -= 1
    elif new_direction == 4:
        agent_pos_x -= 1
    elif new_direction == 6:
        agent_pos_x += 1
    elif new_direction == 7:
        agent_pos_x -= 1
        agent_pos_y += 1
    elif new_direction == 8:
        agent_pos_y += 1
    else:
        agent_pos_x += 1
        agent_pos_y += 1
    updated_pos = []
    updated_pos.append(agent_pos_x)
    updated_pos.append(agent_pos_y)
    return updated_pos#this could be a tuple


#this is the field where the agent will exists.
environment = []
#we do not know if the text has a NxM fixed size.
lowest_right_bound = 99999999999 #infinite
f = open('mapa.txt')
for line in f:
    if len(line) < lowest_right_bound:
        lowest_right_bound = len(line)
    environment.append([line])

agent_pos_x = 10
agent_pos_y = 12

def move_agent(agent_pos_x, agent_pos_y):
    direction = select_direction(get_possible_moves(agent_pos_x, agent_pos_y, environment))
    return update_pos(agent_pos_x, agent_pos_y, direction)
while True:
    new_pos = move_agent(agent_pos_x, agent_pos_y)
    agent_pos_x = new_pos[0]
    agent_pos_y = new_pos[1]
    #print(str(agent_pos_x) + "," + str(agent_pos_y))
    draw(agent_pos_x,agent_pos_y)

#for i in range(10):
    #stdout.write("\r{0}>".format("="*i))
    #stdout.flush()
    #sleep(0.5)
