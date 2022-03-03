from itertools import count
import re


def get_text():
    with open("day2-2020/data.txt", "r") as file:
        nass = file.read()
    return nass
nass=get_text()
lines= nass.split("\n")
print(lines)

def get_secret(line):
    pattern = "([0-9]+)\-([0-9]+) ([a-z]): ([a-z]+)"
    m = re.match(pattern, line)
    return (int(m.groups(0)[0]),int(m.groups(1)[1]),m.groups(2)[2],m.groups(3)[3])
print(get_secret("13-15 c: cqbhncccjsncqcc"))

passwords= list(map(get_secret,lines))

def is_valid(t):
    (min,max,letter,d) = t
    str_count= d.count(letter)
    if str_count>=min and str_count<=max:
        return True
    return False
print(is_valid((13, 15, 'c', 'cqbhncccjsncqcc')))

valid_passwords= list(filter(is_valid,passwords))
print (valid_passwords)
print (len(valid_passwords))

def is_valid2(t):
    (pos1,pos2,letter,d) = t
    firstl= d[pos1-1]
    secondl= d[pos2-1]

    if (letter==firstl) !=  (letter==secondl):
        return True
    return False
valid_passwords2= list(filter(is_valid2,passwords))
print (valid_passwords2)
print (len(valid_passwords2))
