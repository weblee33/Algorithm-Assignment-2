# Algorithm-Assignment-2
## 說明
During our class, we discussed how to calculate the n-th Fibonacci Number, denoted as F(n), using top-down ( divide and conqure/ pure recursive) and bottom-up (dynamic-programming-like) methods. For this exercise, please complete the following tasks:
 
1. Write code to measure the execution time of F(1), F(2), ..., F(100) using both methods. Plot the results as a line chart. (if your program crashes during computation F(n+1) or takes too much time (>12hours) to compute one value, you can just stop and report the maximum value of n.)
2. Let's measure the degree of overlapping subproblem. Calculate the times are F(4) computed when we compute F(5),F(6),.....,F(50). Plot the results into line chart.
## 計算結果
1.
Top-Down演算法( divide and conqure/ pure recursive)的時間複雜度是O(2^n)(嚴格來說是1.618^n)，因此運算時間會隨著n變大而指數成長，運算結果最終在運算F(56)時會超出12小時，所以圖表呈現F(1)到F(56)的結果。
Bottom-up演算法(dynamic-programming-like)的運算時間基本都沒有太大的變化。
![image]
3.
