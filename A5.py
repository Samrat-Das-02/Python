#To generate the first 10 Fibonacci numbers using a generator function and the yield keyword in Python, you can define a generator function that yields the Fibonacci numbers one by one. Here's an example:
def generate_fibonacci(n):
    a, b = 0, 1
    count=0
    while count < n:
        yield a
        a, b = b, a+b
        count += 1
n=int(input("Enter a range : "))
fibo=iter(generate_fibonacci(n))
print("The list of fibonacci numbers within the range :: ")
for i in fibo:
    print(i)
