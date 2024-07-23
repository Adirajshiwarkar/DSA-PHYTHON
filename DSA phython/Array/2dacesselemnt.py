import numpy as np

twodarr= np.array([[10,15,12,3],[14,15,6,9],[1,20,34,56],[30,45,2,0]])
print(twodarr)

def acessElement(array,rowIndex,coloumIndex):
    if rowIndex>=len(array) or coloumIndex>=len(array):
     print("incoreect index")
    else:
     print(array[rowIndex],[coloumIndex])


acessElement(twodarr,1,2)       