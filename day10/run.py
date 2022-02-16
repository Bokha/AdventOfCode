from enum import Enum
class State(Enum):
    valid = 1
    incomplete = 2
    corrupted = 3
def get_text():
    with open("day10/input.txt", "r") as file:
        nass = file.read()
    return nass
nass=get_text()
input= nass.split('\n')
#or ca =='>' or ca==']' or ca==''


def validate_chunk(chunk:str) -> tuple[State, str]:
    "validate chunks "
    stack=[]
    for ca in chunk:
        if ca in ['(','[', '{', '<']:
            stack.append(ca)
        if ca== ')' :
            if stack.pop() != '(':
                return (State.corrupted, ca)
        if ca== ']' :
            if stack.pop() != '[':
                return (State.corrupted, ca)
        if ca== '}' :
            if stack.pop() != '{':
                return (State.corrupted, ca)
        if ca== '>' :
            if stack.pop() != '<':
                return (State.corrupted, ca)
    if len(stack)>0 :
        return (State.incomplete, stack)
    return (State.valid, None)



array= (list(map(validate_chunk, input)))
print(array)
array_without_none= filter(lambda touple: touple[0] == State.corrupted, array)
array_of_ca= list(map(lambda touple: touple[1],array_without_none))
print(array_of_ca)
values = {')': 3,']':57 , '}':1197, '>': 25137 }
array_of_value=sum(map(lambda ca: values[ca], array_of_ca ))
print( 'array_of_value', array_of_value)

print('incomplete', validate_chunk('[({(<(())[]>[[{[]{<()<>>'))

array_incompleted= filter(lambda touple: touple[0] == State.incomplete, array)

def calculating(stst):
    scor = 0
    value=0
    stst.reverse()

    for str in stst:
        if str == '(':
            value=1
        elif str == '[':
            value=2
        elif str == '{':
            value=3
        elif str =='<':
            value=4
        else:
            print("Unknow " + str)
        scor= (scor * 5) + value
    
    print('stst', stst, scor)
    return scor
result= list(map(lambda touple: touple[1] , array_incompleted))
print('result',result)
ddd= list(map(lambda x: calculating(x), result))
sorted= sorted(ddd)
print('sorted',sorted)
print ('24',sorted[int((len(sorted) -1)/2)])
print (len(sorted))

