import sys

arr = ["FizzBuzz", "Fizz", "Buzz"]

for i in range(3):
    a = str(sys.stdin.readline().rstrip())

    if(a not in arr):
        n = int(a) + 3 - i

if(n%3==0 and n%5==0):
    res = "FizzBuzz"
elif(n%3==0 and n%5!=0):
    res = "Fizz"
elif(n%3!=0 and n%5 == 0):
    res = "Buzz"
else:
    res = str(n)

print(res)