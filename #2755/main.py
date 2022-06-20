
def my_round(n):
    n*=100 
    if n-int(n) >= 0.5 :
        return (int(n)+1)/100
    else : 
        return int(n)/100

def main():
    grade_dict = {
        'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
         'C+': 2.3, 'C0': 2.0, 'C-': 1.7,'D+': 1.3, 'D0': 1.0, 'D-': 0.7,'F': 0.0
    }


    num_taken = int(input()) 
    total_credit = 0
    total_result = 0  
    for i in range(num_taken):
        course_id,credit,result = input().split()
        total_credit += int(credit)
        total_result +=grade_dict[result]*float(credit)

    answer = total_result/total_credit
    print('{0:.2f}'.format(my_round(answer)))

    


if __name__ =="__main__":
    main()