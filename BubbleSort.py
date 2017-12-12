"""

BubbleSort: https://en.wikipedia.org/wiki/Bubble_sort

Space complexity: O(1) - swap numbers inside the list
temporal complexity: O(n^2)  - the best case is when the list already ordered O(n)

hint: continuously move the bigger number to the end of the list

"""

def BubbleSort(Num):
    i=0
    j=len(Num)-1 # this is to mark the end of the unordered list
    while i<=j:
        if i==j:
            j=j-1
            i=0 
        if Num[i]>Num[i+1]: 
            temp=Num[i+1]
            Num[i+1]=Num[i]
            Num[i]=temp
        i=i+1    
    return Num
