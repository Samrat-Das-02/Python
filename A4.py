#Regular expression to validate a phone number 
import re
def validate_phone_number(phone_number):
    pattern = "^\d{3}-\d{3}-\d{4}$" #pattern="^[6-9][0-9]{9}"
    if re.fullmatch(pattern, phone_number):
        return True
    else: return False
phn_number=input("Enter a phone number(xxx-xxx-xxxx) to validate :  ")
if(validate_phone_number(phn_number)==True): 
    print("Valid phone number")
else: print("Invalid phone number")
