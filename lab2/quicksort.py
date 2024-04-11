import random
import time

comparisons = 0
moves = 0


def stats_reset():
    global comparisons, moves
    comparisons = 0
    moves = 0


# Quick sort algorithm
def quicksort(array):
    global comparisons, moves
    count = 0
    if len(array) <= 1:
        comparisons += 1
        return array
    for i in range(len(array) - 1):
        comparisons += 1
        if array[i] < array[-1]:
            array[i], array[count] = array[count], array[i]
            moves += 1
            count += 1

    array[count], array[-1] = array[-1], array[count]
    moves += 1

    return quicksort(array[0:count]) + [array[count]] + quicksort(array[count+1:])


# Generation of arrays with 100, 1000 and 10000 random elements
def generate_random_array():
    return ([random.randint(1, 100) for _ in range(100)],
            [random.randint(1, 100) for _ in range(1000)],
            [random.randint(1, 100) for _ in range(10000)])


# Array output
def display_array(array):
    elements_per_line = len(array) / 5
    for i, element in enumerate(array):
        print(element, end=", ")
        if (i + 1) % elements_per_line == 0:
            print()
    print()


# The main function of outputting all data
def main():
    arrays = generate_random_array()
    for i in range(3):
        print(f"Array {10**(i+2)}", "\n")
        print("Unsorted array:")
        display_array(arrays[i])

        stats_reset()
        start_time = time.time()
        sorted_array = quicksort(arrays[i])
        time_taken = (time.time() - start_time) * 1000
        print("Sorted array:")
        display_array(sorted_array)

        print(f"Comparisons: {comparisons}")
        print(f"Moves: {moves}")
        print(f"Time taken: {time_taken} ms", "\n")
        print("-"*200)


# Calculation of average values of comparisons, moves and time for sorting
def average_stats(n):
    total_comparisons, total_moves, total_time_taken = 0, 0, 0
    num_iterations = 100
    print("Iterations:", num_iterations, "\n")
    for i in range(num_iterations):
        array = [random.randint(1, 100) for _ in range(n)]
        stats_reset()
        start_time = time.time()
        quicksort(array)
        time_taken = (time.time() - start_time) * 1000
        total_comparisons += comparisons
        total_moves += moves
        total_time_taken += time_taken
    return total_comparisons/num_iterations, total_moves/num_iterations, total_time_taken/num_iterations


# Output of average values of comparisons, moves and time for arrays
def display_average_stats():
    for i in range(3):
        print(f"Array {10**(i+2)}", "\n")
        average_comparisons, average_moves, average_time_taken = average_stats(10**(i+2))
        print(f"Average comparisons: {average_comparisons}")
        print(f"Average moves: {average_moves}")
        print(f"Average time taken: {average_time_taken} ms", "\n")
        print("-"*200)


main()
display_average_stats()
