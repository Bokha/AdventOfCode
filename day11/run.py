


def get_neighbors(row, col):
    return [(r, c) for r in [row -1,row, row+1] for c in [col-1,col,col+1] if (r,c) != (row, col)  ]

def get_text():
    with open("day11/input.txt", "r") as file:
        the_text = file.read()
        return the_text


def read_input_into_matrix():
    input =get_text()
    dict={}

    lines_split_into_arrays= input.split('\n')
    print (len(lines_split_into_arrays))
    for (row, line) in enumerate(lines_split_into_arrays):
        for (col, digit) in enumerate(line):
            key=(row,col)
            value=int(digit)
            dict[key]=value
    return dict

matrix= read_input_into_matrix()

def adding1_for_a_step(dictionary)-> int:
    list_of_10=[]
    for key in dictionary:
        dictionary[key] += 1
        if dictionary[key]== 10:
            list_of_10.append(key)
    ##flashing
    last_round_of_flashing= [i for i in list_of_10] #
    print('list_of_10', list_of_10)

    while len(last_round_of_flashing) > 0 :
        current = last_round_of_flashing.pop();
        neighbors = get_neighbors(current[0], current[1])
        for key in neighbors:
            if key in dictionary and key not in list_of_10:
                dictionary[key] += 1
                if dictionary[key] > 9:
                    list_of_10.append(key)
                    last_round_of_flashing.append(key)

    for key in list_of_10:
        dictionary[key] = 0
    return len(list_of_10)

ergebnis = 0
for x in range(1000):
    print('iteration ', x)
    num = adding1_for_a_step(matrix)
    if num == len(matrix):
        print ('x+1', x+1)
        exit(0)
    ergebnis +=num
print(ergebnis)