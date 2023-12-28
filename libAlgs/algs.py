"""simple alg library for styding porpouse"""

import random


def insert_sort(A:list[int])->None:
    """insertion in-place sort of array by increasing O(N**2) can sort array partitionally.
    high bound is  included"""
    assert(type(A)==list)
    
    for inserted_item_index in range(1,len(A)):
        j=inserted_item_index
        while j>0 and A[j]<A[j-1]:
            (A[j],A[j-1])=(A[j-1],A[j])
            j-=1            
def bubble_sort(A:list[int])->None:
    """bubble in-place sort of array by increasing O(N**2)"""
    assert(type(A)==list)
    for i in range(1,len(A)):
        for j in range(len(A)-i):
            if A[j]>A[j+1]:
                (A[j],A[j+1])=(A[j+1],A[j])
def choice_sort(A:list[int])->None:
    """choice in-place sort of array by increasing O(N**2)"""
    assert(type(A)==list)
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            if A[j]<A[i]:
                (A[j],A[i])=(A[i],A[j])
def count_sort(A:list[int])->list:
    """ count sort O(N)(!in this realization O(N+M*2)actually but assuming M is small its O(N)!)
     operations O(M) by memory M-diffrent elements in array
    implementation is overcomplicated because I played with situation where we dont know range of M
    """
    assert(type(A)==list)
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
def sort_TH(A:list[int])->None:
    """Quick sort in plase O(N**2)->O(NlogN) in average 
    Splits array by pivots recursivly until parts will be smaller than 10,on small parts uses insert sort"""    

    
    def _sort_TH(A,left,right):
        if right-left<10:
            A[left:right+1]=sorted(A[left:right+1])#fix me to not consume add memory
        else:
            pivot=A[left]
            l=left+1
            r=right
            while True:
                while l<=r and A[l]<=pivot:
                    l+=1                    
                while r>=l and A[r]>=pivot:
                    r-=1                
                if r>l:
                    A[l],A[r]=A[r],A[l]
                else:
                    break              
            A[left],A[r]=A[r],A[left]
            _sort_TH(A,left,r-1)
            _sort_TH(A,r+1,right)
            
    assert(type(A)==list)
    if len(A)<=1:
        return
    _sort_TH(A,0,len(A)-1)
def merge_sort(A:list[int])->None:
    """memory greedy realization of merge sort O(NlogN) operations and O(M) by memory"""
    def merge(A:list,B:list)->list:
        C=[0]*(len(A)+len(B))
        a=0
        b=0
        c=0
        while a<len(A) and b<len(B):
            if A[a]<=B[b]:
                C[c]=A[a]
                a+=1
            else:
                C[c]=B[b]
                b+=1
            c+=1
        while a<len(A):
            C[c]=A[a]
            a+=1
            c+=1
        while b<len(B):
            C[c]=B[b]
            b+=1
            c+=1 
        return C    
    def _merge_sort(A):
        if len(A)<=10:
            A.sort()
        else:
            middle=len(A)//2
            L=A[0:middle]
            R=A[middle:len(A)]
            _merge_sort(L)
            _merge_sort(R)
            sorted=merge(L,R)
            A[::]=sorted[::]
              
    assert(type(A)==list)
    if len(A)==1:
        return A
    _merge_sort(A)
                    

    
    
    


    



        

    
    




    

