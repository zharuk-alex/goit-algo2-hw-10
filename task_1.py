import random
import time
import numpy as np
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr, pivot_type="middle"):
    if len(arr) <= 1:
        return arr

    if pivot_type == "first":
        pivot = arr[0]
    elif pivot_type == "last":
        pivot = arr[-1]
    else:
        pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return (
        deterministic_quick_sort(left, pivot_type)
        + middle
        + deterministic_quick_sort(right, pivot_type)
    )


def measure_time(sort_function, arr, repeats=5):
    times = []
    for _ in range(repeats):
        start_time = time.time()
        sort_function(arr)
        end_time = time.time()
        times.append(end_time - start_time)
    return np.mean(times)


if __name__ == "__main__":
    sizes = [10_000, 50_000, 100_000, 500_000]
    randomized_times = []
    deterministic_times = []

    for size in sizes:
        test_array = [random.randint(0, 1000000) for _ in range(size)]

        rand_time = measure_time(randomized_quick_sort, test_array)
        det_time = measure_time(
            lambda arr: deterministic_quick_sort(arr, "middle"), test_array
        )

        randomized_times.append(rand_time)
        deterministic_times.append(det_time)

        print(f"Розмір масиву: {size}")
        print(f"\tРандомізований QuickSort: {rand_time:.4f} секунд")
        print(f"\tДетермінований QuickSort: {det_time:.4f} секунд")

    plt.figure(figsize=(8, 6))
    plt.plot(sizes, randomized_times, label="Рандомізований QuickSort", marker="o")
    plt.plot(sizes, deterministic_times, label="Детермінований QuickSort", marker="o")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.legend()
    plt.grid()
    plt.show()
