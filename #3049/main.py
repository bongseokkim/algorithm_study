from itertools import combinations
"""
input:
첫째 줄에 N이 주어진다. (3 ≤ N ≤ 100)
output :
첫째 줄에 교차점의 개수를 출력한다.
"""
def combination(arr,n):
    result = [] 
    if n == 0 : 
        return [[]]
    
    for i in range(len(arr)):
        ele = arr[i]
        for rest in combination(arr[i+1:], n-1):
            result.append([ele]+rest)
    return result



def main():
    n = int(input())
    lst = list(range(n))
    print(len(combination(lst,4)))

if __name__ == "__main__" :
    main()