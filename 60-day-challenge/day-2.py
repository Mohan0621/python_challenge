'''Scenario: A university is creating a Smart Registration System. Before approving a student
account, the system must verify whether the entered credentials follow strict university rules.
Your task is to build a Credential Validator using only:
String
Conditional statements
No loops
No lists/dictionaries
No regular expressions
No advanced libraries
1. Problem Statement
Take the following inputs:
1. Student ID
2. Email ID
3. Password
4. Referral Code
Then validate all fields.
If all conditions are satisfied, print:
APPROVED
Otherwise print:
REJECTED
2. Validation Rules
Student ID Rules
Format must be:
CSE-XXX
Where:
 Must start with "CSE"
 4th character must be -
 Last 3 characters must be digits
Valid Example: CSE-245
Invalid: cse-245, CSE245, CSE-2A5
Email ID Rules

 Must contain @ and .
 @ must not be first or last character
 Email must end with .edu
Valid: student@univ.edu
Invalid: @univ.edu, student@gmail.com
Password Rules
 Length ≥ 8
 First character must be uppercase letter
 Must contain at least one digit
Valid: Aman1234
Invalid: aman1234, Amanabcd
Referral Code Rules
Format:
REF##@
Where:
 Must start with &quot;REF&quot;
 Next 2 characters must be digits
 Last character must be @
Valid: REF45@
Invalid: REF4A@, RE45@
3. Expected Output
If ALL valid:
APPROVED
Else:
REJECTED

Instructor Test Cases
a. Test Case 1
ID: CSE-245
Email: student@univ.edu
Password: Aman1234
Referral: REF45@
Output:
APPROVED
b. Test Case 2
ID: CSE245
Email: student@univ.edu
Password: aman1234
Referral: REF4A@
Output:
REJECTED
c. Test Case 3
ID: CSE-12A

Email: @univ.edu
Password: Amanabcd
Referral: REF99@
Output:
REJECTED'''
student_id = input("Enter Student ID: ")
email = input("Enter Email ID: ")
password=input("Enter Password: ")
referral_code=input("Enter Referral Code: ")
valid =True
if not (len(student_id) == 7 and student_id[0:3] == "CSE" and student_id[3] == "-" and student_id[4:7].isdigit()):
    valid = False
if not ("@" in email and "." in email and email[0] != "@" and email[-1] != "@" and email.endswith(".edu") and email.count('@') == 1 and email.count('.') == 1 and email.count('#') == 0 and email.count('$') == 0 and email.count('%') == 0 and email.count('^') == 0 and email.count('&') == 0 and email.count('*') == 0 and "(" not in email and ")" not in email and "_" not in email and "+" not in email and "=" not in email and "!" not in email and "~" not in email and "`" not in email and "/" not in email and "\\" not in email and "," not in email and ";" not in email and ":" not in email and "'" not in email and '"' not in email and "<" not in email and ">" not in email):
    valid = False
if not (len(password) >= 8 and password[0].isupper() and (password.count("0")>0 or password.count("1")>0 or password.count("2")>0 or password.count("3")>0 or password.count("4")>0 or password.count("5")>0 or password.count("6")>0 or password.count("7")>0 or password.count("8")>0 or password.count("9")>0)):
    valid = False
if not (len(referral_code) == 6 and referral_code[0:3] == "REF" and referral_code[3:5].isdigit() and referral_code[5] == "@"):
    valid = False
if valid:
    print("APPROVED")
else:
    print("REJECTED")