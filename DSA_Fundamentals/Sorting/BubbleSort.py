"""
Assignment :
1.  Write a python program to implement Bubble Sort
2. Write a python function to implement modified bubble sort 
"""
def buble_sort(data_list):
    for r in range(1, len(data_list)):
        for i in range(len(data_list) - r):
            if data_list[i] > data_list[i+1]:
                data_list[i], data_list[i+1] = data_list[i+1], data_list[i]

def modified_bubble_sort(data_list):
    flag = False
    for r in range(1, len(data_list)):
        flag = False
        for i in range(len(data_list)-r):
            if data_list[i] > data_list[i+1]:
                data_list[i], data_list[i+1] = data_list[i+1], data_list[i]
                flag = True
        if not flag:
            break
list = [37, 78, 90,23, 13, 42,11]
modified_bubble_sort(list)
print("Modified bubble sort:", list)
# buble_sort(list)
# print("After bubble sort :", list)