import queue



class myqeue(object):
    def __init__(self, num) :
        self.data = list(range(1,num+1))

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
    cnt = 0 
    n = queue.len_qeue()
    middle = int(n/2)

    if idx <= middle : 
        for i in range(idx):
            queue.move_left()
            cnt+=1

    else : 
        for j in range(n-idx):
            queue.move_right()
            cnt+=1 
    queue.pop()
    return queue, cnt 

def main():
    count = 0 
    length, num = input().split()
    required_idx_lst = input().split()
    my_que = myqeue(int(length))
    for i in (required_idx_lst):
        idx = my_que.data.index(int(i))
        queue, cnt = find_lowest_num(my_que, idx)
        count+=cnt 
        my_que = queue
    print(count)

if __name__ =="__main__":
    main()