
"""

HeapSort: https://en.wikipedia.org/wiki/Heapsort

Objective: Sort a list of numbers, from small to big

Method: 
1. build a Heap using fuction BuildHeap - Heap is a binary tree that children nodes are no bigger than parent node,
   the nodes in the heap is indexed from top to bottom, and from left to right.
   a. When building the heap, start from top to bottom, add the new number to a new node;
   b. if the number in the new node is bigger than the parent, swap the values in the parent and child node;
   c. then recursively check the child (now the previous parent) and the new parent till the top of the tree.
   d. repeat the above a,b,c process until all the values are added to the tree
2. swap the top node with bottom right node, now the value for the largest index is the maximum value of the list;
   remove the value from the tree
3. Reorder the Heap using top-down medthod (SiftUp function)
   a. compare the value on the parent node with the children nodes (the top node is parent node in the very beginning)
   b. if one of the children node is bigger than the parent node, swap the parent node with the children nodes that has the bigger value
   c. now the children node with swapped value become the parent node
   d. repeat the above a,b,c process until either the parent node is at the bottom level of the tree, or no value needs to be swapped
4. After SiftUp, the tree becomes a Heap again, now repeat the above 2,3 process untial all the values are removed from the tree

Note added on 2017/12/12: 
The following code sorted the list, and also kept the original index of the list. 
In the situation that only sorted list is requested, one can directed swap/order the numbers in the list, and have true space complexity O(1)
The temporal complexity is O(nlogn)

"""

def HeapSort(nums):

    # type nums: List[int]

    Index=range(0,len(nums))

    Heap=BuildHeap(nums) # build a heap from the list of numbers

    count=len(Heap)-1
    while count>0:
        temp=Heap[0]
        Heap[0]=Heap[count]
        Heap[count]=temp
        count=count-1
        Heap=SiftUp(Heap,count) # reorder the tree such that it is a heap again
    Return Heap                        

def BuildHeap(nums):
    Heap=[[0,0] for i in xrange(0,len(nums))]
    for no,value in enumerate(nums): # add value to the tree one by one
        Heap[no]=[no,value]
        i=no
        while i>0 and Heap[(i-1)/2][1]<Heap[i][1]: # shift the value up the tree until the parent value is bigger than the child
            temp=Heap[i]
            Heap[i]=Heap[(i-1)/2]
            Heap[(i-1)/2]=temp
            i=(i-1)/2                
    return Heap

def SiftUp(Heap,count):
    i=0
    while 2*i<count:
        if 2*i+1<count:      # when there are two children in the last branch
            if Heap[2*i+2][1]>Heap[2*i+1][1] and Heap[2*i+2][1]>Heap[i][1] : # swap with right child
                temp=Heap[i]
                Heap[i]=Heap[2*i+2]
                Heap[2*i+2]=temp
                i=2*i+2
            elif Heap[2*i+1][1]>Heap[i][1] : #swap with left child
                temp=Heap[i]
                Heap[i]=Heap[2*i+1]
                Heap[2*i+1]=temp
                i=2*i+1
            else:             # stop sifting-up
                break
        else:             # when there is only one children in the last branch
            if Heap[2*i+1][1]>Heap[i][1] :
                temp=Heap[i]
                Heap[i]=Heap[2*i+1]
                Heap[2*i+1]=temp
                i=2*i+1
            else:
                break
    return Heap
