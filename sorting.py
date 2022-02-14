n=int(input("Enter the no of elements in the list:"))
lst1=list()
evenlst=list()
oddlst=list()
i=0
while i<n:
    num=int(input("Enter the element:"))
    lst1.append(num)
    if num%2==0:
        evenlst.append(num)
    else:
        oddlst.append(num)
    i=i+1
oddlst.sort()
evenlst.sort(reverse=True)
print(lst1)
print(oddlst)
print(evenlst)
k=0
j=1
for i in range(len(evenlst)):
    oddlst.insert(j,evenlst[i])
    j=j+2
print(oddlst)
