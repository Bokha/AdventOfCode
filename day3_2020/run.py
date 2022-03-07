

def get_text():
    with open("day3_2020/test.txt", "r") as file:
        nass = file.read()
    return nass
nass=get_text()

lines= nass.split("\n")


l=len(lines[0])
print(l)
def get_squares(down,right):
    y=0
    x=0
    number_of_squares=0
    while y < len(lines):
        if lines [y][x]=='#':
            number_of_squares+=1
        x=x+right
        x = x % l
        y=y+down
    return number_of_squares   
    

print(get_squares(1,1))
print(get_squares(1,3))
print(get_squares(1,5))
print(get_squares(1,7))
print(get_squares(2,1))
list=55*250*54*55*39
print (list)
ü=2*2*3*4*7
print(ü)