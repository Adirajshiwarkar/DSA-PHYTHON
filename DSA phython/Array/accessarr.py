import array

arr1=array.array('i',[2,3,4,5,6,7])

def AcessElements(array,index):
    if index>len(array):
        print("this value dose not have index")
    else:
        print(array[index])

AcessElements(arr1,2)        
  
