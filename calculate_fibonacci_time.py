import time
import matplotlib.pyplot as plt


# Top down


def fibonacci_top_down(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_top_down(n - 1) + fibonacci_top_down(n - 2)


# bottom up
def fibonacci_bottom_up(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


def td_execution_time(n):
    start_time = time.time()
    fibonacci_top_down(n)
    end_time = time.time()
    return end_time - start_time


def dp_execution_time(n):
    start_time = time.time()
    fibonacci_bottom_up(n)
    end_time = time.time()
    return end_time - start_time


tp = []
dp = []
n = 0

for i in range(1, 101):
    execution_time = td_execution_time(i)
    tp.append(execution_time)
    execution_time2 = dp_execution_time(i)
    dp.append(execution_time2)
    if execution_time >= 60 * 60 * 12:
        n = i
        break
    print(f"round : {i} ,time : {execution_time:.5f}")
    n = i

x = [i for i in range(1, n + 1)]


plt.plot(x, tp, marker='o', linewidth=1, markersize=2, label='Top down')
plt.plot(x, dp, marker='x', linewidth=1, markersize=2, label='Bottom up')
plt.xlabel('n', {'fontsize': 10, 'color': 'b'})  # 設定 x 軸標籤
plt.ylabel('time(s)', {'fontsize': 10, 'color': 'b'})  # 設定 y 軸標籤
plt.legend()
plt.savefig('fibonacci_execution_time.png')
plt.show()
