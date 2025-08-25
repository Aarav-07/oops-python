#tuple to list add 2 elements
#list given 1. add 3 elements 2. alternate element 3. reverse by slicing
# make a pyramid 1
                #1 2
                #1 2 3
                #1 2 3 4
# make a pyramid 2 1
                #  2 2
                #  3 3 3 
                #  4 4 4 4
t = (1, 2, 3)
lst = list(t)
lst.append(4)
lst.append(5)
print("Tuple to List + 2 elements:", lst)

lst2 = [10, 20, 30]
lst2.extend([40, 50, 60])
print("After adding 3 elements:", lst2)
print("Alternate elements:", lst2[::2])
print("Reversed list:", lst2[::-1])

n = input("Enter a number: ")
n=int(n)
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

for i in range(1, n+1):
    print(" " * (n - i), end="")
    print("*" * (2*i - 1))
