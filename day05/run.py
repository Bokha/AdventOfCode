
import re

def get_text():
    with open("day5/input.txt", "r") as file:
        nass = file.read()
        return nass
input=get_text()
lines= input.split("\n")
line_point= list(map(lambda line: line.split (" -> "), lines))
print("line_point")

# ['5,5', '8,2'] => [[5,5], [8,2]]
def text_to_arrays(l):
    point= list(map(lambda t: list(map(lambda i: int(i) , t.split(",")))  , l))
    return point

vent_lines= []
for x in line_point:
    funk= text_to_arrays(x)
    vent_lines.append(funk)
print("points")
points = []
for vent_line in vent_lines:
    #print('vent_line', vent_line)
    if vent_line[0][0] == vent_line[1][0]:
        x= vent_line[0][0]
        y_from = vent_line[0][1]
        y_to = vent_line[1][1]
        if(y_from > y_to):
            (y_from, y_to) = (y_to, y_from)
        points_to_add = [[x, y] for y in range(y_from, y_to + 1)]
        points = points + points_to_add
    elif vent_line[0][1] == vent_line[1][1]:
        y= min(vent_line[0][1], vent_line[1][1])
        x_from = vent_line[0][0]
        x_to = vent_line[1][0]
        if(x_from > x_to):
            (x_from, x_to) = (x_to, x_from)
        points_to_add = [[x, y] for x in range(x_from, x_to + 1)]
        points = points + points_to_add
    else:
        print('vent_line', vent_line)
        y_start = vent_line[0][1]
        y_target = vent_line[1][1]
        y_step = 1 if y_target > y_start else -1

        x_start = vent_line[0][0]
        x_target = vent_line[1][0]
        x_step = 1 if x_target > x_start else -1
        
        abs_diff = abs(y_target - y_start)
        


        points_to_add = [[x_start + i * x_step, y_start + i  * y_step] for i in range(0, abs_diff  + 1)]
        #print('points_to_add', points_to_add[:5])
        points = points + points_to_add



#points = [str(i[0])+ 'X' + str(i[1]) for i in points]
points = [tuple(i) for i in points]
points_nur_einmal= set(points)
print("points_nur_einmal", len(points_nur_einmal), len(points))

dict = {}
for point in points:
    old = dict.get(point)
    if old == None:
        old = 0
    dict[point] = old + 1  

two = len([ key for (key, value) in dict.items() if value >= 2])
print(two)


def finding_heufigkeiten (toupl):
    return len(list(filter(lambda point: point == toupl,points)))

#more_than_two = list(filter(lambda p: finding_heufigkeiten(p)>=2 ,points_nur_einmal))
#print("more_than_two", len(more_than_two))