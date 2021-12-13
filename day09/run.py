
from re import I


def get_text():
    with open("day09/input.txt", "r") as file:
        nass = file.read()
    return nass
nass=get_text()
width  = len(nass.split('\n')[0])
print('width', width)
print ('nass', nass)
input= list(map(lambda c: int(c), nass.replace('\n','')))
print (input)
def is_local_minimum(index):
    """
        N
    W   x   E
        S
    """
    x_value = input[index]
    #N
    
    if index >= width:
        n= index - width
        n_value=input[n]
        if n_value <= x_value:
            return False
    #E
    if (index+1) % width != 0:
        e = index+1
        e_value=input[e]
        if e_value <= x_value:
            return False

    #S
    if index + width < len(input):
        s= index+width
        s_value=input[s]
        if s_value <= x_value:
            return False
    #W
    if index % width !=0:
        w= index-1
        w_value=input[w]
        if w_value <= x_value:
            return False
    #ELSE
    return True

index_array=range (len(input))
index_gefiltert= filter(is_local_minimum,index_array)
low_point=list(map(lambda index : input[index]+1, index_gefiltert))
print(sum(low_point))
