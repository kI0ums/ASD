import random
import time


# Sort by selection with number of comparisons, moves and time
def selection_sort(array):
    n = len(array)
    start_time = time.time()

    for i in range(n - 1):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    end_time = time.time()
    time_taken = round((end_time - start_time) * 1000, 3)

    return time_taken


# Generation of arrays with 100, 1000 and 10000 random elements
def generate_random_array():
    return ([random.randint(1, 100) for _ in range(100)],
            [random.randint(1, 100) for _ in range(1000)],
            [random.randint(1, 100) for _ in range(10000)])


# Calculation of average values of comparisons, moves and time for sorting
def average_stats(n):
    total_time_taken = 0
    num_iterations = 10
    print("Iterations:", num_iterations, "\n")
    for i in range(num_iterations):
        array = [random.randint(1, 100) for _ in range(n)]
        total_time_taken += selection_sort(array)
    return total_time_taken/num_iterations


# Output of average values of comparisons, moves and time for arrays
def display_average_stats():
    for i in range(3):
        print(f"Array {10**(i+2)}", "\n")
        average_time_taken = average_stats(10**(i+2))
        print(f"Average time taken: {average_time_taken}ms", "\n")
        print("-"*200)


display_average_stats()


# Quick sort algorithm
def quicksort(array):
    count = 0
    if len(array) <= 1:
        return array
    for i in range(len(array) - 1):
        if array[i] < array[-1]:
            array[i], array[count] = array[count], array[i]
            count += 1

    array[count], array[-1] = array[-1], array[count]

    return quicksort(array[0:count]) + [array[count]] + quicksort(array[count+1:])


# Calculation of average values of comparisons, moves and time for sorting
def average_stats2(n):
    total_time_taken = 0
    num_iterations = 100
    print("Iterations:", num_iterations, "\n")
    for i in range(num_iterations):
        array = [random.randint(1, 100) for _ in range(n)]
        start_time = time.time()
        quicksort(array)
        time_taken = (time.time() - start_time) * 1000
        total_time_taken += time_taken
    return total_time_taken/num_iterations


# Output of average values of comparisons, moves and time for arrays
def display_average_stats2():
    for i in range(3):
        print(f"Array {10**(i+2)}", "\n")
        average_time_taken = average_stats2(10**(i+2))
        print(f"Average time taken: {average_time_taken} ms", "\n")
        print("-"*200)


display_average_stats2()