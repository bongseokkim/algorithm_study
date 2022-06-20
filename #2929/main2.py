

def manum_nophine_num_nopode(input_ls): 
    num_nop =0 

    for i in range(len(input_ls)):
        while input_ls[i].isupper() and (i+num_nop)% 4!=0 :
            num_nop+=1 

            

    return num_nop


def main():
    num_nopode_input = input()
    print(manum_nophine_num_nopode(num_nopode_input))

if __name__ == "__main__":
    main()
