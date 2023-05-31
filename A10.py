#filter out the odd squares using map,filter and list
def making_numbers_list(n):
    return list(map(lambda x: x**2, range(1,n+1)))

def odd_squares(n):
    return list(filter(lambda x: x%2!=0, making_numbers_list(n)))

n=int(input("Enter a range of values"))
odd_squares_list=list(odd_squares(n))
for i in odd_squares_list:
    print(i)
    