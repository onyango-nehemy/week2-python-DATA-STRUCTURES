#set 1 is below
numbers1=input("enter set one:")
x=numbers1.split()
set1={int(num) for num in x}
print(set1)
print("\n")

#now set two is below
numbers2=input("enter set two:")
y=numbers2.split()
set2={int(num) for num in y}
print(set2)

commonIntegers=set2.intersection(set1)
print("Common in both:",commonIntegers)