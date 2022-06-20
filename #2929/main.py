

def machine_code(input_ls):
    num_nop = 0 
    prev_idx = 0 
    next_idx = 0
    for i in range(len(input_ls)-1):
        # find next upper letter 
        if input_ls[i+1].isupper():
            next_upper = input_ls[i+1]
            next_idx = i+1
            print(prev_idx, next_idx)
            if next_idx -prev_idx <=4 :
                num_nop += (4-(next_idx-prev_idx))
            else : 
                num_nop+=4-((next_idx-prev_idx) % 4)
            prev_idx = next_idx
            

    return num_nop


def main():
    code_input = input()
    print(machine_code(code_input))

if __name__ == "__main__":
    main()
