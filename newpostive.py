list1=[]
list2=[]

#Direct output
x=int(input("Enter the number of elements for list1: "))
print("Enter the elements of list1")
for i in range (0,x) :
    a=int(input())
    list1.append(a)
print ("The positive no.s for list1 are:")
for element in list1:
    if(element>0):
        print(element, end=" ")
        
#output in the form of list
y=int(input("\nEnter the number of elements for list2: "))
count=0
print("Enter the elements of list2")
for j in range (0,y) :
    b=int(input())
    list2.append(b)
print(list2)
print ("The positive no.s for list2 are:")
for ele in list2:
    if(0>ele):
        list2.pop(count)
    count=+1
print(list2)       
