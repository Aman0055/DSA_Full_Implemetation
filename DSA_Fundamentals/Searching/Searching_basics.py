"""
* Agenda :->>>>>>>>>>>>>>>
1. Linear Search
2. Binary Search

xxxxxxxxxxxxxxxxxxxxxxxxxxxxx  Linear Search  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

list :-> 0      1       2       3       4       5       6       7       8
        32      12      11      13      89      90      32      54      87
        item :-> 90

        for e in list1:
            if e == item:
                return list1.index(e)
            return None

        Time Complexity :-> 0(n)

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  Binary Search  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

list1 :-> 0     1       2       3       4       5       6       7       8
          13    56      3       100     list1[middleIndex]
            return middleIndex
        if item < list1[middleIndex]
            binarySearch(list1, 0, 3)
        else:
            binarySearch(list1, 5, 9)
            
        :-> Time Complexity : O(log2n) 43      123     900     11      0
        For execute the binary search operartion first sort the same :
sort  :->0      3       11      13      43      56      100     123     900

middleIndex = (lowerIndex + upperIndex) / 2

if item == list1[middleIndex]
    return middleIndex
if item < list1[middleIndex]
    binarySearch(list1, 0, 3)
else:
    binarySearch(list1, 5, 9)

:-> Time Complexity : O(log2n)
"""