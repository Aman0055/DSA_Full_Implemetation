"""
Agenda :
1> Sorting
2> Various Sorting Techniques 

Arranging data elements in same logical order is known as Sorting.

Sorting we are going to cover is also known as internal sorting. 

Note :-->> When elements are numbers, sorting means arranging numbers in ascending order(by default).

:-->> When elements are Strings, Sorting means arranging Strings in Dictionary Order(alphabetical)
    order(By Default).

@@@@@ Various Sorting Algorithm @@@@
1> Bubble Sort
2> Modified Bubble Sort
3> Selection Sort 
4> Insertion Sort
5> Quick Sort
6> Merge Sort 
7> Heap Sort

***********************************************************************
*******************************Bubble-Sort*****************************
***********************************************************************

    0       1       2       3       4       5
    24      58      11      67      92      43
1. (0,1)    (1,2)  (2,3)   (3,4)    (4,5)  
    24       11     58       67     43        92
2. (0,1)    (1,2)   (2,3)   (3,4)   (4,5)
    11       24      58      43       67
3. (0,1)    (1,2)   (2,3)      
    11       24      43       58
4. (0,1)    (1,2)   
    11       24     43
5. (0,1)
    11   24

Result : 11, 24, 43, 58, 67, 92    

***********************************************************************
*************************Modified-Bubble-Sort*****************************
***********************************************************************

n elements 
Round-k             0<k<n
            :- No swapping is k_th ground means elements are sorted now, no more 
                rounds to be executed. 

***********************************************************************
*************************Selection-Sort*****************************
***********************************************************************

        0       1       2       3       4       5       6
        38      90      47      69      52      88      18
1.      18      38      90      47      69      52      88      
2.      18      38      90      47      69      52      88
3.      18      38      47      90      69      52      88
4.      18      38      47      52      90      69      88
5.      18      38      47      52      69      90      88
6.      18      38      47      52      69      88      90

***********************************************************************
*************************Insertion-Sort*****************************
***********************************************************************

0       1       2       3       4       5       6       
50  -    20      37      91      64      18      43
20      50   -   37      91      64      18      43
20      37      50   -   91      64      18      43
20      37      50      91   -   64      18      43
20      37      50      64      91    -  18      43
18      20      37      50      64      91    -  43
18      20      37      43      50      64      91      <-- Result 


"""