from os import system
from sys import stdout
from time import sleep 
import random
from agent import *

def find_bounds(file): #f stands for file
    max_rows = 0
    max_global_column = 0
    max_local_column = 0
    f = open(file)
    for line in f:
        max_rows+=1
        max_local_column = len(line)-1
        for c in line:
            if c == '\t':
                max_local_column+=3
        if max_local_column > max_global_column:
            max_global_column = max_local_column
    f.close()
    return [max_rows,max_global_column]

def store_environment(file,bounds):    
    temp_environment = [[' ' for x in range(bounds[1])] for y in range(bounds[0])]
    cnt=0
    f = open(file)
    for line in f:
        cnt2=0;
        for c in line:
            if c == '\t':                
                cnt2+=3
            elif c != '\n' and c != ' ': 
                temp_environment[cnt][cnt2] = c
            cnt2+=1
        cnt+=1
    f.close()
    return temp_environment

#This function clears the terminal
def clear():
    #I like this reference to the functional programming
    _ = system('clear') 

def draw(x,y, environment,bounds,agent,direction,available_directions):
    clear()
    for i in range(0,bounds[0]):
        for j in range(0,bounds[1]):
            if x!=j or y!=i:
                stdout.write(environment[i][j])
            else:
                stdout.write("O")
        stdout.write('\n')

    stdout.write('\n')
    print("Numbering of addresses or sensors")
    print("     1 2 3     ")
    print("     4 * 6     ")
    print("     7 8 9     ")
    stdout.write('\n')
    stdout.write("Possible movements: " + str(available_directions))
    stdout.write('\n')
    stdout.write("Movement: " + str(direction))
    stdout.write('\n')
    stdout.write("Selected with the " + agent.strategy + " strategy")
    stdout.write('\n')
    sleep(0.04)

def get_possible_moves(agent_pos_x, agent_pos_y, environment,bounds, exits):
    #we see the environment as a cartesian plane, so the x"s are our horizontal
    #line in the half of the matrix (it divides
    #the matrix in top and bottom) and the y"s are our vertical line
    #(it divides the matrix in left and right).
    available_directions = []
    is_using_exits = False
    #[1, 2, 3]
    #[4, *, 6]
    #[7, 8, 9]
    #the next two if evaluates if the agent is inside the bounds
    #bounds[1] - 1 is for the column after the real right bound
    if agent_pos_x > 0 and agent_pos_x < bounds[1] - 1:
        if agent_pos_y > 0 and agent_pos_y < bounds[0] - 1:
            #print(str(agent_pos_x) + " " + str(agent_pos_y))
            if environment[agent_pos_y - 1][agent_pos_x - 1] == " ":
                available_directions.append(1)
            if environment[agent_pos_y - 1][agent_pos_x] == " ":
                available_directions.append(2)
            if environment[agent_pos_y - 1][agent_pos_x + 1] == " ":
                available_directions.append(3)
            if environment[agent_pos_y][agent_pos_x - 1] == " ":
                available_directions.append(4)
            if environment[agent_pos_y][agent_pos_x + 1] == " ":
                available_directions.append(6)
            if environment[agent_pos_y + 1][agent_pos_x - 1] == " ":
                available_directions.append(7)
            if environment[agent_pos_y + 1][agent_pos_x] == " ":
                available_directions.append(8)
            if environment[agent_pos_y + 1][agent_pos_x + 1] == " ":
                available_directions.append(9)
        else:
            exit_right_now = random.choice([0,1])
            if agent_pos_y == 0:
                if exit_right_now == 1:
                    available_directions = exits
                    is_using_exits = True
                else:
                    if(environment[agent_pos_y + 1][agent_pos_x]) == " ":
                        available_directions.append(8)
                    else:
                        available_directions = exits
                        is_using_exits = True
            else:
                if exit_right_now == 1:
                    available_directions = exits
                    is_using_exits = True
                else:
                    if(environment[agent_pos_y - 1][agent_pos_x]) == " ":
                        available_directions.append(2)
                    else:
                        available_directions = exits
                        is_using_exits = True
    else:
        exit_right_now = random.choice([0,1])
        if agent_pos_x == 0: 
            if exit_right_now == 1:
                available_directions = exits
                is_using_exits = True
            else:
                if(environment[agent_pos_y][agent_pos_x + 1]) == " ":
                    available_directions.append(6)
                else:
                    available_directions = exits
                    is_using_exits = True                        
        else:
            if exit_right_now == 1:
                available_directions = exits
                is_using_exits = True
            else:
                if(environment[agent_pos_y][agent_pos_x - 1]) == " ":
                    available_directions.append(4)
                else:
                    available_directions = exits
                    is_using_exits = True

    return [available_directions, is_using_exits]

def select_direction(available_directions,agent):
    #[1, 2, 3]
    #[4, *, 6]
    #[7, 8, 9]
    if(agent.times_in_border < 8):
        agent.times_in_border+=1
        agent.strategy="Edge tracking"
        if 6 not in available_directions and 8 in available_directions and 2 in available_directions:
            return 2
        elif 6 not in available_directions and 2 not in available_directions and 7 in available_directions:
            return 7
        elif 2 not in available_directions and 4 in available_directions:
            return 4
        elif 2 not in available_directions and 4 not in available_directions and 9 in available_directions:
            return 9
        elif 4 not in available_directions and 8 in available_directions:
            return 8
        elif 4 not in available_directions and 8 not in available_directions and 3 in available_directions:
            return 3
        elif 8 not in available_directions and 6 in available_directions:
            return 6
        elif 8 not in available_directions and 6 not in available_directions and 1 in available_directions:
            return 1
        else:
            agent.strategy="Random choice"
            selected = random.choice(available_directions)
            agent.times_in_border=0
            return selected
        
    else:
        agent.times_in_border=0
        selected = random.choice(available_directions)
        return selected

def move_agent(agent, environment,bounds, exits):
    directions = get_possible_moves(agent.x, agent.y, environment,bounds, exits)
    
    direction = select_direction(directions[0], agent)

    return agent.update_pos(direction, directions[1]),direction,directions[0]

def get_all_exits(environment,bounds):
    last_row = bounds[0] #it is the wall at the bottom
    exits = []
    for i in range(bounds[0]):
        last_column = bounds[1]
        if i == 0 or i == last_row:
            for j in range(last_column):
                if environment[i][j] == " ":
                    exits.append([j,i])
        else:
            if environment[i][0] == " ":
                exits.append([0, i])
            if environment[i][last_column - 1] == " ":
                exits.append([last_column - 1, i])
    print(exits)
    return exits

def main():
    try:
        text_map = str(input("Insert directory of the text file: "))
        rows,columns = find_bounds(text_map)
        #this is the field where the agent will exists.
        environment = store_environment(text_map,[rows,columns])    
        initial_x = int(input("Enter the position at x of the agent: "))
        initial_y = int(input("Enter the position at y of the agent: "))
        agent = Agent(initial_x, initial_y)
        exits = get_all_exits(environment,[rows,columns])
        print(exits)
        while True:
            new_pos = move_agent(agent, environment, [rows,columns], exits)
            draw(new_pos[0][0], new_pos[0][1], environment,[rows,columns], agent,new_pos[1],new_pos[2])
    except Exception as e:
        print(e)
        print("We fucked it up.")

main()
