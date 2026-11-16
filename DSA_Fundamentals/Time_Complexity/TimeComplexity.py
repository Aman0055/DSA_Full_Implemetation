"""
Agenda :->
1. Basics of function
2. Measuring Algorithm Performance
3. Why analysis is required
4. Types of Algorithm analysis 
5. Time Complexity
6. Asynmptotic Analysis 
7. Asynmptotic Notation 
8. Calculation Big O Notation 

* Diagramatic representation :->>

                    1.  Basics of functions :->

             T = f(n)          [ y = f(x) ]          y = 3x


       T
       ↑
       │
       │
       │                         __________
       │                    ____/
       │                ___/
       │            ___/
       │       ____/
       │   ___/
       │__/
       └────────────────────────────────→ n


                     x                 y
                   _____             _____
                  /     \           /     \
                 |  -2   |         |  -6   |
                 |  -1   |         |  -3   |
                 |   0   |         |   0   |
                 |   1   |         |   3   |
                 |   2   |         |   6   |
                 |   3   |         |   9   |
                  \_____/           \_____/


xxxxxxxxxxxxxxxxxxxxxxxxxxxx  2. Measuring Algorithm Performance  xxxxxxxxxxxxxxxxxxxxxxxxxxx

Algorithm anaylisis is an important part of computational complexity theory, which provide 
theoratical estimation for the required resources of an algorithm to solve a specific 
computational problem.
It is a determination of amount of time and space resources required to execute it.  

xxxxxxxxxxxxxxxxxxxxxxxxxxx  3. Why analysis is required   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

* Predicting behaviour of an algorithm without implimenting.
* Analysis is only approximation, There are many influencing factor.
* It helps us in determining the best algorithm to solve a programming problem. 


xxxxxxxxxxxxxxxxxxxxxxxxxxx 4. Types of Algorithm analysis xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

1. Best Case 
2. Worst Case 
3. Average Case 

:- Certain input takes less time for an algorithm to accomplish its task. It is a best case.
:- Certain input takes max time for an algorithm to accomplish its task. It is a worst case.
:- All other cases / total no of cases = Average Case 

xxxxxxxxxxxxxxxxxxxxxxxxxxx 5. Time Complexity  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

It is a measure of rate of change in time with respect to change in input size.
Various asymptotic notations are there to represent time complexity of an algorithm.


xxxxxxxxxxxxxxxxxxxxxxxxxxxx 6. Asynmptotic Analysis  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

                 Asymptotic Analysis
                 ________________

          पास रहते हुए भी
          कभी न मिलने वाली
          स्थिति।


It is used to analyze performance of algorithms in terms of input size.

We do not calculate the actual time taken by the algorithm to solve the problem, rather 
we are interested in how the time taken by an algorithm increases with the input size.


xxxxxxxxxxxxxxxxxxxxxxxxxxx 7. Asynmptotic Notation  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Big O Notation :- > Provides an upper bound on the growth rate of time. It represent the 
                    wrost case senarios.
Omega Notations :-> Provides a lower bound on the growth rate of time. It represent the best
                    case senarios.
Theta Notations :-> Provides both an upper bound and lower bound on the growth rate of time.
                    It represent the average case senario.

==================================   Theta Notation  ===================================

        Θ(g(n)) = f(n)


                  c₁ × g(n) ≤ f(n) ≤ c₂ × g(n)

                  c₁, c₂ are two constants

                  for all n ≥ n₀


        T(n)
         ↑
         │                            c₂ × g(n)
         │                       ____/
         │                  ____/
         │             ____/          f(n)
         │         ___/          ____/
         │      __/         ____/
         │    _/       ____/             c₁ × g(n)
         │  _/      __/            _____/
         │_/_______/______________/____________→ n
                  n₀


        If g(n) = 3n³ + 5n² + 4

        then

        f(n) = n³

        for some constant c₁, c₂
        such that n ≥ n₀

================================== Big O notation =====================================

              O(g(n)) = f(n)


              0 ≤ f(n) ≤ c g(n)

              for all n ≥ n₀


       T(n)
        ↑
        │                         c × g(n)
        │                    ____/
        │                ___/
        │            ___/       f(n)
        │         __/        __/
        │       _/        __/
        │     _/       __/
        │   _/     ___/
        │__/______/________________________→ n


        f(n) = 2n² + 3n + 4

        g(n) = n²

        3g(n) = 3n²

        3n² ≥ 2n² + 3n + 4
Time Complexity :-> 0(n2)

============================= Omega Notation ================================ 

              Ω(g(n)) = f(n)


              c * g(n) ≤ f(n)

              for all n ≥ n₀


        T(n)
         ↑
         │
         │                         f(n)
         │                   _____/
         │              ____/
         │          ___/
         │      ___/           c * g(n)
         │   __/           ___/
         │ _/          ___/
         │/___________/____________________→ n


        f(n) = 2n² + 3n + 5

        g(n) = n²

        Ω(n²)


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 8. Calculation Big O Notation xxxxxxxxxxxxxxxxxxxxxxxxxxxx

* Calculate O(n) :-
                    1. Factorial 
                    2. Insertion Sort
    
    # Factorial :->
                    f = 1                       -> c1
                    if n == 0 :                 -> c2
                        return 1
                    for i == 1 + n:             
                        f = i x f               -> n.c3
                    return f                    -> c4

    Calcution wala part  : ->>>     f(n) = c3.n+C
                                    g(n) = n
                                    O(n)

    # Insertion Sort :-> 
                        for (i=1 to n):
                            temp = A[i]                         ->C1
                            for (j = n to 0):
                                if A[j] > temp:                 ->C2  | i.C2
                                    A[j+1] = A[j]               
                                else:
                                    break
                            A[j+1] = temp                       ->C3

       Calcution wala part  : ->>>         n(C1 + nC2 + C3) 
                                           f(x) = n(nC2 + C)         |g(n) = n2
                                           C2n2 + Cn                 |O(n2) <- Time Complexity

Time Complexity ranges from best to worst:->>

0(1) < 0(logn) < O(n) < 0(nlogn) < 0(n2) <  0(n2logn) < 0(n3) < 0(n4) 

"""