
import re
def get_text():
    with open("day8-2020/data.txt", "r") as file:
        nass = file.read()
    return nass
nass=get_text()
givinnumbers=list(nass.split("\n"))
givinnumbers=list(map(int, givinnumbers))

def is_valid(x,array):
    all_sum = [array[y]+array[x] for y in range(len(array)) for x in range(len(array)) if x!=y]
    print (all_sum)
    return x in all_sum
        
def checking_sum(arr):
    for i in range(25,len(arr)):
        x = arr[i]
        print(x)
        if is_valid (x,arr[i-25:i])==False:
            print(x)
            return x

#print(checking_sum(givinnumbers))

#PART2

the_sum=393911906
def finding_the_set(arr):
    for x in range(len(arr)-1):
        r=arr[x]
        for z in range(x+1,len(arr)):
            r+=arr[z]
            if r== the_sum:
                arr=arr[x:z]
                return min(arr)+ max(arr)


print(finding_the_set(givinnumbers))
#another way
def finding_the_set2(arr):
    for x in range(len(arr)-1):
        for z in range(x+1,len(arr)):
            if sum(arr[x:z])==the_sum:
                return min(arr[x:z])+ max(arr[x:z])
print(finding_the_set2(givinnumbers))