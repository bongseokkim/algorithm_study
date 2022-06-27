
import re 

def find_row_num(room_info):
    cnt = 0 

    for i in room_info :
        #print(i)
        #split_x=i.split('X')
        split_x = re.split('[X]+',i)
        for j in split_x :
            if len(j) >=2 :
                cnt +=1 
            else:
                cnt+=0
    return cnt 


def transpose(room_info):
    result=["".join([str(j) for j in range(len(room_info))]) for i in range(len(room_info))] 
    for i in range(len(room_info)) :
        for j in range(len(room_info)):
            a =list(result[j])
            a[i]=room_info[i][j]
            result[j]="".join(a)
    return result  

def main():

    def find(li):
        cnt = 0
        for i in range(n):
            tmp = 0
            for j in range(n):
                if li[i][j] == 'X':
                    if tmp >= 2:
                        cnt += 1
                    tmp = 0
                else:
                    tmp += 1
            if tmp >=2: #마지막 원소까지 지나왔다면
                cnt += 1
        return cnt

    n = int(input())
    room_info = []

    for i in range(n):
        row = input()
        room_info.append(row)

    result = transpose(room_info)
    cnt_row = find_row_num(room_info)
    cnt_col = find_row_num(result)
    print('{0} {1}'.format(cnt_row, cnt_col))



if __name__ =='__main__':
    main()