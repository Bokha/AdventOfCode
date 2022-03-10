import timeit
def get_text():
    with open("day5_2020/data.txt", "r") as file:
        nass = file.read()
    return nass
nass=get_text()
lines=list(nass.split("\n"))

def getting_the_row(x):
    k=0
    g= 127
    u=7
    l= 0
    for i in range(7):
        if x[i]== 'F':
            g= (((g-k)/2) +k) - 0.5
        else:
            k= g- ((g-k)/2) +0.5
        #print ('k', k, 'g', g)
    row= k
    for i in [7,8,9,]:
        if x[i]== 'L':
            u= (((u-l)/2) +l) -0.5
        else:
            l= u- ((u-l)/2)+0.5
        #print ('l', l, 'u', u)
    column= l
    ID= (row * 8) + column
    return ID

def get_id(x):
    k=0
    g= 1023
    for i in range(10):
        if x[i]in ['F', 'L']:
            g= (((g-k)/2) +k) - 0.5
        else:
            k= g- ((g-k)/2) +0.5
        print ('k', k, 'g', g)
    
    ID= k
    return ID

def get_id_re(x):
    return int(x.translate(str.maketrans({'F': '0', 'L': '0', 'B': '1', 'R': '1'})),2)

array_of_id= list(map( get_id_re,lines))
array_of_id.sort()
print(max(array_of_id))
#print(array_of_id)


for i in range(len(array_of_id)-1):
    if array_of_id[i]!= array_of_id[i+1]-1:
        print (array_of_id[i]+1)





#print(timeit.timeit('max(list(map( getting_the_row,lines)))',"from __main__ import getting_the_row, lines", number=10000))
#print(timeit.timeit('max(list(map( get_id_re,lines)))' ,"from __main__ import get_id_re, lines", number=10000))