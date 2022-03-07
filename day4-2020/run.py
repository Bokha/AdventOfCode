import re

def get_text():
    with open("day4-2020/data.txt", "r") as file:
        nass = file.read()
    return nass
nass=get_text()
#allpassports= nass.replace('\n', " ")
passports=nass.split("\n\n")
passpor= list(map(lambda x: x.replace('\n', " ").split(" "),passports))
print (passpor[0])

def list_to_dict(l):

    f={item.split(":")[0] : item.split(":")[1]  for item in l}
    return f
d=list(map(list_to_dict,passpor))
print(d[0].get('byrf'))


valid_passports=list(filter(lambda item: item.get ('byr') and item.get ('iyr') and item.get ('eyr') and item.get ('hcl') and item.get ('ecl') and item.get('pid') and item.get('hgt'),d))


def filtering_passports(item):
    if int(item['byr']) not in range(1919,2003):
        return False
    if int(item['iyr']) not in range(2009,2021):
        return False
    if int(item['eyr']) not in range (2019,2031):
        return False
    if item['hgt'][-2:] =="cm":
        if int(item['hgt'][:-2]) not in range(149,194):
            return False
    elif item['hgt'][-2:] =="in":
        if int(item['hgt'][:-2]) not in range(58,77):
            return False
    else:
        return False
    if not re.match(r"^#[0-9a-z]{6}$" , item['hcl']):
        return False
    if item['ecl'] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if not re.match(r"^[0-9]{9}$" , item['pid']):
        return False
    return True
valid_passports2= list(filter(filtering_passports, valid_passports))
print(len(valid_passports2))

    

