#find the number in array:
import numpy as np
myarray=np.array([1,2,3,4,5,6,7,8,9,10,11])
def findNum (array,nums):
    for i in range (len(array)):
        if array[i]==nums:
            print(i)
        


findNum(myarray,10)
        
        
        

    