def Quick_Sort(list1):
    if len(list1)<=1:
        return list1
    else:
        pivot = list1[0]
        lesser = [x for x in list1[1:] if x <= pivot]   # list comprehension
        greater = [x for x in list1[1:] if x > pivot]
        return Quick_Sort(lesser) + [pivot] + Quick_Sort(greater)
ls = [12,45,32,6,9,43,600,654,76,13,11,5,8,88,456]
result = Quick_Sort(ls)
print(result)