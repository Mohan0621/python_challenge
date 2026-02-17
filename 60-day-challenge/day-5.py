'''Scenario
A logistics company receives a list of package weights scheduled for
transport. Before loading, the system must analyze weights to ensure
safety and balance.
Reports may include:
 Invalid weights
 Extremely light packages
 Overloaded packages
 Normal loads
Your task is to prepare a balanced loading report.
Problem Statement
Write a Python program that:
1. Accepts a list of integer weights
2. Uses a for loop to process each weight
3. Categorizes weights
4. Applies personalized adjustment using PLI
5. Displays final loading plan
Base Classification Rules
For each weight:
 &lt; 0 → Invalid Entry
 0–5 → Very Light
 6–25 → Normal Load
 26–60 → Heavy Load
 60 → Overload

Create lists:
 very_light
 normal_load
 heavy_load
 overload
 invalid_entries
Mandatory Personalization Rule (PLI)
Let:
L = length of your full name (excluding spaces)
PLI = L % 3
Apply:
PLI = 0 → Rule A
Move all Overload items to Invalid Entries
` PLI = 1 → Rule B
Remove all Very Light items from the final plan
PLI = 2 → Rule C
Keep only Normal and Heavy loads
Additional Requirements
Your program must also:
 Count total valid weights
 Count affected items due to PLI
 Print L and PLI
 Display final categorized lists
Example Input'''

n=int(input("enter no of weights"))
weights=[0]*n
for i in range(n):
    weights[0]=int(input("enter the weight"))
invalid=[]
very_light=[]
Normal_load=[]
heavy_load=[]
overload=[]
for i in weights:
    if i<0:
        invalid+=[i]
    elif i<6:
        very_light+=[i]
    elif i<26:
        Normal_load+=[i]
    elif i<61:
        heavy_load+=[i]
    else:
        overload+=[i]


total_valid = len(very_light) + len(Normal_load) + len(heavy_load) + len(overload)
affected=len(very_light)

print("\nInvalid Entries:", invalid)
print("Normal Load:", Normal_load)
print("Heavy Load:", heavy_load)
print("Overload:", overload)

print("\nTotal valid weights:", total_valid)
print("Items affected by PLI rule:", affected)