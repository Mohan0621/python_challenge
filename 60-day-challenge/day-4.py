n=int(input("Enter the size of the list:"));
data_list=[0]*n;
nums=[];
strings=[];
print("Enter the data:")
for i in range(n):
    data_list[i]=input(str(i+1)+ ". ");
for data in data_list:
    if data.isdigit():
        nums+=[int(data)]
    elif data!="":
        strings+=[data]
print("Your nums list:",nums,"\n");
print("Your strings list:",strings,"\n");
j=len(nums)-1
for i in range(len(nums)):
    if(i>=j): 
        break
    else:
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
        j=j-1

print("Selecting OPTION_A:REGISTER NUMBER LOGIC")
print("As my REGISTRATION NUMBER(AP24110011742) last digit is EVEN!!!\n")
print("I am gonna do REVERSE the NUMS LIST")
print("REVERSED LIST:",nums,"\n")

print("Total Numbers:",len(nums))
print("Total Strings:",len(strings))
