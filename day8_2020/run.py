from calendar import c
import re
def get_text():
    with open("day8_2020/data.txt", "r") as file:
        nass = file.read()
    return nass
nass=get_text()
lines= nass.split ("\n")
def get_the_direction(line):
    richtung= (line.split(" "))[0]
    num= (line.split(" "))[1]
    return (richtung,int(num))

directions= list(map(get_the_direction, lines))
print(directions)

result=0
list_of_used_directions = []
current_loc = 0

#PART 1
"""""
while current_loc not in list_of_used_directions:
    pair=directions[current_loc]
    list_of_used_directions.append(current_loc)
    if pair[0]=='nop':
            current_loc=current_loc+1
    if pair[0]=='acc':
        result=result+pair[1]
        current_loc=current_loc+1
    if pair[0]=='jmp':
        current_loc=current_loc+pair[1]
            
print (result)
"""""
##Part 2:
def changing_the_direction(tup):
    (richtung,num) = tup
    if richtung== 'nop':
        richtung='jmp'
    if richtung== 'jmp':
        richtung='nop'
    return (richtung,num)
    
def run_directions(directions):
    result=0
    list_of_used_directions = []
    current_loc = 0
    while current_loc not in list_of_used_directions:
        if current_loc==len(directions):
            return result
        pair=directions[current_loc]
        list_of_used_directions.append(current_loc)
        if pair[0]=='nop':
                current_loc=current_loc+1
        if pair[0]=='acc':
            result=result+pair[1]
            current_loc=current_loc+1
        if pair[0]=='jmp':
            current_loc=current_loc+pair[1]
    return None
        
 

for x in range(len(directions)):
    directions2 = directions[:]
    directions2[x] =changing_the_direction(directions2[x])
    result=run_directions(directions2)
    if result !=None :
        print(result)
        exit()
    
