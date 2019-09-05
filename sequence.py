# Design an algorithm that generates the first n numbers 
# in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

# next number is the sum of last 3 numbers

n = int(input("Enter the length of the sequence: "))

counter=3
num_1=1
num_2=2
num_3=3
summa=0

print(num_1)
print(num_2)
print(num_3)

while counter<=n-1:
    summa=num_1+num_2+num_3
    print(summa)
    num_1=num_2
    num_2=num_3
    num_3=summa
    counter+=1


