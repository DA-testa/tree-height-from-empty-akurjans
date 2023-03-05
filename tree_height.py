import sys
import threading
import numpy as np

def compute_height(n, parents):
    # Write this function
    x=np.array(parents)
    
    max_height = 0
    augstums=0
    Nods={}
    # Your code here
    k=0
  
    for i in range(n):
        k=i
        while True:
            if x[i]==-1:
                
                k=i
                
                break
            else:
                max_height+=1
                
                i=x[i]
                
                if i in Nods.keys():
                    
                    max_height=max_height+Nods.get(i)
                    Nods[k]=max_height
                    k=i
                    break
                else:
                    Nods[k]=max_height

                 
                
                
        if augstums<max_height:
            augstums=max_height
        max_height=0

        
    

    return augstums+1


def main():
    
    text= input("I or F:")
    if "I" in text or "i" in text:
        n=int(input())
        parents = list(map(int, input().split()))
        max_aug = compute_height(n, parents)
        print(max_aug)
        
    if "F" in text:
        filename = input()
        file='./test/'+ filename
        if 'a' not in filename:
            with open (file) as file:
                n=int (file.readline())
                parents = list(map(int, file.readline().strip().split()))
                max_aug = compute_height(n, parents)
                print(max_aug)
        else: 
            print ("invalid filename")


        
   
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
