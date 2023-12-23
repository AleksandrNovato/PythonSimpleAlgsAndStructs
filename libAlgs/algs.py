"""simple alg library for styding porpouse"""


def insert_sort(A:list)->None:
    """insertion in-place sort of array by increasing O(N*2)"""
    assert(type(A)==list)
    for inserted_item_index in range(1,len(A)):#item[0] is already sorted in itself
        j=inserted_item_index
        while j>0 and A[j]<A[j-1]:
            (A[j],A[j-1])=(A[j-1],A[j])
            j-=1            
def bubble_sort(A:list)->None:
    """bubble in-place sort of array by increasing O(N*2)"""
    assert(type(A)==list)
    for i in range(1,len(A)):
        for j in range(len(A)-i):
            if A[j]>A[j+1]:
                (A[j],A[j+1])=(A[j+1],A[j])
def choice_sort(A:list)->None:
    """choice in-place sort of array by increasing O(N*2)"""
    assert(type(A)==list)
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            if A[j]<A[i]:
                (A[j],A[i])=(A[i],A[j])
def count_sort(A:list)->list:
    """ count sort O(N)(!in this realization O(N+M*2)actually but assuming M is small its O(N)!)
     operations O(M) by memory M-diffrent elements in array
    implementation is overcomplicated because I played with situation where we dont know range of M
    """
    F=dict()#if we know M that we can use array and implement it much easyer
    output=[]*len(A)
    for item in A:
        if item in F:
            F[item]+=1
        else:
            F[item]=1
    keys=list(F.keys())
    keys.sort()#this is kinda ruins O(N) if M is large because keys.sort depends on M
    #and we doont need it if we know M
    for key in keys:#also depends on M
        for repeat in range(F[key]):#cost nothing if M-small number
            output.append(key)#but if M is large better never use this sort xD
    return output
    

