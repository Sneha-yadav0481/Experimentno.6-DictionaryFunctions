Employee={
    "Ename":"Rahul",
    "EID":100,
    "Department":"Head manager",
    "Salary":50000
    }
print("The dictionary list of employee is:",Employee)
print("\nName of employee is:",Employee["Ename"])
print("Employee ID:",Employee["EID"])
print("Department:",Employee["Department"])
print("Salary:",Employee["Salary"])

print("\nAdding,updating,Deleting Dictionary elements\n")
Employee["Age"]=25
print("After adding:",Employee)
Employee["Salary"]=60000
print("After updating:",Employee)
del Employee["Salary"]
print ("After deleting:",Employee)

print("\nDictionary Method\n")
print("Keys:",Employee.keys())
print("Values:",Employee.values())
print("Items:",Employee.items())
print(" Getting Name:",Employee.get("Ename"))
print("Getting Salary:",Employee.get("Salary","Not Available"))
Employee.update({"Salary":50000,"Branch":"BTM"})
print(" After Update:",Employee)

print("\n Count frequency of Each Character in a string\n")
text=input("Enter a string:")
frequency={}
for ch in text:
    if ch in frequency:
        frequency[ch]=frequency[ch]+1
    else:
         frequency[ch]=1
print("Character Frequency:")
for ch,count in frequency.items():
    print(ch,":",count)
