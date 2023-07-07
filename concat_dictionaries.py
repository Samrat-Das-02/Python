#Write a program to create three dictionaries and concatcnate them to crcate fourth dictionary. Check whether a dictionary is empty or not. 
def concatdict(d1, d2,d3):
    result_dict={}
    result_dict.update(d1)
    result_dict.update(d2)
    result_dict.update(d3)    
    return result_dict
def is_empty(d):
    if(len(d)==0):   #check the lengthh of the dictionary
        return True
    else :
        return False
d1={1:"Ram", 2:"Shyam", 3:"Sam"}
d2={4:"Jack", 5:"Jhon", 6:"Dyan"}
d3= {7:"Dante", 8:"doretto",9:"Rock"}
concat_dict=concatdict(d1,d2,d3)
if(is_empty(concat_dict)):
    print("Empty dictionary")
else:
    print("The result dictionary after concatenation")
    print(concat_dict)    
