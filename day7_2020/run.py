from multiprocessing.sharedctypes import Value
import re
def get_text():
    with open("day7_2020/data.txt", "r") as file:
        nass = file.read()
    return nass
nass=get_text()
lines=list(nass.split("\n"))
 
def splitting_the_line(line):
    result=line.split(" bags contain ")
    print(result[1] .strip(' bags.'))
    tafsil=result[1] .replace(' bags.', '').replace(' bag.', '').replace(" bags, ", " bag, ").split (" bag, ")
    if 'no other' in tafsil:
        tafsil = []
    return (result[0],tafsil)
print(splitting_the_line('pale beige bags contain 1 mirrored fuchsia bag.'))

all_tuplat=list(map(splitting_the_line, lines))

#list_contained_gold=set([])
#for pair in all_tuplat:
#    if any('shiny gold' in s for s in pair[1]):
#        list_contained_gold.add(pair[0])

print(all_tuplat)
def get_the_number(arr):
    listdic=[]
    for item in arr:
        colourdic={}
        new_item=item.split(" ", 1)
        num= new_item[0]
        det=new_item[1]
        colourdic['count']= num
        colourdic['colour']=det
        listdic.append(colourdic)
    return listdic


dic= {  key: get_the_number(val) for (key,val) in all_tuplat }

def count_contained(colour, dic):
    print('colour', colour)
    aadad=[]
    l=dic[colour]
    for x in l:
        aadad.append(int(x['count']) + int(x['count'])* count_contained(x['colour'], dic))
        
    return sum(aadad)


print(count_contained('shiny gold',dic))


## Part 1
"""
old_len = 0
list_contained_gold = set(['shiny gold'])
while len((list_contained_gold)) != old_len:
    old_len= len(list_contained_gold)
    for item in list(list_contained_gold):
        for pair in all_tuplat:
            if any(item in s for s in pair[1]):
              list_contained_gold.add(pair[0])

print (len(list_contained_gold)-1)
"""

#def get_the_colour(line):
 #   pattern = "(^[a-z]+ [a-z]+) bags contain (([0-9] [a-z]+ [a-z]+) bags?(, )?)+"#, ([0-9][a-z]+ [a-z]+), ([0-9][a-z]+ [a-z]+) ([a-z]+.)"
  #  m = re.match(pattern, line)
   # return (m)
#print(get_the_colour("light gold bags contain 2 light lime bags, 1 faded green bag, 3 clear olive bags, 2 dim bronze bags."))

#{'shiny gold': [{'count': 1, 'color': 'dark olive', ....}],'dark olive'}

