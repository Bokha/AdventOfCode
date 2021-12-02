def get_text():
    with open("day2/input.txt", "r") as file:
        the_text = file.read()
        return the_text
nass =get_text()

lines= nass.split("\n")
touplat= list(map(lambda line: line.split(" "), lines))
print (touplat)

up_and_down=[]
forward=[]
for toupl in touplat:
    toupl[1]=int(toupl[1])
    if toupl[0]== 'up':
        toupl[1]=toupl[1]*-1
        up_and_down.append(toupl)
    if toupl[0]== 'down':
        up_and_down.append(toupl)
    if toupl[0]=='forward':
        forward.append(toupl)

    
print(up_and_down)
print(forward)

tief_result= sum(map(lambda toupl: toupl[1], up_and_down))
print(tief_result)
forward_result= sum(map(lambda toupl: toupl[1], forward))
print(forward_result)

the_answer= tief_result*forward_result
print(the_answer)


horizontal = 0
depth = 0
aim = 0

touplat= list(map(lambda line: line.split(" "), lines))
for toupl in touplat:
    toupl[1]=int(toupl[1])
    if toupl[0]== 'up':
       aim= aim - toupl[1]
    if toupl[0]== 'down':
        aim= aim+toupl[1]
    if toupl[0]=='forward':
         horizontal= horizontal+toupl[1]
         depth= depth +(aim* toupl[1])

print("Result 2 ", depth, horizontal, depth * horizontal)
