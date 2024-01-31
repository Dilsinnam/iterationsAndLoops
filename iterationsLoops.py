# while loops:
# while <condition>: (Evaluates as 0 and 1, 0 is false, 1 is true.)
# <statments>

n = int(input("Enter the limit: "))  #

x = 1

while (
    x <= n
):  # compares integer to x, if true, goes to print, prints x, and adds 1 for how many times it needs to. Once it reaches a number larges than the input, it ends.
    print(x, end=" ")  # ' ' leaves a space inbetween.
    x += 1

# factorial calculator

f = 1
while (
    n > 0
):  # if n is 5, 5 is greater than 0, which goes into the code and multiply 1 x 5, storing that in f, and then going and rewriting n by subtracting 1 from n. Keeps checking with new values until false.
    f = f * n
    n = n - 1

# test problem

z = 3
while z < 10:
    z += 2
    while z <= 8:
        z += 3  # inner loop goes first ^, if it does not work, it will go to the outer loop.
print(z)

# for loops
# for val in container:
# <statement>

for i in range(
    1, 100 + 1, 5
):  # variable i is iterating from 1 to 100, limit value is always minus 1 so do one extra. i gets updated after every loop until the limit. Adding an extra comma will set the jump value (will jump by 5 in this case).
    print(i)

# factorial with for loop

forLoop = int(input("Enter the number: "))

p = 1
for i in range(1, forLoop + 1):
    p = p * i
print(p)

# printing patterns

length = int(input("Enter the length: "))

for i in range(1, length + 1):  # takes the length value and adds it until it ends.
    for j in range(1, length + 1):  # creates another line of stars.
        print("*", end="")
    print()  # by putting print here, it waits for the loop to end and creates rows.

# increasing pattern

for i in range(1, length + 1):  # takes the length value and adds it until it ends.
    for j in range(1, i + 1):  # creates another line of stars.
        print("*", end="")
    print()  # by putting print here, it waits for the loop to end and creates rows.

# break statements
# while ___
# break; # ends the whole loop with the current output
# while ___

# continue statements
g = 5
while g <= 10:
    g = g + 3
    continue  # pushes execution to nearest loop, makes any execution below if false.
    g = g + 2
