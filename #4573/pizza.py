import math 


"""
INPUT :
The input contains a series of one or more menus. Each menu starts with the number of options N, 1 ≤ N ≤ 10, followed by N lines,
each containing two integers respectively designating a pizza's diameter D (in inches) 
and price P (in dollars), with 1 ≤ D ≤ 36 and 1 ≤ P ≤ 100. 
The end of the input will be designated with a line containing the number 0

OUTPUT :
For each menu, print a line identifying the menu number and the diameter D of the pizza with the best value, using the format shown below.
"""

def pizza(diameter :int, price :int)-> int :
    radius = diameter/2 
    area = radius**2*math.pi 
    cost_per_inch = price/area 

    return cost_per_inch

def argmin(x):
    return min(range(len(x)), key =lambda i:x[i])

def main():
    cost_all = [] 
    diameter_lst_all=[]
    number_of_option =1 
    while number_of_option :
        number_of_option = int(input())
        cost_lst =[]
        diameter_lst=[]
        for i in range(number_of_option):
            diameter, price = input().split()
            cost = pizza(int(diameter), int(price))
            cost_lst.append(cost)
            diameter_lst.append(int(diameter))
        cost_all.append(cost_lst)
        diameter_lst_all.append(diameter_lst)
    
    for i in range(len(cost_all)-1):
        arg_min_idx = argmin(cost_all[i])
        print(f"Menu {i+1}: {diameter_lst_all[i][arg_min_idx]}")
        










    pass 

if __name__ == "__main__" :
    main()