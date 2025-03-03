# Завдання 1
# Створіть функцію для обчислення факторіала числа. Запустіть декілька завдань,
# використовуючи Thread, і заміряйте швидкість їхнього виконання,
# а потім заміряйте швидкість обчислення,
# використовуючи той же набір завдань на ThreadPoolExecutor.
# Як приклади використовуйте останні значення,
# від мінімальних і до максимально можливих, щоб побачити приріст або втрату продуктивності.


import threading
import time
from concurrent.futures import ThreadPoolExecutor

def factorial(n):
    if n < 0:
        return 'Factorial does not exist'
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def measure_time_threading(numbers):
    threads = []
    start_time = time.time()
    for num in numbers:
        thread = threading.Thread(target=factorial, args=(num,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    return end_time - start_time

def measure_time_threadpool(numbers):
    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        executor.map(factorial, numbers)
    end_time = time.time()
    return end_time - start_time

numbers = [10, 50, 100, 200, 300, 1000000]
threading_time = measure_time_threading(numbers)
threadpool_time = measure_time_threadpool(numbers)

print(f"Execution time using threading: {threading_time:.4f} seconds")
print(f"Execution time using ThreadPoolExecutor: {threadpool_time:.4f} seconds")

# 100000
# Execution time using threading: 3.0392 seconds
# Execution time using ThreadPoolExecutor: 2.8697 seconds
