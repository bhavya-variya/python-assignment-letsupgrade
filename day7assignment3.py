list1=[(1,2,3),[1,2],['a','hit','less']]
list2=[]
list2=[i for each in list1 for i in each]
print ("The required output:",list2)