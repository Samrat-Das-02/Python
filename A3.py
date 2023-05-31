#print first 10 odd and even numbers using iterators and compress.
def check_even(n):
    for i in range(2,n+1):
        if i % 2 == 0:
            yield i
def check_odd(n):
    for i in range(1,n):
        if i % 2 != 0:
            yield i
                       
even_numbers = iter(check_even(10))
odd_numbers = iter(check_odd(10))
print("List of first 10 even numbers")
for i in even_numbers:
    print(i)
print("List of first 10 odd numbers")
for i in odd_numbers:
    print(i)
