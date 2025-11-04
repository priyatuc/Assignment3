import random
import time

def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    middle = []

    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] == pivot:
            middle.append(arr[i])
        else:
            right.append(arr[i])

    return deterministic_quicksort(left) + middle + deterministic_quicksort(right)

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivotIndex = random.randint(0, len(arr) - 1)
    pivot = arr[pivotIndex]
    left = []
    right = []
    middle = []

    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] == pivot:
            middle.append(arr[i])
        else:
            right.append(arr[i])

    return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Measure execution time
def measure_time(sort_fn, arr):
    start = time.perf_counter()
    sort_fn(list(arr)) 
    end = time.perf_counter()
    return round((end - start) * 1000, 3) 

# Generate test arrays 
def generate_arrays(n):
    random_arr = [random.randint(0, n) for _ in range(n)]
    sorted_arr = sorted(random_arr)
    reverse_arr = sorted_arr[::-1]
    repeated_arr = [random.randint(0, 10) for _ in range(n)]
    return random_arr, sorted_arr, reverse_arr, repeated_arr

# Run comparison
sizes = [100, 500, 1000]

for n in sizes:
    random_arr, sorted_arr, reverse_arr, repeated_arr = generate_arrays(n)
    print(f"\nArray size: {n}")

    print(f"Random array     - Deterministic: {measure_time(deterministic_quicksort, random_arr)} ms | Randomized: {measure_time(randomized_quicksort, random_arr)} ms")
    print(f"Sorted array     - Deterministic: {measure_time(deterministic_quicksort, sorted_arr)} ms | Randomized: {measure_time(randomized_quicksort, sorted_arr)} ms")
    print(f"Reverse array    - Deterministic: {measure_time(deterministic_quicksort, reverse_arr)} ms | Randomized: {measure_time(randomized_quicksort, reverse_arr)} ms")
    print(f"Repeated elements- Deterministic: {measure_time(deterministic_quicksort, repeated_arr)} ms | Randomized: {measure_time(randomized_quicksort, repeated_arr)} ms")
