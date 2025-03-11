print("this program accepts lists and then adds them up")
numbers=input("Enter your numbers here:")

numbers_list=numbers.split()
list=[int(num) for num in numbers_list]

total=sum(list)
print("sum:",total)

