import sys

print("Binomial coefficient calculator")
print("Rule: 0 <= k <= n")

def factorial(x):
    i = 1
    while x >= 1:
        i = i * x
        x = x - 1
    return i

flag = True
while flag:
    n = input("Enter n (& to quit): ")
    if n == "&":
        flag = False
        sys.exit()
    k = input("Enter k (& to quit): ")
    if k == "&":
        flag = False
        sys.exit()

    n = int(n)
    k = int(k)
    
    if k > 0 and k < n:
        print("Result: ", int((factorial(n))/(factorial(k)*(factorial(n-k)))))
    elif k == 0 and k < n:
        print("Result: 1")
    else:
        print("Error!")
