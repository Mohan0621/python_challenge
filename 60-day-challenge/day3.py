'''Scenario
A university wants to analyze student performance based on internal assessment marks.
Marks are stored in a list, and the system must process them one by one to determine
performance categories. Your task is to build a Performance Analyzer using:
for loop
list
string
conditional statements
No advanced data structures
No built-in shortcuts like max(), min(), sum()
Problem Statement
Write a Python program that:
1. Takes N student marks as input and stores them in a list
2. Uses a for loop to process each mark
3. Classifies each student based on the following rules
Classification Rules
Marks Range Category
90 – 100 Excellent
75 – 89 Very Good
60 – 74 Good
40 – 59 Average
0 – 39 Fail
&lt; 0 or &gt; 100 Invalid

Additional Requirements

Using the same loop, your program must also:'''
n = int(input("Enter number of students: "))

marks = [0] * n
reg_nos = [0] * n

for i in range(n):
    reg_nos[i] = int(input(f"Enter registration number last 3 digits of student {i+1}: "))
    marks[i] = int(input(f"Enter marks of student {i+1}: "))

print(f"\nMarks of each student in List: {marks}\n")

qualify_count = 0
fail_count = 0
print("Marks:")

for i in range(n):
    mark = marks[i]
    reg_no = reg_nos[i]

    if mark < 0 or mark > 100:
        print(mark, "→ Invalid")
    elif mark >= 90:
        qualify_count += 1
        print(mark, "→ Excellent")
    elif mark >= 75:
        qualify_count += 1
        print(mark, "→ Very Good")
    elif mark >= 60:
        qualify_count += 1
        print(mark, "→ Good")
    elif 35 <= mark < 40 and reg_no % 2 == 1:
        qualify_count += 1
        print(mark + 5, "→ Average (With extra grace marks)")
    elif mark >= 40:
        qualify_count += 1
        print(mark, "→ Average")
    else:
        qualify_count += 1
        fail_count += 1
        print(mark, "→ Fail")

print("\nFinal Summary:")
print("Total Valid Students:", qualify_count)
print("Total Failed Students:", fail_count)

