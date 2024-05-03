import matplotlib.pyplot as plt
import time

# Dictionary to store Fibonacci numbers and counts
memo = {}


# Function to calculate Fibonacci numbers using dynamic programming (top-down approach)
def fibonacci(n):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    # Count the number of times F(4) is computed
    count_f4 = 0
    if n == 4:
        count_f4 = 1

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    # Count the occurrences of F(4) for this recursive call
    memo['count_f4'] = memo.get('count_f4', 0) + count_f4

    return memo[n]


fibonacci(100)

# Get the total count of F(4) across all recursive calls
total_f4_count = memo.get('count_f4', 0)

print("Total number of times F(4) is computed:", total_f4_count)


def count_f4(n):
    if n == 4:
        return 1
    if n < 4:
        return 0
    return count_f4(n - 1) + count_f4(n - 2)


# Calculate Fibonacci numbers from F(5) to F(100)
f4_list = []
x = []
for i in range(5, 51):
    x.append(i)
    start = time.time()
    answer = count_f4(i)
    end = time.time()
    print(f'F({i}) = {answer}, time: {end - start:.5f} seconds')
    f4_list.append(answer)

plt.title('F(4) count', {'fontsize': 10, 'color': 'b'})
plt.plot(x, f4_list, marker='o', linewidth=1, markersize=2, label='f(4) count')
plt.xlabel('n', {'fontsize': 10, 'color': 'b'})  # 設定 x 軸標籤
plt.ylabel('times', {'fontsize': 10, 'color': 'b'})  # 設定 y 軸標籤
plt.legend()
plt.show()