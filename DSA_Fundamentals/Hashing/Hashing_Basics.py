"""
Agenda :----------->
1. Why Hashing ?
2. Hashing 
3. Key Terms
4. Collision
5. Hash Function
6. Collision Resolution

==================================== 1.Why Hashing ? ==============================

Hashing is designed by to solve the problem of needing the efficiently find or store 
an item in a collection.
If we have a list of 100000 of words in English and we want to search a given word in
the list , it would be inefficient to successsively compare the word with all 
1000000 words until we find a mach.

====================================  2. Hashing ==================================

It is a technique of mapping keys, and values into the Hash Table by using a Hash Function.
If implemented correctly, then one can achieve 0(1). time complexity in searching an item 
in the collection of elements.

Efficiency of mapping depends on the efficiency of the hash function used.

=================================== 3.Key Terms ======================================

* Hash Table :- It is a data structure used to store elements.

* Hash Function :- It is a function to map(Hash) key-values to the memory address.

* Hashing :- It is a method for storing and retrieving records from a database.

Ex :- Suppose 100 student records need to be stored in an array of 100 memory slots. Use 
hashing to perform efficient access of student data.

Rollno  →  1 to 100

Key

i = HF(key)

int HF(int key)
{
    return key - 1;
}

      0   ┌──────────────────────────┐
          │                          │
      1   ├──────────────────────────┤
          │                          │
      2   ├──────────────────────────┤
          │                          │
      3   ├──────────────────────────┤
          │                          │
      4   ├──────────────────────────┤
          │                          │
      .   ├──────────────────────────┤
      .   │                          │
      .   ├──────────────────────────┤
          │                          │
     99   └──────────────────────────┘

* Hashing is a method of starting and retrieving records from te data structure.
* It lets you insert, delete and search records based on search by value.  
* When properly implemented these operations can be performed in a contant time.
* This is far better than 0(log2n) average case required to do a binary search on a 
    sorted array.


====================================== 4.Collisions ================================
Collisions occurs when two records hash to the same slot in the table.

Unfortunately, even under the best of circumtances, collisions are nearly unvoidable.


======================================= 5.Hash Function =============================

The hash function creates a mapping between key and value, this is done through the use 
of mathematical formulas.
Various hash functions :
1. Simple Hash Function
2. Division Method
3. Binnning
4. Mid Square Method


===================================== 6. Collision Resolution ============================
Two types of resolutions :
1. Open Hashing (Chaining)
2. Closed Hashing (Open Addressing)
"""