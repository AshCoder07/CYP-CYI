#User function Template for python3

class Solution:
    def isPossible(self,a, b, n, k):
    # Your code goes here
        a.sort(reverse=True)
        b.sort()
        for i in range(n):
            if a[i]+b[i]<k:
                return False
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
    	sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
    	a = [int(x) for x in input().strip().split()]
    	b = [int(x) for x in input().strip().split()]
    	ob=Solution()
    	if ob.isPossible(a, b, n, k):
    		print(1)
    	else:
    		print(0)
    	
    	T -= 1

if __name__ == "__main__":
    main()







# } Driver Code Ends