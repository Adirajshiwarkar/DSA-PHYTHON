#1.create aarray and traverse
import array
array1=array.array('i',[1,2,3,4,5,6])
for i in array1:
    print(i)

#2.Acesss individual element
print("Step2")
print(array1[0])
#3.appending any value to the array
print("step3") 
array1.append(60)
print (array1)
#4. insert an element in the array
print("step4")
array1.insert(0,10) 
print(array1)
#5.extend phython array using method
print("step5")
array2=array.array('i',[11,12,13,14,15,16,17])
array1.extend(array2)
print(array1)
#6.Add item from list into array through methods
print("step6")
temp_list=[20,21,22]
array1.fromlist(temp_list)
print(array1)
#7.Remove an element from the the array
print("step7")
array1.remove(6)
print(array1)
#8.remove last element from array through method
print("step8")
array1.pop()
print(array1)
#9.Fetch any element from a array through methods
print("step9") 
print(array1.index(2))
#10.reverse the phython array 
print("step10")
array1.reverse()
print(array1)
#11.get array buffer information using methods
print("step11")
print(array1.buffer_info())
#12.check number of occurunce of element using methods
print("step12")
print(array1.count(3)) 
#13.convert array to string
print("step13")
print(array1.tobytes())
#14.convert array to list using methods
print("step14")
#print(array1.tolist())
#15.append a string to char array using methods
#16.slicing element from an array
print("step16")
print(array1[1:4])
