# Randomized Quicksort & Hash Table with Chaining

**Overview**

This repository contains implementations of two fundamental algorithms in Python:

🔹 Randomized Quicksort

A sorting algorithm that selects a random pivot for partitioning.

Recursively sorts subarrays to produce a fully sorted list.

Random pivot selection reduces the likelihood of worst-case performance and improves efficiency on patterned datasets.

The repository also includes a report analyzing the algorithm’s theoretical and empirical performance.

🔹 Hash Table with Chaining

Stores data in key-value pairs.

Handles collisions using chaining (each index holds a list of elements).

Supports the following operations: insert, search, and delete.

This implementation ensures efficient handling of collisions while maintaining fast average-case performance.

** How to Run**
1️⃣ Clone the Repository
  git clone <your-repo-link>
  cd Assignment3

2️⃣ Run Randomized QuickSort
  python RandomizedSort.py

3️⃣ Measure Runtime for Randomized QuickSort
  python MeasureRunTime_QuickSort.py

Demonstrates runtime performance for different input sizes.

4️⃣ Run Hash Table with Chaining
python hash_table.py

Demonstrates insert, search, and delete operations.

Outputs show the hash table before and after operations.

**Notes**

Requires Python 3.x.

Scripts are standalone and can be executed independently.

Recommended to check the report for theoretical analysis, empirical results, and discussion of findings.
