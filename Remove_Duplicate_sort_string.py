#Write a program that receives a string containing a sequence of white space separated words and returns a string after removing all duplicate words and sorting them alphanumerically
def process_string(string):
    words=string.split()
    unique_words=sorted(set(words))
    result=' '.join(unique_words)
    return result
string=input("Enter a string :" )
result=process_string(string)
print(result)