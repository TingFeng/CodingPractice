"""
Merge Sort: https://en.wikipedia.org/wiki/Merge_sort

Memory complexity: O(nlogn)
Space complexity: O(n)

Hint: everytime merge two segment and order them

"""


def merge(L1,L2):
    L=L1+L2
    l1=len(L1)
    l2=len(L2)
    i=0
    j=0
    s=0
    while i<l1 and j<l2:
        if L1[i]<=L2[j]:
            L[s]=L1[i]
            i=i+1
        else:
            L[s]=L2[j]
            j=j+1
        s=s+1 
    if i<l1:
        L[s:s+len(L1)-i]=L1[i:]
    if j<l2:
        L[s:s+len(L2)-j]=L2[j:]
    return L   

def MergeSort(Num):
    
    GroupNo=1
    length=len(Num)
    while GroupNo<length:
        for i in xrange(0,length,2*GroupNo):
            Num[i:min([i+2*GroupNo,length])]=merge(Num[i:i+GroupNo],Num[i+GroupNo:min([i+2*GroupNo,length])])
        GroupNo=GroupNo*2
        
    return Num
