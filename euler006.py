#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumofsquare = 0
for i in range (1,100):
    sumofsquare += i**2

squareofsum = 0
for i in range(1,100):
    squareofsum += i
squareofsum = squareofsum**2

print(squareofsum - sumofsquare)
