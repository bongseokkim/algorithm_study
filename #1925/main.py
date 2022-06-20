
from itertools import combinations
import math

def triangle(point_lst):
    a,b,c = point_lst 
    tan_line = [] 

    comb = list(combinations(point_lst,2))
    #print(comb)
    distance = [] 

    for i in comb :
        k,g = i 
        x_diff = abs(k[0]-g[0])
        y_diff = abs(k[1]-g[1])
        tan = y_diff/(x_diff+0.00001)
        tan_line.append(tan)
        distance.append(math.sqrt(x_diff**2+y_diff**2))
    k,j,l = tan_line 
    if round(k) ==round(j) and round(j)==round(l) : 
        print("X")
        return
    a,b,c = distance

    ang_1 = round(math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b))))
    ang_2 = round(math.degrees(math.acos((c**2+a**2-b**2)/(2*a*c))))
    ang_3 = round(math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c))))

    ang_list = [ang_1,ang_2,ang_3]    
    


    
    if a==b and b==c and c==a : 
        print("JungTriangle")
    elif a==b or a==c or b==c :
        # 가장 큰 각이 90°보다 크면 - ‘둔각이등변삼각형’ 출력할 때는 Dunkak2Triangle
        if max(ang_list) > 90 : 
            print("Dunkak2Triangle")
        # 가장 큰 각이 90°이면 - ‘직각이등변삼각형’ 출력할 때는 Jikkak2Triangle
        elif max(ang_list) == 90 :
            print("Jikkak2Triangle")
        
        #가장 큰 각이 90°보다 작으면 - ‘예각이등변삼각형’ 출력할 때는 Yeahkak2Triangle
        elif max(ang_list) <90 :
            print("Yeahkak2Triangle")

    elif  a!=b and a!=c and b!=c :
                    # 가장 큰 각이 90°보다 크면 - ‘둔각이등변삼각형’ 출력할 때는 Dunkak2Triangle
        if max(ang_list) > 90 : 
            print("DunkakTriangle")
        # 가장 큰 각이 90°이면 - ‘직각이등변삼각형’ 출력할 때는 Jikkak2Triangle
        elif max(ang_list) == 90 :
            print("JikkakTriangle")
        
        #가장 큰 각이 90°보다 작으면 - ‘예각이등변삼각형’ 출력할 때는 Yeahkak2Triangle
        elif max(ang_list) <90 :
            print("YeahkakTriangle")


def main():
    n= 3 
    point_lst = [] 
    for i in range(n):
        x,y = input().split()
        point_lst.append([int(x),int(y)])
  
    triangle(point_lst=point_lst)




if __name__ =="__main__":
    main()