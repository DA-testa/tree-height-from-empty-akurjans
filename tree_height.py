import sys
import threading


def compute_height(n, parents):
    a= [0]*n
    root= parents.index(-1)

    def dfs(i) :
        if a[i] != 0:
            
            return a[i]
        
        if parents[i] == -1:
            
            a[i] = 1
        else:
            a[i] = 1 + dfs(parents[i])

        return a[i]
                
    for i in range(n):
        dfs(i)

    return max(a)

def main():
    
    text = input()
    if "I" in text:
        n = int(input())
        parents = list(map(int, input().split()))
        
    elif "F" in text:

        path = "./test/"
        file_name = input("Enter the file name: ")
        file_path = os.path.join(path, file_name)

        if "a" not in filename:
            
            try:
                with open(file_path) as f:
                    n = int(f.readline().strip())
                    parents = list(map(int, f.readline().strip().split()))
            except Exception as e:
                print("Error:", str(e))
                return

    else:
        print("Enter 'I' or 'F':")
        return

    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
