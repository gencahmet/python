

from turtle import position


if __name__ == '__main__':
    x = int(input()) # max x
    y = int(input()) # max y
    z = int(input()) # max z
    n = int(input()) 
    
position = [] # list

for i in range(x+1):  # 0<x<max x 
    for j in range(y+1): # 0<y<maxy
        for k in range(z+1): # 0<z<maxz
            if i+j+k != n:
                position.append([i,j,k]) # list is added to list.

print(position)


    
