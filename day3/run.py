def get_text():
    with open("day3/input.text", "r") as file:
        nass = file.read()
    return nass
numbers=get_text()
print(numbers)

def listing_the_numbers(text):
    lines_split_into_arrays= text.split('\n')
    columns = [[int(a_line_as_array[x]) for a_line_as_array in lines_split_into_arrays] for x in range(12)]
    return columns

columns = listing_the_numbers(numbers)
gamma=[]
beta=[]
for colum in columns:
    anzahl_der_1=sum(colum)
    anzahl_der_0= len (colum) - anzahl_der_1
    if anzahl_der_0> anzahl_der_1:
         gamma.append('0')
         beta.append('1')
    if anzahl_der_1> anzahl_der_0:
       gamma.append('1')
       beta.append('0')


print("gamma", "".join(gamma))
print("beta", "".join(beta))
1816*2279