# string reserve using strinng slicing
def reverse(str):
     result_string = str[::-1]
     if (result_string==str):
          return True
     else :
          return False
str=input("enter the string : ")
if(reverse(str)==True):
     print("The String is palindrome ")
else:
     print("The String is not palindrome")     