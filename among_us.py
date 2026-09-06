'''
Running code because rephactor doesn't show the output
Samuel Yun
Evil Rephactor
'''

def highest_values(num_list, num):
    list.sort(num_list)
    print(num_list)
    return num_list[len(num_list)-num:]

