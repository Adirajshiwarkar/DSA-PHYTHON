import numpy as np

twodarr= np.array([[10,15,12,3],[14,15,6,9],[1,20,34,56],[30,45,2,0]])
print(twodarr)

def searchingTDElemnt(array,value):
    for i in range (len(array)):
        for j in range (len(array[0])):
            if len(array)==value:
                return'the value is located at index'+str(i)+""+str(j)
          
    return 'the element not found'

     
print(searchingTDElemnt(twodarr,0))
