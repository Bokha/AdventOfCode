
def get_text():
    with open("day1/input.txt", "r") as file:
        nass = file.read()
        print (nass)
    return nass
nass=get_text()

numbers= list(map(lambda number: int(number), nass.split("\n")))

rang= range(len(numbers)-1)
found = 0
for x in rang:
    if (numbers[x])< (numbers[x+1]):
        found+=1  
print('Part1',found)

rang= range(len(numbers)-3)
found = 0
for x in rang:
    if (numbers[x])+(numbers[x+1])+(numbers[x+2])< (numbers[x+1])+(numbers[x+2])+(numbers[x+3]):
        found+=1  

print('Part2',found)
