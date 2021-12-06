import re


class Matrix:
    def __init__(self, str):
        self.data =list(map(int,re.split('[^0-9]+', str.strip())))
    def get(self, row, col):
        return self.data[row* 5 + col]

    def is_row_solution(self, row, chosen_number:list[int]):
        for col in range(5):
            number= self.get(row, col)
            if number not in chosen_number:
                return False
        return True
    
    def is_col_solution(self, col, chosen_number):
        for row in range(5):
            number= self.get(row, col)
            if number not in chosen_number:
                return False
        return True
    
    def is_solution(self, chosen_number:list[int]):
        # print('chosen_number', chosen_number)
        for row in range(5):
            if self.is_row_solution(row, chosen_number):
                return True
        for col in range(5):
            if self.is_col_solution(col, chosen_number):
                return True
        return False
            
win_numbers=[93,18,74,26,98,52,94,23,15,2,34,75,13,31,39,76,96,16,84,12,38,27,8,85,86,43,4,79,57,19,40,59,14,21,35,0,90,11,32,17,78,83,54,42,66,82,99,45,55,63,24,5,89,46,80,49,3,48,67,47,50,60,81,51,71,33,72,6,9,30,56,20,77,29,28,69,25,36,91,92,65,22,62,58,64,88,10,7,87,41,44,37,73,70,68,97,61,95,53,1
]
def get_text():
    with open("day4/input.txt", "r") as file:
        nass = file.read()
    return nass
input=get_text()
groups= input.split("\n\n")
print("len", len(groups))

print("group 0", groups[0])


ms = list(map(Matrix, groups))
def print_solution():
    chosen_numbers = []
    for num in win_numbers:
        chosen_numbers.append(num)
        for matrix in ms:‚
            if matrix.is_solution(chosen_numbers):
                print("WINNNNEr")
                print(chosen_numbers)
                print(matrix.data)
                umarked_numbers =list(filter(lambda number: number not in chosen_numbers,matrix.data ))
                result = num * sum(umarked_numbers)
                print("Result", result)
                ms.remove(matrix)

print_solution()

