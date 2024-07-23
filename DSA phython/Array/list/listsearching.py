mylist=[10,20,30,40,50,60,70,80]
target=30
if target in mylist:
    print(f"{target}the element is in list")
else:
    print(f"{target}the element is not in list")

 #linear search   
def linearsearch(p_list,p_target):
    for i in (p_list):
        if i==target:
         return i
    return-1 

