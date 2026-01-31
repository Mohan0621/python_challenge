'''1. Full Name (string)
2. Email ID (string)
3. Mobile Number (string)
4. Age (integer)
Based on the conditions below, determine whether the user profile is VALID or INVALID.
Validation Rules:
1. Full Name Validation
 Must contain at least two words
 Must not start or end with a space
2. Email ID Validation
 Must contain ‘@’ and ‘.’
 ‘@’ must not be the first character
3. Mobile Number Validation
 Must be exactly 10 characters
 Must contain only digits
 Must not start with 0
4. Age Validation
 Age must be between 18 and 60 (inclusive)
Expected Output:

 If all validations pass, print:
o User Profile is VALID
 If any validation fails, print:
o User Profile is INVALID

Test Cases (Mandatory – Your output must match these cases)
o Test Case 1
o Full Name: Yasir Afaq
o Email: yasir@gmail.com
o Mobile: 9622949937 (Must be exactly 10 digits and not start with 0)
o Age: 29
 Output:
 User Profile is VALID

o Test Case 2
o Input
 Full Name: Yasir
 Email: yasirgmail.com
 Mobile: 0876543210
 Age: 17
 Output:
Invalid: Full Name must contain at least two words
 User Profile is INVALID

o Test Case 3:
o Input;
 Full Name: Yasir Afaq
 Email: @gmail.com
 Mobile: 98765abc10
 Age: 45
 Output:
Invalid: Email must not start with '@'
 User Profile is INVALID

Constraints:
 No loops
 No advanced inbuilt functions
(Allowed: len(), count(), replace(), isdigit())
 No regular expressions
 No advanced libraries
 Use only data types, strings, and conditional statements.
'''

name = input("Enter Full Name :")
email = input("Enter Email ID :")
mobile = input("Enter Mobile Number :")
age = int(input("Enter Age :"))
valid=True
if valid:
    if name.count(" ")<1 :
        valid=False
        print("Invalid: Full Name must contain at least two words")
    elif name[0]==" " or name[-1]==" ":
        valid=False
        print("Invalid: Full Name must not start or end with a space")
if valid :
    if email.count('@')!=1 or email.count('.')!=1 or email.count('#')>0 or email.count('$')>0 or email.count('%')>0 or email.count('^')>0 or email.count('&')>0 or email.count('*')>0 or "(" in email or ")" in email or "_" in email or "+" in email or "=" in email or "!" in email or "~" in email or "`" in email or "/" in email or "\\" in email or "," in email or ";" in email or ":" in email or "'" in email or '"' in email or "<" in email or ">" in email:
        valid=False
        print("Invalid: Email should contain '@' and '.' only and it should not contain special characters")
        
    elif email[0]=='@':
        valid=False
        print("Invalid: Email must not start with '@'")
if valid :
    if len(mobile)!=10 or not mobile.isdigit() :
        valid=False
        print("Invalid: Mobile Number must be exactly 10 digits and contain only digits")
    elif mobile[0]=='0':
        valid=False
        print("Invalid: Mobile Number must not start with 0")
if valid :
    if age<18 or age>60:
        valid=False
        print("Invalid : Age Should be between 18 and 60")
if valid:
    print("User Profile is valid")
else:
    print("User Profile is Invalid")