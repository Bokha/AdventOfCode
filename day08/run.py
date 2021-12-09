import re

def get_text():
    with open("day08/input.txt", "r") as file:
        input = file.read()
    return input
input=get_text()
print (input)
inputlines= input.split('\n')
new_input= list(map(lambda line: line.split(' | ')[1] ,inputlines ))
print ('new_input', new_input)
joint_str = ' ' + ' '.join(new_input) + ' '
print ('joint_str', joint_str)

pattern = '( [a-z]{7} )|( [a-z]{2} )|( [a-z]{4} )|( [a-z]{3} )'


m = re.findall(pattern,joint_str)
print ('m', m, len(m))

all_word = ' '.join(new_input).split(' ')
the_words= list(filter(lambda word: len(word) in[2,3,4,7] , all_word))
print ('the words', the_words, len(the_words))