list1=[1,3,5,4,2]
list2=[9,8,10,6,7]
list3=list1+list2
list4=[]
for num in range(min(list3),max(list3)+1):
    if num in list3:
        list4.append(num)
print(list4)