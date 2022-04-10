import re
def get_text():
    with open("day10_2020/data.txt", "r") as file:
        nass = file.read()
    return nass
nass=get_text()
lines=list(nass.split("\n"))
numbers=list(map(lambda x: int(x),lines))
my_adapter= max(numbers)
numbers.append(my_adapter+3)
numbers.append(0)
numbers.sort()
print(numbers)
def getting_adapters(numb):
    ein_zähler=0
    zwei_zähler=0
    drei_zähler=0   
    for i in range(len(numb)-1):
        if numb[i]+1==numb[i+1]:
            ein_zähler+=1
        if numb[i]+2==numb[i+1]:
            zwei_zähler+=1
        if numb[i]+3==numb[i+1]:
            drei_zähler+=1
    return ein_zähler*drei_zähler
print(getting_adapters(numbers))
'part 2'
def getting_the_dif(arr):
    new_list=[]
    for i in range(1,len(arr)):
        d=arr[i]-arr[i-1]
        new_list.append(d)
    return new_list
lista=getting_the_dif(numbers)
print(lista)
def getting_the_chain(lista):
    segmente = [0,0,0,0,0]
    einsen = 0
    for x in lista:
        if x==1:
            einsen +=1
        if x==3:
            segmente[einsen] +=1
            einsen = 0
    return segmente
print(getting_the_chain(lista))

y=2**5
s=4**8
l=7**8
print(y*s*l)
