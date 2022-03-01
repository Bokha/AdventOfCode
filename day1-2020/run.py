def get_text():
    with open("day1-2020/data.txt", "r") as file:
        nass = file.read()
    return nass
nass=get_text()
numbers= list(map(lambda number: int(number), nass.split("\n")))
print(numbers)

def check_sum(numbers, k):   
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == k:
                print(numbers[i]* numbers[j])
                return True
    return False
print(check_sum(numbers,2020))
def check_sum3(numbers, k):   
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for n in range(i+2, len(numbers)):
                if numbers[i] + numbers[j]+numbers[n] == k:
                    print(numbers[i]* numbers[j]*numbers[n])
                    return True
    return False
print(check_sum3(numbers,2020))
