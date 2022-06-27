import math 

def combination(n, m):
    if n < m: return 0
    return math.factorial(n) / (math.factorial(n-m) * math.factorial(m))


def main():
    n,m,k = list(map(int, input().split()))
    result = 0 

    while m-k >=0 :
        total = combination(n,m)
        sucess = combination(m,k)
        fail = combination(n-m, m-k)
        prob = sucess*fail/total
        result+=prob 
        k+=1 

    print(result)

    


if __name__ =='__main__':
    main()