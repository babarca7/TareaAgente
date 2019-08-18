from os import system
from sys import stdout
from time import sleep 
import random
from agent import *

def find_bounds(file):
    f = open(file)

    max_rows = 0
    max_global_column = 0
    max_local_column = 0

    for line in f:
        max_rows+=1
        max_local_column = len(line)
        for c in line:
            if c == '\t':
                max_local_column+=3
        if max_local_column > max_global_column:
            max_global_column = max_local_column

    return [max_rows,max_global_column]

def store_environment(file,bounds):    
    temp_environment = [[' ' for x in range(bounds[1])] for y in range(bounds[0])]
    f = open(file)
    cnt=0
    for line in f:
        cnt2=0;
        for c in line:
            if c == '\t':                
                cnt2+=3
            elif c != '\n' and c != ' ': 
                temp_environment[cnt][cnt2] = c
            cnt2+=1
        cnt+=1
    return temp_environment

#This function clears the terminal
def clear():
    #I like this reference to the functional programming
    _ = system('clear') 

def draw(x,y, environment,bounds):
    clear()
    for i in range(0,bounds[0]):
        for j in range(0,bounds[1]):
            if x!=j or y!=i:
                stdout.write(environment[i][j])
            else:
                stdout.write("O")
        stdout.write('\n')
    sleep(0.4)

def get_possible_moves(agent_pos_x, agent_pos_y, environment,bounds):
    available_directions = []
    #[1, 2, 3]
    #[4, *, 6]
    #[7, 8, 9]
    #the next two if evaluates if the agent is inside the bounds
    if agent_pos_x > 0 and agent_pos_x < bounds[0]:
        if agent_pos_y > 0 and agent_pos_y < bounds[1]:
            #print(str(agent_pos_x) + " " + str(agent_pos_y))
            if environment[agent_pos_y - 1][agent_pos_x - 1] != "X":
                available_directions.append(1)
            if environment[agent_pos_y - 1][agent_pos_x] != "X":
                available_directions.append(2)
            if environment[agent_pos_y - 1][agent_pos_x + 1] != "X":
                available_directions.append(3)
            if environment[agent_pos_y][agent_pos_x - 1] != "X":
                available_directions.append(4)
            if environment[agent_pos_y][agent_pos_x + 1] != "X":
                available_directions.append(6)
            if environment[agent_pos_y + 1][agent_pos_x - 1] != "X":
                available_directions.append(7)
            if environment[agent_pos_y + 1][agent_pos_x] != "X":
                available_directions.append(8)
            if environment[agent_pos_y + 1][agent_pos_x + 1] != "X":
                available_directions.append(9)
    return available_directions

def select_direction(available_directions):
    selected = random.choice(available_directions)
    return selected

def move_agent(agent, environment,bounds):
    direction = select_direction(get_possible_moves(agent.x, agent.y, environment,bounds))
    return agent.update_pos(direction)

def main():
    try:
        text_map = str(input("Insert directory of the text file: "))
        text_map = 'map.txt'
        rows,columns = find_bounds(text_map)
        #this is the field where the agent will exists.
        environment = store_environment(text_map,[rows,columns])        
        initial_x = int(input("Enter the position at x of the agent: "))
        initial_y = int(input("Enter the position at y of the agent: "))
        agent = Agent(initial_x, initial_y)
        print(environment)
        while True:
            new_pos = move_agent(agent, environment, [rows,columns])
            draw(new_pos[0], new_pos[1], environment,[rows,columns])
    except Exception as e:
        print(e)
        print("We fucked it up.")

main()
