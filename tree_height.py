import sys
import threading
import numpy as np

def compute_height(n, parents):
    # Write this function
    x=np.array(parents)
    
    max_height = 0
    max_height_1=0
    node={}
    # Your code here
    k=0
  
    for i in range(n):
        k=i
        while True:
            if x[i]==-1:
                #max_height=0
                k=i
                break
            else:
                max_height+=1
                
                i=x[i]
                
                if i in node.keys():
                    
                    max_height=max_height+node.get(i)
                    node[k]=max_height
                    k=i
                    break
                else:
                    node[k]=max_height

                 
                
                
        if max_height_1<max_height:
            max_height_1=max_height
        max_height=0

        
    

    return max_height_1+1


def main():
    
    text=input()
    if "I"in text:
        n=input()
        parents=input().split(" ")
        parents=map(int,parents)
        parents=list(parents)
        print(compute_height(int(n),parents))
    elif "F"in text:
        
        faila_nosaukums=input()
        if "a" in file_name:
            print("error")
            
        else:
            
            fails=open("./test/"+file_name)
            n=fails.readline()
            n=int(n)
            parents=fails.readline()
            parents=parents.split(" ")
            parents=map(int,parents)
            parents=list(parents)
            print(compute_height(n,parents))
            fails.close()


        pass
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision

    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
