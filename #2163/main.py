
def chocolate(n,m):  
    return (n-1) +n*(m-1)

def main():
    n,m = list(map(int,input().split()))
    result = chocolate(n,m)
    print(result)


if __name__ =='__main__':
    main()
    