from os import system
from sys import stdout
from time import sleep 

def clear():
    _ = system('clear') 

def draw(x,y):
    clear()
    for i in range(0,len(A)):
        for j in range(0,len(A[0][0])):
            if x!=j or y!=i:
                stdout.write(A[i][0][j])
            else:
                stdout.write("O")
    sleep(0.3)

A = []
f = open('mapa.txt')
for line in f:
    A.append([line])


draw(2,2)
draw(3,2)
draw(4,2)
draw(5,2)
draw(6,2)
draw(7,2)
draw(8,2)
draw(9,2)
draw(10,2)
draw(11,2)
draw(12,2)
draw(13,2)
draw(13,3)
draw(13,4)
draw(13,5)
draw(13,6)
draw(13,7)
draw(13,8)
draw(13,9)
