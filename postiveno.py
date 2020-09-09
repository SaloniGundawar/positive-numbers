x=int(input("Enter the number of elements: "))
inputlist=[]
print("Enter the elements")
for i in range (0,x) :
    i=int(input())
    inputlist.append(i)
print ("The positive no.s are:")
for element in inputlist:
    if(element>0):
        print(element, end=" ")
