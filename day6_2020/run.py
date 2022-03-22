


def get_text():
    with open("day6_2020/data.txt", "r") as file:
        nass = file.read()
    return nass
nass=get_text()
groups=list(nass.split("\n\n"))


lista= list(map(lambda group: len(set(group.replace("\n",""))),groups))
print(sum(lista))

#Part2

def inter(group):
    result = 0
    lines=(group.split("\n"))

    for letter in lines[0] : 
        if letter_in_all_lines(letter,lines):
            result+=1
    return result

def letter_in_all_lines(letter, lines):
    for x in range(len(lines)):
        if letter not in lines[x]:
            return False
    return True

l2=list(map(inter,groups))

print(sum(l2))

