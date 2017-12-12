"""
Counting Sort: https://en.wikipedia.org/wiki/Counting_sort

time and space complexity O(n+r) where r=max(Num)

Hint: have a list of the histogram of Numbers first, and then directly insert number to place

"""

def CountingSort(Num):
    length=max(Num)+1
    Count=[0]*length
    for x in Num:
        Count[x]=Count[x]+1
    j=0
    for i in xrange(0,length):
        Num[j:j+Count[i]]=[i]*Count[i]
        j=j+Count[i]
    return Num
