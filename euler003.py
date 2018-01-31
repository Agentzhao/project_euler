n = 600851475143 
i = 2

while i * i < n: 
    while n%i == 0:
        n = n / i
    i = i + 1

print (n)

#------function version-------
def lpfactor(number):
    
    i = 2
    
    while i * i < number:
        while number%i == 0:
            n = n / i
        i = i + 1
    
    return n
