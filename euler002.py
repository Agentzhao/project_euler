#find all the fibon numbers below 4mil
numbers = [1,2]
while numbers[-1] < 4000000:
    numbers.append(numbers[-1]+numbers[-2])
del numbers[-1]

#find all the even numbers
even = []
for i in range (0,len(numbers)):
    if numbers[i]%2 == 0:
        even.append(numbers[i])
    else:
        continue

#find the total
total = 0
for i in range(0, len(even)):
    total = total + even[0]
    del even[0]

print(total)


#--------function version---------
def even_fibonacci(limit):
    numbers = [1,2]
    while numbers[-1] < limit:
      numbers.append(numbers[-1]+numbers[-2])
    del numbers[-1]
    
    #find all the even numbers
    even = []
    for i in range (0,len(numbers)):
      if numbers[i]%2 == 0:
          even.append(numbers[i])
      else:
          continue
    
    #find the total
    total = 0
    for i in range(0, len(even)):
      total = total + even[0]
      del even[0]
    
    return total
