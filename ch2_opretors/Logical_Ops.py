a = 1000 
b = 2000 

##############################################
############# And Operator ###################
##############################################
print("Logical AND Operator Results:")
print(a > b and b < a)   # 1000 > 2000 = False and 2000 < 1000 = False     false  false  false    
print(b > a and b < a)   # 2000 > 1000 = True  and 2000 < 1000 = False     true   false  false
print(b < a and a > b)   # 2000 < 1000 = False and 1000 > 2000 = False     false  false  false
print(a < b and b > a)   # 1000 < 2000 = True  and 2000 > 1000 = True      true   true   true


##############################################
############# OR Operator ###################
##############################################

print("Logical OR Operator Results:")
print(a > b or b < a)   # 1000 > 2000 = False or 2000 < 1000 = False     false  false false
print(b > a or b < a)   # 2000 > 1000 = True  or 1000 < 2000 = True      true   true  true
print(b > a or b < a)   # 2000 > 1000 = True  or 2000 < 1000 = False     true   false true
print(b < a or b > a)   # 2000 < 1000 = False or 2000 > 1000 = True      false  true  true
   

##############################################
########### Membership Operators: ############
##############################################

print("Membership Operators:")

# String Example
print('a' in 'apple')       #  True — 'a' is in 'apple'
print('d' in 'apple')       #  False — 'd' is not in 'apple'


# List Example
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)    # True — banana is in the list
print('grape' not in fruits) # True — grape is not in the list

