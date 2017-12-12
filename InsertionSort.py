"""
Insersion sort: https://en.wikipedia.org/wiki/Insertion_sort

Note: scan number from beginning to end, and everytime place a new number to the right place
Same as bubble sort, time complexity O(n^2), and space complexity O(1)

"""

def InsertionSort(Num):
    i=1
    j=1
    while i<len(Num) and i>=0:
        if i==0:
            i=j
        if Num[i]<Num[i-1]:
            temp=Num[i]
            Num[i]=Num[i-1]
            Num[i-1]=temp
            j=max([i+1,j])
            i=i-1
        else:
            i=max([j,i+1])
    return Num
