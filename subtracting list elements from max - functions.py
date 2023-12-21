def get_max_int(nums):
    #Type your code here. 
    max_num = max(nums)
    return max_num

def main ():
    list_num = []
    input_num = int(input(""))
    while input_num != -1:
        list_num.append (input_num)
        input_num = int(input(""))
    max_num = max (list_num)
    new_list = [max_num - input_num for input_num in list_num] #for each value in the list_num list and include that (input_num) in the new list.
    print (*new_list, sep='\n')

if __name__ == '__main__':
    main ()

    #Type your code here.
