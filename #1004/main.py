

def num_escape(destination_info,planet_info):
    cnt = 0 
    x_1, y_1, x_2, y_2 = destination_info
    for i in planet_info : 
        c_x,c_y, r = i  
        distance_squre= (x_1-c_x)**2 + (y_1-c_y)**2 
        distance_squre_2 = (x_2-c_x)**2 + (y_2-c_y)**2 

        # have to visit (inner side)
        if distance_squre < r**2 and distance_squre_2 > r**2:
            cnt +=1 

        elif distance_squre > r**2 and distance_squre_2 < r**2 : 
            cnt +=1 

        else :
            cnt +=0 

    print(cnt)


def main():
    test_case = int(input())
    for i in range(test_case) :
        destination_info = list(map(int,input().split()))
        num_planet = int(input())
        planet_info = []
        for i in range(num_planet):
            c_x,c_y, r = list(map(int, input().split()))
            planet_info.append([c_x,c_y,r])

        num_escape(destination_info, planet_info)

    



if __name__ == '__main__':
    main()
    pass 
