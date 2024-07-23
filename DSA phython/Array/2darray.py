import numpy as np

twodarr= np.array([[10,15,12,3],[14,15,6,9],[1,20,34,56],[30,45,2,0]])
print(twodarr)
#newtwodarr=np.insert(twodarr,0,[2,5,9,0],axis=0)
#print(newtwodarr)
apptwodarr=np.append(twodarr,[[2,5,9,0]],axis=0)
print(apptwodarr)