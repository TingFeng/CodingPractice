
"""
Hanoi Tower: https://en.wikipedia.org/wiki/Tower_of_Hanoi

move number of n disks of HanoiTower from source to target via the helper

rule: disk can only be moved to the tower if 1) the tower is empty, or 2) the disk is smaller than the top of the tower

Hint:
recursion - reduce the problem of moving n-1 disk to the helper, and then the big one to the target from the source, and then n-1 disk from helper to source
stack (top in and top out, implemented with python list.pop)


"""

def move(n,source,target,helper,tracker):
    if n>0:
        move(n-1,source,helper,target)
        target.append(source.pop())
        move(n-1,helper,target,source)

source=[4,3,2,1]
target=[]
helper=[]

hanoi(len(source),source,helper,target)

print source,helper, target
