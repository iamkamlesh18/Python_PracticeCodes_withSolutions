# Task

# The provided code stub reads and integer,n, from STDIN. 
# For all non-negative integers i<n , print i sqaure(i*i).


if __name__ == '__main__':
    n = int(input())
    a = range(0,n,1)
    for i in a:
        print(i*i , sep="", end="\n")
