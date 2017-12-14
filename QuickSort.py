"""
QuickSort: https://en.wikipedia.org/wiki/Quicksort

Solution:
choose the middle item to divide the list, and move all the numbers smaller than the middle item to the left, and numbers bigger than the middle to the right
do this recursively

note the situation if the middle item got swapped

"""


def QuickSort(Num,start,end):
    
    i=start
    j=end
    No=(end-start)/2+start
    
    if i<j and i!=No and j!=No: 
    
        while i<No and j>No:

            while i<No and Num[i]<Num[No]:
                i=i+1
            while j>No and Num[j]>Num[No]:
                j=j-1
            if i<j:
                temp=Num[i]
                Num[i]=Num[j]
                Num[j]=temp         
            
        if i==No and j==No: # recursively quicksort the left segment and the right segment
            order(Num,start,No)
            order(Num,No,end)
        elif i==No and j!=No:           # the original node has swapped 
            order(Num,start,j) 
            order(Num,j,end) 
        elif j==No and i!=No:          # the original node has swapped        
            order(Num,start,i) 
            order(Num,i,end) 
