list1=[12,14,87,57,564,36,12,44]

sum=0
for i in list1:
    sum=sum+i
print("sum:",sum)

length=len(list1)
print("Length:",length)
print("Average: ",sum/length)
print("Max: ",max(list1))
print("Min: ",min(list1))
print("Sorted: ",sorted(list1))
print("Reversed:",sorted(list1,reverse=True))
