def get_text():
    with open("day12/test.txt", "r") as file:
        the_text = file.read()
        return the_text
input=get_text
print(input)

### dict={'strat': [, , ], 'A': [ , , ], 'end': [ , , ] }
def read_input_into_dict():
    input =get_text()
    dict={}
    lines_split_into_arrays= input.split('\n')
    items_in_line= list(map( lambda line: line.split('-'), lines_split_into_arrays))
    print (items_in_line)
    for item in items_in_line:
        key = item[0]
        additional_value= item[1]
        if key in dict:
            dict[key].append (additional_value)
        else:
            dict[key]=[additional_value]
        
    return dict
print(read_input_into_dict())