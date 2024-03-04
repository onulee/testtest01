numbers = [1,2,3,4,5,5,6,7,4,3,2,12,67,8,9]
counter = {}
for number in numbers:
    if number not in counter:
        counter[number]=0
    counter[number] += 1
print(counter)    