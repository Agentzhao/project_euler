

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


number = 2520
list1 = [11,12,13,14,15,16,17,18,19,20]
list2 = []
found = False

def test():
    for i in list1:
        j = number / i
        if j % 2 == 0:
            list2.append(i)

while found == False:
    test()
    if list1 == list2:
        found = True
        print(number)
    else:
        number += 20
        list2 = []
