

import queue
from xml.etree.ElementTree import Element


class myqeue(object):
    def __init__(self) :
        self.data = list(range(10))

    def pop(self):
        element = self.data[0]
        if len(self.data) > 0 :
            del self.data[0]
        return element

    def move_left(self):
        element = self.data[0]
        del self.data[0]
        self.data = self.data + [element]

    def move_right(self):
        element = self.data[-1]
        del self.data[-1]
        self.data = [element]+self.data 

    def print_out(self):
        print(self.data)
    
    def len_qeue(self):
        return len(self.data)

def find_lowest_num(queue,idx):
    ## 현재 queue의 idx라고 가정 
    n = queue.len_qeue()
    cnt = 0 
    middle_point = int(n/2)

    if n%2 == 0 :
        if idx < middle_point :
            for i in range(idx+1):
                queue.pop()
                cnt+=1 
    

    if idx < middle_point and n %2==0 : 
        for i in range(idx):
            queue.move_left()
            cnt+=1
    else :
        for i in range(n-idx):
            queue.move_right()
            cnt+=1
    
    queue.pop()
    return queue.data, cnt 

def main():
    queue = myqeue()
    print(f'que :{queue.data}')
    que, num = find_lowest_num(queue ,6)
    print(f'que :{que}, num:{num}')
    # length, num = input().split()
    # required_idx_lst = input().split()





if __name__ == "__main__" :
    main()