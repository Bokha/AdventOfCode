import re
def get_text():
    with open("day1_2019/data.txt", "r") as file:
        nass = file.read()
    return nass
nass=get_text()
lines=list(nass.split("\n"))
print(lines)


def calculating(num):
    fuel=0
    result=int((int(num)/3) - 2)
    #part2
    while result >0:
        fuel+=result
        result=int(result/3) - 2
    print(fuel)

    return fuel

list_of_result= list(map(calculating,lines))
print (sum(list_of_result))
